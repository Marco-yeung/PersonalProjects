from calculator import square

def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 square should be 4")
    if square(3) != 9:
        print("3 square should be 9")