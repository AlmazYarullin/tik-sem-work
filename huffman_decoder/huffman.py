from node import Node


class Huffman:
    DEFAULT_PROBABILITY_FILENAME = 'huffman_input.txt'

    def __init__(self, probability_filename=DEFAULT_PROBABILITY_FILENAME):
        self.probability_filename = probability_filename

        self.__symbols_probabilities = {}
        self.__symbols_codes = {}
        self.__tree_root = None

        self.__load_probabilities()
        self.__build_huffman_tree()

    def __load_probabilities(self):
        with open(self.probability_filename, 'r') as f:
            alphabet = f.readline().strip().split()
            probabilities = f.readline().strip().split()
            self.__symbols_probabilities = {alphabet[i]: float(probabilities[i]) for i in range(len(alphabet))}

    def __calculate_symbols_codes(self, node: Node, value=''):
        new_value = value + str(node.code)

        if node.left:
            self.__calculate_symbols_codes(node.left, new_value)
        if node.right:
            self.__calculate_symbols_codes(node.right, new_value)

        if not node.left and not node.right:
            self.__symbols_codes[node.symbol] = new_value

    def __build_huffman_tree(self):
        if not self.__symbols_probabilities:
            raise ValueError('Symbols probabilities are not initialized or empty!')

        symbols = self.__symbols_probabilities.keys()
        nodes = []

        for symbol in symbols:
            nodes.append(Node(self.__symbols_probabilities.get(symbol), symbol))

        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.probability)

            right = nodes[0]
            left = nodes[1]
            left.code = 1
            right.code = 0

            new_node = Node(left.probability + right.probability, left.symbol + right.symbol, left, right)

            nodes.remove(left)
            nodes.remove(right)
            nodes.append(new_node)

        self.__calculate_symbols_codes(nodes[0])
        self.__tree_root = nodes[0]

    def decode(self, encoded_data: str) -> str:
        current_node = self.__tree_root
        output = []
        for x in encoded_data:
            if x == '0':
                current_node = current_node.right
            elif x == '1':
                current_node = current_node.left

            if current_node.left is None and current_node.right is None:
                output.append(current_node.symbol)
                current_node = self.__tree_root

        return ''.join(output)
