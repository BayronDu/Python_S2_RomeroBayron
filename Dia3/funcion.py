x = int(input(""))
y = int(input(""))
z = int(input(""))
n = int(input(""))

cuadrados = [[i,j,k] for i in range(x+1) for j in range(y+1)for k in range(z+1) if i+j+k != n]
print(cuadrados)

# Preguntar al profesor el funcionamiento de las lista de compresión