import json
import sys

def load_prefix_data(json_file="indian_mobile_prefixes.json"):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        lookup = {entry['prefix']: entry for entry in data}
        return lookup
    except FileNotFoundError:
        print(f"Error: {json_file} not found. Please generate it first.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: {json_file} is not valid JSON.")
        sys.exit(1)

def validate_number(number):
    if not number.isdigit():
        return False, "Number must contain only digits."
    if len(number) != 10:
        return False, "Number must be exactly 10 digits."
    if number[0] not in '6789':
        return False, "Indian mobile numbers must start with 6, 7, 8, or 9."
    return True, ""

def main():

    lookup = load_prefix_data()

    if len(sys.argv) > 1:
        number = sys.argv[1]
    else:
        number = input("Enter the 10-digit mobile number (without +91): ").strip()

    valid, msg = validate_number(number)
    if not valid:
        print(f"Invalid number: {msg}")
        return

    prefix = number[:4]
    if prefix in lookup:
        entry = lookup[prefix]
        print("\n=== Original Allocation Details ===")
        print(f"Mobile Number: {number}")
        print(f"Prefix:        {prefix}")
        print(f"Operator:      {entry['operator']}")
        print(f"Circle:        {entry['circle']}")
        print("\nNote: Due to Mobile Number Portability (MNP), the current")
        print("operator and location may differ from the original allocation.")
    else:
        print(f"Prefix {prefix} not found in the dataset.")
        print("Possible reasons: the prefix might be newer or not yet included.")

if __name__ == "__main__":
    main()
