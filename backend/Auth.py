import hashlib
import os


def encrypt(key, block_size=6):
    hash_key = []
    if len(key) % block_size != 0:
        key += ' ' * (block_size - len(key) % block_size)

    blocks = [key[i:i + block_size] for i in range(0, len(key), block_size)]
    for i in range(len(blocks)):
        if i == len(blocks) - 1:
            hash_key.append(f"{blocks[0][0]}{blocks[i][1]}{blocks[0][2]}{blocks[0][3]}{blocks[i][4]}{blocks[i][5]}")
        else:
            hash_key.append(f"{blocks[i + 1][0]}{blocks[i][1]}{blocks[i + 1][2]}{blocks[i + 1][3]}{blocks[i][4]}{blocks[i][5]}")
    return ".".join(hash_key)


def decrypt(hash_key: str):
    hash_key = hash_key.split(".")
    result = ""
    for i in range(len(hash_key)):
        if i == 0:
            result += hash_key[-1][0]
            result += hash_key[i][1]
            result += hash_key[-1][2]
            result += hash_key[-1][3]
            result += hash_key[i][4]
            result += hash_key[i][5]
        else:
            result += hash_key[i - 1][0]
            result += hash_key[i][1]
            result += hash_key[i - 1][2]
            result += hash_key[i - 1][3]
            result += hash_key[i][4]
            result += hash_key[i][5]
    return result


def create_signature(key):
    key_bytes = key.encode('utf-8')
    nonce = os.urandom(16).hex()[:12]
    combined_data = key_bytes + nonce.encode('utf-8')
    h = hashlib.sha256()
    h.update(combined_data)
    signature = h.hexdigest()[:24] + nonce
    return signature


def verify_signature(key, signature):
    expected_hash = signature[:24]
    nonce = signature[24:]
    key_bytes = key.encode('utf-8')
    combined_data = key_bytes + nonce.encode('utf-8')
    h = hashlib.sha256()
    h.update(combined_data)
    return h.hexdigest()[:24] == expected_hash


class Auth:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create_token(self):
        signature = create_signature(self.secret_key)
        return encrypt(signature)

    def verify_token(self, token):
        signature = decrypt(token)
        return verify_signature(self.secret_key, signature)