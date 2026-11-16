# Project Summary

## Simple Billing System

**PS No.: 30**  
**Language:** Python 3

### Objective

The objective of this project is to create a console-based billing system for a small shop in which the cashier can add products with quantities, view the bill, and generate a final bill with subtotal, GST and grand total that is saved to a file.

### Product Catalogue

- Rice — Rs. 50
- Sugar — Rs. 40
- Oil — Rs. 120

### Billing

The program calculates:

- Subtotal
- 5% GST on the subtotal
- Grand total

Formula:

```text
GST         = Subtotal × 5%
Grand Total = Subtotal + GST
```

### Data Structures

The product catalogue is stored in a **dictionary** containing product names and prices.

The bill is stored in a **list**. Each entry is a dictionary holding the product name, quantity, price and amount.

### Program Flow

```text
Start
  ↓
Enter customer name (optional)
  ↓
Display Menu: Add Item / View Bill / Generate Bill / Exit
  ↓
Validate product name and quantity
  ↓
Add item to the bill list
  ↓
Calculate Subtotal
  ↓
Add 5% GST
  ↓
Display Final Bill and save to bill.txt
  ↓
Exit
```

### Validation

The program validates:

1. Product must be Rice, Sugar, or Oil.
2. Quantity must be a whole number and at least 1.
3. A bill cannot be generated when no items have been added.
4. Invalid products, quantities, and menu choices show appropriate error messages.

### Test Case Results

| Test Case | Scenario | Result |
|---|---|---|
| 1 | Rice × 2 | Amount = Rs. 100 |
| 2 | Sugar × 1, generate bill | Grand Total = Rs. 42.00 |
| 3 | Soap / quantity 0 | Invalid inputs are rejected |
| 4 | Rice × 2, Oil × 1, Sugar × 3 (Riya) | Grand Total = Rs. 357.00 |

### Requirements Satisfied

- Python 3 console application (one `.py` file)
- Product catalogue stored in a dictionary
- Bill items stored in a list
- Functions to add an item, view the bill and generate the final bill
- Subtotal, GST and grand total calculation in a neat layout
- Validation of product name and quantity
- Final bill saved to `bill.txt`
- Given test cases supported

### Conclusion

The project successfully implements a Simple Billing System using basic Python programming concepts. It stores the catalogue in a dictionary and the bill in a list, validates user input, supports multiple items, and generates the final bill with the specified 5% GST, saving it to `bill.txt`.
