import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent

# Existing manual labels
manual = pd.read_csv(BASE_DIR / "retrieval_results_manual.csv")

# Retrieval results from all models
FILES = [
    "retrieval_results_all-MiniLM-L6-v2.csv",
    "retrieval_results_bge-base-en-v1_5.csv",
    "retrieval_results_e5-base-v2.csv",
    "retrieval_results_jina-embeddings-v2-base-en.csv",
]

# Build lookup of existing labels
manual_lookup = {}

for _, row in manual.iterrows():
    key = (row["Question ID"], row["Retrieved PDF"])
    manual_lookup[key] = row["Relevant"]

# Read all retrieval files
dfs = []

for file in FILES:
    df = pd.read_csv(BASE_DIR / file)
    dfs.append(df)

# Merge all rows
pool = pd.concat(dfs, ignore_index=True)

# Keep only unique (Question ID, Retrieved PDF) pairs
pool = pool.drop_duplicates(
    subset=["Question ID", "Retrieved PDF"]
).copy()

# Add Relevant column
pool["Relevant"] = pd.NA
# Fill existing labels
for idx, row in pool.iterrows():

    key = (row["Question ID"], row["Retrieved PDF"])

    if key in manual_lookup:
        pool.at[idx, "Relevant"] = int(manual_lookup[key])

# Sort nicely
pool = pool.sort_values(
    by=["Question ID", "Retrieved PDF"]
).reset_index(drop=True)

OUTPUT = BASE_DIR / "pooled_annotation.csv"

pool.to_csv(
    OUTPUT,
    index=False
)


print(pool.head(15))
print(pool["Relevant"].value_counts(dropna=False))

print("=" * 60)
print(f"Pooled file saved as {OUTPUT.name}")
print(f"Total rows : {len(pool)}")

existing = pool["Relevant"].notna()
print(f"Already labeled : {existing.sum()}")
print(f"Need labeling   : {(~existing).sum()}")
print("=" * 60)