# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
class Verticle:
    def __init__(self, key):
        self.key = key
        self.value = None

    # def add_key(self,key):
    #     self.key = key
    def add_value(self, value):
        self.value = value


class Edge_set:
    def __init__(self):
        self.verticles = []
        self.edges = []

    def add_verticle(self, x: Verticle):
        if x.key not in self.get_all_keys():
            self.verticles.append(x)

    def add_edges(self, y):
        self.edges.append(y)

    def get_value_by_key(self, key):
        for v in self.verticles:
            if v.key == key:
                return v.value
            # break

    def get_all_keys(self):
        res = []
        for v in self.verticles:
            res.append(v.key)
        return res


def solution(N, A, B):
    # write your code in Python 3.6
    edge_set = Edge_set()
    va = Verticle(A[0])
    vb = Verticle(B[0])
    edge_set.add_verticle(va)
    edge_set.add_verticle(vb)
    edge_set.add_edges((A[0], B[0]))
    Graph = [edge_set]  # add the first edge: edge A[0],B[0] into the graph
    for i in range(1, N + 1):
        if i not in A and i not in B:  # only a verticle
            verticle_set = Edge_set()
            verticle = Verticle(i)
            # verticle.add_key(key=i)
            verticle_set.add_verticle(verticle)
            Graph.append(verticle_set)
    M = len(A)  # the length of A and B is M
    for i in range(1, M):
        a = A[i]
        b = B[i]
        for edge_set1 in Graph:  # add all edges into the graph
            v_a = Verticle(a)
            v_b = Verticle(b)
            if v_a.key not in edge_set1.get_all_keys() and v_b.key not in edge_set1.get_all_keys():
                edge_set2 = Edge_set()
                edge_set2.add_verticle(v_a)
                edge_set2.add_verticle(v_b)
                edge_set2.add_edges((a, b))
                Graph.append(edge_set2)  # add new edges into the graph
                break
            elif v_a.key in edge_set1.get_all_keys() and v_b.key not in edge_set1.get_all_keys():
                edge_set1.add_verticle(v_b)
                edge_set1.add_edges((a, b))
                break
            elif v_a.key not in edge_set1.get_all_keys() and v_b.key in edge_set1.get_all_keys():
                edge_set1.add_verticle(v_a)
                edge_set1.add_edges((a, b))
                break
            else:
                edge_set1.add_edges((a, b))
                break
    sorted(Graph, key=lambda edge_set: len(edge_set.edges))
    values = [i for i in range(N,0,-1)]
    # sorted(values, reverse=False)
    for edge_set in Graph:
        num_of_v = len(edge_set.verticles)
        for i in range(num_of_v):
            v = edge_set.verticles[i]
            v.add_value(values[i])
        values = values[num_of_v:]
    sum = 0
    for edge_set in Graph:
        for edges in edge_set.edges:
            # for edge in edges:
            key1 = edges[0]
            key2 = edges[1]
            sub_sum = edge_set.get_value_by_key(key1) + edge_set.get_value_by_key(key2)
            sum += sub_sum
    print(sum)
    return sum


solution(5, [2, 2, 1, 2], [1, 3, 4, 4])
