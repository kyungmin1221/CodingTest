import sys

n = int(sys.stdin.readline().strip())
answer = {}
for i in range(n):
    book = sys.stdin.readline().strip()
    if book not in answer:
        answer[book] = 1
    else:
        answer[book] += 1

max_book = max(sorted(answer), key=answer.get)
print(max_book)