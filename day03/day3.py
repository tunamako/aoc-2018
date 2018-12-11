from collections import Counter
import re

# ** Part 1 **

def getCoords(claim):
    claim = re.split(r'[@:]+', claim)
    origin = claim[1].split(',')
    origin = (int(origin[0]), int(origin[1]))

    dims = claim[2].split('x')
    dims = (int(dims[0]), int(dims[1]))

    xCoords = [x for x in range(origin[0], origin[0] + dims[0])]
    yCoords = [y for y in range(origin[1], origin[1] + dims[1])]

    return [(x, y) for x in xCoords for y in yCoords]

def partOne(claimIDs):
    claimed = Counter()
    for claim in claimIDs:
        claimCoords = getCoords(claim)

        for coord in claimCoords:
            claimed[coord] += 1

    return len([x for x in claimed.values() if x > 1])

# ** Part 2 **
def parseID(id):
    claim = re.split(r'[@:]+', id)
    origin = claim[1].split(',')
    origin = (int(origin[0]), int(origin[1]))

    dims = claim[2].split('x')
    dims = (int(dims[0]), int(dims[1]))

    bottomRight = (origin[0] + dims[0], origin[1] + dims[1])

    return {
        "id": int(claim[0][1:]),
        "topLeft": origin,
        "botRight": bottomRight,
        "overlapped": False
    }

def claimsOverlap(A, B):
    A_X1, A_Y1 = A["topLeft"]
    A_X2, A_Y2 = A["botRight"]
    B_X1, B_Y1 = B["topLeft"]
    B_X2, B_Y2 = B["botRight"]

    return A_X1 < B_X2 and \
            A_X2 > B_X1 and \
            A_Y1 < B_Y2 and \
            A_Y2 > B_Y1

def partTwo(claimIDs):
    seenClaims = []

    for _id in claimIDs:
        curClaim = parseID(_id)
        seenClaims.append(curClaim)

    for x in seenClaims:
        for y in seenClaims:
            if x["topLeft"] != y["topLeft"] and claimsOverlap(x, y):
                x["overlapped"] = True
                y["overlapped"] = True

    for claim in seenClaims:
        if not claim["overlapped"]: return claim['id']
    


claimIDs = open("input", 'r').readlines()
print(partOne(claimIDs))
print(partTwo(claimIDs))
