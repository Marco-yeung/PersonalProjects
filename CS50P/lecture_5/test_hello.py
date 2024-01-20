from hello import hello

def test_default():
    assert hello() == "hello, world"
    
def test_argument():
    for name in ["Heriomne", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"