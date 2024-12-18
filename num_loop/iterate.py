shopping_list = ["apple","burns", "juice", "milk"]
item_found = False

while not item_found:
    item = input("inter the list ")
    if item.lower() == "q":
        break  # Exit the loop if user enters 'q'
    if item in shopping_list:
        item_found = True
        print(f"{item} is on your shopping list.")
    else:
        print(f"{item} is not on your list.")