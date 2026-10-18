import re

raw = open('preproinsulin-seq.txt').read()
seq = re.sub(r'[^a-z]', '', raw)
print("Preproinsulin:", len(seq), "characters")

parts = {
    "ls": seq[0:24],
    "b": seq[24:54],
    "c": seq[54:89],
    "a": seq[89:110],
}

for name, part in parts.items():
    print(name, len(part), part)
