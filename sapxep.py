x = int(input("Nhập số x:"))
y = int(input("Nhập số x:"))
z = int(input("Nhập số x:"))
list = []
def solientiep(x,y,z):
    list.append(x)
    list.append(y)
    list.append(z)
    list.sort()
    return list
print(solientiep(x,y,z))