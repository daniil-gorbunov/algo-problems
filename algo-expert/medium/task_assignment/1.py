# medium, greedy algorithms
# time O(nlogn) | space O(n)
def taskAssignment(k, tasks):
    durations = {}
    for i, task in enumerate(tasks):
        if task not in durations:
            durations[task] = set()
        durations[task].add(i)
    tasks.sort()
    assignment = []
    for i in range(k):
        assignment.append([
            durations[tasks[i]].pop(),
            durations[tasks[len(tasks) - 1 - i]].pop()
        ])
    return assignment
