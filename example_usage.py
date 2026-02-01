"""
Example usage of Binary Tree with YAML integration.

This script demonstrates various features of the binary tree implementation.
"""

from binary_tree import BinaryTree


def example_basic_operations():
    """Demonstrate basic tree operations."""
    print("=" * 50)
    print("Basic Binary Tree Operations")
    print("=" * 50)
    
    # Create a new tree and insert values
    tree = BinaryTree()
    values = [10, 5, 15, 3, 7, 12, 17, 1, 4, 6, 8]
    
    print(f"\nInserting values: {values}")
    for value in values:
        tree.insert(value)
    
    print(f"Tree size: {tree.size()}")
    print(f"Tree height: {tree.height()}")
    
    # Search operations
    print("\n--- Search Operations ---")
    search_value = 7
    result = tree.search(search_value)
    if result:
        print(f"Found {search_value} in the tree")
    else:
        print(f"{search_value} not found in the tree")
    
    search_value = 100
    result = tree.search(search_value)
    if result:
        print(f"Found {search_value} in the tree")
    else:
        print(f"{search_value} not found in the tree")
    
    # Traversal operations
    print("\n--- Traversal Operations ---")
    print(f"Inorder traversal: {tree.inorder_traversal()}")
    print(f"Preorder traversal: {tree.preorder_traversal()}")
    print(f"Postorder traversal: {tree.postorder_traversal()}")
    
    # Delete operation
    print("\n--- Delete Operation ---")
    delete_value = 5
    print(f"Deleting {delete_value}...")
    tree.delete(delete_value)
    print(f"Inorder traversal after deletion: {tree.inorder_traversal()}")
    print(f"Tree size after deletion: {tree.size()}")


def example_yaml_serialization():
    """Demonstrate YAML serialization."""
    print("\n" + "=" * 50)
    print("YAML Serialization")
    print("=" * 50)
    
    # Create a tree
    tree = BinaryTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    
    print(f"\nCreating tree with values: {values}")
    for value in values:
        tree.insert(value)
    
    # Convert to YAML
    print("\n--- Tree as YAML ---")
    yaml_str = tree.to_yaml()
    print(yaml_str)
    
    # Save to file
    file_path = "tree_example.yaml"
    tree.to_yaml(file_path)
    print(f"Tree saved to {file_path}")


def example_yaml_deserialization():
    """Demonstrate YAML deserialization."""
    print("\n" + "=" * 50)
    print("YAML Deserialization")
    print("=" * 50)
    
    # Load from file
    file_path = "tree_example.yaml"
    print(f"\nLoading tree from {file_path}")
    tree = BinaryTree.from_yaml(file_path)
    
    print(f"Loaded tree size: {tree.size()}")
    print(f"Loaded tree height: {tree.height()}")
    print(f"Inorder traversal: {tree.inorder_traversal()}")
    
    # Load from YAML string
    print("\n--- Loading from YAML string ---")
    yaml_string = """
value: 100
left:
  value: 50
  left:
    value: 25
    left: null
    right: null
  right:
    value: 75
    left: null
    right: null
right:
  value: 150
  left: null
  right: null
"""
    
    tree2 = BinaryTree.from_yaml(yaml_string)
    print(f"Tree from string - Inorder: {tree2.inorder_traversal()}")


def example_roundtrip():
    """Demonstrate roundtrip serialization/deserialization."""
    print("\n" + "=" * 50)
    print("Roundtrip Test (Serialize -> Deserialize)")
    print("=" * 50)
    
    # Create original tree
    original_tree = BinaryTree()
    values = [45, 25, 65, 15, 35, 55, 75, 10, 20, 30, 40]
    
    print(f"\nOriginal tree values: {values}")
    for value in values:
        original_tree.insert(value)
    
    print(f"Original inorder: {original_tree.inorder_traversal()}")
    
    # Serialize to YAML
    yaml_str = original_tree.to_yaml()
    
    # Deserialize from YAML
    restored_tree = BinaryTree.from_yaml(yaml_str)
    
    print(f"Restored inorder: {restored_tree.inorder_traversal()}")
    
    # Verify they match
    if original_tree.inorder_traversal() == restored_tree.inorder_traversal():
        print("\n✓ Roundtrip successful! Trees match perfectly.")
    else:
        print("\n✗ Roundtrip failed! Trees don't match.")


def main():
    """Run all examples."""
    example_basic_operations()
    example_yaml_serialization()
    example_yaml_deserialization()
    example_roundtrip()
    
    print("\n" + "=" * 50)
    print("Examples completed!")
    print("=" * 50)


if __name__ == "__main__":
    main()
