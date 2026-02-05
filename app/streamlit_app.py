import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

import streamlit as st
from src.main import handle_user_query


st.set_page_config(
    page_title="Agentic Customer Support Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Agentic Customer Support Assistant")
st.caption("Multi-agent system with RAG, policy compliance, escalation, and analytics")

st.markdown("---")

query = st.text_input(
    "Enter your question:",
    placeholder="e.g. What is the leave policy?"
)

if query:
    with st.spinner("Processing your query..."):
        result = handle_user_query(query)

    st.subheader("✅ Answer")
    st.write(result.get("answer", "No answer available."))

    st.markdown("---")

    st.subheader("🧠 Agent Used")
    st.info(result.get("agent", "Unknown Agent"))

    if "sources" in result and result["sources"]:
        st.markdown("---")
        st.subheader("📚 Sources")
        for src in result["sources"]:
            st.write(f"- {src}")

    if "ticket_id" in result:
        st.markdown("---")
        st.subheader("🎫 Support Ticket")
        st.code(result["ticket_id"])
