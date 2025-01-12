from project import compute_yearly_return, compute_one_tpr, compute_tpr_series
import pytest
import pandas as pd
from pandas import testing as tm

def test_compute_yearly_return():
    dates = pd.date_range('20200101', periods = 4)
    monthly_return = pd.Series([0.01, 0.02, 0.05, -0.03], index=dates)
    expected_yearly_return = pd.Series([0.126825, 0.268242, 0.795856, -0.306158], index=dates)
    yearly_return = compute_yearly_return(monthly_return)
    tm.assert_series_equal(expected_yearly_return, yearly_return)


def test_compute_one_tpr():
    dates = pd.date_range('20200101', periods = 10)
    dtr = 0.08
    yearly_return = pd.Series([0.14, 0.13, 0.11, 0.13, 0.09, 0.07, 0.07, 0.07, 0.07, 0.12], index=dates)
    tpr = compute_one_tpr(yearly_return, dtr)
    assert(pytest.approx(tpr, abs=0.005) == 3.79)
    yearly_return = pd.Series([0.1, 0.13, 0.12, 0.13, 0.12, 0.08, 0.08, 0.08, 0.05, 0.11], index=dates)
    tpr = compute_one_tpr(yearly_return, dtr)
    assert(pytest.approx(tpr, abs=0.005) == 2.42)

def test_compute_tpr_series():
    dates = pd.date_range('20200101', periods = 10)
    dtr = 0.08
    span = 10
    yearly_return = pd.Series([0.14, 0.13, 0.11, 0.13, 0.09, 0.07, 0.07, 0.07, 0.07, 0.12], index=dates)
    tpr_series = compute_tpr_series(yearly_return, dtr, span)
    expected_tpr_series = pd.Series([3.79], index = yearly_return.index[span-1:])
    tm.assert_series_equal(expected_tpr_series, tpr_series, rtol=0.005)

    span = 9
    tpr_series = compute_tpr_series(yearly_return, dtr, span)
    expected_tpr_series = pd.Series([3.33, 3.00], index = yearly_return.index[span-1:])
    tm.assert_series_equal(expected_tpr_series, tpr_series, rtol=0.005)
