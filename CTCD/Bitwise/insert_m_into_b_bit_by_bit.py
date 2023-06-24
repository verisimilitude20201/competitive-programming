"""
Complexity:
-----------
Time: O(1)
Space: O(1)
"""
def insert_m_into_n(i, j, m, n):
    all_ones =  ~0
    left_mask = all_ones << (j + 1)
    right_mask = (all_ones << i) - 1
    mask = left_mask | right_mask
    n_cleared = n & mask
    m_shifted = m << i
    return n_cleared | m_shifted