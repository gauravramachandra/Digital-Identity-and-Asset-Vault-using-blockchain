#Import libraries
import random
from Block import Block

class Blockchain:
    """
    A class representing a blockchain with proof of work consensus mechanism.
    """
    # Difficult for proof of work
    difficulty = 3

    def __init__(self):
        """
        Initialize a new blockchain with a genesis block.
        """
        self.pending = [] # pending list of data that needs to go on chain.
        self.chain = [] # blockchain
        genesis_block = Block(0, [], "0") #create a new intital block 
        genesis_block.hash = genesis_block.generate_hash() #generate hash for that block
        self.chain.append(genesis_block) #append it to our chain

    def add_block(self, block, hashl):
        """
        Add a block to the chain after verifying and validating it.
        
        Args:
            block (Block): The block to be added
            hashl (str): Hash of the block
            
        Returns:
            bool: True if block was added successfully, False otherwise
        """
        try:
            prev_hash = self.last_block().hash
            if (prev_hash == block.prev_hash and self.is_valid(block, hashl)):
                block.hash = hashl
                self.chain.append(block)
                return True
            return False
        except Exception as e:
            print(f"Error adding block: {str(e)}")
            return False

    def mine(self):
        """
        Mine a new block with pending transactions.
        
        Returns:
            int/bool: Index of the new block if successful, False otherwise
        """
        try:
            if(len(self.pending) > 0):
                last_block = self.last_block()
                new_block = Block(last_block.index + 1, self.pending, last_block.hash)
                hashl = self.p_o_w(new_block)
                self.add_block(new_block, hashl)
                self.pending = []
                return new_block.index
            return False
        except Exception as e:
            print(f"Error mining block: {str(e)}")
            return False

    def p_o_w(self, block):
        """
        Generate proof of work with random nonce.
        
        Args:
            block (Block): Block to generate proof of work for
            
        Returns:
            str: Hash that meets difficulty requirement
        """
        try:
            block.nonce = 0
            get_hash = block.generate_hash()
            while not get_hash.startswith("0" * Blockchain.difficulty):
                block.nonce = random.randint(0, 99999999)
                get_hash = block.generate_hash()
            return get_hash
        except Exception as e:
            print(f"Error in proof of work: {str(e)}")
            return None

    def p_o_w_2(self, block):
        """
        Generate proof of work with incremental nonce.
        
        Args:
            block (Block): Block to generate proof of work for
            
        Returns:
            str: Hash that meets difficulty requirement
        """
        try:
            block.nonce = 0
            get_hash = block.generate_hash()
            while not get_hash.startswith("0" * Blockchain.difficulty):
                block.nonce += 1
                get_hash = block.generate_hash()
            return get_hash
        except Exception as e:
            print(f"Error in proof of work: {str(e)}")
            return None

    def add_pending(self, transaction):
        """
        Add a new transaction to pending list.
        
        Args:
            transaction: Transaction to be added
        """
        try:
            self.pending.append(transaction)
        except Exception as e:
            print(f"Error adding pending transaction: {str(e)}")
        
    def check_chain_validity(self, chain):
        """
        Check if the entire chain is valid.
        
        Args:
            chain (list): List of blocks to validate
            
        Returns:
            bool: True if chain is valid, False otherwise
        """
        try:
            result = True
            prev_hash = "0"
            for block in chain:
                block_hash = block.hash
                if self.is_valid(block, block.hash) and prev_hash == block.prev_hash:
                    block.hash = block_hash
                    prev_hash = block_hash
                else:
                    result = False
            return result
        except Exception as e:
            print(f"Error checking chain validity: {str(e)}")
            return False

    @classmethod
    def is_valid(cls, block, block_hash):
        """
        Check if a block's hash is valid.
        
        Args:
            block (Block): Block to validate
            block_hash (str): Hash to validate against
            
        Returns:
            bool: True if hash is valid, False otherwise
        """
        try:
            if block_hash.startswith("0" * Blockchain.difficulty):
                return block.generate_hash() == block_hash
            return False
        except Exception as e:
            print(f"Error validating block: {str(e)}")
            return False

    def last_block(self):
        """
        Get the last block in the chain.
        
        Returns:
            Block: The last block in the chain
        """
        try:
            return self.chain[-1]
        except IndexError:
            print("Error: Chain is empty")
            return None
