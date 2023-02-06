from graph import Graph

option = '1'
while option != '0':
  option = input('Informe o arquivo (0 para sair): ')
  if option != '0':
    print("Procesando...")
    g1 = Graph(0, adj_list=[])
    g1.read_file(option)
    # print("G1:", g1.adj_list)
  else: print("Saindo...")
