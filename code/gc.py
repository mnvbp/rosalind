"""rosalind answer"""

file = "/Users/manavparikh/Downloads/rosalind_gc(5).txt"

def get_key(file: str) -> list:
    rawkey: list = []
    key: list = []
    with open(file, "r") as infile:
        for line in infile:
            if line[0] == '>':
                rawkey.append(line)
    for value in rawkey:
        key.append(value.strip())
    return (key)


def get_seq(file: str, key: str) -> dict:
    with open(file, "r") as infile:
        values: list = []
        #delete values before key
        for line in infile:
            values.append(line)
            if line == key + "\n":
                values = []
        concat: list = []
        #delete values after key
        for line in values:
            concat.append(line)
            if line[0] == ">" and line != key + "\n":
                concat.pop()
                break
        concat = ''.join(concat)
        answer = ""
        #strip line break
        for line in concat:
            answer = answer + line.strip()
        return (answer)


def get_gc(file: str, keys: list) -> dict:
    gc_content: dict = {}
    for value in keys:
        sequence = get_seq(file, value)
        length = len(sequence)
        c = sequence.count("C")
        g = sequence.count("G")
        percent = ((c + g) / length) * 100
        gc_content[value] = percent
    return (gc_content)

ans = (get_gc(file, get_key(file)))
print(max(zip(ans.values(), ans.keys())))
