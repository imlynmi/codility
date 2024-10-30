def solution(X, A):
    # Implement your solution here
    pos_set = set()
    jump_time = 0

    for K in range(len(A)):
        if A[K] not in pos_set:
            pos_set.add(A[K])
            jump_time = K
        if len(pos_set) == X:
            return jump_time
        
    return -1