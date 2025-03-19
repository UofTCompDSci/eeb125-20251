"""Automated tests for EEB125 Homework 9

Installation instructions (if running locally)
==============================================

This test script requires a few different libraries, which you can install with:

$ pip install pytest
$ pip install 'git+https://github.com/MarkUsProject/autotest-helpers.git#subdirectory=notebook_helper'
$ pip install 'git+https://github.com/UofTCompDSci/cds-testing'

After installing the libraries, you can run the tests in this file from the command line using:

$ pytest test_hw9.py
"""
import io

# This is a library for helping write some tests
import cds_testing
# This imports the student notebook, but does not yet run all the code cells
# The module name needs to matche the student file name, omitting the .ipynb extension
import Homework_9 as hw
# This imports the solution notebook. Often the autotesting will compare the student's
# computed value against a reference solution's computed value.
# This is illustrated in some tests further down
import Homework_9_solutions as solution
import pandas as pd
import pandas.testing as pdtest
import pytest
# This import is required to import Jupyter notebooks like regular Python files
from notebook_helper import importer


@pytest.fixture(scope='module', autouse=True)
def run_notebooks():
    """This executes the code in the notebooks before running the tests."""
    cells = importer.get_cells(hw)
    for cell in cells:
        cell.run(raise_on_error=False)
    student_number = hw.student_number

    cells = importer.get_cells(solution)
    for cell in cells:
        solution.student_number = student_number
        cell.run(raise_on_error=False)


###############################################################################
# Test cases start here
###############################################################################

##################### Data  Step 1 #######################
DATAS1_VARS = {
    'corals_data': {},
    'corals_clean': {},
}

# test existance
test_data_step1_existance = cds_testing.make_variable_names_test(hw, DATAS1_VARS)

# test types
def test_data_step1_corals_data_type():
    """Test that the variable 'corals_data' refers to a pandas DataFrame.
    """
    assert hasattr(hw, 'corals_data'),\
        "The 'corals_data' variable is not defined in your notebook."
    assert isinstance(hw.corals_data, pd.DataFrame),\
        f"Expected the variable 'corals_data' to refer to a pandas.DataFrame, but found {type(hw.corals_data)}."

def test_data_step_1_corals_clean_type():
    """Test that the variable 'corals_clean' refers to a pandas DataFrame.
    """
    assert hasattr(hw, 'corals_clean'),\
        "The 'corals_clean' variable is not defined in your notebook."
    assert isinstance(hw.corals_clean, pd.DataFrame),\
        f"Expected the variable 'corals_clean' to refer to a pandas.DataFrame, but found {type(hw.corals_clean)}."

# test size (rows and columns)
def test_data_step1_corals_data_size():
    """Test that 'corals_data' has the expected number of rows and columns.
    """
    assert hasattr(hw, 'corals_data'),\
        "The 'corals_data' variable is not defined in your notebook."
    assert isinstance(hw.corals_data, pd.DataFrame),\
        f"Expected the variable 'corals_data' to refer to a pandas.DataFrame, but found {type(hw.corals_data)}."
    axes = hw.corals_data.axes
    rows = len(axes[0])
    cols = len(axes[1])
    soln_axes = solution.corals_data.axes
    soln_rows = len(soln_axes[0])
    soln_cols = len(soln_axes[1])
    assert rows == soln_rows,\
        f"Expected {soln_rows} rows but found {rows} rows in your 'corals_data' DataFrame."
    assert cols == soln_cols,\
        f"Expected {soln_cols} columns but found {cols} columns in your 'corals_data' DataFrame."

def test_data_step1_corals_clean_size():
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

def test_data_step1_corals_clean_column_names():
    assert hasattr(hw, 'corals_clean'),\
        "The 'corals_clean' variable is not defined in your notebook."
    assert isinstance(hw.corals_clean, pd.DataFrame),\
        f"Expected the variable 'corals_clean' to refer to a pandas.DataFrame, but found {type(hw.corals_clean)}."
    true_cols = list(solution.corals_clean.columns)
    cols = list(hw.corals_clean.columns)
    assert cols == true_cols,\
        f"Expected columns in 'corals_clean' with names {true_cols} but found {cols}."

# test equality
test_data_step1_equality = cds_testing.make_answer_equality_test(hw, solution, DATAS1_VARS)


##################### Data Step 2 #######################
DS2_VARS = {
        "corals_select_data": {},
        }

# test existance
test_data_step2_existance = cds_testing.make_variable_names_test(hw, DS2_VARS)

# test types
def test_data_step2_corals_select_data_type():
    """Test that the variable 'corals_select_data' refers to a pandas DataFrame.
    """
    assert hasattr(hw, 'corals_select_data'),\
        "The 'corals_select_data' variable is not defined in your notebook."
    assert isinstance(hw.corals_select_data, pd.DataFrame),\
        f"Expected the variable 'corals_select_data' to refer to a pandas.DataFrame, but found {type(hw.corals_select_data)}."
    
# test equality
test_data_step2_equality = cds_testing.make_answer_equality_test(hw, solution, DS2_VARS)


##################### Comp Step 1 #######################
CS1_VARS = {
        "corals_labelled": {},
        }

# test existance
test_comp_step1_existance = cds_testing.make_variable_names_test(hw, CS1_VARS)

# test types
def test_comp_step1_corals_labelled_type():
    """Test that the variable 'corals_labelled' refers to a pandas DataFrame.
    """
    assert hasattr(hw, 'corals_labelled'),\
        "The 'corals_labelled' variable is not defined in your notebook."
    assert isinstance(hw.corals_labelled, pd.DataFrame),\
        f"Expected the variable 'corals_labelled' to refer to a pandas.DataFrame, but found {type(hw.corals_labelled)}."

