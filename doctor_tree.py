
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def find(self, node, name):
        if node is None:
            return None

        if node.name == name:
            return node

        left = self.find(node.left, name)
        if left is not None:
            return left

        return self.find(node.right, name)

    def insert(self, parent_name, doctor_name, side):
        if side not in ("left", "right"):
            return False

        parent = self.find(self.root, parent_name)

        if parent is None:
            return False

        if getattr(parent, side) is not None:
            return False

        if self.find(self.root, doctor_name) is not None:
            return False

        new_doctor = DoctorNode(doctor_name)

        if side == "left":
            parent.left = new_doctor
        else:
            parent.right = new_doctor

        return True

    def preorder(self, node):
        if node is None:
            return []

        return [node.name] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return []

        return self.inorder(node.left) + [node.name] + self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return []

        return self.postorder(node.left) + self.postorder(node.right) + [node.name]


if __name__ == "__main__":
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("Preorder:", tree.preorder(tree.root))
    print("Inorder:", tree.inorder(tree.root))
    print("Postorder:", tree.postorder(tree.root))

    print("Missing parent:", tree.insert("Dr. Smith", "Dr. Lee", "left"))
    print("Invalid side:", tree.insert("Dr. Croft", "Dr. Lee", "middle"))
