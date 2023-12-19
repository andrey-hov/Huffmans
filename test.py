import unittest
import Decoding
import Encoding
import Code_folders
import os


class InterpreterTest(unittest.TestCase):
    def test_huffman_tree(self):
        self.assertEqual(
            Encoding.build_huffman_tree({"a": 10, "b": 2}), [12, ["b", "0"], ["a", "1"]]
        )

    os.chdir('tests')

    def test_encoding_file(self):
        self.assertEqual(Encoding.start("test.txt"), "1101110010")

    def test_decode(self):
        self.assertEqual(
            Decoding.decompress_data("test_encode.txt"), "Hello"
        )

    def test_get_guffmans_code(self):
        self.assertDictEqual(
            Decoding.get_huffmans_code("test_codes.txt")[0],
            {"0": "l", "10": "o", "110": "H", "111": "e"},
        )

    def test_encod(self):
        self.assertEqual(open("test_encode.txt").read(), "1101110010")

    def test_encodeing(self):
        self.assertEqual(
            open("text2_encode.txt").read(),
            "1111111111010010001101100111000000010000101111",
        )

    def test_file(self):
        self.assertEqual(open("test.txt").read(), "Hello")

    def test_encode_folder(self):
        self.assertEqual(os.path.exists('test_folder/text1_encode'), True)
        self.assertEqual(os.path.exists('test_folder/text2_encode'), True)

    def test_decode_folder(self):
        self.assertEqual(os.path.exists('test_folder/text1_encode/text1_decode.txt'), True)
        self.assertEqual(os.path.exists('test_folder/text2_encode/text2_decode.txt'), True)


if __name__ == "__main__":
    unittest.main()
