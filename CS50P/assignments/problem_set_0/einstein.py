def main():
    print(formula())


def formula():
    while True:
        try:
            m = int(input("m: "))
            # E = m*pow(300000000, 2)
            E = m*(300000000**2)
        except ValueError:
            print("m is not an integer")
        else:
            break
    return E

"""
def formula():
    m = int(input("m: "))
    # E = m*pow(300000000, 2)
    E = m*(300000000**2)
    return E
"""

if __name__ == "__main__":
    main()
