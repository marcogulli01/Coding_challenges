
# Solution of the challenge binary reversal proposed on Coderbyte at https://coderbyte.com/challenges

"""
First, we need to convert the given string to binary. After eliminating its two first characters, which are usually
0b, we should revert it. If its length is not a multiple of 8, we have to add as many 0s as necessary to obtain
a multiple of 8. Finally, we should convert the string to a binary number
"""

def BinaryReversal(string):
    n = str(bin(int(string)))[2:][::-1]
    if len(n) % 8 != 0:
        n += "0" * (8-(len(n) % 8))
    return int(n, 2)

# keep this function call here
print(BinaryReversal(input()))

