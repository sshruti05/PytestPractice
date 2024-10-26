import pytest

@pytest.fixture()
# def setup_list() ->list[str] :
def setup_list():
    print("\n in fixtures.. \n")
    city = ['New York', 'San Francisco', 'Los Angeles', 'Neitherland']
    return city

def test_get_list_items(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New York'
    assert setup_list[::2] == ['New York', 'Los Angeles']

def test_reverse_list(setup_list):
    print(setup_list[::-1])
    print(reverse_using_buildin_python_function(setup_list))
    assert setup_list[::-1] == reverse_using_buildin_python_function(setup_list)

def reverse_using_buildin_python_function(lst):
    lst.reverse()
    return lst

@pytest.mark.usefixtures("setup_list")
def test_userfixtures_demo(): # no need to define fixture in argument here
    