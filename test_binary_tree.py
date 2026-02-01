"""
Test suite for Binary Tree implementation with YAML integration.
"""

import unittest
import os
import tempfile
from binary_tree import BinaryTree, TreeNode


class TestTreeNode(unittest.TestCase):
    """Tests for TreeNode class."""
    
    def test_node_creation(self):
        """Test creating a tree node."""
        node = TreeNode(10)
        self.assertEqual(node.value, 10)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)
    
    def test_node_with_children(self):
        """Test creating a node with children."""
        left = TreeNode(5)
        right = TreeNode(15)
        node = TreeNode(10, left, right)
        
        self.assertEqual(node.value, 10)
        self.assertEqual(node.left.value, 5)
        self.assertEqual(node.right.value, 15)
    
    def test_node_repr(self):
        """Test node string representation."""
        node = TreeNode(10)
        self.assertEqual(repr(node), "TreeNode(10)")


class TestBinaryTree(unittest.TestCase):
    """Tests for BinaryTree class."""
    
    def test_empty_tree(self):
        """Test creating an empty tree."""
        tree = BinaryTree()
        self.assertIsNone(tree.root)
        self.assertEqual(tree.size(), 0)
        self.assertEqual(tree.height(), 0)
    
    def test_insert_single_node(self):
        """Test inserting a single node."""
        tree = BinaryTree()
        tree.insert(10)
        
        self.assertIsNotNone(tree.root)
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.size(), 1)
        self.assertEqual(tree.height(), 1)
    
    def test_insert_multiple_nodes(self):
        """Test inserting multiple nodes."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        
        for value in values:
            tree.insert(value)
        
        self.assertEqual(tree.size(), 7)
        self.assertEqual(tree.height(), 3)
    
    def test_search_existing_value(self):
        """Test searching for an existing value."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7]
        
        for value in values:
            tree.insert(value)
        
        node = tree.search(7)
        self.assertIsNotNone(node)
        self.assertEqual(node.value, 7)
    
    def test_search_non_existing_value(self):
        """Test searching for a non-existing value."""
        tree = BinaryTree()
        values = [10, 5, 15]
        
        for value in values:
            tree.insert(value)
        
        node = tree.search(100)
        self.assertIsNone(node)
    
    def test_delete_leaf_node(self):
        """Test deleting a leaf node."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7]
        
        for value in values:
            tree.insert(value)
        
        tree.delete(3)
        self.assertIsNone(tree.search(3))
        self.assertEqual(tree.size(), 4)
    
    def test_delete_node_with_one_child(self):
        """Test deleting a node with one child."""
        tree = BinaryTree()
        values = [10, 5, 15, 3]
        
        for value in values:
            tree.insert(value)
        
        tree.delete(5)
        self.assertIsNone(tree.search(5))
        self.assertIsNotNone(tree.search(3))
        self.assertEqual(tree.size(), 3)
    
    def test_delete_node_with_two_children(self):
        """Test deleting a node with two children."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        
        for value in values:
            tree.insert(value)
        
        tree.delete(10)
        self.assertIsNone(tree.search(10))
        self.assertEqual(tree.size(), 6)
    
    def test_inorder_traversal(self):
        """Test inorder traversal."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        
        for value in values:
            tree.insert(value)
        
        result = tree.inorder_traversal()
        self.assertEqual(result, [3, 5, 7, 10, 12, 15, 17])
    
    def test_preorder_traversal(self):
        """Test preorder traversal."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        
        for value in values:
            tree.insert(value)
        
        result = tree.preorder_traversal()
        self.assertEqual(result, [10, 5, 3, 7, 15, 12, 17])
    
    def test_postorder_traversal(self):
        """Test postorder traversal."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        
        for value in values:
            tree.insert(value)
        
        result = tree.postorder_traversal()
        self.assertEqual(result, [3, 7, 5, 12, 17, 15, 10])


class TestYAMLIntegration(unittest.TestCase):
    """Tests for YAML serialization and deserialization."""
    
    def test_to_dict(self):
        """Test converting tree to dictionary."""
        tree = BinaryTree()
        values = [10, 5, 15]
        
        for value in values:
            tree.insert(value)
        
        tree_dict = tree.to_dict()
        
        self.assertIsNotNone(tree_dict)
        self.assertEqual(tree_dict['value'], 10)
        self.assertEqual(tree_dict['left']['value'], 5)
        self.assertEqual(tree_dict['right']['value'], 15)
    
    def test_from_dict(self):
        """Test creating tree from dictionary."""
        tree_dict = {
            'value': 10,
            'left': {'value': 5, 'left': None, 'right': None},
            'right': {'value': 15, 'left': None, 'right': None}
        }
        
        tree = BinaryTree.from_dict(tree_dict)
        
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.right.value, 15)
        self.assertEqual(tree.size(), 3)
    
    def test_to_yaml_string(self):
        """Test converting tree to YAML string."""
        tree = BinaryTree()
        values = [10, 5, 15]
        
        for value in values:
            tree.insert(value)
        
        yaml_str = tree.to_yaml()
        
        self.assertIn('value: 10', yaml_str)
        self.assertIn('value: 5', yaml_str)
        self.assertIn('value: 15', yaml_str)
    
    def test_to_yaml_file(self):
        """Test saving tree to YAML file."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7]
        
        for value in values:
            tree.insert(value)
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            temp_file = f.name
        
        try:
            yaml_str = tree.to_yaml(temp_file)
            
            self.assertTrue(os.path.exists(temp_file))
            
            with open(temp_file, 'r') as f:
                content = f.read()
            
            self.assertEqual(content, yaml_str)
            self.assertIn('value: 10', content)
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def test_from_yaml_string(self):
        """Test creating tree from YAML string."""
        yaml_str = """
value: 10
left:
  value: 5
  left: null
  right: null
right:
  value: 15
  left: null
  right: null
"""
        
        tree = BinaryTree.from_yaml(yaml_str)
        
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.right.value, 15)
        self.assertEqual(tree.size(), 3)
    
    def test_from_yaml_file(self):
        """Test loading tree from YAML file."""
        yaml_content = """
value: 10
left:
  value: 5
  left:
    value: 3
    left: null
    right: null
  right:
    value: 7
    left: null
    right: null
right:
  value: 15
  left: null
  right: null
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(yaml_content)
            temp_file = f.name
        
        try:
            tree = BinaryTree.from_yaml(temp_file)
            
            self.assertEqual(tree.root.value, 10)
            self.assertEqual(tree.size(), 5)
            self.assertEqual(tree.inorder_traversal(), [3, 5, 7, 10, 15])
        finally:
            if os.path.exists(temp_file):
                os.remove(temp_file)
    
    def test_roundtrip_yaml(self):
        """Test serializing and deserializing tree."""
        tree1 = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        
        for value in values:
            tree1.insert(value)
        
        yaml_str = tree1.to_yaml()
        tree2 = BinaryTree.from_yaml(yaml_str)
        
        self.assertEqual(tree1.inorder_traversal(), tree2.inorder_traversal())
        self.assertEqual(tree1.preorder_traversal(), tree2.preorder_traversal())
        self.assertEqual(tree1.postorder_traversal(), tree2.postorder_traversal())
        self.assertEqual(tree1.size(), tree2.size())
        self.assertEqual(tree1.height(), tree2.height())


class TestTreeProperties(unittest.TestCase):
    """Tests for tree property methods."""
    
    def test_height_empty_tree(self):
        """Test height of empty tree."""
        tree = BinaryTree()
        self.assertEqual(tree.height(), 0)
    
    def test_height_single_node(self):
        """Test height of tree with single node."""
        tree = BinaryTree()
        tree.insert(10)
        self.assertEqual(tree.height(), 1)
    
    def test_height_balanced_tree(self):
        """Test height of balanced tree."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        
        for value in values:
            tree.insert(value)
        
        self.assertEqual(tree.height(), 3)
    
    def test_size_empty_tree(self):
        """Test size of empty tree."""
        tree = BinaryTree()
        self.assertEqual(tree.size(), 0)
    
    def test_size_with_nodes(self):
        """Test size with multiple nodes."""
        tree = BinaryTree()
        values = [10, 5, 15, 3, 7, 12, 17]
        
        for value in values:
            tree.insert(value)
        
        self.assertEqual(tree.size(), 7)


if __name__ == '__main__':
    unittest.main()
