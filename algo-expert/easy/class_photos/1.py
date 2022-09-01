# easy, greedy algorithms
# time O(nlogn) | space O(1)
def classPhotos(red, blue):
    red.sort()
    blue.sort()
    front, back = (red, blue) if red[0] < blue[0] else (blue, red)
    for i in range(len(back)):
        if back[i] <= front[i]:
            return False
    return True
