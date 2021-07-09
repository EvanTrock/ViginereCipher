def caesarCipher():
    print("Caesar Cipher Encoder/Decoder")
    print("=============================")
    print("enter 1 to encode a message")
    print("enter 2 to decode a message")
    print("enter 3 to quit")
    userSelection = input()
    if userSelection == "1":
        print("Please Enter a phrase to Encrypt")
        phrase = input()
        print("Enter the key number to use for encrypting:")
        myKey = input()
        keyNumber = int(myKey)
        result = ""

        for i in range(len(phrase)):
            char = phrase[i]
            if ((ord(char) >= 65 and ord(char)<= 90) or (ord(char) >= 97 and ord(char)<= 122)):
                if (char.isupper()):
                    result += chr((ord(char) + keyNumber - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + keyNumber - 97) % 26 + 97)
            else:
                result += char
            print("The Encrypted ciphertext message is:" + result)
    if userSelection == "2":
        print("Please Enter a phrase to Decrypt")
        phrase = input()
        print("Enter the key number to use for Decrypting:")
        myKey = input()
        keyNumber = int(myKey)
        result = ""

        for i in range(len(phrase)):
            char = phrase[i]
            if ((ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122)):
                if (char.isupper()):
                    result += chr((ord(char) - keyNumber - 65) % 26 + 65)
                else:
                    result += chr((ord(char) - keyNumber - 97) % 26 + 97)
            else:
                result += char
            print("The Encrypted ciphertext message is:" + result)






if __name__ == '__main__':
    caesarCipher()
