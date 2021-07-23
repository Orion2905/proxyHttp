f = open('1.txt', 'r+')
f2 = open('2.txt', 'r+')
with f:
    for line in f:
        B = f2.write('http://'+line)
        print(B)