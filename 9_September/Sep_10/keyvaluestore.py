import asyncio
import random
from typing import Dict, List, Tuple

class Node:
    def __init__(self, node_id: int, peers: List[int]):
        self.id = node_id
        self.peers = peers
        self.data: Dict[str, str] = {}
        self.vector_clock: Dict[int, int] = {p: 0 for p in peers + [self.id]}

    async def put(self, key: str, value: str):
        self.data[key] = value
        self.vector_clock[self.id] += 1
        await self.propagate(key, value)

    async def get(self, key: str) -> str:
        return self.data.get(key, "Key not found")

    async def propagate(self, key: str, value: str):
        for peer in self.peers:
            try:
                await network.send(peer, ("update", key, value, self.vector_clock.copy()))
            except Exception as e:
                print(f"Failed to propagate to peer {peer}: {e}")

    async def receive_update(self, key: str, value: str, sender_clock: Dict[int, int]):
        if self.is_concurrent_or_newer(sender_clock):
            self.data[key] = value
            self.merge_vector_clocks(sender_clock)

    def is_concurrent_or_newer(self, sender_clock: Dict[int, int]) -> bool:
        return any(sender_clock[node] > self.vector_clock[node] for node in self.vector_clock)

    def merge_vector_clocks(self, sender_clock: Dict[int, int]):
        for node in self.vector_clock:
            self.vector_clock[node] = max(self.vector_clock[node], sender_clock.get(node, 0))

class Network:
    def __init__(self):
        self.nodes: Dict[int, Node] = {}

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    async def send(self, target: int, message: Tuple):
        if random.random() < 0.8:  # Simulating 20% packet loss
            await asyncio.sleep(random.uniform(0.1, 0.5))  # Simulating network delay
            await self.nodes[target].receive_update(*message[1:])

network = Network()

# Create a network of 5 nodes
nodes = [Node(i, [j for j in range(5) if j != i]) for i in range(5)]
for node in nodes:
    network.add_node(node)

async def simulate():
    # Simulate operations
    await nodes[0].put("key1", "value1")
    await asyncio.sleep(1)
    await nodes[2].put("key2", "value2")
    await asyncio.sleep(1)
    
    # Print final state
    for i, node in enumerate(nodes):
        print(f"Node {i} data: {node.data}")
        print(f"Node {i} vector clock: {node.vector_clock}")

asyncio.run(simulate())