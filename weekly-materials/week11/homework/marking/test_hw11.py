"""Automated tests for EEB125 Homework 11

Installation instructions (if running locally)
==============================================

This test script requires a few different libraries, which you can install with:

$ pip install pytest
$ pip install 'git+https://github.com/MarkUsProject/autotest-helpers.git#subdirectory=notebook_helper'
$ pip install 'git+https://github.com/UofTCompDSci/cds-testing'

After installing the libraries, you can run the tests in this file from the command line using:

$ pytest test_hw11.py
"""
import io

# This is a library for helping write some tests
import cds_testing
# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_11 as hw
# This imports the solution notebook. Often the autotesting will compare the student's
# computed value against a reference solution's computed value.
# This is illustrated in some tests further down
import Homework_11_solutions as solution
import numpy as np
import pandas as pd
import pandas.testing as pdtest
import pytest
# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer
from statsmodels.regression.linear_model import OLS, RegressionResults


@pytest.fixture(scope='module', autouse=True)
def run_notebooks():
    """This executes the code in the notebooks before running the tests."""
    importer.run_cells(hw, raise_on_error=False)
    importer.run_cells(solution, raise_on_error=False)

# Test cases start here
###############################################################################

##################### Part 1: Data Section #######################
PART1_VARS = {
    'fish_data': {}, # test all columns at once, even though weight_g_sqrt is added afterward
}

# test existance
test_part1_existance = cds_testing.make_variable_names_test(hw, PART1_VARS)

# test types
def test_part1_fish_data_type():
    """Test that the variable 'fish_data' refers to a pandas DataFrame.
    """
    assert hasattr(hw, 'fish_data'),\
        "The 'fish_data' variable is not defined in your notebook."
    assert isinstance(hw.fish_data, pd.DataFrame),\
        f"Expected the variable 'fish_data' to refer to a pandas.DataFrame, but found {type(hw.fish_data)}."


# test size (rows and columns)
def test_part1_fish_data_size():
    """Test that 'fish_data' has the expected number of rows and columns.
    """
    assert hasattr(hw, 'fish_data'),\
        "The 'fish_data' variable is not defined in your notebook."
    assert isinstance(hw.fish_data, pd.DataFrame),\
        f"Expected the variable 'fish_data' to refer to a pandas.DataFrame, but found {type(hw.fish_data)}."
    axes = hw.fish_data.axes
    rows = len(axes[0])
    cols = len(axes[1])
    soln_axes = solution.fish_data.axes
    soln_rows = len(soln_axes[0])
    soln_cols = len(soln_axes[1])
    assert rows == soln_rows,\
        f"Expected {soln_rows} rows but found {rows} rows in your 'fish_data' DataFrame."
    assert cols == soln_cols,\
        f"Expected {soln_cols} columns but found {cols} columns in your 'fish_data' DataFrame."

# test equality
test_part1_equality = cds_testing.make_answer_equality_test(hw, solution, PART1_VARS)


##################### Part 2: Methods #######################
PART2_VARS = {
        # "regmod1": {},   statsmodel model
        # "regmod1_fit": {}, statsmodel RegressionResultsWrapper
        # "regmod2": {},   statsmodel model
        # "regmod2_fit": {}, statsmodel RegressionResultsWrapper
        "regmod1_rsquared": {},
        "regmod2_rsquared": {},
        }

# test existance
test_part2_existance = cds_testing.make_variable_names_test(hw, PART2_VARS)

def test_part2_regmod1_existance():
    """Test that the variable 'regmod1' exists.
    """
    assert hasattr(hw, 'regmod1'),\
        "The 'regmod1' variable is not defined in your notebook."

def test_part2_regmod2_existance():
    """Test that the variable 'regmod2' exists.
    """
    assert hasattr(hw, 'regmod2'),\
        "The 'regmod2' variable is not defined in your notebook."

def test_part2_regmod1_fit_existance():
    """Test that the variable 'regmod1_fit' exists.
    """
    assert hasattr(hw, 'regmod1_fit'),\
        "The 'regmod1_fit' variable is not defined in your notebook."

def test_part2_regmod2_fit_existance():
    """Test that the variable 'regmod2_fit' exists.
    """
    assert hasattr(hw, 'regmod2_fit'),\
        "The 'regmod2_fit' variable is not defined in your notebook."

# test types
def test_part2_regmod1_type():
    """Test that the variable 'regmod1' refers to statsmodels OLS model.
    """
    assert hasattr(hw, 'regmod1'),\
        "The 'regmod1' variable is not defined in your notebook."
    assert isinstance(hw.regmod1, OLS),\
        f"Expected the variable 'regmod1' to refer to statsmodels OLS model, but found {type(hw.regmod1)}."

def test_part2_regmod2_type():
    """Test that the variable 'regmod2' refers to statsmodels OLS model.
    """
    assert hasattr(hw, 'regmod2'),\
        "The 'regmod2' variable is not defined in your notebook."
    assert isinstance(hw.regmod2, OLS),\
        f"Expected the variable 'regmod2' to refer to statsmodels OLS model, but found {type(hw.regmod2)}."

def test_part2_regmod1_rsquared_type():
    """Test that the variable 'regmod1_rsquared' refers to a float.
    """
    assert hasattr(hw, 'regmod1_rsquared'),\
        "The 'regmod1_rsquared' variable is not defined in your notebook."
    assert isinstance(hw.regmod1_rsquared, float),\
        f"Expected the variable 'regmod1_rsquared' to refer to a float, but found {type(hw.regmod1_rsquared)}."

def test_part2_regmod2_rsquared_type():
    """Test that the variable 'regmod2_rsquared' refers to a float.
    """
    assert hasattr(hw, 'regmod2_rsquared'),\
        "The 'regmod2_rsquared' variable is not defined in your notebook."
    assert isinstance(hw.regmod2_rsquared, float),\
        f"Expected the variable 'regmod2_rsquared' to refer to a float, but found {type(hw.regmod2_rsquared)}."


# test equality
def test_part2_regmod1_fit_param_equality():
    """Test that the variable 'regmod1_fit' has the correct parameters.
    """
    assert hasattr(hw, 'regmod1_fit'),\
        "The 'regmod1_fit' variable is not defined in your notebook."
    soln_params = solution.regmod1_fit.params
    try:
        student_params = hw.regmod1_fit.params
    except:
        raise TypeError(f"Your variable 'regmod1_fit' does not have a 'params' attribute. Make sure you saved the output of fitting the model to this variable" )

    pdtest.assert_series_equal(student_params, soln_params,
        f"Your regmod1_fit params {student_params} do not equal the expected params {soln_params}.",
        check_index=False)

def test_part2_regmod2_fit_param_equality():
    """Test that the variable 'regmod1_fit' has the correct parameters.
    """
    assert hasattr(hw, 'regmod2_fit'),\
        "The 'regmod2_fit' variable is not defined in your notebook."
    soln_params = solution.regmod2_fit.params
    try:
        student_params = hw.regmod2_fit.params
    except:
        raise TypeError(f"Your variable 'regmod2_fit' does not have a 'params' attribute. Make sure you saved the output of fitting the model to this variable" )

    pdtest.assert_series_equal(student_params, soln_params,
        f"Your regmod2_fit params {student_params} do not equal the expected params {soln_params}.",
        check_index=False)


test_part2_equality = cds_testing.make_answer_equality_test(hw, solution, PART2_VARS)