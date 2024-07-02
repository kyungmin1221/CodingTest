import sys

def solution(height):
    # 배열이 비어있을 때
    if not height:
        return 0

    left = 0
    right = len(height) - 1

    left_max = height[left]
    right_max = height[right]

    count = 0

    while left < right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max <= right_max:
            count += left_max - height[left]
            left += 1
        else:
            count += right_max - height[right]
            right -= 1

    return count


n, m = map(int, sys.stdin.readline().strip().split())       # 4 8
height = list(map(int, sys.stdin.readline().strip().split()))
solution(height)
print(solution(height))