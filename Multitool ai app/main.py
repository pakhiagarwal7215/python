from hf import generate_response
import io
from io import BytesIO
import os
import streamlit as st
def export_txt(history):#This function converts a chat history into a downloadable TXT file stored in memory using BytesIO.
    txt = "".join([f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n" for i, h in enumerate(history, 1)])
    bio = io.BytesIO(txt.encode("utf-8")); bio.seek(0); return bio 
def teaching_answer(q: str) -> str:
    return generate_response(q, temperature=0.3, max_tokens=1024)
CSS = """
<style>
.history-wrap {max-height: 420px; overflow-y: auto; padding-right: 6px;}
.qa-card{
    border: 1px solid #e6e6e6;
    background: #ffffff;
    border-radius: 10px;
    padding: 14px 16px;
    margin: 10px 0;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
}
.q{font-weight: 700; color: #0a6ebd; margin-bottom: 8px;}
.a{white-space: pre-wrap; color: #333; line-height: 1.5;}
</style>
"""
def run_ai_teaching_assistant():
    st.set_page_config(page_title="AI teaching assistant",layout="centered")
    st.title("AI teaching assistant")
    st.write("Ask me anything about various subjects, and i will provide an answer")
    st.session_state.setdefault("history",[])
    col_clear,col_export = st.columns([1,2])
    with col_clear:
        if st.button("🧹Clear conversation"):
            st.session_state.history = []
            st.rerun()
    
    with col_export:
        if st.session_state.history:
            st.download_button(
                label="📤 Export Chat History",
                data=export_txt(st.session_state.history),
                file_name="AI_Teaching_Assistant_Conversation.txt",
                mime="text/plain",
            )
    user_input = st.text_input("enter your question here:")
    if st.button("Ask"):
        q = user_input.strip()
        with st.spinner("Generating AI response..."):
         a = generate_response(q, temperature=0.3)
        st.session_state.history.insert(0,{"question": q,"answer":a})
        st.rerun()
    else: 
        st.warning("Please enter a question before clicking Ask.")
        st.markdown("### Conversation History")
    st.markdown(CSS, unsafe_allow_html=True)

    cards = []
    for i, h in enumerate(st.session_state.history, 1):
        cards.append(f'<div class="qa-card"><div class="q">Q{i}: {h["question"]}</div><div class="a">{h["answer"]}</div></div>')
        st.markdown('<div class="history-wrap">' + "".join(cards) + "</div>", unsafe_allow_html=True)
def main():
    st.sidebar.title("Choose Ai feature ")
    opt = st.sidebar.selectbox("",["AI teaching assistant","Math mastermind","safe ai image generator" ])
    if opt == "AI teaching assistant":
        run_ai_teaching_assistant()
if __name__ == "__main__":
    main()