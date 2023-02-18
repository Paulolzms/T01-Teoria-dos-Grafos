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
    start = time.time()
    print("Processando...")
    with open("maze/" + file_name + ".txt", "r") as file:
      num_columns = len(file.readline()) - 1
      num_lines = sum(1 for lines in file)
      file.seek(0, 0)
      
      str = file.read()
      str = str.replace('\n', '')      
      for _ in str:
        self.add_node()
      self.add_edges_maze(str, num_columns)
      path = self.dfs(self.where_start(str), str)
      print(f"Caminho: {self.to_coordinates(num_columns, num_lines, path, str)}")
      print(f"Tempo: {(time.time() - start):,.4f}s")
    

  def add_edges_maze(self, str: str, num_columns: int):
    for i in range(len(str)):
        if str[i] != '#':
          if i-num_columns >= 0 and str[i-num_columns] != '#':
            self.adj_list[i].append(i-num_columns)
          if i-1 >= 0 and str[i-1] != '#':
            self.adj_list[i].append(i-1)
          if i+1 <= len(str)-1 and str[i+1] != '#':
            self.adj_list[i].append(i+1)
          if i+num_columns <= len(str)-1 and str[i+num_columns] != '#':
            self.adj_list[i].append(i+num_columns)
        
  def add_node(self):
    self.count_nodes += 1
    self.adj_list.append([])

  def dfs(self, s: int, str: str) -> list:
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

  def where_start(self, str: str) -> int:
    for i in range(len(str)):
      if str[i] == 'S':
        return i

  def to_coordinates(self, num_columns: int, num_lines: int, path: list, str: str) -> str:
    coordinates = ""
    for j in path:
      for i in range(num_lines):
        if j < num_columns * (i+1):
          u = i
          break
      for k in range(num_columns):
        if j == (num_columns * i) + k:
          v = k
      coordinates += "(" + f"{u}, " + f"{v}" + ") "
    return coordinates
    