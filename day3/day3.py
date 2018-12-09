import re

#1195 @ 502,230: 24x28

def parseLine(claim):
    claim = re.split("[#@:x\W]+", claim)
    claim = [int(x) for x in claim if x != '']
    return {
        "id": claim[0],
        "topLeft": (claim[1], claim[2]),
        "bottomRight": (claim[1] + claim[3], claim[2] + claim[4]),
        "overlapped": False,
    }


def areOverlapping(A, B):
    A_X1, A_Y1 = A["topLeft"]
    A_X2, A_Y2 = A["bottomRight"]
    B_X1, B_Y1 = B["topLeft"]
    B_X2, B_Y2 = B["bottomRight"]

    return A_X1 < B_X2 and \
            A_X2 > B_X1 and \
            A_Y1 < B_Y2 and \
            A_Y2 > B_Y1

claimIDs = open("biginput", 'r').readlines()
seen = []

for claim in claimIDs:
    claim = parseLine(claim)
    print(claim["id"])
    for seenClaim in seen:
        if claim["topLeft"] != seenClaim["topLeft"] and areOverlapping(claim, seenClaim):
            claim["overlapped"] = True
            seenClaim["overlapped"] = True

    seen.append(claim)

for claim in seen:
    if not claim["overlapped"]:
        print(claim)
        exit()

"""
for i, x in enumerate(nonoverlap):
    for y in seen:
        if x["topLeft"] != y["topLeft"] and areOverlapping(x, y):
            x["overlapped"] = True
            y["overlapped"] = True

for claim in nonoverlap:
    if not claim["overlapped"]:
        print(claim)
"""