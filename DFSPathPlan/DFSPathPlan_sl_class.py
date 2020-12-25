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


class DFSPathPlanLeaf:
    # start at fixed leaf switch
    def __init__(self, pathNums, spineMax):
        self.pathNums = pathNums
        self.spineMax = spineMax
        self.run()

    def run(self):
        for i in range(1, self.spineMax):
            spine = i
            Matrix_leaf = self.TopomapMaker_leaf(spine)
            pathNum = DFLSPathPlan(Matrix_leaf)
            self.pathNums.append(pathNum)
        return self.pathNums

    def TopomapMaker_leaf(self, spine):
        sNum = spine * 3
        Matrix_leaf = [[0] * sNum for n in range(sNum)]
        for i in range(spine * 2):
            for j in range(spine * 2, sNum):
                Matrix_leaf[i][j] = 1
                Matrix_leaf[j][i] = 1
        return Matrix_leaf


class DFSPathPlanSpine:
    # start at fixed spine switch
    def __init__(self, pathNums, spineMax):
        self.pathNums = pathNums
        self.spineMax = spineMax
        self.run()

    def run(self):
        for i in range(1, self.spineMax):
            spine = i
            Matrix_spine = self.TopomapMaker_spine(spine)
            pathNum = DFLSPathPlan(Matrix_spine)
            self.pathNums.append(pathNum)
        return self.pathNums

    def TopomapMaker_spine(self, spine):
        sNum = spine * 3
        Matrix_leaf = [[0] * sNum for n in range(sNum)]
        for i in range(spine):
            for j in range(spine, sNum):
                Matrix_leaf[i][j] = 1
                Matrix_leaf[j][i] = 1
        return Matrix_leaf


if __name__ == '__main__':
    pathNums = []
    # DFSPathPlanLeaf(pathNums, 21)
    # [2, 4, 10, 4, 18, 4, 26, 4, 34, 4, 42, 4, 50, 4, 58, 4, 66, 4, 74, 4]
    DFSPathPlanSpine(pathNums, 21)
    # [4, 2, 12, 4, 20, 4, 28, 4, 36, 4, 44, 4, 52, 4, 60, 4, 68, 4, 76, 4]
    print(pathNums)

