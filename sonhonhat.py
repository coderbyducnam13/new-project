number = input("Nhập vào dãy số ")
temp = int(number[i])
for i in number:
    if temp > int(number[i]):
        temp = number[i]
print("Số nhỏ nhất là ",temp)
