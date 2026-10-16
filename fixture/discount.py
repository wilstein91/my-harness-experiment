def apply_discount(price, percent):
    """Return the price after applying a percentage discount."""
    # Intentional bug for the lesson: this returns the discount amount,
    # not the final price after the discount.
    return price * percent / 100
