def breakingRecords(scores):
    min_count = 0
    max_count = 0
    min_score = scores[0]
    max_score = scores[0]
    for score in scores:
        if score > max_score:
            max_count += 1
            max_score = score
        if score < min_score:
            min_count += 1
            min_score = score
    return [min_count, max_count]


if __name__ == "__main__":
    print(breakingRecords([12, 24, 10, 24]))
