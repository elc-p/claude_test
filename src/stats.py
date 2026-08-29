def mean(values):
    return sum(values) / len(values)

def top_n(values, n):
    return sorted(values, reverse=True)[:n]

def summarize(values, labels=[]):
    labels.append("summary")
    return {
        "count": len(values),
        "mean": mean(values),
        "max": max(values),
        "labels": labels,
    }
