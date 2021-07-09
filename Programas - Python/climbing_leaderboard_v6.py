def get_index(points, rank):
    first = 0
    last = len(rank) - 1
    repeated = False

    while first <= last:
        middle = (first + last) // 2
        if rank[middle] == points:
            repeated = True
            return middle, repeated
        elif rank[middle] < points < rank[middle - 1]:
            return middle, repeated
        elif rank[middle + 1] < points < rank[middle]:
            return middle + 1, repeated
        else:
            if points > rank[middle]:
                last = middle - 1
            else:
                first = middle + 1

def climbingLeaderboard(ranked, player):
    player_rank = []
    difference = len(ranked) - len(set(ranked))
    for points in player:
        if points < ranked[-1]:
            ranked.append(points)
            player_rank.append(len(ranked) - difference)
        elif points > ranked[0]:
            ranked.insert(0, points)
            player_rank.append(1)
        else:
            index, repeated = get_index(points, ranked)
            if not repeated:
                ranked.insert(index, points)
            player_rank.append(index - difference + 1)
    return player_rank

if __name__ == '__main__':
    print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))
    # [4, 3, 1]
    print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
    # [6, 4, 2, 1]
    print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
    # [6, 5, 4, 2, 1]
