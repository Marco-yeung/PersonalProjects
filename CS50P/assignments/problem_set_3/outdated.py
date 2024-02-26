def main():
    print(date_split())

month_ls = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# def date_split():
#     while True:
#         try:
#             date = input("date: ")
#             if ',' in date:
#                 month, day, year = date.split()
#                 day = day.replace(",", "")

#                 pass

#             elif '/' in date:    
#                 month, day, year = date.split("/")
#                 day = int(day)
#                 month = int(month)
#                 year = int(year)
#                 if day < 10:
#                     day = f"{day:02}"
#                 if month < 10:
#                     month = f"{month:02}"
#         except:
#             if month > 12:
#                 print("month is out of range")
#             elif day > 31:
#                 print("day is out of range")
            
#         else:
#             break
#     return f"{year}-{month}-{day}"

def date_split():
    while True:
        date = input("date: ")
        try:
            month, day, year = date.split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            if (month >= 1 and month <= 12) and (day >= 1 and day <= 31):
                break
            # if day < 10:
            #     day = f"{day:02}"
            # if month < 10:
            #     month = f"{month:02}"
        except:
            try:
                month, day, year = date.split(" ")
                day = day.replace(",", "")
                for i in range(len(month_ls)):
                    if month == month[i]:
                        month = i+1

                day = int(day)
                month = int(month)
                year = int(year)
                if (month >= 1 and month <= 12) and (day >= 1 and day <= 31):
                    break
            except:
                print()
                pass
    return f"{year}-{month:02}-{day:02}"
                

if __name__ == "__main__":
    main()
