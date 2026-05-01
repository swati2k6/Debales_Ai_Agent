from graph import build_graph

def main():
    print("🤖 Debales AI Assistant (type 'exit' to quit)\n")

    graph = build_graph()

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            print("Goodbye 👋")
            break

        try:
            result = graph.invoke({"query": query})
            print("Bot:", result["answer"], "\n")

        except Exception as e:
            print("⚠️ Error:", str(e), "\n")


if __name__ == "__main__":
    main()