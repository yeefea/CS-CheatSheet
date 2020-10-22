from copy import copy, deepcopy


class State:
    def __init__(self, resource, available, claim, allocation):
        self.n_resource = len(resource)
        self.n_process = len(claim)
        self.resource = resource
        self.available = available
        self.claim = claim
        self.allocation = allocation


def safe(state: State):
    current_avail = copy(state.available)
    rest = set(range(state.n_process))
    possible = True
    while possible:
        k = -1
        for i in rest:
            alloc = state.allocation[i]
            claim = state.claim[i]
            if all(claim[j] - alloc[j] <= current_avail[j] for j in range(state.n_resource)):
                k = i
                break
        if k != -1:
            alloc = state.allocation[k]
            for j in range(state.n_resource):
                current_avail[j] += alloc[j]
            rest.remove(k)
        else:
            possible = False

    return len(rest) == 0


def bankers_algorithm(state: State, i, request):
    claim = state.claim[i]
    allocation = state.allocation[i]
    for j in range(state.n_resource):
        if allocation[j] + request[j] > claim[j]:
            return 'error'
        if request[j] > state.available[j]:
            return 'suspend'
    new_alloc = deepcopy(state.allocation)
    new_avail = copy(state.available)
    for j in range(state.n_resource):
        # increase allocation
        new_alloc[i][j] += request[j]
        # decrease available
        new_avail[j] -= request[j]
    new_state = State(state.resource, new_avail, state.claim, new_alloc)
    if safe(new_state):
        state.allocation = new_state.allocation
        state.available = new_state.available
        return 'ok'
    else:
        return 'suspend'


def demo_bankers_algorithm():
    claim = [[3, 2, 2], [6, 1, 3], [3, 1, 4], [4, 2, 2]]
    alloc = [[1, 0, 0], [5, 1, 1], [2, 1, 1], [0, 0, 2]]
    resource = [9, 3, 6]
    available = [1, 1, 2]
    state = State(resource, available, claim, alloc)
    print(safe(state))
    res = bankers_algorithm(state, 2, [1, 0, 2])
    print(res)


if __name__ == '__main__':
    demo_bankers_algorithm()
