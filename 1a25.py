# exercicio 3
# a = 1
# b = 2
# print(a == b)
# print(b == c)


#exercicio 4
# a = "1"
# a = int(1)
# b = 2
# print(a + b)
# #melhor codigo
# #print(int(a))


#exercicio 5, 6, 7, 8, 9 e 10
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# print(letters[:9:2])
#correcao print(letters[::2])


#exercicio 11:
# l_list = []
# for element in range(1, 21):
#     l_list.append(element)
# print(l_list)


#correcao11:
# myrange= range(1,21)
# print(list(myrange))


#exerccicio 12:
# my_range = range(10, 210, 10)
# print(list(my_range))
#usando o primeiro myrange como input ficaria assim print([10 * x for x in myrange])


#exercicio 13:
# myrange= range(1,21)
# print(list(map(str,myrange)))


#exercicio 14:
# a = ["1", 1, "1", 2]
# a = list(set(a))
# print(a)

#exercicio 15, 16, 17:
# my_dict = {'a': 1,
#  'b':2,
#  'c': 3}
# soma = my_dict['a'] + my_dict['b']
# print(soma)
# #corrigindo
# print(my_dict['a']+my_dict['b'])

#exercicio 19, 20:

# d = {'a': 1,'b':2}
# d['c'] = 3
# print(d)
# print(sum(d.values()))

#exercico 21:

# d = {"a": 1, "b": 2, "c": 3}
# c = {key:value for (key,value) in d.items() if value <= 1}
# print(d.values())
# print(d.keys())
# print(d.values())
# print(c)

#exercicio 22, 23, 24:
# from pprint import pprint
# d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))
# #pprint(d['b'][2])

# for key, value in d.items():
#     print(key, 'has value', value)

#exercicio 25:

# import string
# for letter in string.ascii_lowercase:
#     print(letter)