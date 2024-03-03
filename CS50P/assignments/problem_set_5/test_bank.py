from bank import value
def main():
    test_value()

def test_value():
    assert value("hello, Ben") == 0
    assert value("how are you?") == 20
    assert value("you are handsome") == 100

if __name__ == "__main__":
    main()
