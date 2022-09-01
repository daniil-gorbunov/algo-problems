# hard, recursion
# time O(n) | space O(d)
def getLowestCommonManager(topManager, r1, r2):
    return searchReport(topManager, r1, r2)[1]

def searchReport(node, r1, r2):
    numReportsFound = 0
    for report in node.directReports:
        hasReport, commonManager = searchReport(report, r1, r2)
        if commonManager:
            return True, commonManager
        if hasReport:
            numReportsFound += 1
        if numReportsFound == 2 or (numReportsFound == 1 and node in {r1, r2}):
            return True, node
    if numReportsFound == 1 or node in {r1, r2}:
        return True, None
    return False, None

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
