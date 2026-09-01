import pandas as pd
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
manual = pd.read_csv(
    BASE_DIR / "pooled_annotation_final.csv"
)

DATABASES = {
    "FAISS": {
        "MiniLM": "faiss_all-MiniLM-L6-v2.csv",
        "BGE": "faiss_bge-base-en-v1_5.csv",
        "E5": "faiss_e5-base-v2.csv",
        "Jina": "faiss_jina-embeddings-v2-base-en.csv",
    },
    "Chroma": {
        "MiniLM": "chroma_all-MiniLM-L6-v2.csv",
        "BGE": "chroma_bge-base-en-v1_5.csv",
        "E5": "chroma_e5-base-v2.csv",
        "Jina": "chroma_jina-embeddings-v2-base-en.csv",
    }
}
manual_lookup = {}

for _, row in manual.iterrows():

    qid = row["Question ID"]
    pdf = row["Retrieved PDF"]

    if qid not in manual_lookup:
        manual_lookup[qid] = {}

    manual_lookup[qid][pdf] = row["Relevant"]
results = {}

for db_name, models in DATABASES.items():

    results[db_name] = {}

    for model_name, filename in models.items():

        model = pd.read_csv(BASE_DIR / filename)

        model_lookup = {}

        for _, row in model.iterrows():

            qid = row["Question ID"]

            if qid not in model_lookup:
                model_lookup[qid] = []

            model_lookup[qid].append(row["Retrieved PDF"])

        precision_scores = []
        ndcg_scores = []
        rr_scores = []

        for qid in model_lookup:

            retrieved = model_lookup[qid]
            labels = manual_lookup[qid]

            relevant_found = 0

            for pdf in retrieved:
                if labels.get(pdf, 0) == 1:
                    relevant_found += 1

            precision = relevant_found / len(retrieved)

            import math

            dcg = 0

            for rank, pdf in enumerate(retrieved, start=1):
                if labels.get(pdf, 0) == 1:
                    dcg += 1 / math.log2(rank + 1)

            num_relevant = sum(labels.values())
            ideal_hits = min(5, num_relevant)

            idcg = 0

            for rank in range(1, ideal_hits + 1):
                idcg += 1 / math.log2(rank + 1)

            ndcg = dcg / idcg if idcg else 0

            rr = 0

            for rank, pdf in enumerate(retrieved, start=1):
                if labels.get(pdf, 0) == 1:
                    rr = 1 / rank
                    break

            precision_scores.append(precision)
            ndcg_scores.append(ndcg)
            rr_scores.append(rr)

        results[db_name][model_name] = {
            "Precision": sum(precision_scores) / len(precision_scores),
            "nDCG": sum(ndcg_scores) / len(ndcg_scores),
            "MRR": sum(rr_scores) / len(rr_scores),
        }

rows = []

for model in ["MiniLM", "BGE", "E5", "Jina"]:

    rows.append({
        "Model": model,

        "FAISS P@5": results["FAISS"][model]["Precision"],
        "FAISS nDCG": results["FAISS"][model]["nDCG"],
        "FAISS MRR": results["FAISS"][model]["MRR"],

        "Chroma P@5": results["Chroma"][model]["Precision"],
        "Chroma nDCG": results["Chroma"][model]["nDCG"],
        "Chroma MRR": results["Chroma"][model]["MRR"],
    })

results_df = pd.DataFrame(rows)

print("\n")
print("=" * 110)
print("FAISS vs Chroma Retrieval Comparison")
print("=" * 110)
print(results_df.to_string(index=False))
print("=" * 110)