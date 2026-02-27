from __future__ import annotations
from typing import Optional, Any


class TreeNode:
    def __init__(self, key: int, value: Any) -> None:
        self.key: int = key
        self.value: Any = value
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    # ===== INSERT =====
    def insert(self, key: int, value: Any) -> None:
        self.root = self._insert(self.root, key, value)

    def _insert(self, node: Optional[TreeNode], key: int, value: Any) -> TreeNode:
        if node is None:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            node.value = value

        return node

    # ===== SEARCH =====
    def search(self, key: int) -> Optional[Any]:
        node = self._search(self.root, key)
        return node.value if node else None

    def _search(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # ===== DELETE =====
    def delete(self, key: int) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # узел без детей
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # узел с двумя детьми
            min_node = self._min_value_node(node.right)
            node.key, node.value = min_node.key, min_node.value
            node.right = self._delete(node.right, min_node.key)

        return node

    def _min_value_node(self, node: TreeNode) -> TreeNode:
        while node.left:
            node = node.left
        return node

    # ===== HEIGHT =====
    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    # ===== BALANCED =====
    def is_balanced(self) -> bool:
        return self._check_balance(self.root) != -1

    def _check_balance(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left = self._check_balance(node.left)
        if left == -1:
            return -1

        right = self._check_balance(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)
