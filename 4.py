#!/usr/bin/python3.3

largest_Palindrome = 0
a = 999

while a > 900:
    if a % 11 == 0: #NO TATO PODMIENKA BY MA ZAUJIMALA PRECO TU JE.
        for b in range(999, 900, -1):
            c = a * b
            c = str(c)
            d = c[5] + c[4] + c[3]
            e = c[0] + c[1] + c[2]
            if e == d:
                if int(c) > largest_Palindrome:
                    largest_Palindrome = int(c)
        a = a - 11
    else:
        a = a - a % 11

print(largest_Palindrome)
