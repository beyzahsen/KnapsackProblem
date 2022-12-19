# define the list of items, their weights, and their values
items = ['item1', 'item2', 'item3']
weights = [10, 20, 30]
values = [60, 100, 120]

# define the weight limit
weight_limit = 50

# define the KnapsackProblem class
class KnapsackProblem(LocalSearchProblem):
    def generate_random_state(self):
        # generate a random valid state (i.e. a list of items that fits within the weight limit)
        state = []
        total_weight = 0
        while total_weight <= weight_limit:
            item = random.choice(items)
            if total_weight + weights[items.index(item)] <= weight_limit:
                state.append(item)
                total_weight += weights[items.index(item)]
        return state

    def value(self, state):
        # return the total value of the items in the knapsack
        return sum(values[items.index(item)] for item in state)

    def successors(self, state):
        # generate the successor states by adding or removing an item from the knapsack
        successors = []
        for item in items:
            if item in state:
                new_state = state[:]
                new_state.remove(item)
                successors.append(new_state)
            else:
                new_state = state[:]
                new_state.append(item)
                if sum(weights[items.index(i)] for i in new_state) <= weight_limit:
                    successors.append(new_state)
        return successors

# create an instance of the KnapsackProblem class
problem = KnapsackProblem()

# solve the problem using the hill_climbing algorithm
result = hill_climbing(problem)

# print the final state and its value
print(result.state)
print(result.value)
