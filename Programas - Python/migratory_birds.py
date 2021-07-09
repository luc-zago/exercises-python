def remove_repeated(arr):
    new_array = []
    [new_array.append(item) for item in arr if item not in new_array]
    return new_array

def migratoryBirds(arr):
    arr.sort()
    unique_birds = remove_repeated(arr)
    more_than_one_bird = []
    for unique_bird in unique_birds:
        counter = 0
        for bird in arr:
            if unique_bird == bird:
                counter += 1
        if counter > 1:
            more_than_one_bird.append([unique_bird, counter])
    if len(more_than_one_bird) == 0:
        return arr[0]
    most_repeated_bird, higher_repetition = more_than_one_bird[0][0], more_than_one_bird[0][1]
    for bird_and_repetition in more_than_one_bird:
        if bird_and_repetition[1] > higher_repetition:
            most_repeated_bird, higher_repetition = bird_and_repetition[0], bird_and_repetition[1]
    return most_repeated_bird

if __name__ == '__main__':
    print(migratoryBirds([1, 4, 4, 4, 5, 3]))
    print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))
    print(migratoryBirds([5, 4, 7, 3, 1]))
