from collections import deque


class SnakeGame:

    def __init__(self, rows, cols, foods):
        self.rows = rows
        self.cols = cols
        self.foods = deque(foods)
        self.snakePath = deque()
        self.snakePathSet = set()
        self.score = 0
        self.setInitialPosition()
    
    def setInitialPosition(self):
        position = [0,0]
        self.snakePath.append(position)
        self.snakePathSet.add(tuple(position))
    
    def move(self, direction):
        currentPosition = self.snakePath[-1]
        newPosition = None
        if direction == 'u':
            newPosition = [currentPosition[0]-1, currentPosition[1]]
        elif direction == 'd':
            newPosition = [currentPosition[0]+1, currentPosition[1]]
        elif direction == 'r':
            newPosition = [currentPosition[0], currentPosition[1]+1]
        elif direction == 'l':
            newPosition = [currentPosition[0], currentPosition[1]-1]

        if newPosition[0] < 0 or newPosition[1] < 0 or newPosition[0] >= self.rows or newPosition[1] >= self.cols:
            return -1

        if self.foods and newPosition == self.foods[0]:
            self.score += 1
            self.foods.popleft()
        else:
            popedLocation = self.snakePath.popleft()
            self.snakePathSet.remove(tuple(popedLocation))
            if tuple(newPosition) in self.snakePathSet:
                return -1

        self.snakePath.append(newPosition)
        self.snakePathSet.add(tuple(newPosition))
        
        return self.score

rows = 2
cols = 3
food = [[0, 1], [1, 1], [1, 0], [0, 2]]
moves = ["r", "d", "l", "u", "r", "r", "d", "l", "u"]
scores = [1, 2, 3, 3, 3, 4, 4, 4, -1]
sg = SnakeGame(rows, cols, food)
output = []
for i, move in enumerate(moves):
    score = sg.move(move)
    output.append(score)
    if score == -1:
        break

print("Actual score:   ", output)
print("Expected score: ", scores)