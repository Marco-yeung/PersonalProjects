from um import count

def main():
    test_count()

def test_count():
    assert count("hello, um") == 1
    assert count("um, hello, um, world") == 2
    assert count("yum") == 0
    assert count("um") == 1

if __name__ == "__main__":
    main()