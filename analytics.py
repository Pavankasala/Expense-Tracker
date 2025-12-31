def category_analytics(expenses):
    summary = {}
    for exp in expenses:
        summary[exp["category"]] = summary.get(exp["category"], 0) + exp["amount"]
    return summary

def monthly_analytics(expenses):
    summary = {}
    for exp in expenses:
        month = exp["date"][:7]
        summary[month] = summary.get(month, 0) + exp["amount"]
    return summary
