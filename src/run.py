import os
import sys
import traceback

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

def run_game():
    try:
        from src.main import main
        main()
    except Exception as e:
        print(f"Error running the game: {str(e)}")
        print("\nFull traceback:")
        traceback.print_exc()
        input("Press Enter to exit...")

if __name__ == "__main__":
    run_game()