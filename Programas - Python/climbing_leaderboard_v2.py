def climbingLeaderboard(ranked, player):
    player_rank = []
    rank = sorted(set(ranked))
    for points in player:
        rank.append(points)
        rank = sorted(set(rank))
        player_rank.append(len(rank) - rank.index(points))
    return player_rank

if __name__ == '__main__':
    print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))
    print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
    print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
