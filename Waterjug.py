from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    # Create a set to store visited states
    visited = set()

    # Create a queue for breadth-first search
    queue = deque()

    # Initialize the initial state with both jugs empty
    initial_state = (0, 0)
    queue.append(initial_state)

    # Perform breadth-first search
    while queue:
        current_state = queue.popleft()

        # Check if the target volume is reached
        if current_state[0] == target or current_state[1] == target:
            return current_state

        # Check if the current state has been visited
        if current_state in visited:
            continue

        visited.add(current_state)

        # Perform all possible actions from the current state
        for action in ['fill jug 1', 'fill jug 2', 'pour jug 1 to jug 2', 'pour jug 2 to jug 1', 'empty jug 1', 'empty jug 2']:
            next_state = None

            if action == 'fill jug 1':
                next_state = (jug1_capacity, current_state[1])
            elif action == 'fill jug 2':
                next_state = (current_state[0], jug2_capacity)
            elif action == 'pour jug 1 to jug 2':
                amount = min(current_state[0], jug2_capacity - current_state[1])
                next_state = (current_state[0] - amount, current_state[1] + amount)
            elif action == 'pour jug 2 to jug 1':
                amount = min(current_state[1], jug1_capacity - current_state[0])
                next_state = (current_state[0] + amount, current_state[1] - amount)
            elif action == 'empty jug 1':
                next_state = (0, current_state[1])
            elif action == 'empty jug 2':
                next_state = (current_state[0], 0)

            if next_state and next_state not in visited:
                queue.append(next_state)

    return None

# Test the function
jug1_capacity = 4
jug2_capacity = 3
target = 2

result = water_jug_problem(jug1_capacity, jug2_capacity, target)
if result:
    print(f"Goal reached: {result[0]} gallons in jug 1 and {result[1]} gallons in jug 2")
else:
    print("Goal cannot be reached with the given capacities")

#Footer
print("Question no.9")
print("Name: Saroj Pokharel ")
print("Roll no : 26 ")
print("Section:A")