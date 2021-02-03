left, right, merge = [], [], []
        
        l, r = newInterval
        for i, interval in enumerate(intervals):
            if interval[1] < l:
                left.append(interval)
            elif interval[0] > r:
                right.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        return left + [newInterval] + right