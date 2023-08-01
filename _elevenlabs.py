from elevenlabs import clone, generate, play, set_api_key, VOICES_CACHE, voices
from elevenlabs.api import History
import os

os.environ['ELEVENLABS_API_KEY'] = 'api-key'
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
    