def triangle (a,b,c):
    if a == b and b == c:
        return ('equilateral')
    elif a == b or b == c:
        return ('isosceles)')
    else:
        return ('scalene')

print(triangle(5,7,5))
