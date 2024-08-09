class State:
    def __init__(self, attributes):
        self.attributes = attributes

class Operator:
    def __init__(self, name, conditions, actions):
        self.name = name
        self.conditions = conditions
        self.actions = actions

    def can_apply(self, state):
        return all(condition(state) for condition in self.conditions)

    def apply(self, state):
        for action in self.actions:
            action(state)

class SOAR:
    def __init__(self):
        self.operators = []

    def add_operator(self, operator):
        self.operators.append(operator)

    def run(self, initial_state):
        current_state = initial_state
        while True:
            applicable_operators = [op for op in self.operators if op.can_apply(current_state)]
            if not applicable_operators:
                break
            chosen_operator = self.choose_operator(applicable_operators)
            chosen_operator.apply(current_state)
        return current_state

    def choose_operator(self, operators):
        # In a more complex implementation, this method could use
        # various strategies to choose between multiple applicable operators
        return operators[0]

# Example usage
def is_not_goal(state):
    return state.attributes['value'] < 10

def increment(state):
    state.attributes['value'] += 1

initial_state = State({'value': 0})
increment_operator = Operator('increment', [is_not_goal], [increment])

soar = SOAR()
soar.add_operator(increment_operator)

final_state = soar.run(initial_state)
print(f"Final state: {final_state.attributes}")