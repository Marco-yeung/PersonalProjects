def main():
    print(convert())

def convert():
    while True:
        try:
            x = str(input("Please enter your input: "))
            x = x.replace(":)", "🙂")
            x= x.replace(":(", "🙁")
        except:
            pass
        else:
            break
    return x

if __name__ == '__main__':
    main()
