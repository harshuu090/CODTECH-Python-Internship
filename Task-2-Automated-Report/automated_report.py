import os
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


# Get current file directory
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "sales_data.csv")


# Read CSV File
df = pd.read_csv(file_path)


# Analyze Data
total_sales = df["Sales_Amount"].sum()
average_sales = df["Sales_Amount"].mean()
highest_sales = df["Sales_Amount"].max()
lowest_sales = df["Sales_Amount"].min()


# Create PDF Report
pdf = SimpleDocTemplate(os.path.join(base_dir, "Sales_Report.pdf"))
elements = []

styles = getSampleStyleSheet()

elements.append(Paragraph("<b>Automated Sales Report</b>", styles["Title"]))
elements.append(Spacer(1, 0.5 * inch))

elements.append(Paragraph(f"Total Sales: {total_sales}", styles["Normal"]))
elements.append(Paragraph(f"Average Sales: {average_sales:.2f}", styles["Normal"]))
elements.append(Paragraph(f"Highest Sales: {highest_sales}", styles["Normal"]))
elements.append(Paragraph(f"Lowest Sales: {lowest_sales}", styles["Normal"]))
elements.append(Spacer(1, 0.5 * inch))

elements.append(Paragraph("<b>Individual Sales Data:</b>", styles["Heading2"]))
elements.append(Spacer(1, 0.3 * inch))

for index, row in df.iterrows():
    elements.append(
        Paragraph(f"{row['Sales_Rep']} - {row['Sales_Amount']}", styles["Normal"])
    )

pdf.build(elements)

print("✅ PDF Report Generated Successfully!")

