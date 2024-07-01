import sys


def solution(answer):
    count = 0
    for char in answer:
        dict = {}
        flag = True
        for c in range(len(char)):
            if char[c] not in dict:
                dict[char[c]] = 1
            else:
                if char[c] == char[c-1]:
                    dict[char[c]] += 1
                else:

                    flag = False
                    break
        if flag:
            count += 1

    return count


n = int(sys.stdin.readline().strip())
answer = []
for i in range(n):
    word = sys.stdin.readline().strip()
    answer.append(word)

print(solution(answer))