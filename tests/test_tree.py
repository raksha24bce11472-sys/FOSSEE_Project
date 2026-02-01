"""
Unit tests for the Tree data structure module.
"""

import pytest
import os
import tempfile
from tree import Tree, TreeNode


class TestTreeNode:
    """Test cases for TreeNode class."""
    
    def test_node_creation(self):
        """Test creating a tree node."""
        node = TreeNode(value=10, name="test_node")
        assert node.value == 10
        assert node.name == "test_node"
        assert node.parent is None
        assert len(node.children) == 0
    
    def test_node_creation_without_name(self):
        """Test creating a node without explicit name."""
        node = TreeNode(value=42)
        assert node.value == 42
        assert node.name == "42"
    
    def test_add_child(self):
        """Test adding a child to a node."""
        parent = TreeNode(value="parent")
        child = TreeNode(value="child")
        
        result = parent.add_child(child)
        
        assert result == child
        assert child in parent.children
        assert child.parent == parent
        assert len(parent.children) == 1
    
    def test_add_multiple_children(self):
        """Test adding multiple children."""
        parent = TreeNode(value="parent")
        child1 = TreeNode(value="child1")
        child2 = TreeNode(value="child2")
        child3 = TreeNode(value="child3")
        
        parent.add_child(child1)
        parent.add_child(child2)
        parent.add_child(child3)
        
        assert len(parent.children) == 3
        assert child1 in parent.children
        assert child2 in parent.children
        assert child3 in parent.children
    
    def test_remove_child(self):
        """Test removing a child from a node."""
        parent = TreeNode(value="parent")
        child = TreeNode(value="child")
        parent.add_child(child)
        
        result = parent.remove_child(child)
        
        assert result is True
        assert child not in parent.children
        assert child.parent is None
        assert len(parent.children) == 0
    
    def test_remove_nonexistent_child(self):
        """Test removing a child that doesn't exist."""
        parent = TreeNode(value="parent")
        child = TreeNode(value="child")
        
        result = parent.remove_child(child)
        
        assert result is False
    
    def test_get_depth_root(self):
        """Test getting depth of root node."""
        root = TreeNode(value="root")
        assert root.get_depth() == 0
    
    def test_get_depth_nested(self):
        """Test getting depth of nested nodes."""
        root = TreeNode(value="root")
        child = TreeNode(value="child")
        grandchild = TreeNode(value="grandchild")
        
        root.add_child(child)
        child.add_child(grandchild)
        
        assert root.get_depth() == 0
        assert child.get_depth() == 1
        assert grandchild.get_depth() == 2
    
    def test_is_leaf(self):
        """Test checking if node is a leaf."""
        parent = TreeNode(value="parent")
        child = TreeNode(value="child")
        
        assert parent.is_leaf() is True
        
        parent.add_child(child)
        
        assert parent.is_leaf() is False
        assert child.is_leaf() is True
    
    def test_is_root(self):
        """Test checking if node is root."""
        root = TreeNode(value="root")
        child = TreeNode(value="child")
        
        assert root.is_root() is True
        
        root.add_child(child)
        
        assert root.is_root() is True
        assert child.is_root() is False
    
    def test_node_repr(self):
        """Test string representation of node."""
        node = TreeNode(value=100, name="test")
        repr_str = repr(node)
        assert "TreeNode" in repr_str
        assert "test" in repr_str
        assert "100" in repr_str


