from fpdf import FPDF
import pandas as pd

# Load CSV file
df = pd.read_csv("security_alerts.csv")

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=10)

# Add table headers
pdf.cell(200, 10, "GitHub Security Alerts", ln=True, align="C")
pdf.ln(10)

# Add table rows
for index, row in df.iterrows():
    pdf.cell(40, 10, str(row["ID"]), border=1)
    pdf.cell(40, 10, str(row["Created At"]), border=1)
    pdf.cell(40, 10, str(row["Severity"]), border=1)
    pdf.cell(40, 10, str(row["Package"]), border=1)
    pdf.cell(40, 10, str(row["State"]), border=1)
    pdf.ln()

# Save PDF
pdf.output("security_alerts.pdf")
print("PDF file generated: security_alerts.pdf")
