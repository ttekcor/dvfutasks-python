x = str(input())
y = float(input())
print(f"SELECT\n  id,\n  SUM(product_price) AS revenue_by_user\nFROM\n  dataset.data_table\nWHERE\n  ab_test = '{x}'\nGROUP BY\n  id\nHAVING\n  revenue_by_user < {format(round(y,2), '.2f')}")
