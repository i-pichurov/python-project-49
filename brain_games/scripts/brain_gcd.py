#!/usr/bin/env python3
import brain_games.games.engine
import brain_games.games.gcd


def main():
    brain_games.games.engine.start_game(brain_games.games.gcd.br_gcd)


if __name__ == '__main__':
    main()
