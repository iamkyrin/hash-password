import hashlib
data = b"Hello world"

print("Type in the password you want to hash: ")
user_input = input("")

encoded_input = user_input.encode('utf-8')

hash_obj = hashlib.sha512(encoded_input)

hex_digest = hash_obj.hexdigest()
print(hex_digest)
