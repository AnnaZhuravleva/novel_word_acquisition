import os
import gtts
import pandas as pd
from os import path
from gtts import gTTS as tts
from pydub import AudioSegment
AudioSegment.converter = '/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/ffmpeg-4.2.2/bin/ffmpeg'


AUDIO_PATH = os.path.join(os.getcwd(), 'audio')


def create_audio(path):
    with open(path, 'r', encoding='utf-8') as file:
        table = pd.read_csv(file, sep=';')['word']
    # table = ['sinebu', 'reketre', 'fentime', 'varansu']
    if not os.path.exists(AUDIO_PATH):
        os.mkdir(AUDIO_PATH)
    for word in table:
        try:
            audio = tts(word, lang='ro')
            src = f'audio/{word}.mp3'
            dst = f'audio/{word}.wav'
            audio.save(src)
            sound = AudioSegment.from_mp3(src)
            sound.export(dst, format="wav")
            os.remove(src)
        except:
            print(word)


if __name__ == '__main__':
    create_audio('al.csv')
