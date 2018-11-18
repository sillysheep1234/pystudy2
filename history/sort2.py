
def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L, key=by_name)                 # 按小写Ascll码升序对名字排序
L3 = sorted(L, key=by_score)   # 按小写Ascll码升序对名字排序，后反转
print('Name Ranking：', L2)
print('Score Ranking：', L3)