# В нашей структуре данных, в каждом узле бинарного дерева мы будем
# хранить указатель на левого и правого потомка.

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    # создали класс узла, а в конструкторе записали значение,
    # которое должно храниться в нём. Также инициализировали левого и правого потомка.

    def insert_left(self, next_value):  # метод для вставки на место левого потомка
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):  # метод для вставки на место правого потомка
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self


A_node = BinaryTree('A').insert_left('B').insert_right('C')
# В одной строчке мы создали корневой узел дерева, вставили левого потомка
# и затем — сразу правого. Получая ссылки на потомков через атрибуты left_child
# и right_child, можно проделать ту же самую цепочку действий, чтобы расширить дерево.

# Реализуйте структуру дерева при помощи класса BinaryTree.
# создаём корень и его потомков /7|2|5\
node_root = BinaryTree(2).insert_left(7).insert_right(5)
# левое поддерево корня /2|7|6\
node_7 = node_root.left_child.insert_left(2).insert_right(6)
# правое поддерево предыдущего узла /5|6|11\
node_6 = node_7.right_child.insert_left(5).insert_right(11)
# правое поддерево корня /|5|9\
node_5 = node_root.right_child.insert_right(9)
# левое поддерево предыдущего узла корня /4|9|\
node_9 = node_5.right_child.insert_left(4)
