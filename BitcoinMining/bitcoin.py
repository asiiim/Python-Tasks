import time

from hashlib import sha256
MAX_NONCE = 1000000000

def SHA256(text):
    ''' This method returs the hash value of the given text '''

    # Encode the text
    encoded_text = text.encode("ascii")

    # Get the sha256 object of the encoded text
    sha256_obj = sha256(encoded_text)

    # Get the hash out of sha256 object
    hash_value = sha256_obj.hexdigest()

    return hash_value

def mine_bitcoin(block_number, transactions, prev_hash, prefix_zeroes):
    ''' This method takes the block number, transaction information, previous hased value and
        number of zeroes to be checked in the new hash value to be generated '''

    # Get prefix zeroes string
    prefix_zeroes_str = '0' * prefix_zeroes

    # Show the function is starting
    print("Mining Started !")

    # Hit and trial with variable nonce value with for loop to max range. 
    for nonce in range(MAX_NONCE):
        # Nonce is the number used once to get zeroes in the hash during hit and trial
        text =  str(block_number) + transactions + prev_hash + str(nonce)

        hash_val = SHA256(text)

        # Check if the computed hash contains the prefix zeroes
        if hash_val.startswith(prefix_zeroes_str):
            print(f"*** Congrats ***\nBitcoin is generated with nonce: {nonce}")
            return hash_val

    # Raise the exception if the method could not get the Hash value as expected.
    raise BaseException(f"Couldn't find the Hash after {MAX_NONCE} times !")

if __name__ == '__main__':
    
    # Dummy Transaction sample
    transactions = '''
        X -> Y -> 20,
        A -> B -> 15
    '''
    # Number of zero before hash currently its 20.
    difficulty_level = 6

    # Sample for of previous hash value
    prev_hash = 'b5d4045c3f466fa91fe2cc6abe79232a1a57cdf104f7a26e716e0a1e2789df78'

    # Track the start of the mining time
    start_time = time.time()
    new_hash = mine_bitcoin(5, transactions, prev_hash, difficulty_level)

    # Get the total time of mining
    total_time = str(time.time() - start_time)

    # Show mining details
    print(new_hash)
    print(f"It took {total_time} seconds to mine the coin !")