def organize_ranking(rank):
    unorganized_rank = list(set(rank))
    unorganized_rank.sort()
    return unorganized_rank[::-1]

def climbingLeaderboard(ranked, player):
    player_rank = []
    rank = organize_ranking(ranked)
    for points in player:
        rank.append(points)
        rank = organize_ranking(rank)
        player_rank.append(rank.index(points) + 1)
    return player_rank

if __name__ == '__main__':
    print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))
    print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
    print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
