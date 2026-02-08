def encrypt(plaintext, key):
    ciphertext = ""
    for ch in plaintext:
        if ch.isupper():  
            ciphertext += chr((ord(ch) - ord('A') + key + 26) % 26 + ord('A'))
        elif ch.islower():  
            ciphertext += chr((ord(ch) - ord('a') + key + 26) % 26 + ord('a'))
        else:  
            ciphertext += ch
    return ciphertext
def decrypt(ciphertext, key):
    plaintext = ""
    for ch in ciphertext:
        if ch.isupper():  
            plaintext += chr((ord(ch) - ord('A') - key + 26) % 26 + ord('A'))
        elif ch.islower():
            plaintext += chr((ord(ch) - ord('a') - key + 26) % 26 + ord('a'))
        else:  
            plaintext += ch
    return plaintext


if __name__ == "__main__":
    while True:
        print("\n=== Caesar Cipher Program ===")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter your message to encrypt: ")
            shift = int(input("Enter the key (shift value): "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '2':
            message = input("Enter your message to decrypt: ")
            shift = int(input("Enter the key (shift value): "))
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
    print("=== Caesar Cipher Program ===")
    
    