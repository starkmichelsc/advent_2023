import unittest

from day02.util import Cube, get_cubes, Round, get_rounds, get_game, Game, CUBES


class UtilTestCase(unittest.TestCase):

    def test_get_cubes(self):
        expected = [Cube('red', 1), Cube('green', 2), Cube('blue', 3)]
        self.assertEqual(expected, get_cubes("1 red, 2 green, 3 blue"))

    def test_cube_eq(self):
        self.assertEqual(Cube('red', 1), Cube('red', 1))
        self.assertNotEqual(Cube('red', 1), Cube('red', 2))
        self.assertNotEqual(Cube('red', 1), Cube('blue', 1))
        self.assertNotEqual(Cube('red', 1), "")
        self.assertNotEqual(Cube('red', 1), None)

    def test_round_eq(self):
        self.assertEqual(Round([Cube('red', 1), Cube('green', 2), Cube('blue', 3)]),
                         Round([Cube('red', 1), Cube('green', 2), Cube('blue', 3)]))
        self.assertNotEqual(Round([Cube('red', 1), Cube('green', 2), Cube('blue', 3)]),
                            Round([Cube('red', 1), Cube('green', 2), Cube('blue', 4)]))
        self.assertNotEqual(Round([Cube('red', 1), Cube('green', 2), Cube('blue', 3)]), "")
        self.assertNotEqual(Round([Cube('red', 1), Cube('green', 2), Cube('blue', 3)]), None)

    def test_get_rounds(self):
        expected = [
            Round([Cube('red', 1), Cube('green', 2), Cube('blue', 3)]),
            Round([Cube('red', 4), Cube('green', 5), Cube('blue', 6)])
        ]

        self.assertEqual(expected, get_rounds("1 red, 2 green, 3 blue; 4 red, 5 green, 6 blue"))

    def test_get_game(self):
        expected = Game(1, [Round([Cube('red', 1), Cube('green', 2), Cube('blue', 3)]),
                            Round([Cube('red', 4), Cube('green', 5), Cube('blue', 6)])
                            ]
                        )

        self.assertEqual(expected, get_game("Game 1: 1 red, 2 green, 3 blue; 4 red, 5 green, 6 blue"))

    def test_game_is_possible(self):
        game = get_game(f"Game 1: {CUBES['red']} red, {CUBES['green']} green, {CUBES['blue']} blue; {CUBES['red']-1} red, {CUBES['green']-1} green, {CUBES['blue']} blue")
        self.assertTrue(game.is_possible())
        game2 = get_game(f"Game 1: {CUBES['red']+1} red, {CUBES['green']} green, {CUBES['blue']} blue; {CUBES['red']-1} red, {CUBES['green']-1} green, {CUBES['blue']} blue")
        self.assertFalse(game2.is_possible())
        game3 = get_game(f"Game 1: {CUBES['red']} red, {CUBES['green']} green, {CUBES['blue']} blue; {CUBES['red']+1} red, {CUBES['green']-1} green, {CUBES['blue']} blue")
        self.assertFalse(game3.is_possible())