food_ls = []

while True:
    try:
        food = input('Please enter food you want to buy: ')
        food_ls.append(food)
    except EOFError:
        print("Finished")
        break

print(food_ls)

def find_duplicates(lst):
    counts = {}
    duplicates = []
    for element in lst:
        if element in counts:
            counts[element] += 1
            for item in duplicates:
                if element in item:
                    item[element] += 1
        else:
            counts[element] = 1
            duplicates.append({element: 1})

    return duplicates

duplicates = find_duplicates(food_ls)
if duplicates:
    print("The list has duplicates:")
    for duplicate in duplicates:
        for element, count in duplicate.items():
            print(f"{element} - {count} occurrences")
else:
    print("The list does not have duplicates.")






