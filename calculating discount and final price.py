def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if it's 20% or higher."""
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Display the result
print(f"Final price after discount: ${final_price:.2f}")
