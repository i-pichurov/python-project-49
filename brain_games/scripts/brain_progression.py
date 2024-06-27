#!/usr/bin/env python3
import brain_games.games.engine
import brain_games.games.progression


def main():
    brain_games.games.engine.start_game(brain_games.games.progression.br_progression)


if __name__ == '__main__':
    main()
