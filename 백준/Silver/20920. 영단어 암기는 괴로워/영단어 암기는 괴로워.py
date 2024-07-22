import sys


def solution(english, m):
    dict = {}
    for eng in english:
        if len(eng) >= m:
            if eng not in dict:
                dict[eng] = 1
            else:
                dict[eng] += 1

    # 먼저 key를 기준으로 오름차순 정렬
    # answer = sorted(dict.items(), key=lambda item: item[0])
    # answer = sorted(answer, key=lambda item: len(item[0]), reverse=True)
    # answer = sorted(answer, key=lambda item: item[1], reverse=True)
    answer = sorted(dict.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))
    return answer


n, m = map(int, sys.stdin.readline().strip().split())
english = []
for i in range(n):
    a = sys.stdin.readline().strip()
    english.append(a)
result = solution(english, m)

for ans in result:
    print(ans[0])
