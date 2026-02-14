# what is graph?
# this is non linear data structure that store the direction of the relation, weight of the relation and valu of the node
# there are basically 2 methods of implementing graphs but we will look into one that is more common using adjancency matrix

class Graph():
    def __init__(self,size):
        self.adj_matrix = [[0]* size for _ in range(size)]
        self.size = size
        self.vertex_data = ['']*size
    def add_edge (self,u,v):
        if 0 <= u < self.size and   0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
            
    def add_vertex_data(self,vertex,data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1)  # A - B
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(1, 2)  # B - C

g.print_graph()


# to create a directed and weighted graph we need to make 2 changes
# 1. instead of filling all the values with 0, we fill them with None
# 2. in the code where we have set [v][u] = 1, we want to remove that part and instead of 1 we will set them with the weight argument passed from that method


class weightedGraph:
    def __init__(self,size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = ['']*size
        
    def add_edge(self,u,v,weight):
        if  0<=u<self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            
    def add_vertex_data(self,vertex,data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
            
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print("\nVertex Data:")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
            
gd = weightedGraph(4)
gd.add_vertex_data(0, 'A')
gd.add_vertex_data(1, 'B')
gd.add_vertex_data(2, 'C')
gd.add_vertex_data(3, 'D')
gd.add_edge(0, 1, 3)  # A -> B with weight 3
gd.add_edge(0, 2, 2)  # A -> C with weight 2
gd.add_edge(3, 0, 4)  # D -> A with weight 4
gd.add_edge(2, 1, 1)  # C -> B with weight 1

gd.print_graph()