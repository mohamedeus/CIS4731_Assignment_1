from hashlib import sha256
import hashlib

HEX_DIGEST_FIND = "69d8c7575198a63bc8d97306e80c26e04015a9afdb92a699adaaac0b51570de7"

with open(r'CIS4731_Assignment_1\word_list\dict.txt') as file_in:
    for word in file_in:
        word_digest = hashlib.sha256(
            word.strip().encode("ascii", "ignore")).hexdigest()

        if (word_digest.__eq__(HEX_DIGEST_FIND)):
            print("Found Word: ")
            print(word + " -- " + word_digest)
        else:
            continue
