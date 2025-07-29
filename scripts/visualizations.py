import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the raw table containing team stats
df = pd.read_csv("outputs/extracted_tables/table_1.csv")

# Clean column names if needed
df.columns = [col.strip() for col in df.columns]

# Manually split into four blocks
blocks = {
    "Goals by Period": df.iloc[0:2].copy(),
    "Saves by Period": df.iloc[3:5].copy(),
    "Shots by Period": df.iloc[6:8].copy(),
    "Shots on Goal": df.iloc[9:11].copy()
}

# Set output folder
output_dir = "outputs/visualizations"
os.makedirs(output_dir, exist_ok=True)

# Plot each block
for title, block in blocks.items():
    block = block.rename(columns={block.columns[0]: "Team"})
    block.set_index("Team", inplace=True)
    
    # Convert values to integers
    block = block.apply(pd.to_numeric, errors="coerce")

    # Plot
    block.T.plot(kind="bar", figsize=(8,5))
    plt.title(title)
    plt.ylabel("Count")
    plt.xlabel("Half")
    plt.xticks(rotation=0)
    plt.tight_layout()

    # Save
    file_name = title.lower().replace(" ", "_") + ".png"
    plt.savefig(os.path.join(output_dir, file_name))
    plt.close()

print(f"✅ Visualizations saved in {output_dir}/")