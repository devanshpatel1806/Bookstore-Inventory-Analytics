import pandas as pd
import numpy as np
from pathlib import Path


class Bookstore:

    def __init__(self, inventory, sales):
        self.inventory = inventory
        self.sales = sales

    def view_inventory(self):
        return self.inventory

    def add_book(self):
        print("========== ADD NEW BOOK ==========")

        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author: ").strip()
        category = input("Enter Category: ").strip()
        publisher = input("Enter Publisher: ").strip()

        if not all([book_id, title, author, category, publisher]):
            print("All book details are required.")
            return

        try:
            price = float(input("Enter Price: "))
            stock = int(input("Enter Stock Quantity: "))
            reorder_level = int(input("Enter Reorder Level: "))
            publication_year = int(input("Enter Publication Year: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            return

        if price <= 0:
            print("Price must be greater than 0.")
            return

        if stock < 0:
            print("Stock quantity cannot be negative.")
            return

        if reorder_level < 0:
            print("Reorder level cannot be negative.")
            return

        if not 1 <= publication_year <= pd.Timestamp.today().year:
            print("Please enter a valid publication year.")
            return

        if book_id in self.inventory["Book_ID"].astype(str).values:
            print("Book ID already exists.")
            return

        new_book = {
            "Book_ID": book_id,
            "Title": title,
            "Author": author,
            "Category": category,
            "Publisher": publisher,
            "Price": price,
            "Stock_Quantity": stock,
            "Reorder_Level": reorder_level,
            "Publication_Year": publication_year
        }

        self.inventory = pd.concat(
            [self.inventory, pd.DataFrame([new_book])],
            ignore_index=True
        )

        print("Book added successfully!")

    def update_inventory(self):
        print("========== UPDATE INVENTORY ==========")

        book_id = input("Enter Book ID: ").strip()

        matching_books = self.inventory[
            self.inventory["Book_ID"].astype(str) == book_id
        ]

        if matching_books.empty:
            print("Book not found.")
            return

        try:
            new_quantity = int(input("Enter new stock quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if new_quantity < 0:
            print("Stock quantity cannot be negative.")
            return

        self.inventory.loc[
            self.inventory["Book_ID"].astype(str) == book_id,
            "Stock_Quantity"
        ] = new_quantity

        print("Inventory updated successfully!")

    def check_low_stock(self):
        low_stock = self.inventory[
            self.inventory["Stock_Quantity"]
            <= self.inventory["Reorder_Level"]
        ]

        if low_stock.empty:
            print("No books need to be reordered.")
        else:
            print("========== LOW STOCK BOOKS ==========")
            print(
                low_stock[
                    [
                        "Book_ID",
                        "Title",
                        "Stock_Quantity",
                        "Reorder_Level"
                    ]
                ]
            )

    def record_sale(self):
        print("========== RECORD SALE ==========")

        book_id = input("Enter Book ID: ").strip()

        matching_books = self.inventory[
            self.inventory["Book_ID"].astype(str) == book_id
        ]

        if matching_books.empty:
            print("Book not found.")
            return

        book_index = matching_books.index[0]
        title = self.inventory.loc[book_index, "Title"]
        price = float(self.inventory.loc[book_index, "Price"])
        available_stock = int(
            self.inventory.loc[book_index, "Stock_Quantity"]
        )

        print("Book:", title)
        print("Price:", price)
        print("Available Stock:", available_stock)

        try:
            quantity_sold = int(input("Enter Quantity Sold: "))
            discount = float(input("Enter Discount Percentage: "))
        except ValueError:
            print("Please enter valid numbers.")
            return

        if quantity_sold <= 0:
            print("Quantity sold must be greater than 0.")
            return

        if quantity_sold > available_stock:
            print("Insufficient stock!")
            return

        if discount < 0 or discount > 100:
            print("Discount must be between 0 and 100.")
            return

        gross_amount = price * quantity_sold
        discount_amount = gross_amount * (discount / 100)
        total_amount = gross_amount - discount_amount
        new_stock = available_stock - quantity_sold

        self.inventory.loc[
            book_index, "Stock_Quantity"
        ] = new_stock

        sale_id = "S" + str(len(self.sales) + 1)

        new_sale = {
            "Sale_ID": sale_id,
            "Date": pd.Timestamp.today(),
            "Book_ID": book_id,
            "Quantity_Sold": quantity_sold,
            "Unit_Price": price,
            "Discount_Percent": discount,
            "Total_Amount": total_amount,
            "Payment_Method": "Cash",
            "Customer_Type": "Regular"
        }

        self.sales = pd.concat(
            [self.sales, pd.DataFrame([new_sale])],
            ignore_index=True
        )

        print("\nSale recorded successfully!")
        print("Book:", title)
        print("Quantity Sold:", quantity_sold)
        print("Discount:", discount, "%")
        print("Total Amount:", round(total_amount, 2))
        print("Remaining Stock:", new_stock)

    def generate_report(self):
        print("\n========== BOOKSTORE REPORT ==========")

        total_books = len(self.inventory)
        total_stock = np.sum(self.inventory["Stock_Quantity"])
        total_sales = len(self.sales)
        total_quantity_sold = np.sum(self.sales["Quantity_Sold"])
        total_revenue = np.sum(self.sales["Total_Amount"])

        average_price = (
            np.mean(self.inventory["Price"])
            if not self.inventory.empty else 0
        )

        best_selling = (
            self.sales.groupby("Book_ID")["Quantity_Sold"]
            .sum()
            .sort_values(ascending=False)
        )

        if not best_selling.empty:
            best_book_id = best_selling.index[0]

            matching_book = self.inventory[
                self.inventory["Book_ID"].astype(str)
                == str(best_book_id)
            ]

            best_book_title = (
                matching_book.iloc[0]["Title"]
                if not matching_book.empty
                else "Unknown"
            )
        else:
            best_book_title = "No sales yet"

        low_stock_count = np.sum(
            self.inventory["Stock_Quantity"]
            <= self.inventory["Reorder_Level"]
        )

        print("Total Books:", total_books)
        print("Total Stock:", total_stock)
        print("Total Sales Transactions:", total_sales)
        print("Total Quantity Sold:", total_quantity_sold)
        print("Total Revenue: ₹", round(total_revenue, 2))
        print("Average Book Price: ₹", round(average_price, 2))
        print("Best-Selling Book:", best_book_title)
        print("Low-Stock Books:", low_stock_count)

    def sales_analysis(self):
        print("\n========== SALES ANALYSIS ==========")

        total_revenue = self.sales["Total_Amount"].sum()
        print("Total Revenue: ₹", round(total_revenue, 2))

        total_quantity = self.sales["Quantity_Sold"].sum()
        print("Total Quantity Sold:", total_quantity)

        book_sales = (
            self.sales.groupby("Book_ID")["Quantity_Sold"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nTop 5 Best-Selling Books:")
        print(book_sales.head(5))

        sales_details = self.sales.merge(
            self.inventory[
                ["Book_ID", "Title", "Author", "Category"]
            ],
            on="Book_ID",
            how="left"
        )

        category_sales = (
            sales_details.groupby("Category")["Quantity_Sold"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nSales by Category:")
        print(category_sales)

        author_revenue = (
            sales_details.groupby("Author")["Total_Amount"]
            .sum()
            .sort_values(ascending=False)
        )

        print("\nTop 5 Authors by Revenue:")
        print(author_revenue.head(5))


# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":

    # Find the folder containing this Python file
    project_folder = Path(__file__).resolve().parent

    # Load the CSV files from the project folder
    inventory_path = project_folder / "inventory.csv"
    sales_path = project_folder / "sales.csv"

    if not inventory_path.exists() or not sales_path.exists():
        print("Error: Required CSV files were not found.")
        print("Please keep inventory.csv and sales.csv")
        print("in the same folder as bookstore.py.")
    else:
        inventory_df = pd.read_csv(inventory_path)
        sales_df = pd.read_csv(sales_path)

        # Create Bookstore object
        bookstore = Bookstore(inventory_df, sales_df)

        # Display report
        bookstore.generate_report()
    
