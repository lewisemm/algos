import unittest

from graphs.representations.adj_matrix import Graph


class TestAdjMatrixGraph(unittest.TestCase):
    def create_graph1(self):
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


    def create_graph2(self):
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

    def test_bfs_graph1(self):
        graph1 = self.create_graph1()
        bfs = graph1.bfs('A')
        self.assertEqual(bfs, ['A', 'B', 'E', 'F', 'C', 'G', 'D'])
    
    def test_bfs_graph2(self):
        graph2 = self.create_graph2()
        bfs = graph2.bfs('A')
        self.assertEqual(bfs, ['A', 'B', 'E', 'C', 'D'])

    def test_dfs_graph1(self):
        graph1 = self.create_graph1()
        dfs = graph1.dfs('A')
        self.assertEqual(dfs, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    
    def test_dfs_graph2(self):
        graph2 = self.create_graph2()
        dfs = graph2.dfs('A')
        self.assertEqual(dfs, ['A', 'B', 'C', 'D', 'E'])
