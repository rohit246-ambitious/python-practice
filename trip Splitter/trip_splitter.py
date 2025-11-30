def main():
    print("=" * 50)
    print("🧳 TRIP EXPENSE SPLITTER 🧳")
    print("=" * 50)
    print()
    
    # Get friend names
    person1 = input("Enter your name: ").strip()
    person2 = input("Enter your friend's name: ").strip()
    
    print(f"\nGreat! Let's calculate expenses between {person1} and {person2}\n")
    
    # Store expenses
    expenses = []
    
    while True:
        print("\n--- Add New Expense ---")
        
        # Get expense details
        description = input("What was purchased? (or 'done' to finish): ").strip()
        
        if description.lower() == 'done':
            break
        
        while True:
            try:
                amount = float(input("Amount paid: "))
                if amount <= 0:
                    print("Amount must be positive!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        
        print(f"Who paid? 1) {person1}  2) {person2}")
        while True:
            payer_choice = input("Enter 1 or 2: ").strip()
            if payer_choice in ['1', '2']:
                payer = person1 if payer_choice == '1' else person2
                break
            print("Please enter 1 or 2!")
        
        # Store expense
        expenses.append({
            'description': description,
            'amount': amount,
            'payer': payer
        })
        
        print(f"✓ Added: {description} - ₹{amount:.2f} paid by {payer}")
    
    # Calculate totals
    if not expenses:
        print("\nNo expenses recorded. Goodbye!")
        return
    
    print("\n" + "=" * 50)
    print("📊 EXPENSE SUMMARY")
    print("=" * 50)
    
    person1_total = sum(e['amount'] for e in expenses if e['payer'] == person1)
    person2_total = sum(e['amount'] for e in expenses if e['payer'] == person2)
    total_expenses = person1_total + person2_total
    split_amount = total_expenses / 2
    
    # Display all expenses
    print("\nAll Expenses:")
    print("-" * 50)
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['description']}: ₹{exp['amount']:.2f} (paid by {exp['payer']})")
    
    print("\n" + "-" * 50)
    print(f"\n{person1} paid: ₹{person1_total:.2f}")
    print(f"{person2} paid: ₹{person2_total:.2f}")
    print(f"Total expenses: ₹{total_expenses:.2f}")
    print(f"Each person's share: ₹{split_amount:.2f}")
    
    # Calculate settlement
    print("\n" + "=" * 50)
    print("💰 SETTLEMENT")
    print("=" * 50)
    
    difference = abs(person1_total - person2_total)
    
    if person1_total > person2_total:
        print(f"\n{person2} owes {person1}: ₹{difference / 2:.2f}")
    elif person2_total > person1_total:
        print(f"\n{person1} owes {person2}: ₹{difference / 2:.2f}")
    else:
        print(f"\n✓ All settled! Both paid equally.")
    
    print("\n" + "=" * 50)
    print("Thank you for using Trip Expense Splitter! 🎉")
    print("=" * 50)

if __name__ == "__main__":
    main()