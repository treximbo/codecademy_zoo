from daily_sales import daily_sales

# ------------------------------------------------
# Start coding below!

daily_sales_replaced = daily_sales.replace(";,;", ":")
daily_transactions = daily_sales_replaced.split(",")

daily_transactions_split = []
for item in daily_transactions:
    daily_transactions_split.append(item.split(":"))

transactions_clean = []
for item in daily_transactions_split:
    transaction_clean = []
    for i in range(0, len(item)):
        transaction_clean.append(item[i].strip())
    transactions_clean.append(transaction_clean)

customers = []
sales = []
thread_sold = []
for item in transactions_clean:
    customers.append(item[0])
    sales.append(item[1])
    thread_sold.append(item[2])

total_sales = 0
for item in sales:
    total_sales += float(item.replace("$", ""))

thread_sold_split = []
for item in thread_sold:
    if item.find("&"):
        temp_item = item.split("&")
        for i in range(0, len(temp_item)):
            thread_sold_split.append(temp_item[i])
    else:
        thread_sold_split.append(item)


def color_count(color):
    count = 0
    for item in thread_sold_split:
        if item == color:
            count += 1
    return count


colors = ["red", "yellow", "green", "white", "black", "blue", "purple"]

for color in colors:
    print(
        "Thread Shed sold {} treads of {} thread today".format(
            color_count(color), color
        )
    )
