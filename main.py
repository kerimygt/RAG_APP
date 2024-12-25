from retriever.retriever import Retriever
from generator.generator import Generator

def main():
    retriever = Retriever('data/knowledge_base.json')
    generator = Generator()

    query = input("Ask a question: ")
    results = retriever.search(query)
    response = generator.generate(results)

    print("\n--- Response ---")
    print(response)

if __name__ == "__main__":
    main()
