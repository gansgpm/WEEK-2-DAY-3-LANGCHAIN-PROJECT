from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "What is the capital of Japan? Answer in one word.",
    "Explain in 3 sentences what a general ledger is in accounting.",
    "Write a detailed 500-word explanation of how LLM observability tools "
    "help engineers debug production AI applications, with examples.",
]

for i, p in enumerate(prompts, start=1):
    print(f"\n--- Prompt {i}: {p}")
    print(llm.invoke(p).content)