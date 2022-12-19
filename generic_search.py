# define the list of items, their weights, and their values
items = ['item1', 'item2', 'item3']
weights = [10, 20, 30]
values = [60, 100, 120]

# define the weight limit
weight_limit = 50

# define the KnapsackProblem class
class KnapsackProblem(SearchProblem):
    def actions(self, state):
        # return a list of the items that can be added to the knapsack
        return [item for item in items if item not in state]

    def result(self, state, action):
        # add the given item to the state and return the new state
        state.append(action)
        return state

    def is_goal(self, state):
        # return True if the total weight of the items in the knapsack is less than or equal to the weight limit and the total value is maximized
        total_weight = sum(weights[items.index(item)] for item in state)
        total_value = sum(values[items.index(item)] for item in state)
        return total_weight <= weight_limit and total_value == max(values)

    def heuristic(self, state):
        # return the difference between the total value of the items in the knapsack and the weight limit
        total_weight = sum(weights[items.index(item)] for item in state)
        total_value = sum(values[items.index(item)] for item in state)
        return total_value - weight_limit

# create an instance of the KnapsackProblem class
problem = KnapsackProblem()

# define a list of search algorithms to use
algorithms = [breadth_first, depth_first, greedy, astar]

# solve the problem using the generic_search function
for algorithm in algorithms:
    result = generic_search(problem, algorithm)
    print(f'{algorithm.__name__}:')
    print(f'  state: {result.state}')
    print(f'  value: {result.value}')
