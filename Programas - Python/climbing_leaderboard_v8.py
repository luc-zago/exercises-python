def remove_repeated(array):
    index = 0
    new_list = []
    while index <= len(array) - 1:
        new_list.append(array[index])
        if index != len(array) - 1:
            if array[index] == array[index + 1]:
                while array[index] == array[index + 1]:
                    index += 1
        index += 1
    return new_list

def get_index(points, rank):
    first = 0
    last = len(rank) - 1

    while first <= last:
        middle = (first + last) // 2
        if rank[middle] < points < rank[middle - 1]:
            return middle
        elif rank[middle + 1] < points < rank[middle]:
            return middle + 1
        else:
            if points > rank[middle]:
                last = middle - 1
            else:
                first = middle + 1

def climbingLeaderboard(ranked, player):
    player_rank = []
    rank = remove_repeated(ranked)
    for points in player:
        if points < rank[-1]:
            rank.append(points)
            player_rank.append(len(rank))
        elif points > rank[0]:
            rank.insert(0, points)
            player_rank.append(1)
        else:
            try:
                index = rank.index(points)
            except ValueError:
                index = get_index(points, rank)
                rank.insert(index, points)
            finally:
                player_rank.append(index + 1)
    return player_rank

if __name__ == '__main__':
    print(climbingLeaderboard([100, 90, 90, 80], [70, 80, 105]))
    # [4, 3, 1]
    print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))
    # [6, 4, 2, 1]
    print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
    # [6, 5, 4, 2, 1]
