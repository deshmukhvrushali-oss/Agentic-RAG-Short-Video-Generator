from agents.research_agent import research

print("=" * 50)
print("Agentic RAG Short Video Generator")
print("=" * 50)

topic = input("Enter Topic: ")

result = research(topic)

print("\n")
print("=" * 50)
print("RESEARCH REPORT")
print("=" * 50)

print(result)