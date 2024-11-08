def merge_intervals(interval):
    # sort the elements of parameter w.r.t first element in sublist
    interval.sort(key=lambda i: i[0])
    # initializing a list to store merged elements
    merged = [interval[0]]

    # merging overlapping intervals
    for i in range(1, len(interval)):
        last_merged = merged[-1]
        if last_merged[1] >= interval[i][0]:
            last_merged[1] = interval[i][1]
        else:
            merged.append(interval[i])

    return merged


print(merge_intervals([[1, 3], [2, 4], [3, 5], [6, 8]]))
