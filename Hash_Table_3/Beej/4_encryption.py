# Encryption Table
# Plain Text: HELLOWORLD
# Cipher Text: DOGGEBEUGW
encode_table =  {
    "A": "H",
    "B": "Z",
    "C": "Y",
    "D": "W",
    "E": "O",
    "F": "R",
    "G": "J",
    "H": "D",
    "I": "P",
    "J": "T",
    "K": "I",
    "L": "G",
    "M": "L",
    "N": "C",
    "O": "E",
    "P": "X",
    "Q": "K",
    "R": "U",
    "S": "N",
    "T": "F",
    "U": "A",
    "V": "M",
    "W": "B",
    "X": "Q",
    "Y": "V",
    "Z": "S"
}

# reverse mapping of encode table
decode_table = {}

for k, v in encode_table.items(): # .items returns k,v tuples
    decode_table[v] = k # reverse k, v

def encode(s):
    r = ""

    for c in s:
        r += encode_table[c]

    return r

print(encode("HELLOWORLD"))

def decode(s):
    r = ""

    for c in s:
        r += decode_table[c]

    return r

print(decode("DOGGEBEUGW"))

# dictionaries are great for counting
def letter_count(s):
    d = {}

    for c in s:
        """
        if c not in d:
            d[c] = 1
        else:
            d[c] +=1
        """
        if c not in d:
            d[c] = 0
        d[c] +=1

    return d

print(letter_count("abbbaaaaccaddadada"))