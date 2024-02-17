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