# test size (rows and columns)
def test_comp_step1_corals_labelled_size():
    """Test that 'corals_labelled' has the expected number of rows and columns.
    """
    assert hasattr(hw, 'corals_labelled'),\
        "The 'corals_labelled' variable is not defined in your notebook."
    assert isinstance(hw.corals_labelled, pd.DataFrame),\
        f"Expected the variable 'corals_labelled' to refer to a pandas.DataFrame, but found {type(hw.corals_labelled)}."
    axes = hw.corals_labelled.axes
    rows = len(axes[0])
    cols = len(axes[1])
    soln_axes = solution.corals_labelled.axes
    soln_rows = len(soln_axes[0])
    soln_cols = len(soln_axes[1])
    assert rows == soln_rows,\
        f"Expected {soln_rows} rows but found {rows} rows in your 'corals_labelled' DataFrame."
    assert cols == soln_cols,\
        f"Expected {soln_cols} columns but found {cols} columns in your 'corals_labelled' DataFrame."

# test equality
test_comp_step1_equality = cds_testing.make_answer_equality_test(hw, solution, CS1_VARS)



##################### Comp Step 2 #######################
CS2_VARS = {
        "observed_diff_in_mean_temperature": {},
        }

# test existance
test_comp_step2_existance = cds_testing.make_variable_names_test(hw, CS2_VARS)

# test function existance and correctness
def test_comp_step2_compute_mean_diff_temperature_by_coral_sa():
    """Test that the function 'compute_mean_diff_temperature_by_coral_sa'
    exists and computes the correct value."""
    assert hasattr(hw, 'compute_mean_diff_temperature_by_coral_sa')\
        or hasattr(hw, 'mean_diff_temperature_by_coral_sa'),\
        "The 'compute_mean_diff_temperature_by_coral_sa' variable is not defined in your notebook."
    test_df = solution.corals_labelled
    correct_answer = solution.compute_mean_diff_temperature_by_coral_sa(test_df)
    if hasattr(hw, 'compute_mean_diff_temperature_by_coral_sa'):
        student_answer = hw.compute_mean_diff_temperature_by_coral_sa(test_df)
    else:
        student_answer = hw.mean_diff_temperature_by_coral_sa(test_df)
    assert pytest.approx(correct_answer) == student_answer,\
        "Your 'compute_mean_diff_temperature_by_coral_sa' function returned the wrong value for"\
        f"corals_labelled. Expected: {correct_answer}. Got: {student_answer}."
    
# test type
def test_comp_step2_observed_diff_in_mean_temperature_type():
    """Test that the variable 'observed_diff_in_mean_temperature' refers to a float.
    """
    assert hasattr(hw, 'observed_diff_in_mean_temperature'),\
        "The 'observed_diff_in_mean_temperature' variable is not defined in your notebook."
    assert isinstance(hw.observed_diff_in_mean_temperature, float),\
        f"Expected the variable 'observed_diff_in_mean_temperature' to refer to a float, but found {type(hw.observed_diff_in_mean_temperature)}."

# test equality
test_comp_step2_equality = cds_testing.make_answer_equality_test(hw, solution, CS2_VARS)


##################### Comp Step 4 #######################
CS4_VARS = {
        "resample_test_statistics": {},
        }

# test existance
test_comp_step4_existance = cds_testing.make_variable_names_test(hw, CS4_VARS)

# test type
def test_comp_step4_resample_test_statistics_type():
    """Test that the variable 'resample_test_statistics' refers to a pandas Series.
    """
    assert hasattr(hw, 'resample_test_statistics'),\
        "The 'resample_test_statistics' variable is not defined in your notebook."
    assert isinstance(hw.resample_test_statistics, pd.Series),\
        f"Expected the variable 'resample_test_statistics' to refer to a pandas.Series, but found {type(hw.resample_test_statistics)}."

# test size
def test_comp_step4_resample_test_statistics_size():
    """Test that 'resample_test_statistics' has the expected length.
    """
    assert hasattr(hw, 'resample_test_statistics'),\
        "The 'resample_test_statistics' variable is not defined in your notebook."
    assert isinstance(hw.resample_test_statistics, pd.Series),\
        f"Expected the variable 'resample_test_statistics' to refer to a pandas.Series, but found {type(hw.resample_test_statistics)}."
    assert len(hw.resample_test_statistics) == len(solution.resample_test_statistics),\
        f"Expected {len(solution.resample_test_statistics)} elements in 'resample_test_statistcs'"\
        f" but found {len(hw.resample_test_statistics)} elements."
    
# test equality
test_comp_step2_equality = cds_testing.make_answer_equality_test(hw, solution, CS4_VARS)

##################### Comp Step 5 #######################
CS5_VARS = {
        "p_value": {},
        }

# test existance
test_comp_step5_existance = cds_testing.make_variable_names_test(hw, CS5_VARS)

# test type
def test_comp_step5_p_value_type():
    """Test that the variable 'p_value' refers to a float.
    """
    assert hasattr(hw, 'p_value'),\
        "The 'p_value' variable is not defined in your notebook."
    assert isinstance(hw.p_value, float),\
        f"Expected the variable 'p_value' to refer to a float, but found {type(hw.p_value)}."

# test equality
test_comp_step5_equality = cds_testing.make_answer_equality_test(hw, solution, CS5_VARS)