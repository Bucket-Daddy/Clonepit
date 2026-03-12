# main.py

from backend.spin_engine import spin
from frontend.renderer import run_frontend

def main():
    res, modifiers, result = spin()
    run_frontend(res, result, modifiers)

if __name__ == "__main__":
    main()
