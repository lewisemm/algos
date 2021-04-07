import pytest

from graphs.adj_matrix import Graph

@pytest.fixture
def graph1():
    """
         A
        /|\ 
       B E F
       |   |
       C   G
        \ 
         D
        
    Matrix index mapping:
    A - 0
    B - 1
    C - 2
    D - 3
    E - 4
    F - 5
    G - 6
    """
    g = Graph(7)
    g.set_vertex(0, 'A')
    g.set_vertex(1, 'B')
    g.set_vertex(2, 'C')
    g.set_vertex(3, 'D')
    g.set_vertex(4, 'E')
    g.set_vertex(5, 'F')
    g.set_vertex(6, 'G')
    g.set_edge('A', 'B')
    g.set_edge('A', 'E')
    g.set_edge('A', 'F')
    g.set_edge('B', 'C')
    g.set_edge('C', 'D')
    g.set_edge('F', 'G')
    return g

@pytest.fixture
def graph2():
    """
        A--B
        | /|\ 
        |/ | C
        E--D/

    Matrix index mapping:
    A - 0
    B - 1
    C - 2
    D - 3
    E - 4
    """
    g = Graph(5)
    g.set_vertex(0, 'A')
    g.set_vertex(1, 'B')
    g.set_vertex(2, 'C')
    g.set_vertex(3, 'D')
    g.set_vertex(4, 'E')
    g.set_edge('A', 'B')
    g.set_edge('A', 'E')
    g.set_edge('B', 'C')
    g.set_edge('B', 'D')
    g.set_edge('B', 'E')
    g.set_edge('C', 'D')
    g.set_edge('D', 'E')
    return g

def test_bfs(graph1, graph2):
    bfs = graph1.bfs('A')
    assert bfs == ['A', 'B', 'E', 'F', 'C', 'G', 'D']
    bfs = graph2.bfs('A')
    assert bfs == ['A', 'B', 'E', 'C', 'D']

def test_dfs(graph1, graph2):
    bfs = graph1.dfs('A')
    assert bfs == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    dfs = graph2.dfs('A')
    assert dfs == ['A', 'B', 'C', 'D', 'E']
