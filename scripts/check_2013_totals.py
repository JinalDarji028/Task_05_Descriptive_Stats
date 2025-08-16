import pandas as pd

# Path to the extracted stats CSV for 2013
csv_path = "outputs/extracted_tables/table_1.csv"

try:
    g = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"❌ Could not find {csv_path}. Make sure the CSV exists.")
    exit()

print("✅ CSV loaded successfully!\n")
print("NOTE: This quick script assumes you already confirmed totals manually.")
print("Prompts expect: Goals 332/188, Saves 129/201, Shots 700/413, SOG 533/317.")

# Optional: print the table to verify data visually
print("\n--- Data Preview ---")
print(g.head())
