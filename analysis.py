# analyze sales data from csv file and calculate total sales, category-wise sales, top product and region-wise distribution

import pandas as pd


def main() -> None:
	df = pd.read_csv("data.csv")

	df["Sales"] = df["Quantity"] * df["Price"]

	total_sales = df["Sales"].sum()
	sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
	sales_by_product = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
	top_product = sales_by_product.idxmax()
	top_product_sales = sales_by_product.iloc[0]
	sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
	high_value_orders = df[df["Sales"] > 200]

	print("=== SALES ANALYSIS REPORT ===")
	print(f"Total Sales: ${total_sales:,.2f}\n")

	print("Total Sales by Category:")
	for category, sales in sales_by_category.items():
		print(f"- {category}: ${sales:,.2f}")

	print("\nTop-Selling Product:")
	print(f"- {top_product}: ${top_product_sales:,.2f}")

	print("\nRegion-wise Sales Distribution:")
	for region, sales in sales_by_region.items():
		print(f"- {region}: ${sales:,.2f}")

	print("\nOrders with Sales > $200:")
	if high_value_orders.empty:
		print("- No orders found")
	else:
		display_columns = ["OrderID", "Customer", "Product", "Region", "Sales"]
		print(high_value_orders[display_columns].to_string(index=False))


if __name__ == "__main__":
	main()