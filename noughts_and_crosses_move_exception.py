def invalid_move(Grid,x,y):
    permit=[1,2,3]
    if x not in permit or y not in permit:
        raise ValueError(f"The square ({x},{y}) does not exist.")
        return 1
    if Grid[x-1][y-1]!=' ':
        raise ValueError(f"The square({x},{y}) is already occupied.")
        return 1
    return 0
