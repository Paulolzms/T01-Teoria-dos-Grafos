from graph import Graph

option = True
while option:
  file = input('Informe o arquivo (0 para sair): ')
  if file == '0':
    option = False
    print("Saindo...")
    break
  else:
    g1 = Graph(0, adj_list=[])
    g1.read_file(file)