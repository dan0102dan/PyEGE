# https://inf-ege.sdamgia.ru/problem?id=15800

def f(let):
    if let == 'А':
        return 1
    
    if let == 'Б':
        return sum([f(l) for l in 'А'])

    if let == 'В':
        return sum([f(l) for l in 'БГ'])
                
    if let == 'Г':
        return sum([f(l) for l in 'АБ'])
                
    if let == 'Д':
        return sum([f(l) for l in 'А'])

    if let == 'Е':
        return sum([f(l) for l in 'ДГ'])
                
    if let == 'Ж':
        return sum([f(l) for l in 'ВГЕ'])
                
    if let == 'К':
        return sum([f(l) for l in 'ВЖ'])
                
    if let == 'Л':
        return sum([f(l) for l in 'КЖ'])
                
    if let == 'М':
        return sum([f(l) for l in 'Л'])
                
    if let == 'П':
        return sum([f(l) for l in 'ЛМ'])
                
    if let == 'Р':
        return sum([f(l) for l in 'П'])
                
    if let == 'С':
        return sum([f(l) for l in 'П'])
                
    if let == 'Т':
        return sum([f(l) for l in 'РС'])

print(f('Т'))