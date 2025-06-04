def decimal_to_gray(n):
    """Convert a decimal number to its Gray code representation."""
    return n ^ (n >> 1)

# Example usage
decimal_number = 20
gray_code = decimal_to_gray(decimal_number)

print(f"Decimal: {decimal_number}")
print(f"Gray Code: {bin(gray_code)[2:]}")  # Convert to binary string without '0b' prefix

