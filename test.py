s = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
n = []
entropy = [23,42,41,31,14,2,11,25,50,34,8,30,44,12,21]
sm = sum(entropy)

for i, c in enumerate(s):
    ind = i % len(entropy)
    n.append(ord(c)+sm-(i*entropy[i%len(entropy)])%0x18)
    
print(n)