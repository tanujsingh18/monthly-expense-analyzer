def analyze_expenses(data):
    total = 0
    category_totals = {}

    for item in data:
        amount = item['amount']
        category = item['category']

        total += amount

        if category not in category_totals:
            category_totals[category] = 0
        
        category_totals[category] += amount

    return {
        "Total Spending": total,
        "Category Breakdown": category_totals
    }