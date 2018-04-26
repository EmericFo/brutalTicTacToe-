import unittest


class Line(object):

    line = {}

    # def fillCell(self, line, position, value):
    #     tuple_cell = (position, value)
    #     new_tupleLine = line + (tuple_cell,)
    #     return new_tupleLine

    # line = self.line.fillCell((), 0, self.PLAYER_TWO)
    # line = self.line.fillCell(line, 1, self.PLAYER_TWO)

    def fillCell(self, position, value):
        self.line[position] = value
        return self.line

    def valueOf(self, position):
        return self.line[position]


class TicTocToeTest(unittest.TestCase):
    PLAYER_ONE = "X"
    PLAYER_TWO = "Y"

    def setUp(self):
        self.line = Line()

    def testEmptyLineHasNoWinner(self):
        # Given

        # When

        # Code
        winner = "No Winner"

        # Then
        self.assertEqual(winner, "No Winner")


    def testOnCellLineWithPlayerOneThenPlayerOneWins(self):
        # Given

        # When
        self.line.fillCell(0, self.PLAYER_ONE)

        # Code
        winner = "No Winner"
        if self.line.valueOf(0) == self.PLAYER_ONE:
            winner = "Player One"

        # Then
        self.assertEqual(winner, "Player One")


    def testOneLineTwoCellsWithPlayerOneAndTwoThenNoPlayerWins(self):
        # Given

        # When
        self.line.fillCell(0, self.PLAYER_ONE)
        self.line.fillCell(1, self.PLAYER_TWO)

        # Code
        winner = "No Winner"
        if self.line.valueOf(0) == self.PLAYER_ONE and self.line.valueOf(1) == self.line.valueOf(0):
            winner = "Player One"
        # Then
        self.assertEqual(winner, "No Winner")

    def testOneLineTwoCellsWithPlayerOneOnlyThenPlayerOneWins(self):
        # Given

        # When
        self.line.fillCell(0, self.PLAYER_ONE)
        self.line.fillCell(1, self.PLAYER_ONE)

        # Code
        winner = "No Winner"
        if self.line.valueOf(0) == self.PLAYER_ONE and self.line.valueOf(1) == self.line.valueOf(0):
            winner = "Player One"

        # Then
        self.assertEqual(winner, "Player One")

    def testOneLineTwoCellsWithPlayerTwoOnlyThenPlayerTwoWins(self):
        # Given

        # When
        self.line.fillCell(0, self.PLAYER_TWO)
        self.line.fillCell(1, self.PLAYER_TWO)

        # Code
        winner = "No Winner"
        if self.line.valueOf(0) == self.PLAYER_TWO and self.line.valueOf(1) == self.line.valueOf(0):
            winner = "Player Two"

        # Then
        self.assertEqual(winner, "Player Two")
