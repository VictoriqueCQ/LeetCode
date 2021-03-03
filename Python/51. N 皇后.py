from typing import List

class Solution:


    def solveNQueens(self, n: int) -> List[List[str]]:
        res = self.helper([-1] * n, 0, n, [])
        return res

    def helper(self, positions, rowIndex, n, res):
        if rowIndex == n:
            result = self.printSolution(positions, n)
            res.append(result)
            return

        for column in range(n):
            positions[rowIndex] = column
            if self.isValid(positions, rowIndex):
                self.helper(positions, rowIndex + 1, n, res)
        return res

    def isValid(self, positions, rowIndex):
        for i in range(rowIndex):
            if positions[i] == positions[rowIndex]:
                return False
            if abs(positions[i] - positions[rowIndex]) == rowIndex - i:
                return False
        return True

    def printSolution(self, positions, n):
        result = []
        for row in range(n):
            lines = ""
            for col in range(n):
                if positions[row] == col:
                    lines += "Q"
                else:
                    lines += "."
            result.append(lines)
        return result


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions

