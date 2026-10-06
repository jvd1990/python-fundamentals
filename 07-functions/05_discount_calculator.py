def calculate_discount(rate, price):
    discount_amount = int(price * rate / 100)
    final_price = price - discount_amount

    print("Discount amount:", discount_amount)
    print("Final price:", final_price)


discount_rate = int(input("Enter the discount percentage (0-100): "))
original_price = int(input("Enter the original price: "))

calculate_discount(discount_rate, original_price)