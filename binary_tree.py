"""
Binary Tree Implementation with YAML Integration

This module provides a complete binary tree implementation with support for:
- Tree construction and manipulation
- Various traversal methods
- YAML serialization and deserialization
"""

import os
import yaml
from typing import Any, Optional, List, Dict


class TreeNode:
    """Represents a node in a binary tree."""
    
    def __init__(self, value: Any, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        """
        Initialize a tree node.
        
        Args:
            value: The value stored in the node
            left: Left child node
            right: Right child node
        """
        self.value = value
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.value})"


class BinaryTree:
    """Binary Tree implementation with YAML support."""
    
    def __init__(self, root: Optional[TreeNode] = None):
        """
        Initialize a binary tree.
        
        Args:
            root: Root node of the tree
        """
        self.root = root
    
    def insert(self, value: Any) -> None:
        """
        Insert a value into the binary search tree.
        
        Args:
            value: Value to insert
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node: TreeNode, value: Any) -> TreeNode:
        """
        Recursively insert a value into the tree.
        
        Args:
            node: Current node
            value: Value to insert
            
        Returns:
            Updated node
        """
        if node is None:
            return TreeNode(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        
        return node
    
    def search(self, value: Any) -> Optional[TreeNode]:
        """
        Search for a value in the tree.
        
        Args:
            value: Value to search for
            
        Returns:
            Node containing the value, or None if not found
        """
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: Optional[TreeNode], value: Any) -> Optional[TreeNode]:
        """
        Recursively search for a value in the tree.
        
        Args:
            node: Current node
            value: Value to search for
            
        Returns:
            Node containing the value, or None if not found
        """
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def delete(self, value: Any) -> None:
        """
        Delete a value from the tree.
        
        Args:
            value: Value to delete
        """
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node: Optional[TreeNode], value: Any) -> Optional[TreeNode]:
        """
        Recursively delete a value from the tree.
        
        Args:
            node: Current node
            value: Value to delete
            
        Returns:
            Updated node
        """
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node to be deleted found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children: get the inorder successor
            min_larger_node = self._find_min(node.right)
            node.value = min_larger_node.value
            node.right = self._delete_recursive(node.right, min_larger_node.value)
        
        return node
    
    def _find_min(self, node: TreeNode) -> TreeNode:
        """
        Find the minimum value node in a subtree.
        
        Args:
            node: Root of subtree
            
        Returns:
            Node with minimum value
        """
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self) -> List[Any]:
        """
        Perform inorder traversal (left, root, right).
        
        Returns:
            List of values in inorder
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """
        Recursively perform inorder traversal.
        
        Args:
            node: Current node
            result: List to store values
        """
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> List[Any]:
        """
        Perform preorder traversal (root, left, right).
        
        Returns:
            List of values in preorder
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """
        Recursively perform preorder traversal.
        
        Args:
            node: Current node
            result: List to store values
        """
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> List[Any]:
        """
        Perform postorder traversal (left, right, root).
        
        Returns:
            List of values in postorder
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """
        Recursively perform postorder traversal.
        
        Args:
            node: Current node
            result: List to store values
        """
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def to_dict(self) -> Optional[Dict]:
        """
        Convert tree to dictionary representation.
        
        Returns:
            Dictionary representation of the tree
        """
        return self._node_to_dict(self.root)
    
    def _node_to_dict(self, node: Optional[TreeNode]) -> Optional[Dict]:
        """
        Convert a node and its subtree to dictionary.
        
        Args:
            node: Node to convert
            
        Returns:
            Dictionary representation of the node
        """
        if node is None:
            return None
        
        return {
            'value': node.value,
            'left': self._node_to_dict(node.left),
            'right': self._node_to_dict(node.right)
        }
    
    def to_yaml(self, file_path: Optional[str] = None) -> str:
        """
        Serialize tree to YAML format.
        
        Args:
            file_path: Optional file path to save YAML
            
        Returns:
            YAML string representation
        """
        tree_dict = self.to_dict()
        yaml_str = yaml.dump(tree_dict, default_flow_style=False, sort_keys=False)
        
        if file_path:
            with open(file_path, 'w') as f:
                f.write(yaml_str)
        
        return yaml_str
    
    @classmethod
    def from_dict(cls, data: Optional[Dict]) -> 'BinaryTree':
        """
        Create a binary tree from dictionary representation.
        
        Args:
            data: Dictionary representation of the tree
            
        Returns:
            New BinaryTree instance
        """
        if data is None:
            return cls(None)
        
        root = cls._dict_to_node(data)
        return cls(root)
    
    @classmethod
    def _dict_to_node(cls, data: Optional[Dict]) -> Optional[TreeNode]:
        """
        Convert dictionary to a node and its subtree.
        
        Args:
            data: Dictionary representation
            
        Returns:
            TreeNode instance
        """
        if data is None:
            return None
        
        node = TreeNode(data['value'])
        node.left = cls._dict_to_node(data.get('left'))
        node.right = cls._dict_to_node(data.get('right'))
        
        return node
    
    @classmethod
    def from_yaml(cls, yaml_input: str) -> 'BinaryTree':
        """
        Deserialize tree from YAML format.
        
        Args:
            yaml_input: YAML string or file path
            
        Returns:
            New BinaryTree instance
        """
        # Try to read as file first
        try:
            # Check if it looks like a file path (not containing newlines)
            if '\n' not in yaml_input and os.path.exists(yaml_input):
                with open(yaml_input, 'r') as f:
                    data = yaml.safe_load(f)
            else:
                # Treat as YAML string
                data = yaml.safe_load(yaml_input)
        except (FileNotFoundError, OSError):
            # If file operations fail, treat as YAML string
            data = yaml.safe_load(yaml_input)
        
        return cls.from_dict(data)
    
    def height(self) -> int:
        """
        Calculate the height of the tree.
        
        Returns:
            Height of the tree
        """
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node: Optional[TreeNode]) -> int:
        """
        Recursively calculate tree height.
        
        Args:
            node: Current node
            
        Returns:
            Height from this node
        """
        if node is None:
            return 0
        
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        
        return max(left_height, right_height) + 1
    
    def size(self) -> int:
        """
        Calculate the number of nodes in the tree.
        
        Returns:
            Number of nodes
        """
        return self._size_recursive(self.root)
    
    def _size_recursive(self, node: Optional[TreeNode]) -> int:
        """
        Recursively count nodes.
        
        Args:
            node: Current node
            
        Returns:
            Number of nodes in subtree
        """
        if node is None:
            return 0
        
        return 1 + self._size_recursive(node.left) + self._size_recursive(node.right)
