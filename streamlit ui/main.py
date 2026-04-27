from hf import generate_response
#The re module in Python is used for pattern matching in text Search text Match patterns Replace text
import re
import streamlit as st

def get_answer(text,max_rounds=2):
    # 1) Ask for a clean structured answer (helps avoid unfinished bullets)
    base_prompt = (
        "Answer clearly in numbered points. "
        "Do not cut sentences. Finish each point fully.\n\n"
        f"Question: {text}"
    )
    ans = generate_response(base_prompt, temperature=0.3, max_tokens=1024)
    incomplete = st.text_input("Do you feel it's incomplete?: ")

    # 2) If it looks cut, continue from last line without repeating
    rounds = 0
    while rounds<max_rounds and incomplete=="yes":
        cont_prompt = (
            "Continue EXACTLY from where you stopped. "
            "Do NOT repeat earlier text. "
            "Finish the incomplete point and complete the answer.\n\n"
            f"Question: {text}\n\n"
            f"Answer so far:\n{ans}\n\nContinue:"
        )
        rounds += 1
        more = generate_response(cont_prompt,temperature=0.3,max_tokens=1024)
        if not more or more.strip() in ans:
            break
        #“Join ans and more with one neat line break, without messy spaces.”
        ans = (ans.rstrip() + "\n" + more.lstrip()).strip()

    return ans



st.title("AI Teaching Assistant")
st.write("Welcome! You can ask me anything about various subjects, and I'll provide an answer.")



user_input = st.text_input("Enter your question here: ")
if user_input:
    st.write(f"**Your question:** {user_input}")
    response = get_answer(user_input)
    st.write("**AI's answer:**")
    st.markdown(response)  # markdown renders numbered points nicely
else:
    st.info("Please enter a question to ask.")