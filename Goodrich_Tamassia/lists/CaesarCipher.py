from random import randint


# Arguably the earliest encryption scheme is the Caesar cipher, which is named
# after Julius Caesar, who used this scheme to protect important military messages.
# The Caesar cipher involves replacing each letter in a message with the letter that
# is a certain number of letters after it in the alphabet.

# Given that strings are immutable, we cannot directly edit an instance to encrypt it.
# Instead, our goal will be to generate a new string. A convenient technique for performing
# string transformations is to create an equivalent list of characters, edit the
# list, and then reassemble a (new) string based on the list

# We can represent a replacement rule using another string to describe the translation
# We can precompute a string that represents the replacements that should be used for each character from A to Z
# We can subsequently use this translation string as a guide to encrypt a message. The remaining challenge is how to
# quickly locate the replacement for each character of the original message.
# Fortunately, we can rely on the fact that characters are represented in Unicode
# by integer code points, and the code points for the uppercase letters of the Latin
# alphabet are consecutive (for simplicity, we restrict our encryption to uppercase
# letters).

# Python supports functions that convert between integer code points and
# one-character strings. Specifically, the function ord(c) takes a one-character string
# as a parameter and returns the integer code point for that character. Conversely, the
# function chr(j) takes an integer and returns its associated one-character string.

# In order to find a replacement for a character in our Caesar cipher, we need to
# map the characters A to Z to the respective numbers 0 to 25. The formula for
# doing that conversion is j = ord(c) − ord( A ). As a sanity check, if character c
# is A , we have that j = 0. When c is B , we will find that its ordinal value is
# precisely one more than that for A , so their difference is 1. In general, the integer j
# that results from such a calculation can be used as an index into our precomputed
# translation string,

class CaesarCipher:
    """Class for doing encryption and decryption using a Caesar cipher."""

    def __init__(self, shift):
        """Construct Caesar cipher using given integer shift for rotation."""
        # encoder = [None] * 26  # temp array for encryption
        # decoder = [None] * 26  # temp array for decryption
        # for k in range(26):
        #     encoder[k] = chr((k + shift) % 26 + ord('A'))
        #     decoder[k] = chr((k - shift) % 26 + ord('A'))
        #
        # self._forward = ''.join(encoder)  # will store as string
        # self._backward = ''.join(decoder)  # since fixed

        # In two lines the above code is
        self._forward = ''.join([chr((k + shift) % 26 + ord('A')) for k in range(26)])  # will store as string
        self._backward = ''.join([chr((k - shift) % 26 + ord('A')) for k in range(26)])  # since fixed

    def encrypt(self, message):
        """Return string representing encripted message."""
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        """Return decrypted message given encrypted secret."""
        return self._transform(secret, self._backward)

    def _transform(self, original, code):
        """Utility to perform transformation based on given code string."""
        msg = list(original.upper())
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')  # index from 0 to 25
                msg[k] = code[j]  # replace this character
        return ''.join(msg)


# This implementation take more space, but it allows us to use whatever alphabet-based language provided as a parameter
class CaesarCipher2:

    def __init__(self, letters: [str], shift=None):
        int_to_char = {}
        char_to_int = {}

        for k in range(len(letters)):
            int_to_char[k] = letters[k]
            char_to_int[letters[k]] = k

        self.int_to_char = int_to_char
        self.char_to_int = char_to_int
        self.length = len(letters)

        if shift is None:
            self.shift = randint(2, 20)
        else:
            self.shift = shift

    def encrypt(self, plaintext: str):
        return self._transform(plaintext, self.shift)

    def decrypt(self, ciphertext: str):
        return self._transform(ciphertext, -self.shift)

    def _transform(self, original, shift):
        str_list = list(original.lower())
        for k in range(len(str_list)):
            if str_list[k] in self.char_to_int:
                shifted_index = (self.char_to_int[str_list[k]] + shift) % self.length
                str_list[k] = self.int_to_char[shifted_index]
        return ''.join(str_list)


if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)

    message = "There is a big dog on the bed, you can come for it"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)

    print('------------------------- VERSION 2 --------------------')
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    cipher = CaesarCipher2(abc, 3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)

    message = "There is a big dog on the bed, you can come for it"
    coded = cipher.encrypt(message)
    print('Secret: ', coded)
    answer = cipher.decrypt(coded)
    print('Message:', answer)
