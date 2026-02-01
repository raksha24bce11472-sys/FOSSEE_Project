import os
import tempfile
import unittest
from tree import Node, add_node_by_index_path, get_node_by_index_path, build_tree_from_yaml
class TestGeneralTree(unittest.TestCase):
    def test_add_and_get_by_index_path(self):
        root = Node(1)
        add_node_by_index_path(root, "", 10)
        add_node_by_index_path(root, "", 20)
        add_node_by_index_path(root, "0", 11)
        self.assertEqual(root.children[0].value, 10)
        self.assertEqual(root.children[1].value, 20)
        self.assertEqual(get_node_by_index_path(root, "0/0").value, 11)

    def test_invalid_path_raises(self):
        root = Node("x")
        with self.assertRaises(IndexError):
            get_node_by_index_path(root, "0")

    def test_build_tree_from_yaml(self):
        yaml_text = """\
value: 10
children:
  - value: 5
    children:
      - value: 3
      - value: 7
  - value: 15
    children:
      - value: 18
"""
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".yaml") as f:
            f.write(yaml_text)
            path = f.name

        try:
            root = build_tree_from_yaml(path)
            self.assertIsNotNone(root)
            self.assertEqual(root.value, 10)
            self.assertEqual([c.value for c in root.children], [5, 15])
            self.assertEqual([c.value for c in root.children[0].children], [3, 7])
            self.assertEqual([c.value for c in root.children[1].children], [18])
        finally:
            os.remove(path)
if __name__ == "__main__":
    unittest.main()
