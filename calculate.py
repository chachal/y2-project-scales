def scoreCount(scaleA, points, player, level=0):
    apoints = 0
    contained = list(scaleA.contains)
    for entry in contained:
        if entry.objectID == 0:
            if entry.location[0] != "A":
                level += 1
                points = scoreCount(entry, points, player, level) * abs(entry.location[1])
                level -= 1
            else:
                level += 1
                points += scoreCount(entry, points, player, level) * abs(entry.location[1])
                level -= 1
                apoints += points
                points = 0
        else:
            if scaleA.scaleID == "A" and entry.owner == player.pID:
                apoints += entry.weight
                points = apoints
            elif scaleA.scaleID != "A" and entry.owner == player.pID:
                points += entry.weight
    if level == 0:
        points = apoints
    return points

def isBalanced(scaleA, weight):
    return True
