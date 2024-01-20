# from calculator import square

# def main():
#     test_square()


# def test_square():
#     # if square(2) != 4:
#     #     print("2 square should be 4")
#     # if square(3) != 9:
#     #     print("3 square should be 9")
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 square should be 4")
        
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 square should be 9")        
        
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 square should be 9")  
        
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 square should be 0")  
        
        
# if __name__ == "__main__":
#     main()
    
    
'''
instead of using if condition to say what if sth is not true
we could use assert to say loudly and firmly what sth is really true
but it is not really user friendly as it would only tell what line caused the error, but doesn't tell waht specific error it is 

'''

'''
it could be pretty hard to capture all those darn code for testing purposes
python has third part libraries called pytest to do some o the unit testing
unit teseting: To test the unit in the script, which would be the function you are writing


we could test the function with no main() function, try and except, condition
when using the pytest module
'''


from calculator import square
import pytest 

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-3) == 9
#     assert square(0) == 0
    
'''
we should keep our testing code simple and should seperate it instead of putting it into one test function
we could split it into positive, negative and 0 testing function
'''
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
    
def test_negative():
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")
