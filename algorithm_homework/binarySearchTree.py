import module
import random

# 이진 트리 노드 클래스 정의
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 이진 트리 클래스 정의
class BinaryTree:
    def __init__(self):
        self.root = None

    # 노드 삽입
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(value, self.root)

    def _insert_recursive(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(value, node.right)

    # 노드 검색
    def search(self, value):
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value, node):
        if node is None or node.value == value:
            return node
        elif value < node.value:
            return self._search_recursive(value, node.left)
        else:
            return self._search_recursive(value, node.right)

    # 노드 삭제
    def delete(self, value):
        self.root = self._delete_recursive(value, self.root)

    def _delete_recursive(self, value, node):
        if node is None:
            return node
        elif value < node.value:
            node.left = self._delete_recursive(value, node.left)
        elif value > node.value:
            node.right = self._delete_recursive(value, node.right)
        else:
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                min_right = self._find_min(node.right)
                node.value = min_right.value
                node.right = self._delete_recursive(min_right.value, node.right)
        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

# 랜덤한 숫자 20개 생성
numbers = module.randomNumberGenerator(20)

# 이진 트리 생성
tree = BinaryTree()
for number in numbers:
    tree.insert(number)

# 검색
search_value = random.choice(numbers)
found_node = tree.search(search_value)
print(f"Search {search_value}: {'Found' if found_node else 'Not Found'}")

# 삭제
delete_value = random.choice(numbers)
tree.delete(delete_value)
print(f"Delete {delete_value}")