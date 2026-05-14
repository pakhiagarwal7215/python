from hf import generate_response
import io
import streamlit as st
SYSTEM_PROMPT = """You are a Math Mastermind. For every math problem:

1) Show step-by-step solution 2) Explain reasoning 3) Give alternate method if possible

4) Verify answer if possible 5) Use proper notation 6) Break complex problems into parts

Format: Problem → Steps → **Final Answer** → Concepts used. Be precise and educational."""

def math_generate(problem):
    prompt = "Solve this math problem: " + problem
    answer = generate_response(prompt)
    return answer

def export_txt(history):
    text = ""
    for item in history:#scrolls through each question 1 by 1
        text = text + "Question: " + item["q"] + "\n"
        text = text + "Answer: " + item["a"] + "\n\n"
    #BytesIO changes the text into a file that can be downloaded.
    return io.BytesIO(text.encode())
      


def setup_ui_simple():
    st.title("🧮 Math Mastermind")
    st.write("Ask any math question")
    # history list
    if "history" not in st.session_state:
        st.session_state.history = []
    # input box
    question = st.text_input("Enter Question")
    # solve button
    if st.button("Solve"):
        if question == "":
            st.write("Please enter a question")
        else:
            answer = math_generate(question)

            # save question and answer
            st.session_state.history.append({
                "q": question,
                "a": answer
            })
    
    # download button
    if st.session_state.history:

       st.download_button(
        "Download History",
        export_txt(st.session_state.history),
        "history.txt"
    )
    # show old answers
    st.write("## History")
    for item in st.session_state.history:
        st.write("Question:", item["q"])
        st.write("Answer:", item["a"])
        st.write("----------------")

if __name__=="__main__":
    setup_ui_simple()