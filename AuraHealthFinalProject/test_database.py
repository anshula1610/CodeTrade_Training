from database import retrieve_with_sources

question = "What is anxiety?"

results = retrieve_with_sources(question)

print(results)