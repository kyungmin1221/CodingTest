def solution(clothes):    
    answer = 1
    result = {}
    for name, kind in clothes:
        if kind not in result.keys():
            result[kind] = [name]
        else:
            result[kind] += [name]

    for num in result.values():
        answer *= (len(num) + 1)

    return answer-1