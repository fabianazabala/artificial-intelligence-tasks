from numpy import inf

graph = {'Ustka': {'Slupsk': 21, 'Leba': 64}, 'Slupsk': {'Lebork': 55, 'Bytow': 70, 'Ustka': 21},
         'Leba': {'Wladyslawowo': 66, 'Lebork': 29, 'Ustka': 64}}

costs = {'Slupsk': 0, 'Ustka': inf, 'Leba': inf, 'Lebork': inf}

parents = {}


def search(source, target, graph, costs, parents):
    nextNode = source

    while nextNode != target:

        for neighbor in graph[nextNode]:

            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]

                parents[neighbor] = nextNode

            del graph[neighbor][nextNode]

        del costs[nextNode]

        nextNode = min(costs, key=costs.get)

    return parents


result = search('Ustka', 'Slupsk', graph, costs, parents)


def backpedal(source, target, searchResult):
    node = target

    backpath = [target]

    path = []

    while node != source:
        backpath.append(searchResult[node])

        node = searchResult[node]

    for i in range(len(backpath)):
        path.append(backpath[-i - 1])

    return path


print('parent dictionary={}'.format(result))

print('longest path={}'.format(backpedal('Ustka', 'Slupsk', result)))
