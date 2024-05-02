def mayor(a,b,c,d):
    if(a>b & a>c & a>d):
        return a
    if(b>a & b>c & b>d):
        return b
    if(c>a & c>b & c>d):
        return c
    else: return d
print(mayor(int(input("Ingrese un numero a:")), int(input("Ingrese un numero b: ")), int(input("Ingrese un numero c:")), int(input("Ingrese un numero d: ")))**3)