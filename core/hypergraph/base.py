from enum import Enum
from typing import Dict, Any, Optional
import uuid
import numpy as np

class NodeType(Enum):
    CONCEPT = "concept"
    ENTITY = "entity"
    TOKEN = "token"
    ICON = "icon"

class HyperNode:
    """
    A node in the hypergraph.

    Optimized for memory usage using __slots__.
    """
    __slots__ = ('id', 'type', 'properties', 'embeddings')

    def __init__(
        self,
        node_type: NodeType,
        properties: Optional[Dict[str, Any]] = None,
        node_id: Optional[uuid.UUID] = None
    ):
        self.id = node_id if node_id else uuid.uuid4()
        self.type = node_type
        self.properties = properties if properties else {}
        self.embeddings: Dict[str, np.ndarray] = {}
