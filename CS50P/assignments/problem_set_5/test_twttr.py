from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("away") == "wy"
    assert shorten("harvard") == "hrvrd"
    try:
        assert shorten("hello") == "hll"
    except AssertionError:
        print("hello should be hll")

if __name__ == "__main__":
    main()
    

