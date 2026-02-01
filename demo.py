"""
Demo script for the Tree data structure.

This script demonstrates the usage of the Tree class and its operations.
"""

from tree import Tree, TreeNode


def demo_manual_tree():
    """Demonstrate creating a tree manually."""
    print("=" * 60)
    print("Demo 1: Creating a Tree Manually")
    print("=" * 60)
    
    # Create root node
    root = TreeNode(value="Company", name="root")
    tree = Tree(root)
    
    # Add departments
    hr = TreeNode(value="HR", name="hr_dept")
    engineering = TreeNode(value="Engineering", name="eng_dept")
    sales = TreeNode(value="Sales", name="sales_dept")
    
    root.add_child(hr)
    root.add_child(engineering)
    root.add_child(sales)
    
    # Add employees under HR
    hr.add_child(TreeNode(value="Alice", name="hr_alice"))
    hr.add_child(TreeNode(value="Bob", name="hr_bob"))
    
    # Add teams under Engineering
    backend = TreeNode(value="Backend Team", name="backend")
    frontend = TreeNode(value="Frontend Team", name="frontend")
    engineering.add_child(backend)
    engineering.add_child(frontend)
    
    # Add engineers
    backend.add_child(TreeNode(value="Charlie", name="backend_charlie"))
    backend.add_child(TreeNode(value="David", name="backend_david"))
    frontend.add_child(TreeNode(value="Eve", name="frontend_eve"))
    
    # Add sales people
    sales.add_child(TreeNode(value="Frank", name="sales_frank"))
    
    print("\nTree Structure:")
    print(tree.display())
    
    print(f"Total nodes: {tree.get_node_count()}")
    print(f"Tree height: {tree.get_height()}")
    
    print("\nPre-order traversal:")
    for node in tree.traverse_preorder():
        print(f"  {node.name}: {node.value}")
    
    print("\nLevel-order traversal:")
    for node in tree.traverse_levelorder():
        print(f"  Level {node.get_depth()}: {node.name} ({node.value})")
    
    # Find a specific node
    print("\nFinding node 'backend':")
    node = tree.find_node("backend")
    if node:
        print(f"  Found: {node}")
        print(f"  Depth: {node.get_depth()}")
        print(f"  Is leaf: {node.is_leaf()}")
        print(f"  Children: {[child.name for child in node.children]}")


def demo_yaml_tree():
    """Demonstrate loading a tree from YAML."""
    print("\n" + "=" * 60)
    print("Demo 2: Loading a Tree from YAML")
    print("=" * 60)
    
    try:
        tree = Tree.from_yaml("sample_tree.yaml")
        
        print("\nTree Structure from YAML:")
        print(tree.display())
        
        print(f"Total nodes: {tree.get_node_count()}")
        print(f"Tree height: {tree.get_height()}")
        
        print("\nPost-order traversal:")
        for node in tree.traverse_postorder():
            print(f"  {node.name}: {node.value}")
    
    except FileNotFoundError:
        print("\nError: sample_tree.yaml not found!")
        print("Make sure the file exists in the current directory.")
    except Exception as e:
        print(f"\nError loading tree from YAML: {e}")


def demo_tree_operations():
    """Demonstrate various tree operations."""
    print("\n" + "=" * 60)
    print("Demo 3: Tree Operations")
    print("=" * 60)
    
    # Create a simple tree
    root = TreeNode(value=1, name="root")
    tree = Tree(root)
    
    child1 = TreeNode(value=2, name="child1")
    child2 = TreeNode(value=3, name="child2")
    child3 = TreeNode(value=4, name="child3")
    
    root.add_child(child1)
    root.add_child(child2)
    root.add_child(child3)
    
    grandchild1 = TreeNode(value=5, name="grandchild1")
    grandchild2 = TreeNode(value=6, name="grandchild2")
    child1.add_child(grandchild1)
    child1.add_child(grandchild2)
    
    print("\nInitial tree:")
    print(tree.display())
    
    print(f"Node 'child1' is leaf: {child1.is_leaf()}")
    print(f"Node 'grandchild1' is leaf: {grandchild1.is_leaf()}")
    print(f"Node 'root' is root: {root.is_root()}")
    print(f"Node 'child1' is root: {child1.is_root()}")
    
    print("\nRemoving 'grandchild2' from 'child1':")
    child1.remove_child(grandchild2)
    print(tree.display())
    
    print(f"Node count after removal: {tree.get_node_count()}")


def main():
    """Main function to run all demos."""
    print("\n" + "=" * 60)
    print("TREE DATA STRUCTURE DEMONSTRATION")
    print("=" * 60)
    
    demo_manual_tree()
    demo_yaml_tree()
    demo_tree_operations()
    
    print("\n" + "=" * 60)
    print("Demo Complete!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
