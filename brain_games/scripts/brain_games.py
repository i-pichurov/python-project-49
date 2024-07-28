#!/usr/bin/env python3
import brain_games.cli


def main():
    """
    Calls the start_game() function from the brain_games/engine.py module.
    Args:
        module: brain_games/games/cli.py
    """
    brain_games.cli.welcome_user()


if __name__ == '__main__':
    main()
