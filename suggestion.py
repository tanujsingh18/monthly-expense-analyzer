def generate_suggestions(data, analysis):
    suggestions = []
    total = analysis["Total Spending"]
    categories = analysis["Category Breakdown"]

    # Rule-based suggestions
    if categories.get("food", 0) > 0.3 * total:
        suggestions.append("You are spending a lot on food. Consider cooking more at home.")

    if categories.get("entertainment", 0) > 0.2 * total:
        suggestions.append("Try reducing entertainment expenses like subscriptions or outings.")

    if categories.get("transport", 0) > 0.15 * total:
        suggestions.append("Look into carpooling or public transport to save money.")

    if total > 25000:
        suggestions.append("Your overall spending is high. Consider setting a strict monthly budget.")

    if not suggestions:
        suggestions.append("Great job! Your spending looks balanced.")

    return suggestions