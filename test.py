import hello

def test_say_hello():
    assert hello.say_hello() == "Hello, Jenkins!"

test_say_hello()
print("Test passed!")
