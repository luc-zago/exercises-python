def migratoryBirds(arr):
    birds_set = set(arr)
    s_set = sorted(birds_set)
    m_count = 0
    m_f = s_set[0]
    for m in s_set:
        if arr.count(m) > m_count:
            m_count = arr.count(m)
            m_f = m
    return m_f


if __name__ == "__main__":
    print(migratoryBirds([1, 1, 2, 2, 3]))
