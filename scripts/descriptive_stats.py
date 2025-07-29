import pandas as pd
import tabula
import os

# Step 1: Load PDF and extract all tables
pdf_path = "data/su_lacrosse_2013.pdf"
tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

# Step 2: Handle failure
if not tables or len(tables) == 0:
    print("❌ No tables extracted from the PDF.")
    exit()

# Step 3: Create output folder
output_dir = "outputs/extracted_tables"
os.makedirs(output_dir, exist_ok=True)

# Step 4: Print and save each table
print(f"\n✅ Extracted {len(tables)} tables from the PDF.\n")

for i, table in enumerate(tables):
    print(f"\n--- Table {i} ---")
    
    if isinstance(table, pd.DataFrame):
        print(table.to_string(index=False))  # Print cleanly
        # Save as CSV
        table.to_csv(f"{output_dir}/table_{i}.csv", index=False)
    else:
        print("⚠️ Not a valid DataFrame.")

print(f"\n💾 All tables saved to: {output_dir}")

