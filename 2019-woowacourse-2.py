# lands = [ [10, 0, 30, 5], [0, 30, 20, 50], [30, 30, 40, 40] ]
# wells = [ [15, 15, 25, 25], [40, 10, 50, 20] ]
# point = [10, 10, 30, 30]
lands = [ [0, 0, 20, 10], [10, 20, 20, 40], [30, 0, 50, 20] ]
wells = [ [20, 40, 30, 50], [30, 20, 50, 30] ]
point = [20, 30, 30, 40]



def solution(lands, wells, point):
    answer = True

    for land in lands:
        if point[0] >= land[0] and point[1] <= land[1] \
                and point[2] >= land[2] and point[3] <= land[3]:
            answer = True
        elif point[0] >= land[0] and point[1] >= land[1] \
                and point[2] >= land[2] and point[3] >= land[3]:
            answer = True
        elif point[0] <= land[0] and point[1] <= land[1] \
                and point[2] <= land[2] and point[3] <= land[3]:
            answer = True
        else:
            answer = False
            return answer

    for well in wells:
        if point[0] <= well[0] and point[1] <= well[1] \
                and point[2] >= well[2] and point[3] >= well[3]:
            answer = True
        elif point[0] <= well[0] and point[1] <= well[1] \
                and point[2] <= well[2] and point[3] >= well[3]:
            answer = True
        else:
            answer = False
            return answer
    return answer


print(solution(lands, wells, point))
