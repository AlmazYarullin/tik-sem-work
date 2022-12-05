class MoveToFront:
    DEFAULT_ALPHABET_FILENAME = "alphabet.txt"

    def __init__(self, alphabet_filename=DEFAULT_ALPHABET_FILENAME):
        self.__alphabet = tuple()
        self.__alphabet_filename = alphabet_filename
        self.__read_alphabet()

    def __read_alphabet(self):
        with open(self.__alphabet_filename, 'r', encoding='utf-8') as f:
            self.alphabet = tuple(f.readline().strip().split())

    def decode(self, message: str) -> str:
        raise NotImplementedError('Ask Amir Gaifullin if you wish to decode')

    def set_ascii_alphabet(self):
        self.__alphabet = tuple((chr(i) for i in range(128)))

    def encode(self, message: str) -> list:
        alphabet = list(self.alphabet)
        sequence = []

        for symbol in message:
            symbol_index = alphabet.index(symbol)
            sequence.append(symbol_index)
            alphabet.insert(0, alphabet.pop(symbol_index))

        return sequence
