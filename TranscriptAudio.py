import os
import sys
import subprocess
import scipy
from scipy.io import wavfile
import speech_recognition as sr

def extract(fileExt):
    fileDir = os.getcwd()

    files = []
    
    for file in os.listdir():
        if file.endswith(fileExt):
            files.append(file)

    return (files)


def convert2wav(mp3s):
    os.mkdir("output")
    for file in mp3s:
        subprocess.call(['ffmpeg', '-i', file,"output/"+ file[:-4] + ".wav"])
        

def audioLen(audioName):
    rate, data = wavfile.read(audioName)
    return (len(data) / rate)


def main(LanguageTag):
    convert2wav(extract(".mp3"))
    os.chdir("output")
    files = extract(".wav")

    r = sr.Recognizer()

    for file in files:
        src = sr.AudioFile(file)
        srcMin = audioLen(file) / 60
        for i in range(int(srcMin) + 1):
            with src as source:
                audio = r.record(source, offset = 60 * i, duration = 60)
            transcript = r.recognize_google(audio, language = LanguageTag)
            out = open(file[:-4] + ".odt", "a")
            out.write(transcript)
        out.close()

        
if __name__ == "__main__":
    main(sys.argv[1])
