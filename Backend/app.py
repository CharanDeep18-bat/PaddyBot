from chatbot import PaddyBot
import time


def main():

    bot = PaddyBot()

    while True:

        question = input("\nAsk a question (or type 'exit'): ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        start = time.time()

        response = bot.ask(question)

        end = time.time()

        print(f"\n⏱ Time taken: {end-start:.2f} seconds")

        print("\nAnswer:")
        print("-" * 50)
        print(response["answer"])

        print("\nSources:")
        print("-" * 50)

        seen = set()

        for doc in response["context"]:

            metadata = doc.metadata

            source = metadata.get("source", "Unknown")
            filename = source.split("\\")[-1].split("/")[-1]

            page = metadata.get(
                "page_label",
                metadata.get("page", "Unknown")
            )

            key = (filename, page)

            if key not in seen:
                print(f"📄 {filename} (Page {page})")
                seen.add(key)


if __name__ == "__main__":
    main()