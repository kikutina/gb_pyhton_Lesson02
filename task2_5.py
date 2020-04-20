rating_list = [7, 5, 4, 3, 2]
print(f'Результат: {rating_list}')
rating = int(input('Введите новый элемент : '))
i=0
n = len(rating_list)
while i < n:
    if rating >= rating_list[i]:
        rating_list.insert(i+1, float(rating))
        break
    i += 1
    if i==n:
        rating_list.insert(i, rating)
        break
print(f'Пользователь ввел число {rating}. Результат: {rating_list}')
