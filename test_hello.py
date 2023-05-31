from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_arugument():
    for name in ["Hermione", " Harry", "Ron"]:
        assert hello(name)  == f"Hello, {name}"