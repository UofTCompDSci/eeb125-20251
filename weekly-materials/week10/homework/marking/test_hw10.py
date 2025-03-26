"""Automated tests for EEB125 Homework 10

Installation instructions (if running locally)
==============================================

This test script requires a few different libraries, which you can install with:

$ pip install pytest
$ pip install 'git+https://github.com/MarkUsProject/autotest-helpers.git#subdirectory=notebook_helper'
$ pip install 'git+https://github.com/UofTCompDSci/cds-testing'

After installing the libraries, you can run the tests in this file from the command line using:

$ pytest test_hw10.py
"""
import io

# This is a library for helping write some tests
import cds_testing
# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_10 as hw
# This imports the solution notebook. Often the autotesting will compare the student's
# computed value against a reference solution's computed value.
# This is illustrated in some tests further down
import Homework_10_solutions as solution
import numpy as np
import pandas as pd
import pandas.testing as pdtest
import pytest
# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer


@pytest.fixture(scope='module', autouse=True)
def run_notebooks():
    """This executes the code in the notebooks before running the tests."""
    importer.run_cells(hw, raise_on_error=False)
    student_number = hw.student_number
    cells = importer.get_cells(solution)
    for cell in cells:
        solution.student_number = student_number
        cell.run(raise_on_error=False)

# Test cases start here
###############################################################################

##################### Part 1: Data Section #######################
PART1_VARS = {
    'corals_clean': {},
    'corals_select_data': {},
    'mean_coverage': {},
    'median_coverage': {},
}

# test existance
test_part1_existance = cds_testing.make_variable_names_test(hw, PART1_VARS)

# test types
def test_part1_corals_clean_type():
    """Test that the variable 'corals_clean' refers to a pandas DataFrame.
    """
    assert hasattr(hw, 'corals_clean'),\
        "The 'corals_clean' variable is not defined in your notebook."
    assert isinstance(hw.corals_clean, pd.DataFrame),\
        f"Expected the variable 'corals_clean' to refer to a pandas.DataFrame, but found {type(hw.corals_clean)}."

def test_part1_corals_select_data_type():
    """Test that the variable 'corals_select_data' refers to a pandas DataFrame.
    """
    assert hasattr(hw, 'corals_select_data'),\
        "The 'corals_select_data' variable is not defined in your notebook."
    assert isinstance(hw.corals_select_data, pd.DataFrame),\
        f"Expected the variable 'corals_select_data' to refer to a pandas.DataFrame, but found {type(hw.corals_select_data)}."

def test_part1_median_coverage_type():
    """Test that the variable 'median_coverage' refers to a float.
    """
    assert hasattr(hw, 'median_coverage'),\
        "The 'median_coverage' variable is not defined in your notebook."
    assert isinstance(hw.median_coverage, float),\
        f"Expected the variable 'median_coverage' to refer to a float, but found {type(hw.median_coverage)}."

def test_part1_mean_coverage_type():
    """Test that the variable 'mean_coverage' refers to a float.
    """
    assert hasattr(hw, 'mean_coverage'),\
        "The 'mean_coverage' variable is not defined in your notebook."
    assert isinstance(hw.mean_coverage, float),\
        f"Expected the variable 'mean_coverage' to refer to a float, but found {type(hw.mean_coverage)}."

# test size (rows and columns)
def test_part1_corals_clean_size():
    """Test that 'corals_clean' has the expected number of rows and columns.
    """
    assert hasattr(hw, 'corals_clean'),\
        "The 'corals_clean' variable is not defined in your notebook."
    assert isinstance(hw.corals_clean, pd.DataFrame),\
        f"Expected the variable 'corals_clean' to refer to a pandas.DataFrame, but found {type(hw.corals_clean)}."
    axes = hw.corals_clean.axes
    rows = len(axes[0])
    cols = len(axes[1])
    soln_axes = solution.corals_clean.axes
    soln_rows = len(soln_axes[0])
    soln_cols = len(soln_axes[1])
    assert rows == soln_rows,\
        f"Expected {soln_rows} rows but found {rows} rows in your 'corals_clean' DataFrame."
    assert cols == soln_cols,\
        f"Expected {soln_cols} columns but found {cols} columns in your 'corals_clean' DataFrame."

