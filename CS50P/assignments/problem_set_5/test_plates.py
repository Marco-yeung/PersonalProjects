from plates import is_valid

def main():
    test_plates()

def test_plates():
    assert is_valid("CS50") == "Valid"
    assert is_valid("HELLO") == "Valid"
    assert is_valid("AAA222") == "Valid"


if __name__ == "__main__":
    main()