pair_dict = {
    "aa": "A", "ab": "B", "ac": "C", "ad": "D",
    "ba": "E", "bb": "F", "bc": "G", "bd": "H",
    "ca": "I", "cb": "J", "cc": "K", "cd": "L",
    "da": "M", "db": "N", "dc": "O", "dd": "P"

def compress(string):
    result = ''
    for x in range(0, 40, 2):
        pair = string[x:x + 2]
        result += pair_dict[pair]
    return result

pair_dict2 = {v: k for k, v in pair_dict.items()}

def decompress(string):
    result = ''
    for char in string:
        result += pair_dict2[char]
    return result