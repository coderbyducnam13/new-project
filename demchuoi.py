text = input("Nhập vào chuỗi ")
def kiemtraham(text):
    result = 0
    for letter in text:
        result+=1
    return result
print(kiemtraham(text))