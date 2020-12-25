#!/usr/bin/python
import sys
import copy


def DFLSPathPlan(Matrix):
    sys.setrecursionlimit(1000000)
    linkState = copy.deepcopy(Matrix)
    pathCount = [0]
    paths = []

    def DFLS(v, isNewPath):
        if isNewPath == 1:
            isNewPath = 0
            paths.append('#')
            paths.append(str(v + 1))
            pathCount[0] += 1
        else:
            paths.append(str(v + 1))
        for j in range(len(Matrix)):
            if linkState[v][j] == 1:
                linkState[v][j] = 0
                linkState[j][v] = 0
                isNewPath = DFLS(j, isNewPath)
        return 1
    DFLS(0, 1)
    return pathCount[0]


class DFSPathPlanEdge:
    # start at fixed edge switch
    def __init__(self, pathNums, podMax):
        self.pathNums = pathNums
        self.podMax = podMax
        self.run()

    def run(self):
        for i in range(4, self.podMax, 2):
            Matrix = self.TopomapMaker(i)
            pathNum = DFLSPathPlan(Matrix)
            self.pathNums.append(pathNum)

        return self.pathNums

    def TopomapMaker(self, pod):
        eNum = pod * pod // 2
        aNum = pod * pod // 2
        cNum = pod * pod // 4
        sNum = eNum + aNum + cNum
        Matrix = [[0] * sNum for n in range(sNum)]

        # link_edge_aggre
        aIndex = eNum
        for eIndex in range(0, eNum, pod // 2):
            for i in range(pod // 2):
                for j in range(pod // 2):
                    Matrix[eIndex + i][aIndex + j] = 1
                    Matrix[aIndex + j][eIndex + i] = 1
            aIndex += (pod // 2)

        # link_aggre_core
        for cIndex in range(eNum + aNum, sNum):
            if cIndex < eNum + aNum + cNum // 2:
                aIndex = eNum
            else:
                aIndex = eNum + 1
            while aIndex < (eNum + 2 * cNum):
                Matrix[cIndex][aIndex] = 1
                Matrix[aIndex][cIndex] = 1
                aIndex += 2

        return Matrix


class DFSPathPlanCore:
    # start at fixed core switch
    def __init__(self, pathNums, podMax):
        self.pathNums = pathNums
        self.podMax = podMax
        self.run()

    def run(self):
        for i in range(4, self.podMax, 2):
            Matrix = self.TopomapMaker(i)
            pathNum = DFLSPathPlan(Matrix)
            self.pathNums.append(pathNum)
        return self.pathNums

    def TopomapMaker(self, pod):
        eNum = pod * pod // 2
        aNum = pod * pod // 2
        cNum = pod * pod // 4
        sNum = eNum + aNum + cNum
        Matrix = [[0] * sNum for n in range(sNum)]

        # link_aggre_core
        for cIndex in range(cNum):
            if cIndex < cNum // 2:
                aIndex = cNum
            else:
                aIndex = cNum + 1
            while aIndex < (aNum + cNum):
                Matrix[cIndex][aIndex] = 1
                Matrix[aIndex][cIndex] = 1
                aIndex += 2

        # link_edge_aggre
        aIndex = cNum
        for eIndex in range(cNum + aNum, sNum, pod // 2):
            for i in range(pod // 2):
                for j in range(pod // 2):
                    Matrix[eIndex + i][aIndex + j] = 1
                    Matrix[aIndex + j][eIndex + i] = 1
            aIndex += (pod // 2)

        return Matrix


if __name__ == "__main__":
    # pathNums = [1]
    # DFSPathPlanEdge(pathNums, 21)
    # [1, 4, 32, 4, 96, 4, 191, 4, 319, 4][482, 4, 682, 4, 821, 4]
    pathNums = [2]
    DFSPathPlanCore(pathNums, 21)
    # [1, 5, 26, 9, 79, 13, 171, 17, 287, 21][424, 25, 567, 29, 721, 33]
    print(pathNums)
