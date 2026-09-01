from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_prompt():
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are PaddyBot, an AI assistant specialized in paddy (rice) cultivation.

Use ONLY the provided context to answer.

Rules:
1. Answer only from the provided context.
2. Never make up facts.
3. If the answer is not found, say:
'I couldn't find this information in the provided knowledge base.'
4. Keep answers concise.
5. Use bullet points whenever appropriate.

Context:
{context}
"""
            ),

            MessagesPlaceholder(variable_name="chat_history"),

            (
                "human",
                "{input}"
            )
        ]
    )

    return prompt