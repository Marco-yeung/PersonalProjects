def get_input():
    while True:
        try:
            x = str(input("Please enter your name: "))
        except:
            pass
        else:
            break
    return x

def main():
    print(get_input().replace(" ", "..."))

if __name__ == "__main__":
    main()

