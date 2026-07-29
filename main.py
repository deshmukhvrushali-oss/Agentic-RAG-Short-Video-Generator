from agents.research_agent import ResearchAgent

print("=" * 50)
print("Agentic RAG Short Video Generator")
print("=" * 50)

topic = input("Enter Topic: ")

agent = ResearchAgent()

results = agent.search(topic)

print("\nTop Search Results\n")

for i, result in enumerate(results, start=1):
    print(f"\n{i}. {result['title']}")
    print(result["url"])
    print(result["body"])