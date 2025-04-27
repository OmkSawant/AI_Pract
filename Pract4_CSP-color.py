# Constraint Satisfaction Problem: Map Coloring

colors = ["Red", "Blue", "Green"]
states = ["WA", "NT", "SA", "Q", "NSW", "V"]

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "Q": ["NT", "SA", "NSW"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"]
}

colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state, []):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def backtrack(state_index):
    if state_index == len(states):
        return True  # All states are colored
    state = states[state_index]
    for color in colors:
        if promising(state, color):
            colors_of_states[state] = color  # Assign color
            if backtrack(state_index + 1):  # Recurse to next state
                return True
            colors_of_states[state] = None  # Undo assignment (backtrack)
    return False  # No valid color found

def main():
    if backtrack(0):
        print(colors_of_states)
    else:
        print("No solution found")

if __name__ == "__main__":
    main()
