import random
x_x = random.randint(0,1)
total = 0
if x_x==1:
    random_cpt = random.randint(1,3)
    print("Máy đi trước . Máy chọn",random_cpt)
    total +=random_cpt
    print("Điểm hiện tại là",total)
else:
    player = int(input("Vui lòng chọn 1-3"))
    total +=player
    print("Điểm hiện tại là",total)
    random_cpt = random.randint(1,3)
    print("Máy chọn",random_cpt)
    total +=random_cpt
    print("Điểm hiện tại là",total)
while total < 21:
    player = int(input("Vui lòng chọn 1-3"))
    total +=player
    print("Điểm hiện tại là",total)
    if 21>total>=18:
        print("Máy chọn",21-total)
        print("Máy dành chiến thắng ")
        total=21
    if total ==21:
        print("Bạn đã dành chiến thắng")
    else:
        random_cpt = random.randint(1,3)
        print("Máy chọn",random_cpt)
        total +=random_cpt
        print("Điểm hiện tại là",total)
    