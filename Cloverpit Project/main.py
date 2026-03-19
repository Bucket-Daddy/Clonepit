# main.py

from backend.spin_engine import GameState, spin
from frontend.renderer import run_frontend

def main():
    state = GameState()

    # for now: single spin, single render
    res, modifiers, result = spin(state)
    run_frontend(res, result, modifiers)

if __name__ == "__main__":
    main()
