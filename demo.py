from bst import BinarySearchTree

tree = BinarySearchTree()

tree.insert(50, "A")
tree.insert(30, "B")
tree.insert(70, "C")
tree.insert(20, "D")
tree.insert(40, "E")
tree.insert(60, "F")
tree.insert(80, "G")

print("Поиск 40:", tree.search(40))
print("Высота дерева:", tree.height())
print("Сбалансировано:", tree.is_balanced())

tree.delete(30)
print("После удаления 30:")
print("Поиск 30:", tree.search(30))
print("Высота дерева:", tree.height())
print("Сбалансировано:", tree.is_balanced())
