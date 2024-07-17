import sys

n = int(sys.stdin.readline().strip().strip())
room = {}
answer = 0

for i in range(n):
    chat = sys.stdin.readline().strip()
    if chat == "ENTER":
        room = {}
        continue

    if chat not in room:
        room[chat] = 1
        answer += 1
    else:
        continue


print(answer)

