from tree import build_tree_from_edges, print_tree, build_tree_from_yaml
if __name__ == "__main__":
    root = build_tree_from_edges(
        "A",
        [
            ("", "B"), 
            ("", "C"), 
            ("0", "D"),
            ("0", "E"),
            ("1", "F"),
            ("0/0", "G"),
        ],
    )
    print("Tree after additions:")
    print_tree(root)
    yaml_file = "sample_tree.yaml"
    print(f"\nBuilding tree from '{yaml_file}':")
    yaml_root = build_tree_from_yaml(yaml_file)
    if yaml_root:
        print("\nTree built from YAML:")
        print_tree(yaml_root)
