from analyzer import analyze_expenses
from suggestions import generate_suggestions
from utils import format_currency
import json

def load_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def main():
    data = load_data('data_sample.json')
    analysis = analyze_expenses(data)

    print("\n--- Expense Summary ---")
    print(f"Total Spending: {format_currency(analysis['Total Spending'])}")

    print("\nCategory Breakdown:")
    for k, v in analysis["Category Breakdown"].items():
        print(f"  {k}: {format_currency(v)}")

    suggestions = generate_suggestions(data, analysis)

    print("\n--- Savings Suggestions ---")
    for s in suggestions:
        print(f"✔ {s}")

if __name__ == "__main__":
    main()