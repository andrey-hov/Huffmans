import Encoding
import Decoding
import argparse
import Code_folders
import os


def decoding(compressed_data):
    return Decoding.decompress_data(compressed_data)

def encoding(file_name):
    return Encoding.start(file_name)

def decoding_folder(folder_name):
    return Code_folders.decode_folder(folder_name)

def encoding_folder(folder_name):
    return Code_folders.encode_folder(folder_name)


parser = argparse.ArgumentParser(description='Huffman')
parser.add_argument('code', type=str, help='Encode or decode')
parser.add_argument('file_path', type=str, help='The path to the file')
args = parser.parse_args()

if args.code == 'decode':
    if args.file_path[-4:] == '.txt':
        os.chdir(args.file_path[:-4])
        decoding(args.file_path)
        os.chdir('..')
    else:
        decoding_folder(args.file_path)
elif args.code == 'encode':
    if args.file_path[-4:] == '.txt':
        encoding(args.file_path)
    else:
        encoding_folder(args.file_path)
else:
    raise Exception('Введите encode или decode')
