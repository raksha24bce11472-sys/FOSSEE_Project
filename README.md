# FOSSEE_Project

Developing a GUI application (as a Blender Addon) to alleviate the effort of constructing OpenFOAM cases.

## Binary Tree Implementation with YAML Integration

This repository includes a comprehensive binary tree implementation in Python with YAML serialization/deserialization capabilities.

### Features

- **Complete Binary Search Tree Implementation**
  - Insert, search, and delete operations
  - Three traversal methods: inorder, preorder, postorder
  - Tree properties: height and size calculation

- **YAML Integration**
  - Serialize tree to YAML format (string or file)
  - Deserialize tree from YAML format (string or file)
  - Roundtrip support with full data integrity

### Files

- `binary_tree.py` - Main implementation of the binary tree with YAML support
- `test_binary_tree.py` - Comprehensive test suite with 26 tests
- `example_usage.py` - Example demonstrating all features
- `requirements.txt` - Python dependencies (PyYAML)

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```python
from binary_tree import BinaryTree

# Create a tree and insert values
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

# Traversals
print(tree.inorder_traversal())  # [5, 10, 15]

# Search
node = tree.search(5)

# Delete
tree.delete(5)

# Serialize to YAML
yaml_str = tree.to_yaml()
tree.to_yaml("tree.yaml")  # Save to file

# Deserialize from YAML
tree2 = BinaryTree.from_yaml(yaml_str)
tree3 = BinaryTree.from_yaml("tree.yaml")  # Load from file
```

### Running Tests

```bash
python -m unittest test_binary_tree -v
```

### Running Examples

```bash
python example_usage.py
```

This will demonstrate:
- Basic tree operations (insert, search, delete, traversals)
- YAML serialization and deserialization
- Roundtrip testing (serialize -> deserialize)

