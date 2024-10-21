import pytest
pytestmark = [pytest.mark.sanity, pytest.mark.smoke]
@pytest.mark.sanity
@pytest.mark.smoke
def test_str01():
    num = 9/4
    s1 = "I like "+ "pytest automation"
    assert str(num) == '2.25'
    assert s1 == 'I like pytest automation'
    assert s1 + str(num) == 'I like pytest automation2.25'
@pytest.mark.smoke
def test_str02():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert len(letters) == 26

def test_str03():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[0] == 'a'
    assert letters[-1] == 'z' == letters[25]

def test_strslice():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[:] == letters
    assert letters[1:3] == 'bc'
    assert letters[5:] == 'fghijklmnopqrstuvwxyz'
    assert letters[-3:] == 'xyz'
    assert letters[:21:5] == 'afkpu'

def test_strsplit():
    s1 = 'Python,pytest and Automation'
    assert s1.split() == ['Python,pytest', 'and', 'Automation']
    assert s1.split(',') == ['Python', 'pytest and Automation']

