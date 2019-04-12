#! python3
# 42_trianglewords.py


def wordsum(word):
    som = 0
    for letter in word:
        som += ord(letter) - ord('A') + 1
    return som


with open("42_words.txt", "r") as f:
    text = f.read()
    
words = text.replace("\"", "").split(",")

triangles = set([n * (n + 1) // 2 for n in range(1, 101)])
print(triangles)

res = []

for word in words:
    if wordsum(word) in triangles:
        res.append(word)
        
print(res)
print(len(res))
