This is the documentation to downsample audio files.
The platform used in Python (IDE - Anaconda - Spyder)
OS : Windows (Currently in Covid 19 lockdown - so do not have access to an Ubuntu system)
Using Anaconda with Spyder installation in it.

1. Install pip using Anacona command prompt
Go to Anaconda Navigator.
Go to Environmanets
Search for pip in "Installed" list - if it exists, it means that Spyder has pip installed.
Now you can use Anaconda command prompt - to install all packages you want using pip.

2. Install librosa for audio reading

In Anaconda command prompt type:

pip install librosa
conda install -c conda-forge ffmpeg

3. Python code:
#note that the wav files are replaced by the downsampled version. Please take a backup version of your higher sampling rate files before running the code
import librosa    #installation in README
import os, glob
path = 'path/to/wav/folder/'
for filename in glob.glob(os.path.join(path, '*.wav')):
    y, sr = librosa.load(filename, sr=16000) # Downsample 44.1kHz to 16kHz Here y is the new wav file and sr is the new sampling rate.
    librosa.output.write_wav(filename, y, sr)
    
#the process takes a while depending on the number of files you have


4. Checking using Audacity

Open the converted wav file in Audacity and check the project rate. It should be the new sampling value.
