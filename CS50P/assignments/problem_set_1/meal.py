def main():
    print(convert(input("What time is it? ")))


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)/60
    total = hours + minutes
    if total >= 7 and total <= 8:
        return "breakfast time"
    elif total >= 12 and total <= 13:
        return "lunch time"
    elif total >= 18 and total <= 19:
        return "dinner time"
    else:
        pass


if __name__ == "__main__":
    main()