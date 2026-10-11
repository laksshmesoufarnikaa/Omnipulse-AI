import streamlit as st

st.set_page_config(
    page_title="OmniPulse AI",
    page_icon="✨"
)

st.title("✨ OmniPulse AI")
st.subheader("One source. Many stories.")

st.write(
    "Turn research into engaging social media content."
)

url = st.text_input("Paste a research URL")

if st.button("Generate Content"):
    if url.strip():
        st.success("URL received successfully!")
        st.write(url)
    else:
        st.warning("Please enter a URL.")