def test_part1_corals_select_data_size():
    """Test that 'corals_select_data' has the expected number of rows and columns.
    """
    assert hasattr(hw, 'corals_select_data'),\
        "The 'corals_select_data' variable is not defined in your notebook."
    assert isinstance(hw.corals_select_data, pd.DataFrame),\
        f"Expected the variable 'corals_select_data' to refer to a pandas.DataFrame, but found {type(hw.corals_select_data)}."
    axes = hw.corals_select_data.axes
    rows = len(axes[0])
    cols = len(axes[1])
    soln_axes = solution.corals_select_data.axes
    soln_rows = len(soln_axes[0])
    soln_cols = len(soln_axes[1])
    assert rows == soln_rows,\
        f"Expected {soln_rows} rows but found {rows} rows in your 'corals_select_data' DataFrame."
    assert cols == soln_cols,\
        f"Expected {soln_cols} columns but found {cols} columns in your 'corals_select_data' DataFrame."

# test equality
test_part1_equality = cds_testing.make_answer_equality_test(hw, solution, PART1_VARS)


##################### Part 2: Bootstrap Confidence Interval #######################
PART2_VARS = {
        # "one_bootstrap_med": {},  # function
        "bootstrap_medians": {},
        "lower_bound": {},
        "upper_bound": {},
        }

# test existance
test_part2_existance = cds_testing.make_variable_names_test(hw, PART2_VARS)

def test_part2_one_bootstrap_med_existance():
    """Test that the variable 'one_bootstrap_med' exists.
    """
    assert hasattr(hw, 'one_bootstrap_med'),\
        "The 'one_bootstrap_med' variable is not defined in your notebook."

# test types
def test_part2_bootstrap_medians_type():
    """Test that the variable 'bootstrap_medians' refers to a list of floats.
    """
    assert hasattr(hw, 'bootstrap_medians'),\
        "The 'bootstrap_medians' variable is not defined in your notebook."
    assert isinstance(hw.bootstrap_medians, list),\
        f"Expected the variable 'bootstrap_medians' to refer to a list, but found {type(hw.bootstrap_medians)}."
    sample_value = hw.bootstrap_medians[0]
    assert isinstance(sample_value, float),\
        f"Expected the elements of 'bootstrap_medians' to be floats, but found {type(sample_value)}"

def test_part2_lower_bound_type():
    """Test that the variable 'lower_bound' refers to a float.
    """
    assert hasattr(hw, 'lower_bound'),\
        "The 'lower_bound' variable is not defined in your notebook."
    assert isinstance(hw.lower_bound, float),\
        f"Expected the variable 'lower_bound' to refer to a float, but found {type(hw.lower_bound)}."

def test_part2_upper_bound_type():
    """Test that the variable 'upper_bound' refers to a float.
    """
    assert hasattr(hw, 'upper_bound'),\
        "The 'upper_bound' variable is not defined in your notebook."
    assert isinstance(hw.upper_bound, float),\
        f"Expected the variable 'upper_bound' to refer to a float, but found {type(hw.upper_bound)}."

# test size 
def test_part2_bootstrap_medians_size():
    """Test that 'bootstrap_medians' has the expected length.
    """
    assert hasattr(hw, 'bootstrap_medians'),\
        "The 'bootstrap_medians' variable is not defined in your notebook."
    assert isinstance(hw.bootstrap_medians, list),\
        f"Expected the variable 'bootstrap_medians' to refer to a list, but found {type(hw.bootstrap_medians)}."
    assert len(hw.bootstrap_medians) == len(solution.bootstrap_medians), \
        f"Expected the variable 'bootstrap_medians' to have length {len(solution.bootstrap_medians)} but found {len(hw.bootstrap_medians)}"

# test equality
def test_part2_one_bootstrap_med_equality():
    """Test that the function 'one_bootstrap_med' computes the correct values.
    """
    assert hasattr(hw, 'one_bootstrap_med'),\
        "The 'one_bootstrap_med' variable is not defined in your notebook."
    np.random.seed(10101)
    data = solution.corals_select_data
    hw_med = hw.one_bootstrap_med(data)
    np.random.seed(10101)
    soln_med = solution.one_bootstrap_med(data)
    assert hw_med == pytest.approx(soln_med),\
        f"The 'one_bootstrap_med' function did not compute expected value\n"\
        f"Expected {soln_med} with np.random.seed(10101), got {hw_med}.)"

test_part2_equality = cds_testing.make_answer_equality_test(hw, solution, PART2_VARS)