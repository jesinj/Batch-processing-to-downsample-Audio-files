# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:03:17 2020

@author: jjam194
Code to downsample all wav files in a folder to 16000 Hz and save to another folder
"""
#note that the wav files are replaced by the downsampled version. Please take a backup version of your higher sampling rate files before running the code
import librosa    #installation in README
import os, glob
path = 'D:/UOA_research/2020/Maori_TTS/wav_original_16k/'
for filename in glob.glob(os.path.join(path, '*.wav')):
    y, sr = librosa.load(filename, sr=16000) # Downsample 44.1kHz to 16kHz Here y is the new wav file and sr is the new sampling rate.
    librosa.output.write_wav(filename, y, sr)
    
