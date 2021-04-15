def d_to_t(n):
    global b
    i = 7
    while n > 0:
        b[i] = str(n % 3) if n % 3 != 2 else 'x'
        n = n // 3
        i -= 1

b = ['0'] * 8
d_to_t(int(input()))
print(b)