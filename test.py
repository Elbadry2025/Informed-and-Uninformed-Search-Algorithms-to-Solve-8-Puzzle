import unittest
import main


class TestMethods(unittest.TestCase):

    def test_swap(self):
        self.assertEqual(main.swap('123045678', 0, 1), '213045678')

    def test_getNeighbours(self):
        self.assertEqual(main.get_neighbors('123045678'),['023145678', '123405678', '123645078'])

    def test_getNeighbours1(self):
        self.assertEqual(main.get_neighbors('012345678'), ['102345678', '312045678'])

    def test_BFS(self):
        self.assertEqual(main.BFS('867254301'), False)

    def test_BFS1(self):
        self.assertEqual(main.BFS('208174653'), False)

    def test_BFS2(self):
        self.assertEqual(main.BFS('283164705'), False)