import numpy as np
import tensorflow as tf
import librosa
import os
import scipy.io.wavfile
import glob


def time_cutting(time, audio_path,resample):
    audio, sr = librosa.load(audio_path)
    real_audio = librosa.resample(audio,sr,resample)
    for i in range(int(len(real_audio)/(resample*time))):               
        temp_audio = real_audio[resample*time*i:resample*time*(i+1)]
        print(os.path.splitext(audio_path)[0]+ '_splited_' + str(i+1) + '.wav')
        scipy.io.wavfile.write(audio_path+ '_splited_' + str(i+1) + '.wav' ,resample, temp_audio)


a,b=1,3

print(b)