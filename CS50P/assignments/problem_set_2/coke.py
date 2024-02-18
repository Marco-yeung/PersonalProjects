amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    insert_coin = int(input("Insert Coin: "))
    if insert_coin in (5, 10, 25):
        amount_due -= insert_coin
    else:
        pass
    # print(f"Amount Due: {amount_due}")

change_owed = -amount_due
print(f"Change Owed: {change_owed}")

