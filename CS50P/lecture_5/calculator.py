# def main():
#     x = int(input("what is x? "))
#     print("the squared of it is" , square(x))
          
# def square(x):
#     return x**2
#     # x = x ** 2
#     # remember that when defining a function would need to return a value
    
# # main wont be called every time when adding this function, like importing square function from other script    
# if __name__ == "__main__":
#     main()


'''
lesson learned from this script/ mistake maken in doing it
objective of this lesson is to do unit testing, test for the corner cases

point:
x = int(input("what is x? ")): forgot to add int at the start, finally added after getting an type error

point:
forgot to add a return object at start when defining a function

'''

# demonstrating a bug here
def main():
    x = int(input("what is x? "))
    print("the squared of it is" , square(x))
          
def square(x):
    return x + x

    
if __name__ == "__main__":
    main()