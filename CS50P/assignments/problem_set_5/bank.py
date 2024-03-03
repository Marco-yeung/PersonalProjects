"""
def main():
    y = get_amount()
    if y.startswith("hello"):
        print("$0")
    elif y.startswith("h"):
        print("$20")
    else:
        print("$100")

def get_amount():
    x = input("Greeting: ")
    return x.lower().strip()
    

if __name__ == "__main__":
    main()
"""

def main():
    print(value(input("Greeting: ")))


def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100
    


if __name__ == "__main__":
    main()