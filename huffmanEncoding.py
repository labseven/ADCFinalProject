from collections import Counter, deque

"""
Huffman Coding library.
Author: Adam Novotny

genHuffmanTree(text)
    Given text, creates a huffman coding tree
    Returns: root, nodesDict {symbol: node}

genHuffmanFromFile(filename)
    Given a text file, generates a huffman coding tree
    Returns: root, nodesDict {symbol: node}

decodeHuffman(root, data)
    Given the root of a huffman tree (Tree()) and data ([1, 0]), decodes the data to symbols
    Returns: list of symbols

genHuffmanEncodeDict(root)
    Given the root of a huffman tree (Tree()), generates a dict to encode symbols
    Returns: dict {symbol: code} ( {'a': (1,0)} )

encodeHuffman(treeDict, message)
    given a huffman coding dict, encodes a message (str)
    Returns: list of bits ( [1,0,0,1] )
"""


class Tree():
    def __init__(self, data=None, left=None, right=None, parent=None, weight=None, layer=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.data = data
        self.weight = weight
        self.layer = layer

    def __str__(self):
        return("{}, {}".format(self.data, self.weight))

def genHuffmanTree(text):
    c = Counter(text)
    c = sorted(c.items(), key=lambda c: c[1])[::-1]

    nodes_remain = []
    nodes_dict = dict()
    for char in c:
        nodes_remain.append(Tree(data=char[0], weight=char[1]))
        nodes_dict[char[0]] = nodes_remain[-1]

    # for node in nodes_remain[::-1]:
    #     print(node)

    while len(nodes_remain) >= 2:
        node1 = nodes_remain.pop()
        node2 = nodes_remain.pop()

        new_node = Tree(left=node1, right=node2, weight=node1.weight+node2.weight)
        node1.parent = new_node
        node2.parent = new_node
        nodes_remain.append(new_node)
        # Inoptimal sorting. A better thing to do would be to append new nodes to a second list, and  compare the first two nodes in each list 
        nodes_remain = sorted(nodes_remain, key=lambda node: node.weight)[::-1]

    return nodes_remain[0], nodes_dict

def genHuffmanFromFile(filename):
    with open(filename, "r") as infile:
        data=infile.read().replace('\n', '')

    root, treeDict = genHuffmanTree(data)
    huffDict = genHuffmanEncodeDict(root)

    return root, huffDict


def printTree(root):
    nodes_remain = deque([root])

    i = 0
    while nodes_remain:
        i += 1
        node = nodes_remain.pop()

        if node.data:
            print(node.data, node.weight)
        else:
            nodes_remain.append(node.left)
            nodes_remain.append(node.right)

def decodeHuffman(root, data):
    curNode = root
    output = []
    for x in data:
        if x == 1:
            curNode = curNode.left
        if x == 0:
            curNode = curNode.right

        if curNode.data:
            output.append(curNode.data)
            curNode = root

    if curNode != root:
        print("error, bits remain")

    return output

def listToStr(inList):
    string = ""
    for x in inList:
        string = string + str(x)
    return string

def genHuffmanEncodeDict(root):
    huffDict = dict()
    curNode = root
    lastNode = root

    curEncode = []

    while True:
        if curNode.data:
            huffDict[curNode.data] = tuple(curEncode)
            lastNode = curNode
            curNode = curNode.parent
            curEncode.pop()

        elif curNode.right == lastNode:
            if curNode == root:
                break

            lastNode = curNode
            curNode = curNode.parent
            curEncode.pop()

        elif curNode.left == lastNode:
            lastNode = curNode
            curNode = curNode.right
            curEncode.append(0)

        else:
            lastNode = curNode
            curNode = curNode.left
            curEncode.append(1)

    return huffDict

def encodeHuffman(treeDict, message):
    data = []
    for c in message:
        data = data + list(treeDict[c])

    return data


if __name__ == '__main__':
    with open("english.txt", "r") as infile:
        data=infile.read().replace('\n', '')

    root, treeDict = genHuffmanTree(data)
    huffDict = genHuffmanEncodeDict(root)

    # print(huffDict)
    # for i in huffDict:
    #     print("{}: {}".format(i, huffDict[i]))

    message = encodeHuffman(huffDict, "hi, I'm doing well")

    printTree(root)

    print(message)
    decoded = decodeHuffman(root, message)
    print(listToStr(decoded))
