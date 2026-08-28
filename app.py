import streamlit as st

from supportgpt.engine import (
    SupportEngine,
)


st.set_page_config(
    page_title="SupportGPT AI",
    page_icon="🤖",
    layout="wide",
)


@st.cache_resource
def load_engine():
    return SupportEngine()


engine = load_engine()


st.title(
    "🤖 SupportGPT AI"
)

st.caption(
    "Intelligent technical support "
    "for software products"
)


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in (
    st.session_state.messages
):
    with st.chat_message(
        message["role"]
    ):
        st.markdown(
            message["content"]
        )


prompt = st.chat_input(
    "Describe your software issue..."
)


if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message(
        "user"
    ):
        st.markdown(
            prompt
        )

    result = engine.answer(
        prompt
    )

    response = (
        result["answer"]
        + "\n\n"
    )

    if result["steps"]:
        response += (
            "### Suggested steps\n"
        )

        for index, step in enumerate(
            result["steps"],
            start=1,
        ):
            response += (
                f"{index}. {step}\n"
            )

    response += (
        "\n**Knowledge source:** "
        + result["source"][
            "title"
        ]
    )

    if result[
        "escalation_recommended"
    ]:
        response += (
            "\n\n⚠️ **Low retrieval "
            "confidence — human "
            "escalation recommended.**"
        )

    with st.chat_message(
        "assistant"
    ):
        st.markdown(
            response
        )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )
