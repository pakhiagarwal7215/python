from hf import generate_response
import io
from io import BytesIO
import os
import streamlit as st
import requests
from huggingface_hub import InferenceClient
import config
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
# ---- Part 2: paste this function into Part 1 (replace placeholder) ----
def run_safe_ai_image_generator():
    FILTER_API_URL = "https://filters-zeta.vercel.app/api/filter"

    # fallback model if needed: "black-forest-labs/FLUX.1-schnell"
    IMG_MODEL = "stabilityai/stable-diffusion-3-medium-diffusers"
    img_client = InferenceClient(provider="hf-inference", api_key=config.HF_API_KEY)

    st.title("🖼️ Safe AI Image Generator")

    def is_prompt_safe(prompt: str):
        try:
            response = requests.post(
                FILTER_API_URL,
                json={"text": prompt},
                timeout=15
            )

            if response.status_code != 200:
                return False, f"Filter API failed with status {response.status_code}: {response.text}"

            data = response.json()

            if data.get("ok") is True:
                return True, None
            return False, data.get("reason", "⚠️ Unsafe prompt.")

        except Exception as e:
            return False, f"Filter API error: {e}"

    def generate_image(prompt: str):
        safe, err = is_prompt_safe(prompt)
        if not safe:
            return None, err

        try:
            image = img_client.text_to_image(prompt=prompt, model=IMG_MODEL)
            return image, None
        except Exception as e:
            return None, f"Error during image generation: {e}"

    with st.form("img_form"):
        p = st.text_area("Image description:", height=120)
        ok = st.form_submit_button("Generate Image")

    if ok:
        if not p.strip():
            st.warning("⚠️ Enter a description.")
        else:
            with st.spinner("Generating image..."):
                im, err = generate_image(p.strip())

            if err:
                st.error(err)
            else:
                st.image(im, use_container_width=True)
                st.session_state.generated_image = im

    im = st.session_state.get("generated_image")
    if im:
        buf = BytesIO()
        im.save(buf, format="PNG")
        st.download_button(
            "📥 Download",
            buf.getvalue(),
            "ai_generated_image.png",
            "image/png"
        )
    
def math_mastermind():
    mastermind_st_ui()
    
def math_generate(problem):
        prompt = f"Solve this math problem = {problem}"
        answer = generate_response(problem)
        return answer

def mastermind_st_ui():
        st.title("🧮Math mastermind")
        st.write("*Ask me any math problem and i will solve it*")
        if "history" not in st.session_state:
            st.session_state.history =[]
        question = st.text_input("Enter Question:")
        if st.button("Solve"):
            if question == "":
                st.write("Please enter a question")
            else:
                answer = math_generate(question)
                st.session_state.history.append({
                    "q":question,
                    "a":answer
                })
        st.write("## History")
        for item in st.session_state.history:
            st.write("Question:", item["q"])
            st.write("Answer:", item["a"])
            st.write("----------------")       

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
    if opt == "Math mastermind":
        math_mastermind()
    if opt == "safe ai image generator":
        run_safe_ai_image_generator()

if __name__ == "__main__":
    main()