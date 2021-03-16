# #
# # lru design
# # @param operators int整型二维数组 the ops
# # @param k int整型 the k
# # @return int整型一维数组
# # def LRU(self , operators , k ):
# import collections
# import sys
#
#
# class Solution:
#     def __init__(self, k):
#         self.dic = collections.OrderedDict()
#         self.capacity = k
#
#     def set(self, key, value):
#         if key in self.dic:
#             self.dic.pop(key)
#         else:
#             if self.capacity > 0:
#                 self.capacity -= 1
#             else:
#                 self.dic.popitem(False)
#         self.dic[key] = value
#
#     def get(self, key):
#         if key not in self.dic:
#             return -1
#         val = self.dic.pop(key)
#         self.dic[key] = val
#         return val
#
#
# for line in sys.stdin.readlines():
#     line = line.strip()
#     line = line.replace(' ', '')
#     a = line.split(']],')
#     k = int(a[1])
#     res = []
#     s = Solution(k)
#     for item in a[0][2:].split('],['):
#         m = item.split(',')
#         if m[0] == '1':
#             s.set(int(m[1]), int(m[2]))
#         else:
#             res.append(s.get(int(m[1])))
#     print(str(res).replace(' ', ''))

#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
# import collections
# class LRUCache():
#     def __init__(self, k):
#         self.dic = collections.OrderedDict()
#         self.capacity = k
#
#     def set(self, key, value):
#         if key in self.dic:
#             self.dic.pop(key)
#         else:
#             if self.capacity > 0:
#                 self.capacity -= 1
#             else:
#                 self.dic.popitem(False)
#         self.dic[key] = value
#
#     def get(self, key):
#         if key not in self.dic:
#             return -1
#         val = self.dic.pop(key)
#         self.dic[key] = val
#         return val
# class Solution:
#     def LRU(self , operators , k ):
#         # write code here
#         res = []
#         s = LRUCache(k)
#         for i in operators:
#             if i[0] == 1:
#                 s.set(i[1],i[2])
#             else:
#                 res.append(s.get(i[1]))
#         return res
#
# from collections import OrderedDict
# class Solution:
#     def __init__(self):
#         self.cache = OrderedDict()
#
#     def get(self, key):
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)
#         return self.cache[key]
#
#     def set(self, key, value, k):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > k:
#             self.cache.popitem(last=False)
#
#     def LRU(self, operators, k):
#         res = []
#         for opt in operators:
#             if opt[0] == 1:
#                 self.set(opt[1], opt[2], k)
#             elif opt[0] == 2:
#                 res.append(self.get(opt[1]))
#         return res


#
# lru design
# @param operators int整型二维数组 the ops
# @param k int整型 the k
# @return int整型一维数组
#
class Solution:
    def __init__(self, operators, k):
        self.k = k
        self.out = []
        self.l = []
        self.d = {}
        self.operators = operators

    def LRU(self, operators, k):
        # write code here
        self.k = k
        for o in operators:
            if o[0] == 1:
                self.set(o[1], o[2])
            else:
                self.out.append(self.get(o[1]))
        return self.out

    def get(self, key):
        if key in self.d:
            self.l.remove(key)
            self.l.append(key)
            return self.d[key]
        return -1

    def set(self, key, value):
        if key in self.d:
            self.l.remove(key)
            self.l.append(key)
        else:
            self.l.append(key)
            self.d[key] = value
        if len(self.l) > self.k:
            old = self.l.pop(0)
            self.d.pop(old)


import sys

for line in sys.stdin.readlines():
    line = line.strip()
    line = line.replace(' ', '')
    a = line.split(']],')
    k = int(a[1])
    res = []
    s = Solution(k)
    for item in a[0][2:].split('],['):
        m = item.split(',')
        if m[0] == '1':
            s.set(int(m[1]), int(m[2]))
        else:
            res.append(s.get(int(m[1])))
    print(str(res).replace(' ', ''))

s = Solution()
print(s.LRU([[1, 1, 1], [1, 2, 2], [1, 3, 2], [2, 1], [1, 4, 4], [2, 2]], 3))
