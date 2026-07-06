import streamlit as st
from rag import ask_rag

# -----------------------------------
# Page Settings
# -----------------------------------

st.set_page_config(
    page_title="AuraHealth Nexus",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------------
# Title
# -----------------------------------

st.title("🤖 AuraHealth Nexus")
st.caption("AI Assistant powered by Gemini + ChromaDB")

# -----------------------------------
# Sidebar
# -----------------------------------

with st.sidebar:

    st.header("🏥 AuraHealth Nexus")

    st.write("""
This AI Assistant answers questions only from the uploaded AuraHealth documents.

**Technology Used**
- Gemini
- ChromaDB
- Sentence Transformers
- Streamlit
""")

    st.success("🟢 Gemini Connected")
    st.success("🟢 ChromaDB Connected")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------------
# Chat History
# -----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------------
# Welcome Message
# -----------------------------------

if len(st.session_state.messages) == 0:

    st.info("""
👋 **Welcome to AuraHealth Nexus**

Ask questions related to the uploaded healthcare documents.

### Example Questions

- What is NeuroCrystal Syndrome?
- Who is the Head of the OmniHeal initiative?
- What are the symptoms of Phase 2?
- What is the treatment for Phase 2?
- What is the override code during the Cognitive Reset Sequence?
""")

# -----------------------------------
# Display Previous Messages
# -----------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------------
# Chat Input
# -----------------------------------

question = st.chat_input("Ask anything...")

# -----------------------------------
# New Question
# -----------------------------------

if question:

    # Store User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # -----------------------------------
    # Build Chat History
    # -----------------------------------

    chat_history = ""

    for message in st.session_state.messages:
        chat_history += f"{message['role']}: {message['content']}\n"

    # -----------------------------------
    # Generate Answer
    # -----------------------------------

    with st.spinner("🧠 Searching documents and generating answer..."):

        answer, sources, distances = ask_rag(
            question,
            chat_history
        )

    # -----------------------------------
    # Display Assistant Response
    # -----------------------------------

    with st.chat_message("assistant"):

        st.markdown(answer)

        with st.expander("📚 Retrieved Documents"):

            shown = set()

            for source, distance in zip(sources, distances):

                filename = source["source"]

                if filename not in shown:

                    shown.add(filename)

                    st.write(f"📄 **{filename}**")
                    st.caption(f"Similarity Distance : {distance:.4f}")

    # -----------------------------------
    # Save Assistant Response
    # -----------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )