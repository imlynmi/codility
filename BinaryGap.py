def solution(N):
    # Implement your solution here
    binary_str = '{0:b}'.format(N)
    last_1 = binary_str.rfind('1')
    binary_str = binary_str[:last_1]
    gap_list = binary_str.split('1')
    longest_gap = 0

    for g in gap_list:
        longest_gap = max(longest_gap, len(g))

    return longest_gap