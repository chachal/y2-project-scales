def scoreCount(scaleA, points, player, level=0):
    apoints = 0
    contained = sortContains(list(scaleA.contains))
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
            if scaleA.scaleID == "A" and entry.ownerID == player.plrID:
                apoints += entry.mass
                points = apoints
                player.points = points
            elif scaleA.scaleID != "A" and entry.ownerID == player.plrID:
                points += entry.mass
                player.points = points
    if level == 0:
        points = apoints
    return points

def sortContains(contlist):
    W = []
    S = []
    contained = []
    while contlist:
        popper = contlist.pop()
        if popper.objectID == 0:
            S.append(popper)
        elif popper.objectID == 1:
            W.append(popper)
    S = sorted(S, key=lambda scale: scale.scaleID)
    W = sorted(W, key=lambda weight: weight.location[0])
    while S:
        popper = S.pop(0)
        contained.append(popper)
    while W:
        popper = W.pop(0)
        contained.append(popper)
    return contained


def isBalanced(scaleToPlace, weightLoc, scaleA, scales, bal=0, level=0):
    if scaleA.scaleID == scaleToPlace.scaleID:
        if abs(scaleA.balance + weightLoc[1]) > int(scaleA.length/2):
            return False

    for entry in scaleA.scales:
        if not entry.scales and entry.scaleID == scaleToPlace.scaleID:
            scaleA.balance += entry.mass
            if abs(scaleA.balance + (weightLoc[1] * entry.location[1])) > int(scaleA.length/2):
                return False
            elif abs(entry.balance + weightLoc[1]) > int(entry.length/2):
                return False
            else:
                return True
        elif entry.scales and entry.scaleID == scaleToPlace.scaleID:
            isBalanced(scaleToPlace, weightLoc, entry, scales, bal=0, level=0)
        else:
            scaleA.balance += entry.mass


    return True



    return True
