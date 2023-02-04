class Graph:
  def __init__(self, count_nodes: int = 0, count_edges: int = 0, adj_list: list[list[int]] = []) -> None:
    self.count_nodes = count_nodes
    self.count_edges = count_edges
    self.adj_list = adj_list
    if adj_list == []:
      for _ in range(self.count_nodes):
        adj_list.append([])

  def read_file(self, file_name: str):
    f = open("maze/" + file_name)
    num_lines = len(f.readline()) - 1
    f.close()
    f = open("maze/" + file_name)
    str = f.read()
    str = str.replace('\n', '')
    for _ in str:
      self.adj_list.append([])
    print(num_lines)
    self.add_edges_maze(str, num_lines)

  def add_edges_maze(self, str, num_lines):
    for i in range(len(str)):
        if str[i] != '#':
          if i-num_lines >= 0 and str[i-num_lines] != '#':
            self.adj_list[i].append(i-num_lines)
          if i-1 >= 0 and str[i-1] != '#':
            self.adj_list[i].append(i-1)
          if i+1 <= len(str)-1 and str[i+1] != '#':
            self.adj_list[i].append(i+1)
          if i+num_lines <= len(str)-1 and str[i+num_lines] != '#':
            self.adj_list[i].append(i+num_lines)
        
  def add_node(self):
    self.count_nodes += 1
    self.adj_list.append([])

  def dfs(self, s) -> list:
    desc = [0 for _ in self.adj_list]
    S = [s]
    R = [s]
    desc[s] = 1
    while S != []:
        u = S[-1]
        desempilhar = True
        for v in self.adj_list[u]:
            if desc[v] == 0:
                desempilhar = False
                S.append(v)
                R.append(v)
                desc[v] = 1
                break
        if desempilhar:
            S.pop()
    return R
