# Simple Billing System

**PS No.: 30**  
**Project Title:** Simple Billing System  
**Language:** Python 3

## 1. Project Description

This project is a console-based Simple Billing System for a small shop. It simulates the work of a cashier by allowing the user to:

- Enter the customer name (optional).
- Add one or more products with quantities to the bill.
- View the current bill at any time.
- Generate the final bill with **subtotal**, **5% GST** and **grand total**.
- Save the final bill to a file named **bill.txt**.

## 2. Product Catalogue

| Item | Price |
|---|---:|
| Rice | Rs. 50 |
| Sugar | Rs. 40 |
| Oil | Rs. 120 |

## 3. Billing Formula

- **Amount** = Item price × quantity
- **Subtotal** = Sum of all item amounts
- **GST** = Subtotal × 5%
- **Grand Total** = Subtotal + GST

For example, for Sugar × 1:

- Subtotal = Rs. 40.00
- GST = Rs. 2.00
- Grand Total = Rs. 42.00

## 4. Data Structures Used

### Product catalogue dictionary

The catalogue is stored in a dictionary:

```python
PRODUCTS = {
    "Rice": 50,
    "Sugar": 40,
    "Oil": 120,
}
```

This makes it easy to find the price of a product.

### Bill items list

The bill is stored in a list. Each entry is a dictionary describing one bill line:

```python
bill_items = [
    {"name": "Rice",  "qty": 2, "price": 50,  "amount": 100},
    {"name": "Oil",   "qty": 1, "price": 120, "amount": 120},
    {"name": "Sugar", "qty": 3, "price": 40,  "amount": 120},
]
```

## 5. Main Features

1. **Product validation**  
   Only Rice, Sugar, and Oil can be added (not case-sensitive).

2. **Quantity validation**  
   Quantity must be a whole number and at least 1.

3. **Multiple items**  
   The menu loop allows the cashier to add any number of items.

4. **View bill**  
   The current items and totals can be viewed at any time.

5. **Final bill**  
   The program calculates subtotal, GST, and grand total and prints them in a neat layout.

6. **File saving**  
   The final bill is written to `bill.txt`.

7. **Empty bill check**  
   A bill cannot be generated until at least one item is added.

## 6. How to Run

### Requirement

Python 3 must be installed on the computer.

### Command

Open Command Prompt/Terminal in the project folder and run:

```bash
python Simple_Billing_System.py
```

If your system uses `python3`, run:

```bash
python3 Simple_Billing_System.py
```

## 7. Program Menu

After starting, the program asks for the customer name and then provides:

```text
1. Add item
2. View bill
3. Generate final bill
4. Exit
```

## 8. Given Test Cases

### Test Case 1: Normal Input

**Input:**
- Add item: Rice
- Quantity: 2

**Expected result:**

```text
Rice x2 added | Amount: 100
```

### Test Case 2: Boundary / Minimum Input

**Input:**
- Add item: Sugar
- Quantity: 1
- Generate bill

**Expected result:**

```text
Subtotal:   40.00
GST (5%):    2.00
Grand Total: 42.00
```

### Test Case 3: Invalid Input

**Invalid product:**
```text
Add item: Soap
Invalid product. Available: Rice, Sugar, Oil
```

**Invalid quantity:**
```text
Add item: Rice
Quantity: 0
Quantity must be at least 1.
```

### Test Case 4: Different Valid Scenario

**Input:**
- Customer: Riya
- Rice × 2
- Oil × 1
- Sugar × 3
- Generate bill

**Expected calculation:**

```text
Rice  x2 = 100
Oil   x1 = 120
Sugar x3 = 120
Subtotal    = 340.00
GST (5%)    = 17.00
Grand Total = 357.00
Bill saved to bill.txt
```

## 9. Concepts Used

The project demonstrates the required Python concepts:

- Lists
- Dictionaries
- Functions
- File handling (`open()` and `write()`)
- `for` loops
- `while` loops
- `if-elif-else`
- Input/output
- Exception handling using `try-except`
- Validation
- Arithmetic and billing calculations
- String formatting (f-strings)

## 10. Project Files

The main program is:

```text
Simple_Billing_System.py
```

The final bill is saved to:

```text
bill.txt
```

No external Python libraries are required.
