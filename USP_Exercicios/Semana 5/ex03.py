def maior_primo(num):
    for c in range(num,0,-1):
        if c%2!=0 and c%3!=0:
            break
    return c
