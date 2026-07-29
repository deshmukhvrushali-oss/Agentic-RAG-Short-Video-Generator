from duckduckgo_search import DDGS

class ResearchAgent:

    def search(self, topic):
        results = []

        with DDGS() as ddgs:
            search_results = ddgs.text(topic, max_results=5)

            for result in search_results:
                results.append({
                    "title": result["title"],
                    "url": result["href"],
                    "body": result["body"]
                })

        return results