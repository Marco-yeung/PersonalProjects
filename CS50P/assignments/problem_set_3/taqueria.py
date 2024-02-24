"""
def main():
    print(order())
    # output = order()
    # print(f"Total ${output:.2f}", end = '')


def order():
    total_amount = 0
    order_dict = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
    while True:
        food = input("Item: ").title()
        try:
            if food in order_dict:
                total_amount += order_dict[food]
                print(f"Total ${total_amount:.2f}", end='')
        
        # except KeyError:
        #     print("Please try enter again.")
        except EOFError:
            print()
            exit()

        # return total_amount

if __name__ == "__main__":
    main()

"""
order_dict = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }
total_amount = 0
while True:
    try:
        food = input("Item: ").title()  
        if food in order_dict:
            total_amount += order_dict[food]
            print("Total: $", end='')
            print("{:.2f}".format(total_amount))
    except EOFError:
        print('Finished !')
        break

