# Test 2 Lab - COMP120 Section 002

This project was created for the **Test 2 Lab** of **COMP120 (Section 002)**.

## Author

- **Name:** Pedro Bilhalva Oliveira
- **Student Number:** 301541005

## Project Overview

This project analyzes sales data from a CSV file using Python and pandas.

The script in `analysis.py` performs the following tasks:

- Calculates total sales (`Quantity x Price`)
- Finds total sales by category
- Identifies the top-selling product
- Finds region-wise sales distribution
- Displays orders where sales are greater than `$200`

## Files

- `analysis.py` - Python script with the sales analysis
- `data.csv` - Input dataset
- `requirements.txt` - Python dependencies

## How to Run

1. Open a terminal in this project folder.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the analysis script:

```bash
python analysis.py
```

## Expected Output

The program prints a sales analysis report that includes:

- Total sales amount
- Sales totals by category
- Top-selling product
- Region-wise sales totals
- A list of orders with sales above `$200`