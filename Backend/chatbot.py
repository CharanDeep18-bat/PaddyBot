from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_core.messages import HumanMessage, AIMessage

from retriever import get_retriever
from llm import get_llm
from prompt import get_prompt


class PaddyBot:

    def __init__(self):
        print("🌾 Loading PaddyBot...\n")

        self.retriever = get_retriever()
        self.llm = get_llm()
        self.prompt = get_prompt()

        document_chain = create_stuff_documents_chain(
            llm=self.llm,
            prompt=self.prompt
        )

        self.rag_chain = create_retrieval_chain(
            self.retriever,
            document_chain
        )

        self.chat_history = []

        print("✅ PaddyBot Ready!\n")

    def ask(self, question):

        response = self.rag_chain.invoke(
            {
                "input": question,
                "chat_history": self.chat_history
            }
        )

        self.chat_history.append(
            HumanMessage(content=question)
        )

        self.chat_history.append(
            AIMessage(content=response["answer"])
        )

        return response