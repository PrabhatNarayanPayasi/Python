from PyPDF2 import PdfWriter
import os

# Initialize the PdfWriter
merger = PdfWriter()

# Get all PDF files in the current directory
files = [file for file in os.listdir() if file.endswith(".pdf")]

# Ensure there are PDF files
if not files:
    print("No PDF files found in the current directory.")
else:
    # Sort files alphabetically (or however you want to merge them)
    files.sort()

    # Append each PDF to the merger
    for pdf in files:
        try:
            # Open the file in read-binary mode
            with open(pdf, "rb") as file:
                merger.append(file)
        except Exception as e:
            print(f"Error merging {pdf}: {e}")

    # Write the merged PDF to a new file
    with open("merged-pdf.pdf", "wb") as output_pdf:
        merger.write(output_pdf)

    print("Merge complete!")
