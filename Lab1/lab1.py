print('================= TASK-1 =================')


def max_infected(grid):
    max_infected_count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "Y":
                max_infected_count = max(max_infected_count, dfs(grid, r, c))
    print(max_infected_count)


def dfs(grid, r, c):
    grid[r][c] = "Visited"
    infected_count = 1
    directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1), (r - 1, c - 1), (r + 1, c + 1), (r + 1, c - 1),
                  (r - 1, c + 1)]
    for row, col in directions:
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 'Y':
            infected_count += dfs(grid, row, col)
    return infected_count


# Input 1
with open('task1_input1.txt', 'r') as f:
    grid1 = [[item for item in line.replace('\n', '').split(' ')] for line in f if line.strip() != ""]

# Input 2
with open('task1_input2.txt', 'r') as f:
    grid2 = [[item for item in line.replace('\n', '').split(' ')] for line in f if line.strip() != ""]

print('---------')
print("Output 1:")
max_infected(grid1)
print('---------')
print("Output 2:")
max_infected(grid2)

print('================= TASK-2 =================')


def attacks(grid, row, col):
    level_track = [[0] * col for x in range(row)]

    if not grid or not grid[0]:
        return 0

    max_time = []
    for i in range(row):

        for j in range(col):

            if grid[i][j] == "A":
                max_time.append(bfs(i, j, grid, row, col, level_track))

    survivors = sum(row.count('H') for row in grid)
    time = max([max(row) for row in level_track])

    print('Time:', str(time), 'minutes')
    if survivors:
        print(str(survivors), 'survived')
    else:
        print('No one survived')


def bfs(r, c, grid, row, col, level_track):
    directions = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
    queue = [(r, c)]
    while queue:
        r, c = queue.pop()
        for i, j in directions:
            if 0 <= i < row and 0 <= j < col and grid[i][j] == "H" and level_track[i][j] == 0:
                grid[i][j] = "A"
                level_track[i][j] = level_track[r][c] + 1
                queue.insert(0, (i, j))


# Input 1
with open('task2_input1.txt', 'r') as f:
    grid3 = [[item for item in line.replace('\n', '').split(' ')] for line in f if line.strip() != ""]

row1 = int(grid3.pop(0)[0])
col1 = int(grid3.pop(0)[0])

print('---------')
print("Output 1:")
attacks(grid3, row1, col1)

# Input 2
with open('task2_input2.txt', 'r') as f:
    grid4 = [[item for item in line.replace('\n', '').split(' ')] for line in f if line.strip() != ""]

row2 = int(grid4.pop(0)[0])
col2 = int(grid4.pop(0)[0])

print('---------')
print("Output 2:")
attacks(grid4, row2, col2)

'''
OUTPUT ----->>>>

================= TASK-1 =================
---------
Output 1:
7
---------
Output 2:
5
================= TASK-2 =================
---------
Output 1:
Time: 4 minutes
No one survived
---------
Output 2:
Time: 4 minutes
1 survived

'''
