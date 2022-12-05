from huffman import Huffman


def main():
    huffman = Huffman()
    encoded_data = input("Enter encoded data: ")
    print("Output:", huffman.decode(encoded_data), sep='\n')


if __name__ == '__main__':
    main()
