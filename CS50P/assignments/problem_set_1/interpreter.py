def main():
    number = modify()
    print(f"{number:.1f}")

def modify():
    # while True:
    try:
        expression = input("Expression: ")
        x, y, z = expression.split(" ")
        x = int(x)
        z = int(z)
        if y == "+":
            answer =  x + z
        elif y == "-":
            answer =  x - z
        elif y == "*":
            answer =  x * z
        else:
            answer =  x / z
    except ValueError:
        print("please follow with the format: x sth y, with the spacing")
    except UnboundLocalError as error:
        print("we need a formula, not other thing like string or integer")
    # else:
    #     break
    return answer
    
if __name__ == '__main__':
    main()