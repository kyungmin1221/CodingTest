import sys

def solution(box, m):
    answer = 0
    sum = 0
    for i in range(len(box)):
        sum = 0
        for j in range(i, len(box)):
            sum += box[j]
            if sum == m:
                answer += 1
                sum = 0
                break
            if sum > m:
                sum = 0
                break


    return answer


n, m = map(int, sys.stdin.readline().strip().split())
box = list(map(int,sys.stdin.readline().strip().split()))
ans = solution(box, m)
print(ans)