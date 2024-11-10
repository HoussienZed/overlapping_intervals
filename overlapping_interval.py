def merge_intervals(interval):
    # sort the elements of parameter w.r.t first element in sublist
    interval.sort(key=lambda i: i[0])
    # initializing a list to store merged elements
    merged = [interval[0]]

    # merging overlapping intervals
    for i in range(1, len(interval)):
        last_merged = merged[-1]
        if last_merged[1] >= interval[i][0]:
            if last_merged[1] <= interval[i][1]:
                last_merged[1] = interval[i][1]
            else:
                continue

        else:
            merged.append(interval[i])

    return merged


print(merge_intervals([[2, 3], [3, 4], [4, 5], [1, 8]]))


def merge_intervals_without_lambda(interval):
    # comparing the first element of each subarray and appending them to a merged list
    sorted_interval = []
    length = len(interval)
    for i in range(length - 1, 0, -1):                         # i = 3 , 2, 1
        # target index = 1
        target_index = len(interval) - 1
        for j in range(len(interval) - 2, -1, -1):                  # j = 0
            # interval[1][0] = 2 > interval[0][0] =1 => true
            if interval[target_index][0] > interval[j][0]:
                continue                               # target_index = 1
            else:
                target_index = j
                # sorted_interval = [[6, 8][3,4][2,5]]
        sorted_interval.append(interval[target_index])
        # interval = [1,2][2,5]
        interval.pop(target_index)
    sorted_interval.append(interval[0])
    sorted_interval.reverse()
    print(f"sorted_interval is {sorted_interval}")  # to check the sorted array
    merged = [sorted_interval[0]]

    # merging overlapping intervals
    for i in range(1, len(sorted_interval)):
        last_merged = merged[-1]
        if last_merged[1] >= sorted_interval[i][0]:
            if last_merged[1] <= sorted_interval[i][1]:
                last_merged[1] = sorted_interval[i][1]
            else:
                continue

        else:
            merged.append(sorted_interval[i])

    return merged


print(merge_intervals_without_lambda([[2, 3], [3, 4], [4, 5], [7, 8]]))
