def check_query(query):
    elements = query.split(', ')
    if len(elements) > 1:
        return ', '.join(elements[1:])
    else:
        return query

queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '—', result)