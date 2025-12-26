import unittest
import uuid
import numpy as np
from core.hypergraph.base import HyperNode, NodeType

class TestHyperNode(unittest.TestCase):
    def test_initialization(self):
        node = HyperNode(NodeType.CONCEPT)
        self.assertIsInstance(node.id, uuid.UUID)
        self.assertEqual(node.type, NodeType.CONCEPT)
        self.assertEqual(node.properties, {})
        self.assertEqual(node.embeddings, {})

    def test_slots_optimization(self):
        node = HyperNode(NodeType.ENTITY)
        with self.assertRaises(AttributeError):
            node.new_attribute = "this should fail"

        # Verify slots are working
        self.assertFalse(hasattr(node, '__dict__'))

    def test_properties_and_embeddings(self):
        props = {"name": "test"}
        embeddings = {"vec": np.array([1, 2, 3])}
        node = HyperNode(NodeType.TOKEN, properties=props, embeddings=embeddings)

        self.assertEqual(node.properties["name"], "test")
        np.testing.assert_array_equal(node.embeddings["vec"], np.array([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()
