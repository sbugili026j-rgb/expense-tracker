import json
from datetime import date
from pathlib import Path

DATA_FILE = Path("expenses.json")


def load_expenses():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open() as f:
        return json.load(f)


def save_expenses(expenses):
    with DATA_FILE.open("w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(expenses):
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please enter a number.")
        return
    if amount <= 0:
        print("Amount must be more than zero.")
        return
    category = input("Category (food, transport, ...): ").strip().lower() or "other"
    note = input("Note (optional): ").strip()
    expenses.append(
        {
            "date": str(date.today()),
            "amount": amount,
            "category": category,
            "note": note,
        }
    )
    save_expenses(expenses)
    print("Saved.")


def list_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['date']}  {e['amount']:.2f}  {e['category']}  {e['note']}")


def show_totals(expenses):
    if not expenses:
        print("No expenses yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    for category, total in sorted(totals.items()):
        print(f"{category}: {total:.2f}")
    print(f"TOTAL: {sum(totals.values()):.2f}")


def main():
    expenses = load_expenses()
    while True:
        print("\n1) Add  2) List  3) Totals  4) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_totals(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()