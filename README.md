# 📚 Bookstore Inventory & Analytics System

## 1. Project Overview

The **Bookstore Inventory & Analytics System** is a Python-based project developed to manage bookstore inventory, record book sales, monitor stock levels, and analyze sales performance.

The project uses **Object-Oriented Programming (OOP)** to organize inventory operations and uses **Pandas and NumPy** for data handling and numerical analysis. Matplotlib and Seaborn are used to create visualizations that help understand sales trends, category-wise performance, revenue distribution, and relationships between book prices and sales volume.

The system demonstrates how Python can be used to solve real-world bookstore management problems and support data-driven decisions.

## 2. Project Objectives

- Manage book inventory efficiently.
- Display available books and their stock quantities.
- Add new books to the inventory.
- Update the stock quantity of existing books.
- Identify books that have reached their reorder levels.
- Record book sales and calculate sale amounts.
- Analyze total revenue and quantity sold.
- Generate a summary report of bookstore performance.
- Create charts to understand sales and revenue patterns.
- Apply OOP, Pandas, NumPy, and data visualization concepts in a practical project.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Object-Oriented Programming (OOP) | Organizing bookstore operations using a class and methods |
| Pandas | Reading, managing, and analyzing CSV datasets |
| NumPy | Numerical calculations and statistical operations |
| Matplotlib | Creating bar, line, and pie charts |
| Seaborn | Creating the correlation heatmap |
| Jupyter Notebook | Development, analysis, and visualization |
| Visual Studio Code | Writing and running the Python program |
| CSV | Storing inventory and sales data |
| GitHub | Project hosting and version control |

## 4. Main Features

### 4.1 View Inventory

Displays the available bookstore inventory, including book ID, title, author, category, publisher, price, stock quantity, reorder level, and publication year.

**Screenshot:**

![View Inventory Output](screenshots/view_inventory.png)

### 4.2 Add a New Book

Allows the user to enter the details of a new book, such as its ID, title, author, category, publisher, price, stock quantity, and reorder level.

**Screenshot:**

![Add Book Output](screenshots/add_book.png)

### 4.3 Update Inventory

Allows the user to update the stock quantity of an existing book. This helps maintain accurate inventory records.

**Screenshot:**

![Update Inventory Output](screenshots/update_inventory.png)

### 4.4 Check Low-Stock Books

Identifies books whose stock has reached or fallen below the defined reorder level. This helps the bookstore identify items that may need replenishment.

**Screenshot:**

![Low Stock Output](screenshots/low_stock.png)

### 4.5 Record a Sale

Records a book sale by taking the required book and quantity details. The system calculates the sale amount and displays the sale information.

**Screenshot:**

![Record Sale Output](screenshots/record_sale.png)

### 4.6 Sales Analysis

Analyzes sales information to understand revenue, total quantity sold, sales transactions, best-selling books, and other useful sales performance details.

**Screenshot:**

![Sales Analysis Output](screenshots/sales_analysis.png)

### 4.7 Generate Bookstore Report

Generates a summary of bookstore performance, including total books, total stock, sales transactions, quantity sold, total revenue, average book price, best-selling book, and low-stock book count.

**Screenshot:**

![Generate Report Output](screenshots/generate_report.png)

## 5. Data Visualization and Analysis

The project includes four visualizations to present important bookstore sales insights.

### 5.1 Bar Chart — Total Sales by Category

The bar chart compares the total sales quantity across book categories. It helps identify which categories contribute the most to sales volume.

**Screenshot:**

![Bar Chart - Total Sales by Category](screenshots/bar_chart.png)

### 5.2 Line Chart — Monthly Sales Trends

The line chart presents monthly sales trends. It helps observe changes in sales over time and identify periods with higher or lower sales activity.

**Screenshot:**

![Line Chart - Monthly Sales Trends](screenshots/line_chart.png)

### 5.3 Pie Chart — Revenue Share by Category

The pie chart displays the share of revenue contributed by different book categories. It helps compare the relative contribution of each category to total revenue.

**Screenshot:**

![Pie Chart - Revenue Share by Category](screenshots/pie_chart.png)

### 5.4 Heatmap — Correlation Between Book Price and Sales Volume

The heatmap displays correlations between numerical variables such as book price, stock quantity, quantity sold, and total sale amount. It helps identify relationships between these variables.

**Screenshot:**

![Heatmap - Correlation Between Price and Sales Volume](screenshots/heatmap.png)

