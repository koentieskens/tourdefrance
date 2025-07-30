import pandas as pd
import webbrowser
import sys
import os
import traceback


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def main():
    try:
        print("Tour de France Rider Page Opener")
        print("-" * 30)

        # If no argument provided, ask for input
        if len(sys.argv) != 2:
            bib_number = input("Enter rider bib number: ").strip()
        else:
            bib_number = sys.argv[1].strip()

        if not bib_number:
            print("Error: No bib number provided.")
            input("Press Enter to exit...")
            return

        # Load the CSV file using the resource path
        csv_path = resource_path("tdf2025_startlist.csv")
        print(f"Looking for CSV file at: {csv_path}")  # Debug info

        try:
            df = pd.read_csv(csv_path)
        except FileNotFoundError:
            print("Error: Could not find tdf2025_startlist.csv file.")
            print(f"Expected location: {csv_path}")
            input("Press Enter to exit...")
            return

        # Look up the row
        row = df[df["bib"] == bib_number]

        if row.empty:
            print(f"No rider found with bib number {bib_number}.")
            input("Press Enter to exit...")
            return

        rider_name = row.iloc[0]["rider_name"]
        rider_url = row.iloc[0]["rider_link"]
        print(f"Opening webpage for {rider_name}: {rider_url}")
        """
        try:
            webbrowser.get("windows-default").open(rider_url)
            print("Webpage opened successfully!")
        except Exception as e:
            print(f"Error opening webpage: {str(e)}")
        """
        input("Press Enter to exit...")

    except Exception as e:
        print("\nAn error occurred:")
        print("-" * 30)
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nFull error details:")
        print(traceback.format_exc())
        input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
