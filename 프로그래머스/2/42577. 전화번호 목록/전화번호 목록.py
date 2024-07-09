def solution(phone_book):
    answer = True
    result = {}

    for num in phone_book:
        result[num] = True

    for char in phone_book:
        for i in range(1, len(char)):
            check = char[:i]
            if check in result:
                answer = False
                return answer

    return answer