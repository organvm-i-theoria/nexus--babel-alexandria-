import uuid
from enum import Enum
from typing import Any, Dict, Optional
import numpy as np

class NodeType(Enum):
    CONCEPT = "concept"
    ENTITY = "entity"
    TOKEN = "token"
    ICON = "icon"

class HyperNode:
    """
    Base node class for the Hypergraph.
    Optimized for memory usage using __slots__.
    """
    __slots__ = ('id', 'type', 'properties', 'embeddings')

    def __init__(
        self,
        node_type: NodeType,
        properties: Optional[Dict[str, Any]] = None,
        embeddings: Optional[Dict[str, np.ndarray]] = None,
        node_id: Optional[uuid.UUID] = None
    ):
        self.id = node_id or uuid.uuid4()
        self.type = node_type
        # Lazy initialization for properties and embeddings can be handled
        # by defaulting to empty dicts only when accessed, but for __slots__
        # we typically just initialize them.
        # To strictly follow "lazy initialization" memory tip:
        # We could set them to None and init on property access, but that adds overhead.
        # For now, we'll stick to the __slots__ optimization as the primary one.
        self.properties = properties if properties is not None else {}
        self.embeddings = embeddings if embeddings is not None else {}

    def __repr__(self):
        return f"<HyperNode id={self.id} type={self.type.value}>"
