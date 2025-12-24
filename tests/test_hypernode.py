import pytest
import sys
import uuid
import numpy as np

from core.hypergraph.base import HyperNode, NodeType, HyperEdge

class StandardNode:
    """A standard class without __slots__ for comparison."""
    def __init__(self, node_type, properties=None):
        self.id = uuid.uuid4()
        self.type = node_type
        self.properties = properties if properties else {}
        self.embeddings = {}

def test_hypernode_creation():
    node = HyperNode(NodeType.CONCEPT, {"name": "Test"})
    assert isinstance(node.id, uuid.UUID)
    assert node.type == NodeType.CONCEPT
    assert node.properties["name"] == "Test"
    assert isinstance(node.embeddings, dict)

def test_hypernode_slots_optimization():
    """
    Verify that HyperNode uses __slots__ and consumes less memory than a standard class.
    """
    # Create instances
    optimized_node = HyperNode(NodeType.ENTITY, {"data": "test"})
    standard_node = StandardNode(NodeType.ENTITY, {"data": "test"})

    # Check for __dict__ presence
    assert not hasattr(optimized_node, '__dict__'), "HyperNode should not have __dict__ when using __slots__"
    assert hasattr(standard_node, '__dict__'), "StandardNode should have __dict__"

    # Basic size check (shallow)
    # Note: sys.getsizeof doesn't account for referenced objects, but it shows the structure overhead
    size_optimized = sys.getsizeof(optimized_node)
    size_standard = sys.getsizeof(standard_node) + sys.getsizeof(standard_node.__dict__)

    # The optimized node structure should be smaller
    print(f"\nSize of optimized node (structure): {size_optimized} bytes")
    print(f"Size of standard node (structure + dict): {size_standard} bytes")

    assert size_optimized < size_standard, "Optimized node should use less memory for structure"

def test_hyperedge_creation():
    node_id1 = uuid.uuid4()
    node_id2 = uuid.uuid4()
    nodes = {node_id1, node_id2}
    edge = HyperEdge(nodes, "related_to", weight=0.5)

    assert isinstance(edge.id, uuid.UUID)
    assert edge.nodes == nodes
    assert edge.label == "related_to"
    assert edge.weight == 0.5
    assert not hasattr(edge, '__dict__')

def test_numpy_embedding():
    node = HyperNode(NodeType.TOKEN)
    embedding = np.array([0.1, 0.2, 0.3], dtype=np.float32)
    node.embeddings["bert"] = embedding

    assert "bert" in node.embeddings
    assert np.array_equal(node.embeddings["bert"], embedding)
