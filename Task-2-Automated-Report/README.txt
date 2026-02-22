# 📊 Automated Sales Report Generator

## 📌 Project Overview

This project automatically reads sales data from a CSV file, analyzes it, and generates a professional PDF sales report using Python.

The report includes:

- Total Sales
- Average Sales
- Highest Sales
- Lowest Sales
- Individual Sales Representative Data

---

## 🛠 Technologies Used

- Python
- Pandas
- ReportLab
- OS Module

---

## 📂 Input File

The program reads data from:

```
sales_data.csv
```

Required columns:

- Sales_Rep
- Sales_Amount

Example:

```
Sales_Rep,Sales_Amount
John,5000
Alice,7000
Bob,3000
```

---

## 📄 Output File

The program generates:

```
Sales_Report.pdf
```

The PDF includes:
- Summary statistics
- Individual sales records

---

## ⚙ How It Works

1. The CSV file is read using Pandas.
2. Sales statistics are calculated.
3. ReportLab is used to generate a formatted PDF.
4. All information is structured and exported automatically.

---

## 🚀 How to Run

1. Install required libraries:

```
pip install pandas reportlab
```

2. Place `sales_data.csv` in the same directory as the script.

3. Run the script:

```
python sales_report.py
```

4. The PDF file will be generated automatically.

---

## 📊 Features

- Automated data analysis
- Professional PDF generation
- Dynamic report creation
- Easy to modify and extend

---

## 🔮 Future Improvements

- Add charts and graphs to PDF
- Add date filtering
- Add monthly comparison
- Add Excel file support
- Add email automation for report sending

---

## 👨‍💻 Author

Harsh Kushwah  
Python Developer | Automation Enthusiast