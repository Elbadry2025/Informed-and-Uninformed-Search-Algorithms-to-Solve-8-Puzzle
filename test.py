import unittest

import A_Star
import main
import dfs


class TestMethods(unittest.TestCase):

    def test_swap(self):
        self.assertEqual(main.swap('123045678', 0, 1), '213045678')

    def test_getNeighbours(self):
        self.assertEqual(main.get_neighbors('123045678'),['123405678', '123645078', '023145678'])

    def test_getNeighbours1(self):
        self.assertEqual(main.get_neighbors('012345678'), ['102345678', '312045678'])

    def test_BFS(self):
        self.assertEqual(main.BFS('867254301'), False)

    def test_BFS1(self):
        self.assertEqual(main.BFS('208174653'), False)

    def test_BFS2(self):
        self.assertEqual(main.BFS('283164705'), False)

    def test_solvability(self):
        self.assertEqual(main.isSolvable('103245678'),False)



    # DFS
    def test_DFS_getNeighbours(self):
        self.assertEqual(dfs.get_neighbours('123045678'),['123405678', '123645078', '023145678'])


    #A*

    #Unsolvable State
    def test_A_Star(self):
        self.assertEqual(A_Star.A_Star("123456870",False),False)


    # Compare between Manhattan and Euclidean
    #Solvable State with Euclidean Distance
    def test_A_Star1(self):
        self.assertEqual(A_Star.A_Star("145678023", False)[1], 19824 )
    #Solvable State with Manhattan Distance
    def test_A_Star2(self):
        self.assertEqual(A_Star.A_Star("145678023",True)[1], 558)


