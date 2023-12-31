def main():
    x = int(input("x: "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
# def is_even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

def is_even(n):
    return True if n % 2 == 0 else False
    # return (n % 2 == 0)
main()