## 6. Dataset Description

The project uses two CSV datasets: `inventory.csv` and `sales.csv`.

### 6.1 Inventory Dataset

The inventory dataset contains information about books available in the bookstore.

| Column | Description |
|---|---|
| `Book_ID` | Unique identifier for each book |
| `Title` | Name of the book |
| `Author` | Name of the author |
| `Category` | Book category |
| `Publisher` | Name of the publisher |
| `Price` | Price of the book |
| `Stock_Quantity` | Number of copies available |
| `Reorder_Level` | Stock level used to identify books requiring replenishment |
| `Publication_Year` | Year the book was published |

### 6.2 Sales Dataset

The sales dataset contains information about bookstore transactions.

| Column | Description |
|---|---|
| `Sale_ID` | Unique identifier for each sale |
| `Date` | Date of the sale |
| `Book_ID` | Identifier of the book sold |
| `Quantity_Sold` | Number of copies sold |
| `Unit_Price` | Price per copy at the time of sale |
| `Discount_Percent` | Discount applied to the sale |
| `Total_Amount` | Total amount for the transaction |
| `Payment_Method` | Method used to make the payment |
| `Customer_Type` | Type of customer |

## 7. Project Structure

The project files are organized as follows:

```text
Bookstore_Inventory_Analytics/
│
├── bookstore.py
├── Bookstore_Inventory_Analytics.ipynb
├── inventory.csv
├── sales.csv
├── README.md
│
└── screenshots/
    ├── view_inventory.png
    ├── add_book.png
    ├── update_inventory.png
    ├── low_stock.png
    ├── record_sale.png
    ├── sales_analysis.png
    ├── generate_report.png
    ├── bar_chart.png
    ├── line_chart.png
    ├── pie_chart.png
    └── heatmap.png
```

## 8. Installation and Requirements

Make sure Python is installed on your computer.

Install the required libraries by running the following command in Command Prompt or the VS Code terminal:

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

## 9. How to Run the Project

### Step 1: Download or Clone the Repository

Download the project from GitHub and extract the ZIP file, or clone the repository using:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the actual URL of your GitHub repository.

### Step 2: Open the Project Folder

Open the `Bookstore_Inventory_Analytics` folder in Visual Studio Code or your preferred Python environment.

### Step 3: Check the Dataset Files

Ensure that these files are present in the same folder as `bookstore.py`:

- `inventory.csv`
- `sales.csv`

### Step 4: Run the Python Program

Open the terminal in the project folder and execute:

```bash
python bookstore.py
```

The program loads the inventory and sales datasets and displays the bookstore report.

### Step 5: Run the Jupyter Notebook

To explore the data analysis and visualizations, run:

```bash
jupyter notebook
```

Open `Bookstore_Inventory_Analytics.ipynb` and execute the notebook cells in order.

## 10. Applications

This project can be useful for:

- Small and medium-sized bookstores.
- Managing book stock and identifying low-stock items.
- Monitoring sales transactions and revenue.
- Comparing sales performance across book categories.
- Understanding monthly sales patterns.
- Supporting inventory and purchasing decisions.

## 11. Learning Outcomes

Through this project, the following concepts are demonstrated:

- Designing a Python class and using its methods.
- Applying Object-Oriented Programming concepts.
- Reading and working with CSV files.
- Using Pandas for data manipulation and analysis.
- Using NumPy for numerical calculations.
- Performing inventory and sales operations.
- Creating data visualizations with Matplotlib and Seaborn.
- Generating reports from structured datasets.
- Organizing and documenting a Python project using GitHub.

## 12. Future Enhancements

Possible future improvements include:

- A graphical user interface for easier interaction.
- Database integration for persistent storage.
- Automatic stock alerts when inventory becomes low.
- Advanced sales forecasting.
- Exporting reports into PDF or Excel format.

## 13. Conclusion

The **Bookstore Inventory & Analytics System** demonstrates how Python programming and data analysis can be combined to manage bookstore inventory and understand sales performance.

The project brings together OOP, Pandas, NumPy, Matplotlib, and Seaborn to support inventory management, sales recording, reporting, and visual analysis. The four visualizations provide different perspectives on category-wise sales, monthly trends, revenue distribution, and correlations between numerical variables.

This project provides practical experience in Python development, data analysis, visualization, and project documentation.

## 14. Author

**Devansh Patel**

Academic Python Project — Bookstore Inventory & Analytics System
