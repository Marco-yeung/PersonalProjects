# Here we are creating our own module, with a hello and goodbye function
# this would be associated with the say script
def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"Hello, {name}")
    
def goodbye(name):
    print(f"Hello, {name}")
    
    
if __name__ == "__main__":
    main()    


