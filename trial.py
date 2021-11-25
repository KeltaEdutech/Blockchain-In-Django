import hashlib
import json

def hash(block):
    encoded_block = json.dumps(block, sort_keys = True).encode()
    return hashlib.sha256(encoded_block).hexdigest()

def is_chain_valid(chain):
    # Code goes here
    previous_block = chain[0]
    block_index = 1

    while block_index < len(chain):

        block = chain[block_index]
        if block['previous_hash'] != hash(previous_block):
            return False
        
        previous_nonce = previous_block['nonce']
        nonce = block['nonce']
        hash_operation = hashlib.sha256(str(nonce**2 - previous_nonce**2).encode()).hexdigest()
        
        if hash_operation[:4] != '0000':
            return False
        previous_block = block
        block_index += 1

    return True
    

f = open("file2.json", "r")
chain = json.loads(f.read())
print(is_chain_valid(chain['chain']))