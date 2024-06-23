def solution(n, lost, reserve):
    cloth = [1] * (n + 1)  # 모든 학생이 기본적으로 체육복을 한 벌씩 가지고 있다고 가정

    for i in reserve:
        cloth[i] += 1
    for i in lost:
        cloth[i] -= 1

    for i in range(1, n + 1):
        if cloth[i] == 0:
            if i > 1 and cloth[i - 1] > 1:
                cloth[i] += 1
                cloth[i - 1] -= 1
            elif i < n and cloth[i + 1] > 1:
                cloth[i] += 1
                cloth[i + 1] -= 1

    count = sum(1 for i in range(1, n + 1) if cloth[i] > 0)
    return count

n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))  # 예상 출력: 3
