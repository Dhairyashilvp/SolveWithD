class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # co = [(0,0)]
        # x, y = 0, 0
        # for d in path:
        #     if d == "N":
        #         x += 1
        #     elif d == "S":
        #         x -= 1
        #     elif d == "E":
        #         y += 1
        #     else:
        #         y -= 1
        #     if (x,y) in co:
        #         return True
        #     co.append((x,y))
        # return False
        coordinates = [0,0]
        cross = False
        visited= []
        visited.append([0,0])
        for x in path:
            if x == "N":
                coordinates[0]+=1
            if x == "S":
                coordinates[0] -= 1
            if x == "E":
                coordinates[1] += 1
            if x == "W":
                coordinates[1] -= 1
            if coordinates in visited:
                cross= True
                break
            newcoordinates=list(coordinates)
            visited.append(newcoordinates)
        return(cross)