def test_list01():
    list1 = ['my', 'name']
    list2 = ['is', 'Sneha']
    print(list1+list2)
    assert list1+list2 == ['my', 'name', 'is', 'Sneha']
    list1.extend(list2)
    print(list1)
    assert list1 == ['my', 'name', 'is', 'Sneha']
    print("TO convert list to String")
    print(' '.join(list1))