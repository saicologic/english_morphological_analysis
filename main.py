import speech_recognition as sr
from termcolor import cprint
import nltk

r = sr.Recognizer()

def input_audio():

    with sr.Microphone(sample_rate=16000) as source:
        r.adjust_for_ambient_noise(source)
        print("マイクから英語の音声を取得中...")

        audio = r.listen(
            source,
            timeout=None,
        )
        print("音声入力を終了します。")
        return audio

def voice_to_text(audio):
    text = r.recognize_whisper_api(audio)
    return text

def save_audio(file, audio):
    with open(file, 'wb') as f:
        f.write(audio.get_wav_data())

def load_audio(file):
    audio_file = sr.AudioFile(file)
    with audio_file as source:
        audio_data = r.record(source)
    return audio_data

def get_pos_tag(text):
    tokens = nltk.word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    return pos_tags

def print_morphemed_text(pos_tags):
    for tag in pos_tags:
        if tag[1].startswith('V'):
            cprint(tag[0], "red", end=" ")
        elif tag[1].startswith('N'):
            cprint(tag[0], "blue", end=" ")
        else:
            cprint(tag[0], "black", end=" ")

    print("")

def main():
    save_audio_file = "./output.wav"
    audio = input_audio()
    save_audio(save_audio_file, audio)
    text = voice_to_text(load_audio(save_audio_file))
    pos_tags = get_pos_tag(text)
    print_morphemed_text(pos_tags)

if __name__ == '__main__':
    main()
