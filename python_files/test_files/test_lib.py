"""
Testing the library file functions

"""

import io
import sys

sys.path.append("python_files")

from python_files.lib import (
    load_dataset,
    full_describe,
    mens_bar_chart,
    womens_bar_chart,
)

# Shortened mock CSV data as a string (only "year" and "fatal" columns)
mock_csv_data = """year,less_than_hs,high_school,some_college,bachelors_degree,advanced_degree
2010,12.50,15.00,17.50,23.50,30.00
2020,15.75,17.25,20.75,25.75,35.50
2030,17.00,18.50,22.00,27.00,40.00
2040,19.25,20.75,25.25,30.25,50.50
2050,21.50,24.00,27.50,35.50,60.00"""

mock_mens_data = """year,men_less_than_hs,men_high_school,men_some_college,men_bachelors_degree,men_advanced_degree
2010,12.50,15.00,17.50,23.50,30.00
2020,15.75,17.25,20.75,25.75,35.50
2030,17.00,18.50,22.00,27.00,40.00
2040,19.25,20.75,25.25,30.25,50.50
2050,21.50,24.00,27.50,35.50,60.00
"""

mock_womens_data = """year,women_less_than_hs,women_high_school,women_some_college,women_bachelors_degree,women_advanced_degree
2010,12.50,15.00,17.50,23.50,30.00
2020,15.75,17.25,20.75,25.75,35.50
2030,17.00,18.50,22.00,27.00,40.00
2040,19.25,20.75,25.25,30.25,50.50
2050,21.50,24.00,27.50,35.50,60.00
"""

full_test_path = io.StringIO(mock_csv_data)
mens_test_path = io.StringIO(mock_mens_data)
womens_test_path = io.StringIO(mock_womens_data)


def test_load_dataset():
    """test that loading the CSV will work"""
    result = load_dataset(full_test_path)
    assert result is not None
    assert result.shape == (5, 6)


def test_full_describe():
    test_path = io.StringIO(mock_csv_data)
    test_df = load_dataset(test_path)
    result = full_describe(test_df)
    assert result is not None


def test_mens_bar_chart():
    test_path = io.StringIO(mock_mens_data)
    test_df = load_dataset(test_path)
    result = mens_bar_chart(test_df, False)
    assert result is None


def test_womens_bar_chart():
    test_path = io.StringIO(mock_womens_data)
    test_df = load_dataset(test_path)
    result = womens_bar_chart(test_df, False)
    assert result is None


if __name__ == "__main__":
    test_load_dataset()
    test_full_describe()
    test_mens_bar_chart()
    test_womens_bar_chart()
