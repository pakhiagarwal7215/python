from hf import generate_response
import re
import streamlit as st
def get_answer(text,max_rounds=4):
    base_prompt=("Answer clearly in numbered points. "
        "Do not cut sentences. Finish each point fully.\n\n"
        f"Question: {text}"
    )
    ans = generate_response(base_prompt,temperature=0.3,max_tokens=1024)
    incomplete = st.text_input("Do you feel it's incomplete?: ")
    rounds = 0
    while rounds<max_rounds and incomplete=="yes":
        cont_prompt = (
            "Continue EXACTLY from where you stopped. "
            "Do NOT repeat earlier text. "
            "Finish the incomplete point and complete the answer.\n\n"
            f"Question: {text}\n\n"
            f"Answer so far:\n{ans}\n\nContinue:"
        )
        rounds +=1
        more = generate_response(cont_prompt,temperature=0.3,max_tokens=1024)
        if not more or more.strip() in ans:
            break
        ans = (ans.rstrip()+"\n"+more.lstrip()).strip()
    return ans
st.title("AI teaching assistant")
st.write("Welcome! you can ask me anything about various subject,and I'll provide an answer.")
user_input = st.text_input("Enter your question here:")
if user_input:
    st.write(f"***Your question:** {user_input}")
    response = get_answer(user_input)
    st.write(f"**AI's answer:** {user_input}")
    response = get_answer(user_input)
    st.write("**AI's answer:**")
    st.markdown(response)
else:
    st.info("please enter a question to ask")