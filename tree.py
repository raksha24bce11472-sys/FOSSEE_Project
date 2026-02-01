from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Iterable, List, Optional, Sequence
import yaml

@dataclass(slots=True)
class Node:
    value: Any
    children: List["Node"] = field(default_factory=list) 
    def add_child(self, value: Any) -> "Node":
        child = Node(value)
        self.children.append(child)
        return child

def add_node_by_index_path(root: Node, path: str, value: Any) -> Node:
    target = get_node_by_index_path(root, path)
    return target.add_child(value)

def get_node_by_index_path(root: Node, path: str) -> Node:
    cur = root
    p = path.strip()
    if not p:
        return cur

    for raw in p.split("/"):
        if raw == "":
            raise ValueError(f"Invalid path '{path}'")
        i = int(raw)
        if i < 0 or i >= len(cur.children):
            raise IndexError(f"Invalid path '{path}': no child at index {i}")
        cur = cur.children[i]
    return cur


def print_tree(root: Optional[Node]) -> None:
    if root is None:
        print("Root:None")
        return
    print(f"Root:{root.value}")

    def _walk(node: Node, prefix: str) -> None:
        for idx, child in enumerate(node.children):
            print(f"{prefix}C{idx}---{child.value}")
            _walk(child, prefix + "    ")
    _walk(root, "    ")

def build_tree_from_yaml(yaml_file: str) -> Optional[Node]:
    with open(yaml_file, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    def _build(d: Any) -> Optional[Node]:
        if d is None:
            return None
        if not isinstance(d, dict) or "value" not in d:
            raise ValueError("Each YAML node must be a mapping with a 'value' key")

        node = Node(d["value"])
        children = d.get("children", []) or []
        if not isinstance(children, list):
            raise ValueError("'children' must be a YAML list (or omitted)")

        for child in children:
            built = _build(child)
            if built is not None:
                node.children.append(built)
        return node
    return _build(data)

def build_tree_from_edges(root_value: Any, edges: Sequence[tuple[str, Any]]) -> Node:
    root = Node(root_value)
    for path, value in edges:
        add_node_by_index_path(root, path, value)
    return root
