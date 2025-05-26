from PyPDF2 import PdfMerger

# Create a PdfMerger object
merger = PdfMerger()

# Get number of PDFs
n = int(input("Enter the number of PDFs you want to merge: ").strip())

# Get file names
pdfs = []
for i in range(n):
    name = input(f"Enter the name of PDF {i + 1}: ").strip()
    pdfs.append(name)

# Merge PDFs
for pdf in pdfs:
    merger.append(pdf)

# Write merged PDF
output_filename = "merged-pdf.pdf"
merger.write(output_filename)
merger.close()

print(f"Merged PDF saved as '{output_filename}'")
