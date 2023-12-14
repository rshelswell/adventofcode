import numpy as np

def day8a():
    file8 = open("aoc2022/day8.input", "r")
    lines = file8.readlines()
    file8.close()
    rows = np.array([[int(i) for i in line.strip()] for line in lines])
    print(rows.shape)
    cols = rows.transpose()
    row_count = rows.shape[0]
    col_count = rows.shape[1]
    total = 2 * row_count + 2 * col_count - 4
    for x in range(1,row_count-1):
        for y in range(1,col_count-1):
            tallest = rows[x][y] > max(rows[x][0:y]) or rows[x][y] > max(rows[x][y+1:]) or cols[y][x] > max(cols[y][0:x]) or cols[y][x] > max(cols[y][x+1:])
            if tallest:
                total += 1
            print(f"Last location: {(x,y)}, tallest: {tallest}, total: {total}")
    print(total)

def get_index_first_gte_in_list(lst, num):
    return next((i for i, x in enumerate(lst) if x >= num), None)

def day8b():
    file8 = open("aoc2022/day8.input", "r")
    lines = file8.readlines()
    file8.close()
    rows = np.array([[int(i) for i in line.strip()] for line in lines])
    print(rows.shape)
    row_count = rows.shape[0]
    col_count = rows.shape[1]
    max_view = -1
    for x in range(row_count):
        for y in range(col_count):
            #up:
            if x == 0:
                continue
            up = get_index_first_gte_in_list(reversed([r[y] for r in rows[:x]]), rows[x][y])
            if up is None:
                up = x
            else:
                up += 1
            
            #down:
            if x == row_count - 1:
                continue
            down = get_index_first_gte_in_list([r[y] for r in rows[x+1:]], rows[x][y])
            if down is None:
                down = row_count - x - 1
            else:
                down += 1

            #left:
            if y == 0:
                continue
            left = get_index_first_gte_in_list(reversed(rows[x][:y]), rows[x][y])
            if left is None:
                left = y
            else:
                left += 1
            
            #right:
            if y == col_count - 1:
                continue
            right = get_index_first_gte_in_list(rows[x][y+1:], rows[x][y])
            if right is None:
                right = col_count - y - 1
            else:
                right = right + 1

            max_view = max(max_view, up * down * left * right)
            if max_view == up * down * left * right:
                print(f"{(x,y)} up: {up}, down: {down}, left: {left}, right: {right}, view: {up * down * left * right}")
    print(f"Most scenic tree has a view of {max_view}")



if __name__ == "__main__":
    day8b()