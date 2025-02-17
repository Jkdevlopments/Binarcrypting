# Mapping letters to numbers for encryption
data = {
    "a": 2, "b": 3, "c": 4, "d": 5, "e": 6, "f": 7, "g": 8, "h": 9, "i": 10,
    "j": 11, "k": 12, "l": 13, "m": 14, "n": 15, "o": 16, "p": 17, "q": 18, "r": 19,
    "s": 20, "t": 21, "u": 22, "v": 23, "w": 24, "x": 25, "y": 26, "z": 27, " ": 1, "$": 0
}

# Reverse mapping for decryption
datas = {v: k for k, v in data.items()}

# Function to encrypt a message
def encrypt_message(message):
    quotients = []
    remainders = []
    
    # Convert message to lowercase to handle uppercase input
    message = message.lower()
    
    for char in message:
        if char in data:
            quotients.append(data[char] // 2)
            remainders.append(data[char] % 2)
        else:
            print(f"Warning: Character '{char}' is not supported and will be ignored.")

    # Combine quotient and remainder lists
    combined_list = quotients + remainders

    # Adjust all 1s to 2s
    for i in range(len(combined_list)):
        if combined_list[i] == 1:
            combined_list[i] = 2

    # Convert numbers back to characters
    encrypted_message = "".join(datas[i] for i in combined_list)

    return encrypted_message, quotients, remainders  # Returning additional data for decryption

# Function to decrypt a message
def decrypt_message(encrypted_text, original_quotients, original_remainders):
    decrypted_numbers = [(original_quotients[i] * 2) + original_remainders[i] for i in range(len(original_quotients))]
    decrypted_message = "".join(datas[num] for num in decrypted_numbers)
    return decrypted_message

# User Input
message = input("Enter the message to encrypt: ")
encrypted_text, stored_quotients, stored_remainders = encrypt_message(message)
print("\nEncrypted message:", encrypted_text)

# Decrypting the message back
decrypted_text = decrypt_message(encrypted_text, stored_quotients, stored_remainders)
print("Decrypted message:", decrypted_text)