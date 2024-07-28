#!/usr/bin/env python3
import brain_games.engine
import brain_games.games.prime


def main():
    """
    Calls the start_game() function from the brain_games/engine.py module.
    Args:
        module: brain_games/games/prime.py
    """
    brain_games.engine.start_game(brain_games.games.prime)


if __name__ == '__main__':
    main()
