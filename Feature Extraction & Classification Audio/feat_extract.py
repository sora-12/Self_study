
#!/usr/bin/env python
# coding= UTF-8
# https://github.com/mtobeiyf/audio-classification


import code
import glob
import os
import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
import soundfile as sf
import csv


def extract_feature(file_name=None):

    print('Extracting', file_name)
    X, sample_rate = sf.read(file_name, dtype='float32')

    if X.ndim > 1: X = X[:,0]
    X = X.T

    # stft = short term fourier transfrom 
    # 주파수 특성이 시간에 따라 달라지는 사운드 분석하기 위함 , 시계열을 일정한 시간 구간으로 나누고 각 구간에 대해 스펙트럼을 구한 데이터
    stft=np.abs(librosa.stft(X))

    # mfcc (mel-frequency cepstrum) / 40
    # mel scale spectrum을 40개의 주파수 구역으로 묶은 뒤 다시 푸리에 변환하여 얻은 계수 , 스펙트럼이 어떤 모양으로 되어 있는지를 나타내는 특성값
    mfccs=np.mean(librosa.feature.mfcc(y=X,sr=sample_rate,n_mfcc=40).T,axis=0)
    
    # chroma / 12
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)

    # melspectrogram / 128 
    mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)

    # spectral contrast / 7
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)

    # tone / 6
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
    return mfccs,chroma,mel,contrast,tonnetz,file_name

def parse_audio_files(parent_dir,file_ext='*.wav'):

    sub_dirs = os.listdir(parent_dir)
    sub_dirs.sort()
    features, labels = np.empty((0,193)), np.empty(0)
    # 파일이름과  label feature 까지 볼 수 있는 list
    totals=[]
        # others 0 target 1
    for label, sub_dir in enumerate(sub_dirs):
        if os.path.isdir(os.path.join(parent_dir, sub_dir)):
            print('파일 있음')
            for fn in glob.glob(os.path.join(parent_dir, sub_dir, file_ext)):
                try: mfccs, chroma, mel, contrast,tonnetz,file_name = extract_feature(fn)
                except Exception as e:
                    print("[Error] extract feature error in %s. %s" % (fn,e))
                    continue

                totals.append([file_name,label,list(mfccs), list(chroma), list(mel), list(contrast),list(tonnetz)])
                
                ext_features = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
                features = np.vstack([features,ext_features])
                # labels = np.append(labels, fn.split('/')[1])
                labels = np.append(labels, label)
                
            print("extract %s features done" % (sub_dir))
    return np.array(features), np.array(labels, dtype = np.int),totals

def parse_predict_files(parent_dir,file_ext='*.wav'):
    sub_dirs=os.listdir(parent_dir)
    sub_dirs.sort()
    features, labels = np.empty((0,193)), np.empty(0)
    for label, sub_dir in enumerate(sub_dirs):
        if os.path.isdir(os.path.join(parent_dir, sub_dir)):
            for fn in glob.glob(os.path.join(parent_dir, sub_dir, file_ext)):
                try: 
                    mfccs, chroma, mel, contrast,tonnetz,fiilename = extract_feature(fn)
                except Exception as e:
                    print("[Error] extract feature error in %s. %s" % (fn,e))
                    continue
                ext_features = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
                features = np.vstack([features,ext_features])
                labels = np.append(labels, label)
            print("extract %s features done" % (sub_dir))
    return np.array(features), np.array(labels, dtype = np.int)

def main():
    # Get features and labels
    if not os.path.exists('feat.npy'):
        features, labels,totals = parse_audio_files(r'C:\Users\Owner\tmp_python\data')
        np.save('feat.npy', features)
        np.save('label.npy', labels)
        # list to csv
    
        with open('train_total.csv','w',newline='',encoding='utf8') as file:
            writer=csv.writer(file,quoting=csv.QUOTE_ALL)
            writer.writerow(['file_name','label','mfccs', 'chroma', 'mel', 'contrast','tonnetz'])
            for row in totals:
                writer.writerow(row)
            

    if not os.path.exists('predict_feat_bad.npy'):
        # Predict new
        features, label= parse_predict_files(r'C:\Users\Owner\tmp_python\predict_bad')
        np.save('predict_feat_bad.npy', features)
        np.save('predict_label_bad.npy', label)

# if __name__ == '__main__': main()
