from db import collection, embedder
from tools import datetime_tool, calculator_tool
import os
from langchain_groq import ChatGroq

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY") or " "
,
    model="llama-3.1-8b-instant",
    temperature=0
)

MAX_EVAL_RETRIES = 2


def memory_node(state):
    messages = state.get("messages", [])
    question = state["question"]

    messages.append({"role": "user", "content": question})
    messages = messages[-6:]

    return {
        **state,
        "messages": messages
    }


def router_node(state):
    question = state["question"]

    prompt = f"""
    Decide the route:
    - 'retrieve' → if academic concept
    - 'tool' → if calculation or time
    - 'skip' → casual/memory

    Question: {question}

    Answer ONLY one word: retrieve/tool/skip
    """

    response = llm.invoke(prompt).content.strip().lower()

    return {**state, "route": response}

def retrieval_node(state):
    question = state["question"]
    query_embedding = embedder.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]

    retrieved_parts = []
    sources = []

    for doc, meta in zip(docs, metas):
        topic = meta.get("topic", "Unknown Topic")
        retrieved_parts.append(f"[{topic}]\n{doc}")
        sources.append(topic)

    return {
        **state,
        "retrieved": "\n\n".join(retrieved_parts),
        "sources": sources,
        "tool_result": ""
    }


def skip_retrieval_node(state):
    return {
        **state,
        "retrieved": "",
        "sources": [],
        "tool_result": ""
    }


def tool_node(state):
    question = state["question"].lower()

    if "time" in question or "date" in question:
        tool_result = datetime_tool(question)
    else:
        tool_result = calculator_tool(question)

    return {
        **state,
        "tool_result": tool_result,
        "retrieved": "",
        "sources": []
    }


def answer_node(state):
    question = state["question"]
    context = state.get("retrieved", "")
    tool_result = state.get("tool_result", "")

    if tool_result:
        answer = f"Tool result: {tool_result}"
    else:
        prompt = f"""
        You are a helpful study assistant.

        Answer ONLY using the context below.
        If answer not in context, say "I don't know".

        Context:
        {context}

        Question:
        {question}

        Give clear, structured answer.
        """

        response = llm.invoke(prompt)
        answer = response.content

    return {**state, "answer": answer}

def eval_node(state):
    retrieved = state.get("retrieved", "")
    answer = state.get("answer", "")
    retries = state.get("eval_retries", 0)

    if not retrieved:
        faithfulness = 1.0 if state.get("tool_result") else 0.5
    else:
        grounded_hits = 0
        for src in state.get("sources", []):
            if src.lower() in answer.lower():
                grounded_hits += 1

        faithfulness = 0.9 if grounded_hits > 0 else 0.75

    return {
        **state,
        "faithfulness": faithfulness,
        "eval_retries": retries + 1
    }


def save_node(state):
    messages = state.get("messages", [])
    messages.append({"role": "assistant", "content": state["answer"]})

    return {
        **state,
        "messages": messages
    }
