from order_system import Order

def test_total_price():
    order = Order(1, "Laptop", 2, 50000)
    assert order.total_price() == 100000

def test_process_order_valid():
    order = Order(2, "Mouse", 3, 500)
    assert order.process_order() == "Order Processed"

def test_process_order_invalid():
    order = Order(3, "Keyboard", 0, 1000)
    assert order.process_order() == "Invalid Order"
