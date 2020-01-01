def newRoadSystem(roadRegister):
    return [l.count(True) for l in roadRegister] == [l.count(True) for l in zip(*roadRegister)]


roadRegister = [[False, True, False, False],
                [False, False, True, False],
                [True, False, False, True],
                [False, False, True, False]]

print(newRoadSystem(roadRegister))