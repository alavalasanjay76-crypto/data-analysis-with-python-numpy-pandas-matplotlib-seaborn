# E-Commerce Sales & Customer Analytics

## 📌 Project Overview
A real-world, end-to-end Python data analysis project for an e-commerce business. The goal is to help management understand revenue, profitability, customer value, product performance, sales channels, payment behavior, and order outcomes.

## 🎯 Business Questions
- How is revenue changing month over month?
- Which categories and products generate the most revenue and profit?
- Who are the highest-value customers?
- What is the average order value?
- Which sales channel performs best?
- What percentage of orders are cancelled or returned?
- Which areas need attention based on the data?

## 🗂️ Dataset
Synthetic but realistic business data created for portfolio/learning use:
- 10,000 customers
- 1,000 products
- 50,000 orders
- 100,000 order-line transactions
- 2023–2025 order history

## 🛠️ Tech Stack
Python, Pandas, NumPy, Matplotlib, Jupyter Notebook

## 🔎 Analysis Workflow
1. Load source data
2. Inspect structure and data quality
3. Handle missing values and duplicates
4. Join customer, product, order, and transaction data
5. Calculate KPIs
6. Analyze monthly trends
7. Analyze category/product performance
8. Analyze customer value
9. Analyze channels, payments, and order status
10. Export reports and visualizations

## 📊 Key Metrics
Revenue, Profit, Orders, Customers, Units Sold, Average Order Value, Product Revenue, Customer Revenue, Return/Cancel Rate.

## ▶️ How to Run

```bash
pip install -r requirements.txt
python src/analysis.py
```

Or open `notebooks/ecommerce_analysis.ipynb` in Jupyter Notebook.

## 📁 Project Structure

```text
ecommerce-sales-customer-analytics/
├── data/
├── notebooks/
│   └── ecommerce_analysis.ipynb
├── src/
│   └── analysis.py
├── reports/
├── requirements.txt
└── README.md
```

## 💼 Resume Description
**E-Commerce Sales & Customer Analytics | Python, Pandas, NumPy, Matplotlib**
- Analyzed 100K+ transaction records to identify revenue, profitability, customer, and product trends.
- Cleaned and joined multiple business datasets using Pandas and performed exploratory data analysis.
- Built KPI and customer/product performance analyses to support data-driven business decisions.
- Created business-focused visualizations for monthly revenue and category performance.

## ⚠️ Note
The dataset is synthetic and intended for portfolio/educational use.
