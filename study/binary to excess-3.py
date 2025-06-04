def binary_to_excess_3(binary_str):
    # Convert binary to decimal
    decimal_num = int(binary_str, 2)
    
    # Add 3 to each digit
    excess_3_decimal = decimal_num + 3
    
    # Convert the excess-3 decimal back to binary
    excess_3_binary = bin(excess_3_decimal)[2:]  # Remove the '0b' prefix
    
    return excess_3_binary

# Example usage
binary_input = "011"  # Replace with your binary input
excess_3_output = binary_to_excess_3(binary_input)
print(f"Excess-3 code for {binary_input}: {excess_3_output}")
