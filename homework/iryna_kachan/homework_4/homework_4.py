my_dict = {'tuple': 'tuple', 'list': 'list', 'dict': 'dict', 'set': 'set'}
my_dict['tuple'] = (1, 3, 5, 7, None, 'hello', False, 'Iryna')
my_dict['list'] = [1, 100, 'hello,world', 3.14, 'exit']
my_dict['dict'] = {'name': 'iryna', 'last name': 'kachan', 'age': 34, 'test': 'test'}
my_dict['set'] = {1, 2, 3, 4, 5}
print('last element of the tuple:', my_dict['tuple'][-1])  # last element of the tuple
my_dict['list'][-1] = 'here'  # add new last element to list
my_dict['list'].pop(1)  # deleting second element of the list
my_dict['dict']['i am a tuple'] = 12345  # add new element to the dictionary
my_dict['dict'].pop('age')  # deleting element of the dictionary
my_dict['set'].add(6)  # add new element to the set
my_dict['set'].pop()  # deleting element of the set
print('all dictionary:', my_dict)  # print of the edited dictionary
