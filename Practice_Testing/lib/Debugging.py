# def say_hello(name):
#     return f"hello {name}"
# say_hello('kay')

# ##################


def encode(text, key):
    cipher = make_cipher(key)

    ciphertext_chars = []
    for i in text:
        # Sifting through given text to find where the error is
        # print(f"Letter '{i}")
        # print(f"Cipher index: {cipher.index(i)}")
        # print (cipher)
        ciphered_char = chr(65 + cipher.index(i)) # 'a' is expected
        ciphertext_chars.append(ciphered_char)
    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        # print(f"Letter i is: '{i}'")
        # print(f"Letter ord(i) is: {ord(i)}") 
        # print(f"Letter 65 - ord(i) is: {65 - ord(i)}")
        # print(f"Letter cipher[65 - ord(i)] is: {cipher[65 - ord(i)]}")

        # cipher[ord(i) - 65] - correct
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    # Gives the alphabet but with no 'a' or 'b' and a '{' at the end
    # alphabet = [chr(i + 96) for i in range(1, 26)] - original broken code

    # Debugged code - chr(97) is the beggining of the alphabet 0,26 for all values in
    # the alphabet
    alphabet = [chr(i + 97) for i in range(0, 26)]
    # print (alphabet)
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher


# print(f"""
# Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
# Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
# Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
# Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)

# ###################################################################


def get_most_common_letter(text):
    _text = ""
    for i in text:
        if i != " ":
            _text += i
    counter = {}
    for char in _text:
        counter[char] = counter.get(char, 0) + 1
        print (counter)
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(letter)
    return letter

print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
