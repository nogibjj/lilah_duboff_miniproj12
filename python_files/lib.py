import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Takes a csv file, reads it, and creates graphs"""


# create a function that loads in a dataset
def load_dataset(path):
    """Takes a string URL path to a csv file,
    loads it into the script for analysis,
    returns a dataframe"""
    try:
        data = pd.read_csv(path)
        return data
    except FileNotFoundError:
        print(f"File {path} not found")
        return None
    except Exception as error:
        print(f"Error while loading CSV File: {str(error)}")
        return None


def full_describe(wages_and_education_df):
    """function that sets a new df variable equal to the summary stats"""
    subset = wages_and_education_df[
        [
            "year",
            "less_than_hs",
            "high_school",
            "some_college",
            "bachelors_degree",
            "advanced_degree",
        ]
    ]
    summary_stats = subset.describe()
    print(summary_stats)
    return summary_stats


def mens_bar_chart(wages_and_education_df, is_jupyter):
    """builds a histogram out of the target columns"""
    men_data = {
        "Year": wages_and_education_df["year"],
        "Advanced degree": wages_and_education_df["men_advanced_degree"],
        "Bachelors degree": wages_and_education_df["men_bachelors_degree"],
        "Some college": wages_and_education_df["men_some_college"],
        "High school": wages_and_education_df["men_high_school"],
        "Less than high school": wages_and_education_df["men_less_than_hs"],
    }

    df = pd.DataFrame(men_data)
    df_long = pd.melt(
        df,
        id_vars=["Year"],
        value_vars=[
            "Advanced degree",
            "Bachelors degree",
            "Some college",
            "High school",
            "Less than high school",
        ],
        var_name="Education_Level",
        value_name="Wages",
    )

    plt.figure(figsize=(8, 6))

    sns.lineplot(
        data=df_long, x="Year", y="Wages", hue="Education_Level", legend="full"
    )
    plt.title("Average Hourly Wages by Education Level (Men)")
    plt.xlabel("Year")
    plt.ylabel("Average Hourly Wages")
    plt.legend(title="Education Level")

    plt.savefig("python_files/outputs/wages_men.png")
    plt.show()


def womens_bar_chart(wages_and_education_df, is_jupyter):
    """builds a histogram out of the target columns"""
    women_data = {
        "Year": wages_and_education_df["year"],
        "Advanced degree": wages_and_education_df["women_advanced_degree"],
        "Bachelors degree": wages_and_education_df["women_bachelors_degree"],
        "Some college": wages_and_education_df["women_some_college"],
        "High school": wages_and_education_df["women_high_school"],
        "Less than high school": wages_and_education_df["women_less_than_hs"],
    }

    df = pd.DataFrame(women_data)
    df_long = pd.melt(
        df,
        id_vars=["Year"],
        value_vars=[
            "Advanced degree",
            "Bachelors degree",
            "Some college",
            "High school",
            "Less than high school",
        ],
        var_name="Education_Level",
        value_name="Wages",
    )

    plt.figure(figsize=(8, 6))

    sns.lineplot(
        data=df_long, x="Year", y="Wages", hue="Education_Level", legend="full"
    )
    plt.title("Average Hourly Wages by Education Level (Women)")
    plt.xlabel("Year")
    plt.ylabel("Average Hourly Wages")
    plt.legend(title="Education Level")

    plt.savefig("python_files/outputs/wages_women.png")
    plt.show()
