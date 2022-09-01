# hard, famous algorithms
# time O(j+d) | space O(j+d)
def topologicalSort(jobs, deps):
    depJobs = {job: [] for job in jobs}
    for [req, job] in deps:
        depJobs[req].append(job)
    temp = set()
    visited = set()
    sortedJobs = []
    for job in jobs:
        if visit(job, depJobs, temp, visited, sortedJobs) == -1:
            return []
    return sortedJobs[::-1]

def visit(job, depJobs, temp, visited, sortedJobs):
    if job in visited:
        return
    if job in temp:
        return -1
    temp.add(job)
    for depJob in depJobs[job]:
        if visit(depJob, depJobs, temp, visited, sortedJobs) == -1:
            return -1
    temp.remove(job)
    visited.add(job)
    sortedJobs.append(job)
