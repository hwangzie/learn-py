def sandwich_items(*items):
    """Prints a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item.title()}")


sandwich_items('ham', 'cheese', 'lettuce', 'tomato')
sandwich_items('turkey', 'cheese')
sandwich_items('peanut butter', 'jelly')
    
