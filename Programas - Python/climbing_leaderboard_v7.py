def climbingLeaderboard(ranked, player):
    player_rank = []
    index = len(ranked) - 1
    difference = len(ranked) - len(set(ranked))
    count = 1
    for points in player:
        if points < ranked[-1]:
            ranked.append(points)
            player_rank.append(index - difference + count + 1)
        elif points > ranked[0]:
            ranked.insert(0, points)
            player_rank.append(1)
        else:
            while index > 0:
                if points == ranked[index]:
                    player_rank.append(index - difference + count)
                    break
                elif ranked[index - 1] > points > ranked[index]:
                    ranked.insert(index, points)
                    player_rank.append(index - difference + count)
                    break
                elif ranked[index] > points > ranked[index + 1]:
                    ranked.insert(index + 1, points)
                    player_rank.append(index - difference + count + 1)
                    break
                if ranked[index] == ranked[index - 1]:
                    while ranked[index] == ranked[index - 1]:
                        index -= 1
                        count += 1
                index -= 1
    return player_rank


if __name__ == '__main__':
    print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))
    # [4, 3, 1]
    print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
    # [6, 4, 2, 1]
    print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
    # [6, 5, 4, 2, 1]
    print(climbingLeaderboard([100, 90, 90, 80, 75, 75, 60], [50, 65, 77, 90, 102]))
    # [6, 5, 4, 2, 1]
    print(climbingLeaderboard([100, 90, 90, 80, 75, 75, 75, 60], [50, 65, 77, 90, 102]))
    # [6, 5, 4, 2, 1]
    print(climbingLeaderboard([100, 90, 90, 90, 80, 75, 75, 75, 60], [50, 65, 77, 90, 102]))
    # [6, 5, 4, 2, 1]
