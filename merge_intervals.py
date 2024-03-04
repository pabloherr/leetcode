
#def merge(intervals: list[list[int]]) -> list[list[int]]:
#        for i in range(len(intervals)-1):
#            if i != len(intervals)-1:
#                if intervals[i][1]>= intervals[i+1][0]:
#                    # + +
#                    if intervals[i][0] > intervals[i+1][0] and intervals[i][1] > intervals[i+1][1]:
#                        intervals[i] = [intervals[i+1][0],intervals[i][1]]
#                        del intervals[i+1]
#                        
#                    #+ -
#                    elif intervals[i][0] >= intervals[i+1][0] and intervals[i][1] <= intervals[i+1][1]:
#                        del intervals[i]
#                        
#                    # - +
#                    elif intervals[i][0] <= intervals[i+1][0] and intervals[i][1] >= intervals[i+1][1]:
#                        del intervals[i+1]
#                        
#                    # - -
#                    elif intervals[i][0] < intervals[i+1][0] and intervals[i][1] < intervals[i+1][1]:
#                        intervals[i] = [intervals[i][0],intervals[i+1][1]]
#                        del intervals[i+1]
#                    
#                    else:
#                        intervals[i] = [intervals[i][0],intervals[i+1][1]]
#                        del intervals[i+1]
#        return intervals
#
#print(merge([[0,0],[2,]]))


def merge( intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals, key=lambda x: x [0]) #ordeno lista 
    print(intervals)
    ans = []
    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])
    
    return ans

print(merge([[3,7],[2,6],[8,10],[15,18]]))