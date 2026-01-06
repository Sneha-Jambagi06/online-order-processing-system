import sys

def calculate_total_amount(prices, quantities):
    total = 0
    for p, q in zip(prices, quantities):
        total += p * q
    return total


def order_status(total_amount):
    if total_amount >= 5000:
        return "Premium Order"
    elif 2000 <= total_amount < 5000:
        return "Standard Order"
    else:
        return "Basic Order"


if __name__ == "__main__":
    script_name = sys.argv[0]

    if len(sys.argv) > 4:
        customer_name = sys.argv[1]
        product_name = sys.argv[2]
        prices = list(map(int, sys.argv[3].split(",")))
        quantities = list(map(int, sys.argv[4].split(",")))
        print("User provided order details:")
    else:
        customer_name = "John"
        product_name = "Electronics"
        prices = [1000, 1500, 500]
        quantities = [1, 2, 3]
        print("No input given - using default values:")

    total_items = sum(quantities)
    total_amount = calculate_total_amount(prices, quantities)
    status = order_status(total_amount)

    print("\n========== Online Order Processing ==========")
    print("Script Name:", script_name)
    print("Customer Name:", customer_name)
    print("Product Category:", product_name)
    print("Item Prices:", prices)
    print("Item Quantities:", quantities)
    print("Total Items Ordered:", total_items)
    print("Total Order Amount:", total_amount)
    print("Order Status:", status)
