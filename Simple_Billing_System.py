"""
PS 30 - Simple Billing System
Console billing system for a small shop.
Concepts used: Lists, Dictionaries, Functions, File Handling
"""

# Product catalogue (dictionary): name -> price in Rs.
PRODUCTS = {
    "Rice": 50,
    "Sugar": 40,
    "Oil": 120,
}

GST_RATE = 0.05          # 5% GST on the subtotal
BILL_FILE = "bill.txt"

# The bill items (list). Each item is a dictionary:
# {"name": ..., "qty": ..., "price": ..., "amount": ...}
bill_items = []


def find_product(name):
    """Return the catalogue name matching `name` (case-insensitive), else None."""
    for product in PRODUCTS:
        if product.lower() == name.strip().lower():
            return product
    return None


def add_item(name, quantity):
    """Validate and add an item to the bill. Returns (success, message)."""
    product = find_product(name)
    if product is None:
        return False, "Invalid product. Available: " + ", ".join(PRODUCTS)

    try:
        qty = int(quantity)
    except (ValueError, TypeError):
        return False, "Quantity must be a whole number and at least 1."

    if qty < 1:
        return False, "Quantity must be at least 1."

    price = PRODUCTS[product]
    amount = price * qty
    bill_items.append({"name": product, "qty": qty, "price": price, "amount": amount})
    return True, f"{product} x{qty} added | Amount: {amount}"


def calculate_totals():
    """Return (subtotal, gst, grand_total) for the current bill."""
    subtotal = sum(item["amount"] for item in bill_items)
    gst = subtotal * GST_RATE
    grand_total = subtotal + gst
    return subtotal, gst, grand_total


def format_bill(customer=""):
    """Build the bill as a neatly formatted string."""
    subtotal, gst, grand_total = calculate_totals()
    line = "=" * 46
    thin = "-" * 46

    lines = [line, "SIMPLE BILLING SYSTEM".center(46), line]
    if customer:
        lines.append(f"Customer: {customer}")
        lines.append(thin)
    lines.append(f"{'Item':<14}{'Qty':>5}{'Price':>12}{'Amount':>13}")
    lines.append(thin)
    for item in bill_items:
        lines.append(
            f"{item['name']:<14}{item['qty']:>5}{item['price']:>12.2f}{item['amount']:>13.2f}"
        )
    lines.append(thin)
    lines.append(f"{'Subtotal:':<32}{subtotal:>14.2f}")
    lines.append(f"{'GST (5%):':<32}{gst:>14.2f}")
    lines.append(f"{'Grand Total:':<32}{grand_total:>14.2f}")
    lines.append(line)
    return "\n".join(lines)


def view_bill(customer=""):
    """Print the current bill."""
    if not bill_items:
        print("No items added yet.")
        return
    print(format_bill(customer))


def generate_bill(customer=""):
    """Print the final bill and save it to bill.txt."""
    if not bill_items:
        print("No items added yet. Add at least one item first.")
        return False

    text = format_bill(customer)
    print(text)
    with open(BILL_FILE, "w") as f:
        f.write(text + "\n")
    print(f"Bill saved to {BILL_FILE}")
    return True


def show_catalogue():
    print("\nAvailable products:")
    for name, price in PRODUCTS.items():
        print(f"  {name:<8} Rs.{price}")


def main():
    print("=== Simple Billing System ===")
    customer = input("Customer name (optional): ").strip()
    show_catalogue()

    while True:
        print("\n1. Add item")
        print("2. View bill")
        print("3. Generate final bill")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Add item: ")
            quantity = input("Quantity: ")
            ok, message = add_item(name, quantity)
            print(message)
        elif choice == "2":
            view_bill(customer)
        elif choice == "3":
            if generate_bill(customer):
                break
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")


if __name__ == "__main__":
    main()
