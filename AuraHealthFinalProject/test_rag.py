from rag import ask_rag

question = input("Ask a question: ")

# No previous chat in this test
answer, sources, distances = ask_rag(
    question,
    chat_history=""
)

print("\n" + "="*60)
print("ANSWER")
print("="*60)

print(answer)

print("\n" + "="*60)
print("RETRIEVED SOURCES")
print("="*60)

shown = set()

for source, distance in zip(sources, distances):

    filename = source["source"]

    if filename not in shown:

        shown.add(filename)

        print(f"📄 {filename}")

        print(f"Similarity Distance : {distance:.4f}")

        print("-"*40)