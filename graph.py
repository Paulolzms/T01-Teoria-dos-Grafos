import time

class Graph:
  def __init__(self, count_nodes: int = 0, count_edges: int = 0, adj_list: list[list[int]] = []) -> None:
    self.count_nodes = count_nodes
    self.count_edges = count_edges
    self.adj_list = adj_list
    if adj_list == []:
      for _ in range(self.count_nodes):
        adj_list.append([])


  def read_file(self, file_name: str):
    tempo_inicial = time.time()
    f = open("maze/" + file_name)
    num_caracter_in_line = len(f.readline()) - 1
    f.close()
    f = open("maze/" + file_name)
    str = f.read()
    str = str.replace('\n', '')
    for _ in str:
      self.add_node()
    self.add_edges_maze(str, num_caracter_in_line)
    print("Caminho:", self.dfs(self.where_start(str), str))
    tempo_final = time.time()
    print("Tempo execução:", (tempo_final - tempo_inicial))

  def add_edges_maze(self, str, num_line):
    for i in range(len(str)):
        if str[i] != '#':
          if i-num_line >= 0 and str[i-num_line] != '#':
            self.adj_list[i].append(i-num_line)
          if i-1 >= 0 and str[i-1] != '#':
            self.adj_list[i].append(i-1)
          if i+1 <= len(str)-1 and str[i+1] != '#':
            self.adj_list[i].append(i+1)
          if i+num_line <= len(str)-1 and str[i+num_line] != '#':
            self.adj_list[i].append(i+num_line)
        
  def add_node(self):
    self.count_nodes += 1
    self.adj_list.append([])

  def dfs(self, s, str) -> list:
    desc = [0 for _ in self.adj_list]
    S = [s]
    R = [s]
    desc[s] = 1
    while S != []:
      u = S[-1]
      if str[u] == 'E':
        return S
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
    if S == []:
      print("Non-existent path!")

  def where_start(self, str):
    for i in range(len(str)):
      if str[i] == 'S':
        return i