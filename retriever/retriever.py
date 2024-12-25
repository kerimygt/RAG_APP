import json

class Retriever:
    def __init__(self, knowledge_base_path):
        with open(knowledge_base_path, 'r') as f:
            self.knowledge_base = json.load(f)

    def search(self, query):
        results = [item for item in self.knowledge_base if query.lower() in item['question'].lower()]
        return results if results else [{"question": "No match found", "answer": "Try asking differently."}]
