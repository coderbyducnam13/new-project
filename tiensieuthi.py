sotien = int(input("Give me a price: "))
if sotien >= 150:
	print("Số tiền cần thanh toán là ", sotien - 50)
elif sotien >= 100:
	print("Số tiền cần thanh toán là : ", sotien - 25)
elif sotien >= 75:
	print("Số tiền cần thanh toán là : ", sotien - 15)
else:
	print("Số tiền cần thanh toán là : ", sotien)