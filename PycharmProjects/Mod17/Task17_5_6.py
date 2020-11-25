"""
метод постфиксного обхода дерева в глубину
"""


def post_order(self):
    if self.left_child is not None:  # если левый потомок существует
        self.left_child.post_order()  # рекурсивно вызываем функцию

    if self.right_child is not None:  # если правый потомок существует
        self.right_child.post_order()  # рекурсивно вызываем функцию

    print(self.value)  # процедура обработки
