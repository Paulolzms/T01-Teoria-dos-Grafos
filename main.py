from graph import Graph

g1 = Graph(0)
g1.read_file("toy.txt")
print("G1:", g1.adj_list)
print("DFS:", g1.dfs(8))
