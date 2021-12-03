import os
import sys
import subprocess
import scipy
from scipy.io import wavfile
import speech_recognition as sr

def extract(fileExt):
    """ Extracts file with given paramter
    Parameters: 
        file's extention
    Returns:
        string array of files which end with the given extention
    """
    fileDir = os.getcwd()

    files = []
    
    for file in os.listdir():
        if file.endswith(fileExt):
            files.append(file)

    return (files)


def convert2wav(mp3s):
    """ Creates a folder and converts .mp3 files into .wav ones into the folder
    Parameters:
        string array of mp3 files
    """
    os.mkdir("output")
    for file in mp3s:
        subprocess.call(['ffmpeg', '-i', file,"output/"+ file[:-4] + ".wav"])
        

def audioLen(audioName):
    """ Calculates the length of a given .wav file
    Parameters:
        name of the audio file
    Returns:
        .wav file's length in seconds
    """
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
