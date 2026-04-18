import streamlit as st
from graph import ask

st.set_page_config(page_title="Study Buddy AI", page_icon="🎓")

st.title("🎓 Study Buddy AI")
st.write("Ask questions from DBMS, AI, ML, NLP, and networking topics.")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "student-session-1"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

with st.sidebar:
    st.header("Project Info")
    st.write("Domain: Education")
    st.write("User: B.Tech students")
    st.write("Features: RAG, memory, tools, evaluation")
    if st.button("New conversation"):
        st.session_state.thread_id = f"student-session-{len(st.session_state.chat_history) + 2}"
        st.session_state.chat_history = []
        st.rerun()

user_question = st.text_input("Enter your question")

if st.button("Ask") and user_question.strip():
    result = ask(user_question, st.session_state.thread_id)

    st.session_state.chat_history.append(("You", user_question))
    st.session_state.chat_history.append(("Assistant", result["answer"]))

    st.subheader("Latest Answer")
    st.write(result["answer"])

    with st.expander("Debug Info"):
        st.write("Route:", result["route"])
        st.write("Sources:", result["sources"])
        st.write("Faithfulness:", result["faithfulness"])
        st.write("Eval retries:", result["eval_retries"])

if st.session_state.chat_history:
    st.subheader("Conversation")
    for speaker, msg in st.session_state.chat_history:
        st.write(f"**{speaker}:** {msg}")