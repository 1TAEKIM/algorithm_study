S = input()

spell = 'abcdefghijklmnopqrstuvwxyz'
for i in spell:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1, end=' ')