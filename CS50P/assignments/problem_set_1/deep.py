def main():
    print(get_answer())

def get_answer():
    x= input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    x=  x.lower()
    match x:
        case 42 | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No") 

if __name__ == "__main__":
    main()