# Tipping Point Ratio (Sortino Ratio) Calculator

This project consists of a Python script (`project.py`) that calculates the **Tipping Point Ratio (TPR)**, also known as the **Sortino Ratio**, for a given set of stocks. It also includes a unit testing script (`test_project.py`) to validate the correctness of the implemented functions.

## Video Demo: https://youtu.be/POG4R6le8Fs?si=H7-9Y-9_-vRg9QhJ

## Files in the Project

1. **`project.py`**:
   - Contains the main implementation of the TPR computation and related functions.
   - Includes functionality to compute yearly returns, TPR, and output results.

2. **`test_project.py`**:
   - Unit tests for key functions in `project.py` using `pytest`.
   - Validates the accuracy of computations for `compute_yearly_return`, `compute_one_tpr`, and `compute_tpr_series`.

## Installation

1. Clone or download the repository to your local machine.
2. Install the required Python libraries:
   ```bash
   pip install yfinance pandas numpy matplotlib tabulate pytest
   ```

## Usage

### Running the Main Program
Execute the main script to compute TPR for a set of stocks:
```bash
python project.py
```

### Running Unit Tests
To ensure the correctness of the implementation, run the tests using `pytest`:
```bash
pytest test_project.py
```

## Main Script: `project.py`

### Key Functions
1. **`compute_yearly_return(monthly_return)`**:
   - Converts monthly returns to annualized returns by extrapolation.

2. **`compute_one_tpr(yearly_return, dtr)`**:
   - Computes the TPR for a given series of yearly returns and a desired target return (DTR).

3. **`compute_tpr_series(yearly_return, dtr, span)`**:
   - Computes a time series of TPR values using a rolling window.

4. **`plot(tpr_df, plot_file)`**:
   - Plots the TPR values for each stock and saves the plot as a PDF.

5. **`table_output(tpr_df, table_file)`**:
   - Outputs the TPR data in markdown table format.

## Unit Testing Script: `test_project.py`

### Tests
1. **`test_compute_yearly_return()`**:
   - Verifies that annualized returns are computed correctly from monthly returns.

2. **`test_compute_one_tpr()`**:
   - Tests the calculation of the TPR for a single series of yearly returns.

3. **`test_compute_tpr_series()`**:
   - Checks the rolling computation of TPR values over a series of yearly returns.

### Example
Run tests with `pytest`:
```bash
pytest test_project.py
```

Sample output:
```
============================= test session starts =============================
platform linux -- Python 3.x
collected 3 items

test_project.py ...                                                          [100%]

============================== 3 passed in 0.12s ==============================
```

## Outputs

1. **TPR Table**:
   - Markdown-formatted table with TPR values for all stocks.
   - File: `tpr_table.txt`

2. **TPR Plot**:
   - A time-series plot of TPR values.
   - File: `tpr_plot.pdf`

## Dependencies

- **Python**: 3.7 or higher
- **Libraries**:
  - `yfinance`: Fetching stock data.
  - `pandas`: Data manipulation.
  - `numpy`: Mathematical operations.
  - `matplotlib`: Plotting.
  - `tabulate`: Markdown table formatting.
  - `pytest`: Unit testing.


