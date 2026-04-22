# analyze sales data from csv file and calculate total sales, category-wise sales, top product and region-wise distribution

import pandas as pd
import sys


REQUIRED_COLUMNS = {
	"OrderID",
	"Date",
	"Customer",
	"Product",
	"Category",
	"Quantity",
	"Price",
	"Region",
}


def print_section(title: str) -> None:
	print(f"\n{title}")
	print("-" * len(title))


def print_sales_breakdown(title: str, sales_series: pd.Series) -> None:
	print_section(title)
	label_width = max(len(str(label)) for label in sales_series.index)
	for label, value in sales_series.items():
		print(f"{str(label):<{label_width}} : ${value:>10,.2f}")


def validate_dataframe(df: pd.DataFrame) -> pd.DataFrame:
	missing_columns = REQUIRED_COLUMNS - set(df.columns)
	if missing_columns:
		raise ValueError(f"Missing required columns: {', '.join(sorted(missing_columns))}")

	df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
	df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

	invalid_rows = df[df[["Quantity", "Price"]].isna().any(axis=1)]
	if not invalid_rows.empty:
		raise ValueError("Invalid numeric data found in Quantity or Price columns.")

	return df


def main() -> None:
	try:
		df = pd.read_csv("data.csv")
		df = validate_dataframe(df)

		df["Sales"] = df["Quantity"] * df["Price"]

		total_sales = df["Sales"].sum()
		sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
		sales_by_product = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
		top_product = sales_by_product.idxmax()
		top_product_sales = sales_by_product.iloc[0]
		sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
		high_value_orders = df[df["Sales"] > 200]

		print("=== SALES ANALYSIS REPORT ===")
		print("=" * 27)
		print(f"Total Sales: ${total_sales:,.2f}")

		print_sales_breakdown("Total Sales by Category", sales_by_category)

		print_section("Top-Selling Product")
		print(f"Product : {top_product}")
		print(f"Sales   : ${top_product_sales:,.2f}")

		print_sales_breakdown("Region-wise Sales Distribution", sales_by_region)

		print_section("Orders with Sales > $200")
		if high_value_orders.empty:
			print("No orders found")
		else:
			display_columns = ["OrderID", "Customer", "Product", "Region", "Sales"]
			high_value_orders = high_value_orders.sort_values(by="Sales", ascending=False)
			print(
				high_value_orders[display_columns].to_string(
					index=False,
					formatters={"Sales": lambda value: f"${value:,.2f}"},
				)
			)

	except FileNotFoundError:
		print("Error: data.csv was not found in the project folder.")
		sys.exit(1)
	except pd.errors.EmptyDataError:
		print("Error: data.csv is empty.")
		sys.exit(1)
	except pd.errors.ParserError:
		print("Error: data.csv has invalid CSV formatting.")
		sys.exit(1)
	except ValueError as exc:
		print(f"Error: {exc}")
		sys.exit(1)
	except Exception as exc:
		print(f"Unexpected error: {exc}")
		sys.exit(1)


if __name__ == "__main__":
	main()