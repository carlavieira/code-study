
class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def build_order(projects, dependences):

    def depth_first_search(graph, project, order):
        order.append(project)
        graph[project][2] = True
        for dependence in graph[project][0]:
            if not graph[dependence][2]:
                depth_first_search(graph, dependence, order)

    graph = {}
    # graph = { project: ([projetos que dependem dele], depende de alguem, visitado)
    for project in projects:
        graph[project] = [[], False, False]
    for dependence in dependences:
        #dependence a -> b     -    a : ([b], False, False), b : [[], True, False)
        print(graph[dependence[0]][0])
        graph[dependence[0]][0].append(dependence[1])
        graph[dependence[1]][1] = True
        print(graph)

    order = []
    for project in projects:
        if not graph[project][1]:
            if not graph[project][2]:
                depth_first_search(graph, project, order)

    for x in graph.values():
        if not x[2]:
            raise Exception("Can't build order")

    return order

projects = ["a", "b", "c", "d", "e", "f"]
dependencies = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")]

print(build_order(projects, dependencies))