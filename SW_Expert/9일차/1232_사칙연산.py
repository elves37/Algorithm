class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def in_order(_node):
    if _node is None:
        return
    in_order(_node.left)
    global box
    if _node.data[1] == '+':
        in_order(_node.right)
        _node.data[1] = str(float(_node.left.data[1]) + float(_node.right.data[1]))
        box.append(_node.data[1])
        while len(_node.data) > 2:
            _node.data.pop()
    elif _node.data[1] == '-':
        in_order(_node.right)
        _node.data[1] = str(float(_node.left.data[1]) - float(_node.right.data[1]))
        box.append(_node.data[1])
        while len(_node.data) > 2:
            _node.data.pop()
    elif _node.data[1] == '*':
        in_order(_node.right)
        _node.data[1] = str(float(_node.left.data[1]) * float(_node.right.data[1]))
        box.append(_node.data[1])
        while len(_node.data) > 2:
            _node.data.pop()
    elif _node.data[1] == '/':
        in_order(_node.right)
        _node.data[1] = str(float(_node.left.data[1]) / float(_node.right.data[1]))
        box.append(_node.data[1])
        while len(_node.data) > 2:
            _node.data.pop()
    else:
        in_order(_node.right)


T = 10
for test_case in range(1, T + 1):
    node_num = int(input())
    table = []
    new_table = []
    box = []
    for i in range(node_num):
        table = list(map(str, input().split()))
        node = Node(table)
        new_table.append(node)
    for i in range(node_num):
        for j in range(node_num):
            if len(new_table[i].data) >= 3:
                if new_table[i].data[2] == new_table[j].data[0]:
                    new_table[i].left = new_table[j]
            if len(new_table[i].data) == 4:
                if new_table[i].data[3] == new_table[j].data[0]:
                    new_table[i].right = new_table[j]
    in_order(new_table[0])
    print('#%d %d' % (test_case, float(box.pop())//1))
