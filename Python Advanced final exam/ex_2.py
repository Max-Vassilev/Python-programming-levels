size = int(input())
car_num = input()

matrix = []
distance = 0
row = 0
col = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(size):
    matrix.append(input().split())

while True:
    command = input()
    if command == "End":
        print(f"Racing car {car_num} DNF.")
        break
    row += directions[command][0]
    col += directions[command][1]

    if matrix[row][col] == ".":
        distance += 10
        continue

    elif matrix[row][col] == "F":
        distance += 10
        print(f"Racing car {car_num} finished the stage!")
        break

    elif matrix[row][col] == "T":

        matrix[row][col] = '.'
        distance += 30

        for r in range(len(matrix)):
            if "T" in matrix[r]:
                c = matrix[r].index("T")
                tunnel_pos = [r, c]
                row = tunnel_pos[0]
                col = tunnel_pos[1]
                matrix[row][col] = '.'
                break


matrix[row][col] = 'C'

print(f"Distance covered {distance} km.")

for row in matrix:
    print(''.join(row))

