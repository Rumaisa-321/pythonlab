my_dict = {input('key:'):
int(input('value:'))for _ in
range(int(input('number of items:')))}
print('Ascending:',
dict(sorted(my_dict.items())))
print('Descending:',
dict(sorted(my_dict.items(),reverse=True)))
~                                            
