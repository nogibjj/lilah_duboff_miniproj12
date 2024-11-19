"""Takes a csv file, reads it, and creates graphs"""

import lib


def main():
    """Loads a dataset
    generates summary stats and visualizations"""
    path = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/wages_by_education.csv"
    wages_and_education_df = lib.load_dataset(path)
    if wages_and_education_df is not None:
        lib.full_describe(wages_and_education_df)
        lib.mens_bar_chart(wages_and_education_df, False)
        lib.womens_bar_chart(wages_and_education_df, False)


if __name__ == "__main__":
    main()
