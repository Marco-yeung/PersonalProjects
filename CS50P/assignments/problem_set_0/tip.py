def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# input returns a string

def dollars_to_float(d):
    y = d.split("$")
    answer = round(float(y[1]), 1)
    return answer


def percent_to_float(p):
    y = p.split("%")
    z = y[0]
    answer = round((float(z)/100),2)
    return answer


if __name__ == "__main__":
    main()
