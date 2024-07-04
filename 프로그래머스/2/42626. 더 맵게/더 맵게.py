import heapq

def solution(scoville, k):
    answer = 0  # 섞은 횟수

    heapq.heapify(scoville)

    while len(scoville) > 1:
        first_food = heapq.heappop(scoville)
        if first_food >= k:
            return answer
        second_food = heapq.heappop(scoville)
        if first_food < k:
            mix = first_food + (second_food * 2)
            heapq.heappush(scoville, mix)
            answer += 1

    if scoville[0] >= k:
        return answer
    else:
        return -1