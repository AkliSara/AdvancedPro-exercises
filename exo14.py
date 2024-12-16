word = input("Word: ")
espaces = (30 - len(word)) // 2
print('*' * 30)
print('*' + ' ' * espaces + word + ' ' * (30 - len(word) - espaces - 2) + '*')
print('*' * 30)