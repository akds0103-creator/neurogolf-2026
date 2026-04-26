import json
import numpy as np

def find_period(grid):
    """Find the smallest period p such that grid repeats with period p"""
    n = len(grid)
    for p in range(1, n+1):
        valid = True
        for i in range(n):
            if grid[i] != grid[i % p]:
                valid = False
                break
        if valid:
            return p
    return n

def solve(input_grid):
    grid = [tuple(row) for row in input_grid]
    n = len(grid)  # always 6
    
    p = find_period(grid)
    
    # Continue the sequence for 3 more rows
    extended = list(input_grid)
    for i in range(3):
        next_row = list(input_grid[(n + i) % p])
        extended.append(next_row)
    
    # Replace 1→2
    result = [[2 if x == 1 else x for x in row] for row in extended]
    return result

with open('../data/task003.json', 'r') as f:
    task = json.load(f)

print("=== TRAINING EXAMPLES ===")
for i, example in enumerate(task['train']):
    predicted = solve(example['input'])
    expected = example['output']
    print(f"Train {i+1}: {'✓ CORRECT' if predicted == expected else '✗ WRONG'}")

print("\n=== TEST PREDICTION ===")
prediction = solve(task['test'][0]['input'])
for row in prediction:
    print(row)

with open('../submissions/task003_prediction.json', 'w') as f:
    json.dump({"output": prediction}, f)
print("\nSaved!")