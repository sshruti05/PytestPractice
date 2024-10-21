import pytest

#NOTE: xfail means you expect a test to fail for some reason. e.g know bug

def test_strjoin():
    s1 = "Python,pytest and automation"
    l1 = ['Python,pytest', 'and', 'automation']
    l2 = ['Python', 'pytest and automation']
    print(' '.join(l1)) #Python,pytest and automation
    assert ' '.join(l1) == s1
    assert s1.split(',') == l2

@pytest.mark.xfail(reason = 'know bug')
def test_alphabets():
    str = 'abcdefghijklmnopqrstuvwxyz'
    assert str[100] #IndexError: string index out of range

@pytest.mark.xfail
def teststring_int_concate():
    letters = 'Sneha'
    num = str(123)
    assert letters + num == 'Sneha123'