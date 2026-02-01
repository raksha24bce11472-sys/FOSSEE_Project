"""
Tree Data Structure Module

This module provides a simple tree data structure implementation with basic operations
like adding nodes, traversing, and loading from YAML configuration.
"""

import yaml
from collections import deque
from typing import List, Optional, Any, Dict


class TreeNode:
    """A node in a tree structure."""
    
    def __init__(self, value: Any, name: Optional[str] = None):
        """
        Initialize a tree node.
        
        Args:
            value: The value stored in the node
            name: Optional name for the node
        """
        self.value = value
        self.name = name or str(value)
        self.children: List[TreeNode] = []
        self.parent: Optional[TreeNode] = None
    
    def add_child(self, child: 'TreeNode') -> 'TreeNode':
        """
        Add a child node to this node.
        
        Args:
            child: The child node to add
            
        Returns:
            The added child node
        """
        child.parent = self
        self.children.append(child)
        return child
    
    def remove_child(self, child: 'TreeNode') -> bool:
        """
        Remove a child node from this node.
        
        Args:
            child: The child node to remove
            
        Returns:
            True if the child was removed, False otherwise
        """
        if child in self.children:
            child.parent = None
            self.children.remove(child)
            return True
        return False
    
    def get_depth(self) -> int:
        """
        Get the depth of this node in the tree.
        
        Returns:
            The depth (0 for root)
        """
        depth = 0
        current = self.parent
        while current is not None:
            depth += 1
            current = current.parent
        return depth
    
    def is_leaf(self) -> bool:
        """
        Check if this node is a leaf (has no children).
        
        Returns:
            True if the node is a leaf, False otherwise
        """
        return len(self.children) == 0
    
    def is_root(self) -> bool:
        """
        Check if this node is the root (has no parent).
        
        Returns:
            True if the node is the root, False otherwise
        """
        return self.parent is None
    
    def __repr__(self) -> str:
        return f"TreeNode(name='{self.name}', value={self.value})"


class Tree:
    """A tree data structure."""
    
    def __init__(self, root: Optional[TreeNode] = None):
        """
        Initialize a tree.
        
        Args:
            root: The root node of the tree
        """
        self.root = root
    
    def traverse_preorder(self, node: Optional[TreeNode] = None) -> List[TreeNode]:
        """
        Traverse the tree in pre-order (root, left, right).
        
        Args:
            node: The starting node (defaults to root)
            
        Returns:
            List of nodes in pre-order
        """
        if node is None:
            node = self.root
        
        if node is None:
            return []
        
        result = [node]
        for child in node.children:
            result.extend(self.traverse_preorder(child))
        return result
    
    def traverse_postorder(self, node: Optional[TreeNode] = None) -> List[TreeNode]:
        """
        Traverse the tree in post-order (left, right, root).
        
        Args:
            node: The starting node (defaults to root)
            
        Returns:
            List of nodes in post-order
        """
        if node is None:
            node = self.root
        
        if node is None:
            return []
        
        result = []
        for child in node.children:
            result.extend(self.traverse_postorder(child))
        result.append(node)
        return result
    
    def traverse_levelorder(self) -> List[TreeNode]:
        """
        Traverse the tree in level-order (breadth-first).
        
        Returns:
            List of nodes in level-order
        """
        if self.root is None:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node)
            queue.extend(node.children)
        
        return result
    
    def find_node(self, name: str) -> Optional[TreeNode]:
        """
        Find a node by name.
        
        Args:
            name: The name of the node to find
            
        Returns:
            The found node or None
        """
        for node in self.traverse_preorder():
            if node.name == name:
                return node
        return None
    
    def get_height(self, node: Optional[TreeNode] = None) -> int:
        """
        Get the height of the tree from a given node.
        
        Args:
            node: The starting node (defaults to root)
            
        Returns:
            The height of the tree
        """
        if node is None:
            node = self.root
        
        if node is None or node.is_leaf():
            return 0
        
        return 1 + max(self.get_height(child) for child in node.children)
    
    def get_node_count(self) -> int:
        """
        Get the total number of nodes in the tree.
        
        Returns:
            The number of nodes
        """
        return len(self.traverse_preorder())
    
    def display(self, node: Optional[TreeNode] = None, prefix: str = "", is_last: bool = True) -> str:
        """
        Display the tree structure as a string.
        
        Args:
            node: The starting node (defaults to root)
            prefix: Prefix for indentation
            is_last: Whether this is the last child
            
        Returns:
            String representation of the tree
        """
        if node is None:
            node = self.root
        
        if node is None:
            return ""
        
        result = prefix
        result += "└── " if is_last else "├── "
        result += f"{node.name} ({node.value})\n"
        
        prefix += "    " if is_last else "│   "
        
        for i, child in enumerate(node.children):
            is_last_child = i == len(node.children) - 1
            result += self.display(child, prefix, is_last_child)
        
        return result
    
    @staticmethod
    def from_yaml(yaml_file: str) -> 'Tree':
        """
        Load a tree structure from a YAML file.
        
        Args:
            yaml_file: Path to the YAML file
            
        Returns:
            A Tree object
        """
        with open(yaml_file, 'r') as f:
            data = yaml.safe_load(f)
        
        def build_node(node_data: Dict) -> TreeNode:
            """Build a tree node from YAML data."""
            node = TreeNode(
                value=node_data.get('value', ''),
                name=node_data.get('name', str(node_data.get('value', '')))
            )
            
            for child_data in node_data.get('children', []):
                child = build_node(child_data)
                node.add_child(child)
            
            return node
        
        root_node = build_node(data)
        return Tree(root_node)
