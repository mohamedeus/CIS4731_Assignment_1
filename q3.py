def make_block(lst):
    return (ord(lst[0]) << 24) + (ord(lst[1]) << 16) + (ord(lst[2]) << 8) + ord(lst[3])


def encrypt(message, key):
    rv = ""
    l = list(message)
    n = len(message)
    blocks = []
    for i in range(0, n, 4):  # break message into 4-character blocks
        if i+4 <= n:
            blocks.append(make_block(l[i: i+4]))
        else:  # pad end of message with white-space if the lenght is not divisible by 4
            end = l[i:n]
            end.extend((i+4-n)*[' '])
            blocks.append(make_block(end))
    extended_key = (key << 24) + (key << 16) + (key << 8) + (key)
    for block in blocks:  # encrypt each  block separately
        encrypted = str(hex(block ^ extended_key))[2:]
        for i in range(8 - len(encrypted)):
            rv += '0'
        rv += encrypted
    return rv


def decrypt_block(block):

    block_hex = str(hex(int(block)))
    letter1 = chr(int(block_hex[2:4], 16))
    letter2 = chr(int(block_hex[4:6], 16))
    letter3 = chr(int(block_hex[6:8], 16))
    letter4 = chr(int(block_hex[8:10], 16))
    return (letter1 + letter2 + letter3 + letter4)


def decrypt(cipher_text, key):
    plaintext = ""
    cipher_list = list(cipher_text)
    extended_key = (key << 24) + (key << 16) + (key << 8) + (key)
    decrypted_blocks = []
    n = len(cipher_text)

    for i in range(0, n, 8):
        j = i
        while (cipher_list[j] == '0'):
            cipher_list[j] = ''
            j += 1
        decrypted_blocks.append(str(
            int("".join(cipher_list[i:(i+8)]), 16)
            ^ extended_key))

    for block in decrypted_blocks:
        plaintext += decrypt_block(block)

    print("Decrypted Word:")
    print(plaintext)

    return plaintext

# Question 3 Part B


def find_word_with_cipher_text(cipher_text):
    key_word = {
    }
    with open(r'CIS4731_Assignment_1\word_list\dict.txt') as file_in:

        for word in file_in:
            for i in range(0, 256, 1):
                if (cipher_text == encrypt(word.strip(), i)):
                    key_word = {
                        'word': word.strip(),
                        'key': i
                    }
                    return key_word
                else:
                    key_word = {
                        'word': "Not found",
                        'key': "Not found"
                    }

    return key_word


print(find_word_with_cipher_text("10170d1c0b17180d10161718151003180d101617"))
