def print_table(headers, rows):
    """Print a formatted table"""
    # Calculate column widths
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Print header
    print("\n" + "-" * (sum(col_widths) + len(headers) * 3 + 1))
    header_row = "| "
    for i, header in enumerate(headers):
        header_row += str(header).ljust(col_widths[i]) + " | "
    print(header_row)
    print("-" * (sum(col_widths) + len(headers) * 3 + 1))
    
    # Print rows
    for row in rows:
        row_str = "| "
        for i, cell in enumerate(row):
            row_str += str(cell).ljust(col_widths[i]) + " | "
        print(row_str)
    
    print("-" * (sum(col_widths) + len(headers) * 3 + 1))


def main():
    print("=" * 60)
    print("🧳 TRIP EXPENSE SPLITTER - MULTI FRIENDS 🧳")
    print("=" * 60)
    print()
    
    # Get number of friends
    while True:
        try:
            num_friends = int(input("How many friends are going on the trip? "))
            if num_friends < 2:
                print("Need at least 2 friends!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")
    
    # Get friend names
    friends = []
    print(f"\nEnter the names of {num_friends} friends:")
    for i in range(num_friends):
        name = input(f"Friend {i+1}: ").strip()
        friends.append(name)
    
    print(f"\nGreat! Trip with: {', '.join(friends)}")
    print()
    
    # Initialize expense tracking
    expenses = []
    friend_expenses = {friend: [] for friend in friends}
    
    while True:
        print("\n--- Add New Expense ---")
        
        # Get expense details
        description = input("What was purchased? (or 'done' to finish): ").strip()
        
        if description.lower() == 'done':
            break
        
        while True:
            try:
                amount = float(input("Amount paid: ₹"))
                if amount <= 0:
                    print("Amount must be positive!")
                    continue
                break
            except ValueError:
                print("Please enter a valid number!")
        
        # Show friends list
        print("\nWho paid?")
        for i, friend in enumerate(friends, 1):
            print(f"{i}) {friend}")
        
        while True:
            try:
                payer_choice = int(input("Enter number: "))
                if 1 <= payer_choice <= len(friends):
                    payer = friends[payer_choice - 1]
                    break
                print(f"Please enter a number between 1 and {len(friends)}!")
            except ValueError:
                print("Please enter a valid number!")
        
        # Store expense
        expenses.append({
            'description': description,
            'amount': amount,
            'payer': payer
        })
        friend_expenses[payer].append({'description': description, 'amount': amount})
        
        print(f"✓ Added: {description} - ₹{amount:.2f} paid by {payer}")
    
    # Calculate totals
    if not expenses:
        print("\nNo expenses recorded. Goodbye!")
        return
    
    print("\n" + "=" * 60)
    print("📊 EXPENSE SUMMARY")
    print("=" * 60)
    
    # Create expense table by person
    max_expenses = max(len(friend_expenses[friend]) for friend in friends)
    
    for friend in friends:
        print(f"\n💰 {friend}'s Expenses:")
        if friend_expenses[friend]:
            headers = ["#", "Item", "Amount (₹)"]
            rows = []
            for i, exp in enumerate(friend_expenses[friend], 1):
                rows.append([i, exp['description'], f"₹{exp['amount']:.2f}"])
            print_table(headers, rows)
            total = sum(e['amount'] for e in friend_expenses[friend])
            print(f"Total paid by {friend}: ₹{total:.2f}")
        else:
            print(f"  No expenses paid by {friend}")
    
    # Calculate totals
    print("\n" + "=" * 60)
    print("💵 TOTAL SUMMARY")
    print("=" * 60)
    
    totals = {}
    for friend in friends:
        totals[friend] = sum(e['amount'] for e in friend_expenses[friend])
    
    total_expenses = sum(totals.values())
    per_person_share = total_expenses / len(friends)
    
    # Summary table
    headers = ["Friend", "Paid (₹)", "Should Pay (₹)", "Balance"]
    rows = []
    balances = {}
    
    for friend in friends:
        paid = totals[friend]
        balance = paid - per_person_share
        balances[friend] = balance
        
        if balance > 0:
            balance_str = f"+₹{balance:.2f} (gets back)"
        elif balance < 0:
            balance_str = f"-₹{abs(balance):.2f} (owes)"
        else:
            balance_str = "₹0.00 (settled)"
        
        rows.append([friend, f"₹{paid:.2f}", f"₹{per_person_share:.2f}", balance_str])
    
    print_table(headers, rows)
    
    print(f"\nTotal Trip Expenses: ₹{total_expenses:.2f}")
    print(f"Each Person's Share: ₹{per_person_share:.2f}")
    
    # Calculate settlements
    print("\n" + "=" * 60)
    print("💰 SETTLEMENTS NEEDED")
    print("=" * 60)
    
    # Separate who owes and who should receive
    owes = {friend: abs(bal) for friend, bal in balances.items() if bal < 0}
    receives = {friend: bal for friend, bal in balances.items() if bal > 0}
    
    if not owes:
        print("\n✓ All settled! Everyone paid their fair share.")
    else:
        print()
        settlements = []
        
        for debtor in sorted(owes.keys(), key=lambda x: owes[x], reverse=True):
            debt = owes[debtor]
            
            for creditor in sorted(receives.keys(), key=lambda x: receives[x], reverse=True):
                if receives[creditor] <= 0:
                    continue
                
                settlement_amount = min(debt, receives[creditor])
                settlements.append(f"• {debtor} pays {creditor}: ₹{settlement_amount:.2f}")
                
                debt -= settlement_amount
                receives[creditor] -= settlement_amount
                
                if debt == 0:
                    break
        
        for settlement in settlements:
            print(settlement)
    
    print("\n" + "=" * 60)
    print("Thank you for using Trip Expense Splitter! 🎉")
    print("=" * 60)


if __name__ == "__main__":
    main()