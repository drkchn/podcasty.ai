from elevenlabs import clone, generate, play, set_api_key, VOICES_CACHE, voices
from elevenlabs.api import History
import os

import streamlit as st

os.environ['ELEVENLABS_API_KEY'] = st.secrets["ELEVENLABS_API_KEY"]
set_api_key(os.environ.get("ELEVENLABS_API_KEY"))

def with_custom_voice(podcaster, guest, description, prompt, file_path):
    name = f'Podcast between {podcaster} and {guest}'
    temp = name.replace(' ', '_')
    audio_path = f'{temp}.mp3'

    voice = clone(
        name=f'Podcast between {podcaster} and {guest}',
        description=description,
        files=[file_path,],
    )

    audio = generate(text=prompt, voice=voice)

    play(audio)

    try:
        with open(audio_path, 'wb') as f:
            f.write(audio)

        return audio_path
    
    except Exception as e:
        print(e)
        
        return ""
    
def with_premade_voice(prompt, voice):
    audio_path = f'{voice}.mp3'

    audio = generate(
        text=prompt,
        voice=voice,
        model="eleven_monolingual_v1"
    )

    try:
        with open(audio_path, 'wb') as f:
            f.write(audio)

        return audio_path
    
    except Exception as e:
        print(e)

        return ""
    
def get_voices():
    names = []

    v_list = voices()

    for v in v_list:
        names.append(v.name)

    return names
