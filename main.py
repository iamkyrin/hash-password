import hashlib


try:
    while True:
        if 1 == 1:
            user_input = input("Type in the password you want to hash: ")

            encoded_input = user_input.encode('utf-8')

            hash_obj = hashlib.sha512(encoded_input)

            hex_digest = hash_obj.hexdigest()
            print(hex_digest)
            user_input2 = input("Do you wish to exit? (Y/N): ").lower()
            if user_input2 == "y":
                break
            elif user_input2 == "n":
                pass

except Exception as error:
    print(error)
    print("Error while running")
