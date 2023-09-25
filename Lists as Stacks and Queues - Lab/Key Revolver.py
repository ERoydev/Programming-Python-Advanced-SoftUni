from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())

shooted = 0
counter = 0

while locks and bullets:
    bullet = bullets.pop()
    lock = locks.popleft()

    shooted += 1
    counter += 1

    if bullet <= lock:
        print("Bang!")

    else:
        print("Ping!")
        locks.appendleft(lock)

    if bullets:
        if counter % 10 == gun_barrel_size:
            counter = 0
            print("Reloading!")


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")

else:
    earned_money = intelligence_value - (shooted * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")