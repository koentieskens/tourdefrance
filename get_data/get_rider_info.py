import pandas as pd
import webbrowser
import argparse


def open_rider_page(bib_number):
    """Open the webpage for a rider given their bib number."""
    try:
        # Load the CSV file
        df = pd.read_csv("tdf2025_startlist.csv")
        bib_number = int(bib_number)
        # Look up the row
        row = df[df["bib"] == bib_number]

        if row.empty:
            print(f"No rider found with bib {bib_number}.")
            return False

        rider_name = row.iloc[0]["rider_name"]
        rider_url = row.iloc[0]["rider_link"]
        print(f"{rider_name} page: {rider_url}")
        #webbrowser.get("windows-default").open(rider_url)
        return True

    except FileNotFoundError:
        print("Error: Could not find tdf2025_startlist.csv file.")
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Open a rider\'s webpage using their bib number.')
    parser.add_argument('bib', type=str, help='The bib number of the rider')

    args = parser.parse_args()
    open_rider_page(args.bib)


if __name__ == "__main__":
    main()
