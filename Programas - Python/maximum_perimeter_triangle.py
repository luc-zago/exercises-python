def maximumPerimeterTriangle(sticks):
    s_sticks = sorted(sticks)
    degenerate_triangles = list()
    for i in range(len(sticks)):
        try:
            if s_sticks[i] + s_sticks[i + 1] > s_sticks[i + 2]:
                degenerate_triangles.append(s_sticks[i : i + 3])
        except IndexError:
            break
    if degenerate_triangles:
        return degenerate_triangles[-1]
    return [-1]


if __name__ == "__main__":
    print(maximumPerimeterTriangle([1, 2, 3, 4, 5, 10]))
    print(maximumPerimeterTriangle([1, 2, 3]))
