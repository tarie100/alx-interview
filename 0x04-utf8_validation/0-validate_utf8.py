#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """ a method that determines if a given data set
    represents a valid UTF-8 encoding
    """
    # Initialize a variable to keep track of the number of remaining bytes
    remaining_bytes = 0

    # Iterate through each integer in the data
    for byte in data:
        # Check if the byte is a continuation byte (starts with '10xxxxxx')
        if remaining_bytes > 0:
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            remaining_bytes -= 1
        else:
            # Determine the number of bytes for the current character
            if (byte >> 7) == 0b0:
                # Single-byte character
                remaining_bytes = 0
            elif (byte >> 5) == 0b110:
                # Two-byte character
                remaining_bytes = 1
            elif (byte >> 4) == 0b1110:
                # Three-byte character
                remaining_bytes = 2
            elif (byte >> 3) == 0b11110:
                # Four-byte character
                remaining_bytes = 3
            else:
                return False  # Invalid start byte

    # Ensure all bytes were consumed
    return remaining_bytes == 0

# Example usage:
data_set = [197, 130, 1]  # Represents the character 'Ç' (U+00C7)
print(validUTF8(data_set))  # Output: True

