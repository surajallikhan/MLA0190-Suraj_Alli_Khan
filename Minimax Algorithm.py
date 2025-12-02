INF = 10**9

class Node:
    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or []

def minimax(node, max_player):
    if not node.children:
        return node.value
    if max_player:
        best = -INF
        for c in node.children:
            best = max(best, minimax(c, False))
        return best
    else:
        best = INF
        for c in node.children:
            best = min(best, minimax(c, True))
        return best

if __name__ == "__main__":
    # simple example tree
    a = Node(children=[Node(3), Node(5), Node(2)])
    b = Node(children=[Node(9), Node(1), Node(4)])
    root = Node(children=[a, b])
    print("Minimax value:", minimax(root, True))