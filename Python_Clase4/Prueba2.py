def numeros(a,b):
    if a%b==0:
        print("a es multiplo de b")
    if b%a==0:
        print("b es multiplo de a")
print(numeros(int(input("Ingrese un numero a:")), int(input("Ingrese un numero b: "))))