import os


def decompress_data(file_compressed_data):
    with open(file_compressed_data) as file:
        compressed_data = file.read()
    huff_codes_reversed, code_n = get_huffmans_code(file_compressed_data[:-10] + 'codes.txt')
    decoded_data = ""
    temp_code = ""

    for bit in compressed_data:
        temp_code += bit
        if temp_code in huff_codes_reversed:
            if temp_code == code_n:
                decoded_data += '\n'
            else:
                decoded_data += huff_codes_reversed[temp_code]
            temp_code = ""
    
    name = file_compressed_data[:-11] + '_decode' + '.txt'
    my_file = open(name, "w+")
    my_file.write(decoded_data)

    return decoded_data

def get_huffmans_code(file_huff_codes):
    huff_codes_reversed = {}
    code_n = ''
    with open(file_huff_codes) as file:
        lines = file.readlines()
        for line in lines:
            if line[0:2] == '  ':
                huff_codes_reversed.update({line[:-1].split()[0]: ' '})
            else:
                line = line[:-1].split()
                try:
                    if line[0] == '\\n':
                        code_n = line[1]
                    huff_codes_reversed.update({line[1]: line[0]})
                except:
                    pass
    return (huff_codes_reversed, code_n)
