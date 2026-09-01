def precision_at_k(retrieved_docs, relevant_docs, k=5):
    """
    Precision@K = Relevant retrieved / K
    """

    retrieved = retrieved_docs[:k]

    hits = sum(1 for doc in retrieved if doc in relevant_docs)

    return hits / k


def recall_at_k(retrieved_docs, relevant_docs, k=5):
    """
    Recall@K = Relevant retrieved / Total relevant
    """

    if len(relevant_docs) == 0:
        return 0

    retrieved = retrieved_docs[:k]

    hits = sum(1 for doc in retrieved if doc in relevant_docs)

    return hits / len(relevant_docs)


def reciprocal_rank(retrieved_docs, relevant_docs):
    """
    Reciprocal Rank = 1 / rank of first relevant document
    """

    for rank, doc in enumerate(retrieved_docs, start=1):
        if doc in relevant_docs:
            return 1 / rank

    return 0