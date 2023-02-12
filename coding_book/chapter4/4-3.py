input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

count = 0
steps = [(-2, -1), (-2, +1), (-1, +2), (-1, -2), (+2, -1), (+2, +1), (+1, -2), (+1, +2)]

for dx, dy in steps:
    n_row = 0
    n_col = 0
    n_row += row + dx
    n_col += col + dy

    if n_row < 1 or n_col < 1 or n_row > 8 or n_col > 8:
        continue
    count += 1

print(count)