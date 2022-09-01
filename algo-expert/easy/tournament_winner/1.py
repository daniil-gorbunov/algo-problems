# easy, arrays
# time O(n) | space O(t) n - competitions num, k - teams num
def tournamentWinner(competitions, results):
    best = competitions[0][0]
    scores = {best: 0}
    for i, comp in enumerate(competitions):
        winner = comp[results[i] - 1]
        scores[winner] = scores.setdefault(winner, 0) + 3
        if scores[winner] > scores[best]:
            best = winner
    return best
