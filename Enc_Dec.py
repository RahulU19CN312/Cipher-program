class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        
        plaintext = plaintext.replace(" ", "").upper()

        
        num_rows = len(plaintext) // self.key
        if len(plaintext) % self.key != 0:
            num_rows += 1

        
        grid = [['' for _ in range(self.key)] for _ in range(num_rows)]

        
        index = 0
        for col in range(self.key):
            for row in range(num_rows):
                if index < len(plaintext):
                    grid[row][col] = plaintext[index]
                    index += 1

        
        encrypted_message = ''.join([''.join(row) for row in grid])

        return encrypted_message

try:
    cipher_key = int(input("Enter the key : "))
    transposition_cipher = TranspositionCipher(cipher_key)
    plaintext_message = input("Enter Your Message : ")
    
    encrypted_message = transposition_cipher.encrypt(plaintext_message)

    print(f"Plaintext: {plaintext_message}")
    print(f"Encrypted: {encrypted_message}")
except:
    print("Enter integer value as key.")

