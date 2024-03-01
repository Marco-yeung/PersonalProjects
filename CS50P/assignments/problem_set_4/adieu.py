import inflect
p = inflect.engine()
def main():
    output = p.join(print_name())
    print("Adieu, adieu, to", output)
    

def print_name():
    name_ls = []
    while True:
            try:
                user_input = input("Name: ")
                name_ls.append(user_input)
            except EOFError:
                break
    return name_ls


if __name__ == "__main__":
     main()
