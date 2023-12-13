import os
import Encoding
import Decoding


def encode_folder(directory):
    files = []
    for filename in os.listdir(directory):
        f = filename
        if filename.endswith('.txt'):
            files.append(f)

    os.chdir(directory)
    for file in files:
        Encoding.start(file)


def decode_folder(directory):
    folders = []
    for filename in os.listdir(directory):
        f = filename
        if not ('.' in filename):
            folders.append(f)
    
    os.chdir(directory)
    for folder in folders:
        Decoding.decompress_data(folder + '.txt')
        os.chdir('..')
