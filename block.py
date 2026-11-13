import hashlib
import time

class Block:
    def __init__(self,index,data,previous_hash,miner_id):
        self.index=index
        self.timestamp=time.time()
        self.data=data
        self.previous_hash=previous_hash
        self.miner_id=miner_id
        self.nonce=0
        self.hash=self.calculate_hash()
        


    def calculate_hash(self):
        block_string=f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.miner_id}{self.nonce}"
        encoded_string=block_string.encode()
        return hashlib.sha256(encoded_string).hexdigest()



    def mine_block(self,difficulty):
        target= "0"*difficulty
        while self.hash[:difficulty]!=target:
            self.nonce+=1
            self.hash=self.calculate_hash()
        print(f"Block successfully mined! Hash: {self.hash}")


class Blockchain:
    def __init__(self):
        self.difficulty=4
        self.chain=[self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0,"genesis block", "0","System Admin")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self,new_block):
        new_block.previous_hash=self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

my_deai_chain= Blockchain()
print('mining block 1...\n')
my_deai_chain.add_block(Block(1,'shreyansh dubey 1', '','shreyanshdubey29_67318'))
print('mining block 2...\n')
my_deai_chain.add_block(Block(2,'shreyansh dubey 2', '','shreyansh'))

for block in my_deai_chain.chain:
    print(f'Index: {block.index}')
    print(f'Miner ID: {block.miner_id}')
    print(f'Nonce (Attempts): {block.nonce}')
    print(f'Data: {block.data}')
    print(f'Hash: {block.hash}')
    print(f'Previous hash: {block.previous_hash}')
    print('-'*30)
    
