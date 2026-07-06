from database import retrieve_with_sources
from config import llm


def ask_rag(question, chat_history=""):

    # Retrieve relevant document chunks
    results = retrieve_with_sources(
        question,
        top_k=5
    )

    # Combine retrieved chunks into one context
    context = "\n\n".join(results["documents"][0])

    # Prompt for Gemini
    prompt = f"""
You are AuraHealth Nexus AI Assistant.

You must follow these rules strictly:

1. Answer ONLY using the provided context.
2. Never use your own knowledge.
3. Never guess or assume anything.
4. Preserve exact names, numbers, dosages, percentages, room numbers, codes, and dates exactly as written.
5. If the answer is not present in the context, reply exactly:

I could not find that information in the provided documents.

6. If the answer contains multiple steps, use a numbered list.
7. If there are multiple conditions, use bullet points.
8. Keep the answer clear and concise.

-------------------------
Previous Conversation
-------------------------
{chat_history}

-------------------------
Context
-------------------------
{context}

-------------------------
Question
-------------------------
{question}

Answer:
"""

    response = llm.generate_content(prompt)

    return (
        response.text,
        results["metadatas"][0],
        results["distances"][0]
    )