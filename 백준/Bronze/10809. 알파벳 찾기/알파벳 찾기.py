S = input()

for i in range(97, 122):
    print(S.find(chr(i)), end=' ')
print(S.find(chr(122)))