# Graph Maze Solver

## Descrição

Este projeto implementa um resolvedor de labirintos usando teoria de grafos. O programa lê um labirinto a partir de um arquivo de texto, representa-o como um grafo e utiliza o algoritmo DFS (Busca em Profundidade) para encontrar um caminho do ponto inicial 'S' ao ponto de saída 'E'.

## 📦 Funcionalidades

- Leitura e processamento de labirintos a partir de arquivos de texto
- Representação do labirinto como um grafo (lista de adjacência)
- Implementação do algoritmo DFS para encontrar caminhos
- Conversão de posições lineares para coordenadas (linha, coluna)
- Medição de tempo de execução

## 📂 Estrutura do Projeto
```
project/
├── maze/
│ └── maze10.txt # Exemplo de arquivo de labirinto
├── graph.py # Implementação da classe Graph
├── main.py # Interface principal
└── README.md # Este arquivo
```
## ▶️ Como Usar

1. Clone o repositório ou copie os arquivos
2. Coloque seus arquivos de labirinto na pasta `maze/` (formato igual ao `maze10.txt`)
3. Execute o programa:
```bash
python main.py
```

## 📤 Exemplo de Saída

Para o labirinto maze10.txt:
```bash
Informe o arquivo (0 para sair): maze10
Processando...
Caminho: (1, 1) (1, 2) (2, 2) (3, 2) ... (19, 19)
Tempo: 0.0025s
```

## 🧰 Requisitos

- Python 3.x
- Nenhuma dependência externa necessária

## ⛔ Limitações

- Atualmente só implementa DFS
- Não mostra o caminho visualmente no labirinto
- Assume que sempre existe um caminho válido

## 🚀 Melhorias Futuras
- Implementar outros algoritmos (BFS, A*)
- Adicionar visualização gráfica do labirinto e caminho
- Tratar melhor casos sem solução
- Otimizar a construção do grafo
