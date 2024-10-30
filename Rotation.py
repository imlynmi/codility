def solution(A, K):
    # Implement your solution here
    N = len(A)
    result = [0] * N
    
    if N == 0:
        return A

    if K == 0 or K % N == 0 or N == 1:
        return A

    if K > N:
        K = K % N

    for i in range(N):
        if i+K < N:
            rot_i = i + K
        else:
            rot_i = i + K - N
        
        result[rot_i] = A[i]

    return result