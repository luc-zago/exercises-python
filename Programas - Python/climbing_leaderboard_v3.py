def climbingLeaderboard(ranked, player):
    player_rank = []
    rank = []
    [rank.append(points) for points in ranked if points not in rank]
    for points in player:
        if points < rank[-1]:
            rank.append(points)
            player_rank.append(len(rank))
        else:
            for index, rank_points in enumerate(rank):
                if points == rank_points:
                    player_rank.append(index + 1)
                    break
                elif points > rank_points:
                    rank.insert(index, points)
                    player_rank.append(index + 1)
                    break
    return player_rank

if __name__ == '__main__':
    print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))
    # [4, 3, 1]
    print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
    # [6, 4, 2, 1]
    print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
    # [6, 5, 4, 2, 1]
