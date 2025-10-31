# --- Operators ---
# These functions just describe the actions

def move(subject, x1, x2):
    return f"Move {subject} from {x1} to {x2}"

def push_box(x1, x2):
    return f"Push box from {x1} to {x2}"

def climb_box(x, direction):
    return f"Climb box at {x} {direction}"

def have_banana(x):
    return f"Have banana at {x}"

# --- Initial State ---
# This defines the start of the problem
initial_state = {
    'monkeyAt0': True,
    'monkeyLevel': 'Down',
    'bananaAt1': True,
    'boxAt2': True
}

# --- Goal State ---
# This defines what we want to achieve
goal_state = {
    'GetBanana': True,
    'at': 1
}

# --- Planning Algorithm ---
# This function determines the steps to get from the initial state to the goal state
def plan_actions(initial_state, goal_state):
    actions = []

    # This is a hard-coded plan for the specific problem defined
    # in initial_state. A real AI planner would search for these steps.
    
    # Check for the specific problem: Monkey at 0, Banana at 1, Box at 2
    if (initial_state.get('monkeyAt0') and 
        initial_state.get('bananaAt1') and 
        initial_state.get('boxAt2') and
        initial_state.get('monkeyLevel') == 'Down'):
        
        # 1. Monkey must go to the box.
        actions.append(move('Monkey', 0, 2))
        
        # 2. Monkey must push the box under the banana.
        actions.append(push_box(2, 1))
        
        # 3. Monkey must climb the box.
        actions.append(climb_box(1, 'Up'))
        
        # 4. Monkey can now get the banana.
        actions.append(have_banana(1))
    
    else:
        # Handle other possible starting states, or return empty
        pass

    return actions

# Execute the planning algorithm
actions = plan_actions(initial_state, goal_state)

# Print the actions in the plan
print("Plan:")
for action in actions:
    print(action)