print("Hello Sneha")

def test_a1():
    print("This is my first test")
    assert 5 + 5 == 10
    assert 5 - 5 == 0
    assert 5 * 5 == 25
    assert 5 / 5 == 1

def test_a2():
    str = 'India'
    print(str[-1])  # a
    print(str[:-1]) # Indi
    print(str[::-1])# aidnI
    print(str[::2]) # Ida
    print(str[::-2])# adI