import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __str__(self):
        return f"Block(index={self.index}, previous_hash={self.previous_hash}, timestamp={self.timestamp}, data={self.data}, nonce={self.nonce}, hash={self.hash})"

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", int(time.time()), "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        new_block = self.proof_of_work(new_block)
        self.chain.append(new_block)

    def proof_of_work(self, block, difficulty=4):
        required_prefix = '0' * difficulty
        while not block.hash.startswith(required_prefix):
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def __str__(self):
        chain_str = ""
        for block in self.chain:
            chain_str += str(block) + "\n"
        return chain_str

# Usage example
if __name__ == "__main__":
    my_blockchain = Blockchain()
    print("Genesis block:")
    print(my_blockchain)

    print("Adding new blocks:")
    my_blockchain.add_block(Block(1, "", int(time.time()), "Block 1 Data"))
    my_blockchain.add_block(Block(2, "", int(time.time()), "Block 2 Data"))

    print(my_blockchain)

    print(f"Blockchain valid? {my_blockchain.is_chain_valid()}")
