from itertools import permutations

def solve_cryptarithmetic(crypt):
    # Split the words and find all unique letters
    words = crypt.split()
    unique_letters = set(''.join(words))
    if len(unique_letters) > 10:
        return "Invalid input: Too many unique letters"
    
    # Generate all possible digit permutations
    for perm in permutations(range(10), len(unique_letters)):
        digit_map = {l:d for l,d in zip(unique_letters, perm)}
        
        # Skip permutations with leading zeros
        if digit_map[words[0][0]] == 0 or digit_map[words[1][0]] == 0 or digit_map[words[2][0]] == 0:
            continue
        
        # Evaluate the equation with the digit map
        send = digit_map['S']*1000 + digit_map['E']*100 + digit_map['N']*10 + digit_map['D']
        more = digit_map['M']*1000 + digit_map['O']*100 + digit_map['R']*10 + digit_map['E']
        money = digit_map['M']*10000 + digit_map['O']*1000 + digit_map['N']*100 + digit_map['E']*10 + digit_map['Y']
        
        if send + more == money:
            return f"S = {digit_map['S']}, E = {digit_map['E']}, N = {digit_map['N']}, D = {digit_map['D']}, M = {digit_map['M']}, O = {digit_map['O']}, R = {digit_map['R']}, Y = {digit_map['Y']}"
    
    return "No solution found"
print(solve_cryptarithmetic("SEND + MORE = MONEY"))
