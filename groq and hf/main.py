import hf
from groq import generate_response
import time
def temprature_promt_activity():
    print("="*70)
    print("ADVANCED PROMPT ENGINERING:TEMPRATURE + INSTRUCTIONS")
    print("="*70)
    print("PART 1: TEMPRATURE EXPLORATION")
    prompt = input("enter a creative prompt").strip()
    for t, label in [(0.1, "LOW (0.1) - Dermenistic "),
                     (0.5, "MEDIUM(0.5) - BALANCED"),
                     (0.9, "HIGH(0.9) - CREATIVE")]:
        print(f"*************{label}******************")
        print(generate_response(prompt,t,max_tokens=512))
        time.sleep(1)
    print("PART 2: INSTRUCTION BASED PROMPTS")
    topic = input("Choose a topic (e.g., climate change, space exploration): ").strip()
    prompts = [
        f"Summarize key facts about {topic} in 3-4 sentences.",
        f"Explain {topic} as if I'm a 10-year-old child.",
        f"Write a pro/con list about {topic}.",
        f"Create a fictional news headline from 2050 about {topic}.",
    ]
    for i, p in enumerate(prompts, 1):
        print(f"\n--- INSTRUCTION {i} ---\n{p}")
        print(generate_response(p, temperature=0.7, max_tokens=512))
        time.sleep(1)



temprature_promt_activity()


