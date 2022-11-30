import math
import random


def alpha_beta_MiniMax(level, node_index, points, alpha, beta, maximizingPlayer):
   if level == 3:  # 4 level binary tree, starts from 0
       return points[node_index]

   if maximizingPlayer:

       maxEva = min_points

       for i in range(0, 2):

           value = alpha_beta_MiniMax(level + 1, node_index * 2 + i, points, alpha, beta, False)
           maxEva = max(maxEva, value)
           alpha = max(alpha, maxEva)

           if beta <= alpha:
               break

       return maxEva

   else:
       maxEva = max_points

       for i in range(0, 2):

           value = alpha_beta_MiniMax(level + 1, node_index * 2 + i, points, alpha, beta, True)
           maxEva = min(maxEva, value)
           beta = min(beta, maxEva)

           if beta <= alpha:
               break

       return maxEva


# INPUT
my_id = '17564039'
my_id = my_id.translate(str.maketrans("0", "8"))
target = int(my_id[:-3:-1])
max_points = math.ceil(target * 1.5)
min_points = list(map(int, my_id))[4]

# Task1 OUTPUT
points = [random.randrange(min_points, max_points, 1) for i in range(8)]
print('Generated 8 random points between the minimum and maximum point limits:', points)
print('Total points to win:', target)
result = alpha_beta_MiniMax(0, 0, points, min_points, max_points, True)
print('Achieved point by applying alpha-beta pruning =', result)
if result >= target:
   print('The winner is Optimus Prime')
else:
   print('The winner is Megatron')

points_list = []
win_count = 0
for i in range(8):
   random.shuffle(points)
   result = alpha_beta_MiniMax(0, 0, points, min_points, max_points, True)
   points_list.append(result)
   if result >= target:
       win_count += 1

# Task2 OUTPUT
print()
print('After the shuffle:')
print('List of all points values from each shuffles:', points_list)
print('The maximum value of all shuffles:', max(points_list))
print('Won', win_count, 'times out of 8 number of shuffles')

