def mean(values):
    return sum(values) / len(values)

def top_n(values, n):
    return sorted(values, reverse=True)[:n]