from chatbot import PaddyBot
import streamlit as st

st.set_page_config(
    page_title="PaddyBot",
    page_icon="🌾",
    layout="wide"
)



@st.cache_resource
def load_bot():
    return PaddyBot()

bot = load_bot()



if "messages" not in st.session_state:
    st.session_state.messages = []


# ---------------- Sidebar ---------------- #

with st.sidebar:
    st.title("🌾 PaddyBot")

    st.markdown("---")

    st.subheader("💬 Recent Chats")

    if "chat_titles" not in st.session_state:
        st.session_state.chat_titles = []

    if len(st.session_state.chat_titles) == 0:
        st.info("No conversations yet.")
    else:
        for i, title in enumerate(reversed(st.session_state.chat_titles), start=1):
            st.markdown(f"**{i}.** {title}")

    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):

        st.session_state.messages = []
        st.session_state.chat_titles = []

        bot.chat_history = []

        st.rerun()

# ---------------- Main Page ---------------- #


if len(st.session_state.messages) == 0:

    st.title("🌾 PaddyBot")

    st.markdown(
        """
        ### Your AI Assistant for Paddy Farming 🌱

        Welcome! I can help you with:

        - 🌾 Paddy diseases
        - 🍂 Symptoms & diagnosis
        - 💊 Treatment recommendations
        - 🐛 Pest management
        - 💧 Irrigation
        - 🌱 Fertilizers
        - 🚜 Harvesting & cultivation
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("🦠 What are the symptoms of blast disease?")

        st.info("💧 How often should I irrigate my paddy field?")

    with col2:
        st.info("🌱 Which fertilizer is best during tillering stage?")

        st.info("🐛 How do I control brown planthopper?")

    st.success("👇 Ask your own question below to begin.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.markdown("---")


question = st.chat_input("Ask anything about paddy cultivation...")

if question:

    if question not in st.session_state.chat_titles:
        title = question[:35] + "..." if len(question) > 35 else question
        st.session_state.chat_titles.append(title)

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("🌾 PaddyBot is thinking..."):

            response = bot.ask(question)

            

            answer = response["answer"]

            st.markdown(answer)

            # ---------------- Sources ---------------- #

            sources = response.get("sources", [])

            if sources:

                with st.expander("📄 Sources Used"):

                    for source in sources:

                        st.markdown(
                            f"""
                            **📘 {source['document']}**

                            Page: {source['page']}
                            """
                        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()