# atelier3_challenge
# Custom Hash Function

This project contains a Python function that computes a unique hash for a given string using bitwise operations and arithmetic. It is a simple and efficient solution for basic hashing needs where security is not a primary concern.

## How It Works

The function `custom_hash(data)` follows these steps:

1. **Initialize**: Sets `hash_value` to 5381, a prime number commonly used in hash functions to reduce collisions.
2. **Iterate Through Characters**: For each character in the input string:
   - Left-shifts `hash_value` by 5 bits (multiplies by 32), adds the current `hash_value`, and performs XOR with the ASCII code of the character. This combines each character into the hash uniquely.
3. **Limit Hash Size**: Applies a bitwise AND with `0xFFFFFFFFFFFFFFFF` to ensure the hash remains within 64 bits.
4. **Return**: Outputs the result as a hexadecimal string.
