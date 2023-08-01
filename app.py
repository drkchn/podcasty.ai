import os
import logging

import streamlit as st

from _langchain import get_response
from _elevenlabs import with_custom_voice, with_premade_voice, get_voices

logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

st.set_page_config(page_title="podcasty.ai", page_icon="🎧")

if "podcast_generate" not in st.session_state:
    st.session_state.podcast_generate = ""

if "output_file_path" not in st.session_state:
    st.session_state.output_file_path = ""

if "input_file_path" not in st.session_state:
    st.session_state.input_file_path = ""

if "text_error" not in st.session_state:
    st.session_state.text_error = ""

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"

st.write(
    """
    <style>
    [data-testid="column"] {
        width: calc(50% - 1rem);
        flex: 1 1 calc(50% - 1rem);
        min-width: calc(50% - 1rem);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Welcome to podcasty.ai!")

st.markdown(
    "This is a demo of podcasty.ai"
)

file = st.file_uploader(label="Upload file", type=["mp3",])
if file is not None:
    filename = "sample.mp3"
    with open(filename, "wb") as f:
        f.write(file.getbuffer())
    st.session_state.input_file_path = "sample.mp3"

voice = st.selectbox('Choose your voice', (i for i in get_voices()))

col1, col2 = st.columns(2)

with col1:
    podcaster = st.text_input(label="Podcaster", placeholder="Ex. Michael Barbaro")

with col2:
    guest = st.text_input(label="Guest", placeholder="Ex. Sabrina Tavernise")

prompt = st.text_area(label="Podcast info", placeholder="Ex. Sabrina Tavernise joins Michael Barbaro in conversation about current events as reported by the New York Times.", height=100)

st.button(
    label="Generate Podcast",
    help="Click to generate podcast",
    key="generate_podcast",
    type="primary",
    on_click=generate_podcast,
    args=(voice, prompt, podcaster, guest),
)

