from collections import defaultdict, deque
class Solution:
    def topological_order(self, course, queue, seen, graph):
        if course not in seen:
            seen.add(course)

            if course in graph:
                for dependent in graph[course]:
                    if dependent not in seen:
                       self.topological_order(dependent, queue, seen, graph)

            queue.appendleft(course)



    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])

        queue = deque()
        seen = set()

        for course in graph:
            if course not in seen:
                self.topological_order(course, queue, seen, graph)

        return queue if len(queue) == numCourses else []


prerequisites = [[1,0],[2,0],[3,1],[3,2]]
solution = Solution()
print(solution.findOrder(prerequisites=prerequisites))