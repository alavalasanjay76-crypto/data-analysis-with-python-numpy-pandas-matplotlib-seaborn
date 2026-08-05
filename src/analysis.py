"""
E-Commerce Sales & Customer Analytics
Run: python src/analysis.py
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
REPORTS.mkdir(exist_ok=True)

customers = pd.read_csv(DATA / "customers.csv", parse_dates=["signup_date"])
products = pd.read_csv(DATA / "products.csv")
orders = pd.read_csv(DATA / "orders.csv", parse_dates=["order_date"])
items = pd.read_csv(DATA / "order_items.csv")

# 1. Data quality checks
print("\n--- DATA QUALITY ---")
for name, df in {"customers": customers, "products": products, "orders": orders, "order_items": items}.items():
    print(f"{name}: {df.shape}, duplicates={df.duplicated().sum()}, missing={df.isna().sum().sum()}")

# 2. Build analysis dataset
df = (items.merge(orders, on="order_id", how="left")
           .merge(products, on="product_id", how="left")
           .merge(customers, on="customer_id", how="left"))

completed = df[df["status"].isin(["Completed", "Shipped"])].copy()

# 3. Executive KPIs
kpis = pd.Series({
    "revenue": completed["sales_amount"].sum(),
    "profit": completed["profit_amount"].sum(),
    "orders": completed["order_id"].nunique(),
    "customers": completed["customer_id"].nunique(),
    "units_sold": completed["quantity"].sum(),
})
kpis["average_order_value"] = kpis["revenue"] / kpis["orders"]
print("\n--- KPIs ---")
print(kpis.round(2))

# 4. Monthly revenue
monthly = (completed.assign(month=completed["order_date"].dt.to_period("M").astype(str))
           .groupby("month", as_index=False)
           .agg(revenue=("sales_amount","sum"), profit=("profit_amount","sum")))
monthly.to_csv(REPORTS / "monthly_sales.csv", index=False)

plt.figure(figsize=(10,5))
plt.plot(monthly["month"], monthly["revenue"], marker="o")
plt.xticks(rotation=60)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(REPORTS / "monthly_revenue.png", dpi=150)
plt.close()

# 5. Category performance
category = (completed.groupby("category", as_index=False)
            .agg(revenue=("sales_amount","sum"),
                 profit=("profit_amount","sum"),
                 units=("quantity","sum"))
            .sort_values("revenue", ascending=False))
category.to_csv(REPORTS / "category_performance.csv", index=False)

plt.figure(figsize=(9,5))
plt.bar(category["category"], category["revenue"])
plt.xticks(rotation=35, ha="right")
plt.title("Revenue by Category")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(REPORTS / "category_revenue.png", dpi=150)
plt.close()

# 6. Top products
top_products = (completed.groupby(["product_id","product_name"], as_index=False)
                .agg(revenue=("sales_amount","sum"),
                     profit=("profit_amount","sum"),
                     units=("quantity","sum"))
                .sort_values("revenue", ascending=False).head(10))
top_products.to_csv(REPORTS / "top_10_products.csv", index=False)

# 7. Customer value
customer_value = (completed.groupby(["customer_id","first_name","last_name"], as_index=False)
                  .agg(revenue=("sales_amount","sum"),
                       orders=("order_id","nunique"),
                       profit=("profit_amount","sum"))
                  .sort_values("revenue", ascending=False))
customer_value["avg_order_value"] = customer_value["revenue"] / customer_value["orders"]
customer_value.to_csv(REPORTS / "customer_value.csv", index=False)

# 8. Payment and channel analysis
channel = (completed.groupby("channel", as_index=False)
           .agg(revenue=("sales_amount","sum"), orders=("order_id","nunique"))
           .sort_values("revenue", ascending=False))
channel.to_csv(REPORTS / "channel_performance.csv", index=False)

payment = (orders.groupby("payment_method", as_index=False)
           .agg(orders=("order_id","nunique")))
payment.to_csv(REPORTS / "payment_methods.csv", index=False)

# 9. Returns/cancellations
status = orders["status"].value_counts().rename_axis("status").reset_index(name="orders")
status["percentage"] = status["orders"] / status["orders"].sum() * 100
status.to_csv(REPORTS / "order_status.csv", index=False)

print("\nAnalysis complete. Results saved in /reports.")
