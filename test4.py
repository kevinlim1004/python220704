#교집합 함수
from turtle import pos


def intersect(pre,post):
    result = []
    for x in pre:
        if x in post and x not in result:
            result.append(x)
    return result

print(intersect("banana","nanaba"))