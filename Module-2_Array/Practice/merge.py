def overlapping(intervals):
    """
    :param intervals:
    """
    for i in range(1, len(intervals)):
        print(intervals[i][1] < intervals[i-1][1])


if __name__ == '__main__':
    # n = int(input())
    # values = [list(map(int, input().split())) for _ in range(n)]
    # print(values)
    overlapping([[1, 5], [6, 25]])
    #Todo: Not done yet