class TestTree:
    """Test cases for Tree class."""
    
    def test_tree_creation_empty(self):
        """Test creating an empty tree."""
        tree = Tree()
        assert tree.root is None
    
    def test_tree_creation_with_root(self):
        """Test creating a tree with a root node."""
        root = TreeNode(value="root")
        tree = Tree(root)
        assert tree.root == root
    
    def test_traverse_preorder_empty(self):
        """Test pre-order traversal on empty tree."""
        tree = Tree()
        result = tree.traverse_preorder()
        assert result == []
    
    def test_traverse_preorder(self):
        """Test pre-order traversal."""
        root = TreeNode(value=1, name="root")
        child1 = TreeNode(value=2, name="child1")
        child2 = TreeNode(value=3, name="child2")
        grandchild = TreeNode(value=4, name="grandchild")
        
        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild)
        
        tree = Tree(root)
        result = tree.traverse_preorder()
        
        assert len(result) == 4
        assert result[0] == root
        assert result[1] == child1
        assert result[2] == grandchild
        assert result[3] == child2
    
    def test_traverse_postorder_empty(self):
        """Test post-order traversal on empty tree."""
        tree = Tree()
        result = tree.traverse_postorder()
        assert result == []
    
    def test_traverse_postorder(self):
        """Test post-order traversal."""
        root = TreeNode(value=1, name="root")
        child1 = TreeNode(value=2, name="child1")
        child2 = TreeNode(value=3, name="child2")
        grandchild = TreeNode(value=4, name="grandchild")
        
        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild)
        
        tree = Tree(root)
        result = tree.traverse_postorder()
        
        assert len(result) == 4
        assert result[0] == grandchild
        assert result[1] == child1
        assert result[2] == child2
        assert result[3] == root
    
    def test_traverse_levelorder_empty(self):
        """Test level-order traversal on empty tree."""
        tree = Tree()
        result = tree.traverse_levelorder()
        assert result == []
    
    def test_traverse_levelorder(self):
        """Test level-order traversal."""
        root = TreeNode(value=1, name="root")
        child1 = TreeNode(value=2, name="child1")
        child2 = TreeNode(value=3, name="child2")
        grandchild1 = TreeNode(value=4, name="grandchild1")
        grandchild2 = TreeNode(value=5, name="grandchild2")
        
        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child2.add_child(grandchild2)
        
        tree = Tree(root)
        result = tree.traverse_levelorder()
        
        assert len(result) == 5
        assert result[0] == root
        assert result[1] == child1
        assert result[2] == child2
        assert result[3] == grandchild1
        assert result[4] == grandchild2
    
    def test_find_node_exists(self):
        """Test finding a node that exists."""
        root = TreeNode(value="root", name="root")
        child = TreeNode(value="child", name="target")
        root.add_child(child)
        
        tree = Tree(root)
        result = tree.find_node("target")
        
        assert result == child
    
    def test_find_node_not_exists(self):
        """Test finding a node that doesn't exist."""
        root = TreeNode(value="root", name="root")
        tree = Tree(root)
        result = tree.find_node("nonexistent")
        
        assert result is None
    
    def test_get_height_empty(self):
        """Test getting height of empty tree."""
        tree = Tree()
        assert tree.get_height() == 0
    
    def test_get_height_single_node(self):
        """Test getting height of single node tree."""
        root = TreeNode(value="root")
        tree = Tree(root)
        assert tree.get_height() == 0
    
    def test_get_height_multiple_levels(self):
        """Test getting height of multi-level tree."""
        root = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        grandchild = TreeNode(value=4)
        
        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild)
        
        tree = Tree(root)
        assert tree.get_height() == 2
    
    def test_get_node_count_empty(self):
        """Test counting nodes in empty tree."""
        tree = Tree()
        assert tree.get_node_count() == 0
    
    def test_get_node_count(self):
        """Test counting nodes in tree."""
        root = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        grandchild = TreeNode(value=4)
        
        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild)
        
        tree = Tree(root)
        assert tree.get_node_count() == 4
    
    def test_display_empty(self):
        """Test displaying empty tree."""
        tree = Tree()
        result = tree.display()
        assert result == ""
    
    def test_display_simple_tree(self):
        """Test displaying a simple tree."""
        root = TreeNode(value="Root", name="root")
        child = TreeNode(value="Child", name="child")
        root.add_child(child)
        
        tree = Tree(root)
        result = tree.display()
        
        assert "root" in result
        assert "child" in result
        assert "Root" in result
        assert "Child" in result
    
    def test_from_yaml(self):
        """Test loading tree from YAML file."""
        # Create a temporary YAML file
        yaml_content = """
name: root
value: Root Node
children:
  - name: child1
    value: Child 1
    children: []
  - name: child2
    value: Child 2
    children:
      - name: grandchild
        value: Grandchild
        children: []
"""
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
            f.write(yaml_content)
            temp_file = f.name
        
        try:
            tree = Tree.from_yaml(temp_file)
            
            assert tree.root is not None
            assert tree.root.name == "root"
            assert tree.root.value == "Root Node"
            assert len(tree.root.children) == 2
            assert tree.get_node_count() == 4
            
            # Check children
            child1 = tree.root.children[0]
            assert child1.name == "child1"
            assert child1.value == "Child 1"
            
            child2 = tree.root.children[1]
            assert child2.name == "child2"
            assert len(child2.children) == 1
            
            grandchild = child2.children[0]
            assert grandchild.name == "grandchild"
            
        finally:
            os.unlink(temp_file)
    
    def test_from_yaml_file_not_found(self):
        """Test loading tree from non-existent YAML file."""
        with pytest.raises(FileNotFoundError):
            Tree.from_yaml("nonexistent_file.yaml")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
