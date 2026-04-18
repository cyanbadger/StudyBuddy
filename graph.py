from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from state import CapstoneState
from nodes import (
    memory_node,
    router_node,
    retrieval_node,
    skip_retrieval_node,
    tool_node,
    answer_node,
    eval_node,
    save_node,
    MAX_EVAL_RETRIES
)


def route_decision(state: CapstoneState):
    route = state["route"]
    if route == "retrieve":
        return "retrieve"
    if route == "tool":
        return "tool"
    return "skip"


def eval_decision(state: CapstoneState):
    if state["faithfulness"] < 0.7 and state["eval_retries"] < MAX_EVAL_RETRIES:
        return "answer"
    return "save"


graph = StateGraph(CapstoneState)

graph.add_node("memory", memory_node)
graph.add_node("router", router_node)
graph.add_node("retrieve", retrieval_node)
graph.add_node("skip", skip_retrieval_node)
graph.add_node("tool", tool_node)
graph.add_node("answer", answer_node)
graph.add_node("eval", eval_node)
graph.add_node("save", save_node)

graph.set_entry_point("memory")

graph.add_edge("memory", "router")

graph.add_conditional_edges(
    "router",
    route_decision,
    {
        "retrieve": "retrieve",
        "tool": "tool",
        "skip": "skip"
    }
)

graph.add_edge("retrieve", "answer")
graph.add_edge("tool", "answer")
graph.add_edge("skip", "answer")

graph.add_edge("answer", "eval")

graph.add_conditional_edges(
    "eval",
    eval_decision,
    {
        "answer": "answer",
        "save": "save"
    }
)

graph.add_edge("save", END)

memory = MemorySaver()
app = graph.compile(checkpointer=memory)


def ask(question: str, thread_id: str = "default-thread"):
    initial_state = {
        "question": question,
        "messages": [],
        "route": "",
        "retrieved": "",
        "sources": [],
        "tool_result": "",
        "answer": "",
        "faithfulness": 0.0,
        "eval_retries": 0,
    }

    config = {"configurable": {"thread_id": thread_id}}
    return app.invoke(initial_state, config=config)