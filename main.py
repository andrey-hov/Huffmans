import Encoding
import Decoding
import argparse


def decoding(compressed_data, file_huffman_codes):
    return Decoding.decompress_data(compressed_data, file_huffman_codes)


def encoding(file_name):
    return Encoding.start(file_name)

parser = argparse.ArgumentParser(description='Huffman')
parser.add_argument('code', type=str, help='Encode or decode')
parser.add_argument('file_path', type=str, help='The path to the file')
parser.add_argument('file_decode_path', type=str, help='The path to the file')
args = parser.parse_args()

if args.code == 'decode':
    decoding(args.file_path, args.file_decode_path)
elif args.code == 'encode':
    encoding(args.file_path)
else:
    raise Exception('Введите encode или decode')
