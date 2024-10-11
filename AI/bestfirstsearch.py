import heapq

GOAL_STATE = [[1,2,3], [4,5,6], [7,8,0]]

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j]!=0:
                distance += abs(i - (state[i][j]-1) //3) + abs(j - (state[i][j]-1) %3)
    return distance

def best_first_search(initial_state):
    queue = [(0, initial_state, [])]
    heapq.heapify(queue)

    visited = set()

    while queue:
        cost, state, moves = heapq.heappop(queue)

        print("State:")
        for row in state:
            print(row)
        print("Heuristic Value:", heuristic(state))
        print()

        if state == GOAL_STATE:
            print("Solution found!")
            print("Moves:", moves)
            return cost 
        
        visited.add(tuple(map(tuple, state)))

        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    
                    if i>0:
                        new_state = [row[:] for row in state]
                        new_state[i][j], new_state[i-1][j] = new_state[i-1][j], new_state[i][j]

                    if tuple(map(tuple, new_state)) not in visited:
                        new_moves = moves + ["Up"]
                        heapq.heappush(queue, (cost + 1 + heuristic(new_state), new_state,  new_moves))

                    if i<2:
                        new_state = [row[:] for row in state]
                        new_state[i][j], new_state[i+1][j] = new_state[i+1][j], new_state[i][j]

                        if tuple(map(tuple, new_state)) not in visited:
                            new_moves = moves + ["Down"]
                            heapq.heappush(queue, (cost + 1 + heuristic(new_state), new_state, new_moves))

                    if j>0:
                        new_state = [row[:] for row in state]
                        new_state[i][j], new_state[i][j-1] = new_state[i][j-1], new_state[i][j]
                        
                        if tuple(map(tuple, new_state)) not in visited:
                            new_moves = moves + ["Left"]
                            heapq.heappush(queue, (cost + 1 + heuristic(new_state), new_state, new_moves))

                    if j<2:
                        new_state = [row[:] for row in state] 
                        new_state[i][j], new_state[i][j+1] = new_state[i][j+1], new_state[i][j]
                        
                        if tuple(map(tuple, new_state)) not in visited:
                            new_moves = moves + ["Right"]
                            heapq.heappush(queue, (cost + 1 + heuristic(new_state), new_state, new_moves))

                            return -1

initial_state = [[1,2,3], [4,5,6], [7,5,8]]
best_first_search(initial_state)