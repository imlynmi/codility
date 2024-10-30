def solution(X, Y, D):
    # Implement your solution here
    if X == Y:
        return 0
    
    if D >= Y:
        return 1
    
    if (Y - X) % D == 0:
        return (Y - X) // D
    else:
        return (Y - X) // D + 1