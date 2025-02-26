import os
import pandas as pd
import kagglehub
import kaggle
from kagglehub import KaggleDatasetAdapter

def main():
    import_data()


def pull_data():
    '''
    Pulls University Rankings Dataset down from the Kaggle site
        and stores it in the data/ directory.
    '''
    # Authenticate with the Kaggle API
    kaggle.api.authenticate()

    # Download the specified dataset
    kaggle.api.dataset_download_files(
        dataset="joebeachcapital/qs-world-university-rankings-2024",
        path = "data/",
        unzip=True,
        quiet=False
    )

    # Rename the downloaded dataset
    os.rename("data/2024 QS World University Rankings 1.1 (For qs.com).csv", "data/university_ranks.csv")
    
def import_data():
    '''
    Checks to see if the data is already in the proper place and
        then opens the dataset
    '''

    # If the dataset is not yet in the proper place, pull the data
    if not os.path.isfile("data/university_ranks.csv"):
        pull_data()

    # Open the dataset
    with open("data/university_ranks.csv", "r") as infile:
        uni_ranks = pd.read_csv(infile)

    print(uni_ranks.head(5))

if __name__ == "__main__":
    main()
