class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from collections import Counter, defaultdict
        # 所有点统计
        points_dict = Counter(tuple(point) for point in points)
        # 把唯一点列举出来
        not_repeat_points = list(points_dict.keys())
        n = len(not_repeat_points)
        if n == 1: return points_dict[not_repeat_points[0]]
        res = 0
        # 求最大公约数
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        for i in range(n - 1):
            # 点1
            x1, y1 = not_repeat_points[i][0], not_repeat_points[i][1]
            # 斜率
            slope = defaultdict(int)
            for j in range(i + 1, n):
                # 点2
                x2, y2 = not_repeat_points[j][0], not_repeat_points[j][1]
                dy, dx = y2 - y1, x2 - x1
                # 方式一 利用公约数
                g = gcd(dy, dx)
                if g != 0:
                    dy //= g
                    dx //= g
                slope["{}/{}".format(dy, dx)] += points_dict[not_repeat_points[j]]
                # --------------------
                # 方式二, 利用除法(不准确, 速度快)
                # if dx == 0:
                #     tmp = "#"
                # else:
                #     tmp = dy * 1000 / dx * 1000
                # slope[tmp] += points_dict[not_repeat_points[j]]
                #------------------------------
            res = max(res, max(slope.values()) + points_dict[not_repeat_points[i]])
        return res


class Solution:
    def maxPoints(self, points):
        res = 0
        if not points:
            return res
        for i in range(len(points)):
            dic = {}
            same = 0
            curMax = 0
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same += 1
                    continue
                if (points[i][0] - points[j][0]) == 0:
                    rate = float('inf')
                else:
                    rate = (points[i][1] - points[j][1]) * 1000 / (points[i][0] - points[j][0]) * 1000
                dic[rate] = dic.get(rate, 0) + 1
                curMax = max(curMax, dic[rate])
            res = max(res, curMax + same + 1)
        return res
