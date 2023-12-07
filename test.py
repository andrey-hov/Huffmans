import unittest
import Decoding
import Encoding


class InterpreterTest(unittest.TestCase):
    def test_huffman_tree(self):
        self.assertEqual(Encoding.build_huffman_tree({'a': 10, 'b': 2}), 
                                                    [12, ['b', '0'], ['a', '1']])
    
    def test_decode(self):
        self.assertEqual(Decoding.decompress_data('test_encode.txt', 'test_codes.txt'), 'Hello')
    
    def test_get_guffmans_code(self):
        self.assertDictEqual(Decoding.get_huffmans_code('test_codes.txt')[0], 
                             {'0': 'l', '10': 'o', '110': 'H', '111': 'e'})
    
    def test_encodeing(self):
        self.assertEqual(Encoding.start('test.txt'), '1101110010')


if __name__ == '__main__':
    unittest.main()