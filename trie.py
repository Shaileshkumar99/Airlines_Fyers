class Node(object):
    def __init__(self, character):
        self.character = character
        self.left = None
        self.right = None
        self.middle = None
        self.root = None
        self.value = 0


class TST(object):

    def __init__(self):
        self.root = None

    def put(self, key, value):
        self.root = self.putitem(self.root, key, value, 0)

    def putitem(self, node, key, value, index):

        c = key[index]

        if node == None:
            node = Node(c)

        if c < node.character:
            node.left = self.putitem(node.left, key, value, index)
        elif c < node.character:
            node.right = self.putitem(node.right, key, value, index)
        elif index < len(key) - 1:
            node.middle = self.putitem(node.middle, key, value, index + 1)
        else:
            node.value = value

        return node

    def get(self, key):

        node = self.getitem(self.root, key, 0)

        if node == None:
            return -1

        return node.value

    def getitem(self, node, key, index):

        if node == None:
            return None
        c = key[index]

        if c < node.character:
            return self.getitem(node.left, key, index)
        elif c > node.character:
            return  self.getitem(node.right, key, index)
        elif index < len(key) -1:
            return  self.getitem(node.middle, key, index + 1)
        else:
            return node

if __name__ == "__main__":
    t = TST()
    t.put("apple",100)
    t.put("orange",90)

    print(t.get("something"))
