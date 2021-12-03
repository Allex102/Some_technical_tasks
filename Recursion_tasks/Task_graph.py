from collections import defaultdict
class incidenceMatrix:
    def __init__(self, vertexNumber):
        self.matrix = [[] for k in range(vertexNumber)]

    def showGraph(self):
        for i, row in enumerate(self.matrix, 1):
            print (i, row)

    def isEdge(self, v1, v2):
        return any(x and y for x, y in zip(self.matrix[v1-1], self.matrix[v2-1]))

    def addEdge(self, v1, v2):
        for i, row in enumerate(self.matrix, 1):
            row.append(int(v1==i or v2==i))

    def removeEdge(self, v1, v2):
        num_edges = len(self.matrix[0])
        for j in range(num_edges):
            if self.matrix[v1-1][j] and self.matrix[v2-1][j]:
                for row in self.matrix:
                    del row[j]
                return
        raise Exception('Edge(%d, %d) not found' % (v1, v2))

    def removeVertex(self, v):
        targetrow = self.matrix.pop(v-1)
        for col, selector in reversed(list(enumerate(targetrow))):
            if selector:
                for row in self.matrix:
                    del row[col]

a, b, c, d, e, f, g, h = range(8)                   #Список смежности
N = [
{b:2, c:1, d:3, e:9, f:4},    # a
{c:4, e:3},                   # b
{d:8},                        # c
{e:7},                        # d
{f:5},                        # e
{c:2, g:2, h:2},              # f
{f:1, h:6},                   # g
{f:9, g:8}                    # h
   ]
edges = [('a', 'b'), ('a', 'b'), ('a', 'c')]

adj_list = defaultdict(lambda: defaultdict(lambda: 0))
for start, end in edges:
    adj_list[start][end] += 1
    print (adj_list['a'])


if __name__ == '__main__':
    GrafIM = incidenceMatrix(5) #verticesNumber
    GrafIM.addEdge(2,3)
    GrafIM.addEdge(1,3)
    GrafIM.addEdge(2,1)
    GrafIM.addEdge(5,2)
    print (GrafIM.isEdge(2,4))
    for pair in [(2,3), (1,3), (2,1), (5,2)]:
        print (GrafIM.isEdge(*pair))
    GrafIM.showGraph()
    print ("-------")
    GrafIM.removeEdge(2,5)
    GrafIM.showGraph()
    print ("-------")
    GrafIM.removeVertex(2)
    GrafIM.showGraph()    