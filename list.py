def find_index_item(myTempList, item_name):
    result = -1
    length = len(myTempList)
    for i in range(length):
        if myTempList[i]['name'] == item_name:
            result = i
    return result
def add_item(myTempList, item):    
    myTempList.append(item)
expenses = []
loop = True
while loop:
    print("What do you want to do? -\n"
        "1. Add\n"
        "2. Remove\n"
        "3. Cancel\n")
    option = int(input("Select option 1 or 2: "))
    if option == 1:
        name_input = input("Item name: ")
        cost_input = int(input("Item cost: "))
        date_input = input("Date: ")
        item = {'name': name_input, 'cost':cost_input, 'date':date_input}
        add_item(expenses, item)
        print("Your expenses: ", expenses)
    elif option == 2:
        remove_item(expenses, name_input)
        print("Your expenses: ", expenses)
    else:
        loop = False
    