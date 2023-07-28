from game.core.puzzle_game import PuzzleGame
from game.core.utils.puzzle_dificulty_enum import PuzzleDifficultyEnum

if __name__ == '__main__':
    game = PuzzleGame()
    # game.run_game(x_size=2, y_size=3, difficulty=PuzzleDifficultyEnum.Hard)
    game.run_game()