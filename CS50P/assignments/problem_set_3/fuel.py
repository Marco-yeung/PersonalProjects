# try:
#     x = input("Fraction: ")
#     if x == "1/4":
#         print("25%")
#     elif x == "1/2":
#         print("50%")
#     elif x == "3/4":
#         print("75%")
#     elif x == "1":
#         print("F")
#     elif x == "0/4":
#         print("E")

# except:
#     x = input("Fraction: ")

    
    
def main():
    print(test())

def test():
    while True:
        try:
            expression = input("Fraction: ")
            x, y = expression.split("/")
            x = int(x)
            y = int(y)
            if x/y == 0.25:
                output = "25%"
            elif x/y == 0.5:
                output = "50%"
            elif x/y == 0.75:
                output = "75%"
            elif x/y == 1:
                output = "F"
            elif x == 0:
                output = "E"
            else:
                print("Please enter the fraction again.")
                continue

        except ValueError:
            print("Please enter the fraction again.")
        except ZeroDivisionError:
            print("Please enter the fraction again.")
        except:
            if x > y:
                print("Please enter the fraction again.")
        else:
            break
    return output

if __name__ == "__main__":
    main()
