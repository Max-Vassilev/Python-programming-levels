from collections import deque

caffeine = list(map(int, input().split(', ')))
drinks = deque(map(int, input().split(', ')))

total_caffeine = 0

while caffeine and drinks:
    current_caffeine = caffeine[-1]
    current_drink = drinks[0]

    current_sum = current_caffeine * current_drink

    if current_sum + total_caffeine <= 300:
        caffeine.pop()
        drinks.popleft()
        total_caffeine += current_sum

    elif current_sum + total_caffeine > 300:
        caffeine.pop()
        drinks.append(drinks.popleft())
        if total_caffeine >= 30:
            total_caffeine -= 30


if drinks:
    print(f"Drinks left: {', '.join(str(s) for s in drinks)}")

else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")