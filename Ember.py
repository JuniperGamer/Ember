import re
import os

# Welcome to Ember!
# Ember detects and removes code based on given patterns

# This is a framework and not an actual program.

def load_custom_patterns_from_file(file_path):
    custom_patterns = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            custom_patterns = [line.strip() for line in file.readlines()]
    return custom_patterns

def create_malicious_library():
    folder = 'malicious_library'
    file_path = os.path.join(folder, 'MALlib.txt')

    os.makedirs(folder, exist_ok=True)
    with open(file_path, 'w') as file:
        file.write('# Add your custom malicious patterns here, one per line')

def scan_for_malicious_code(code):
    # Define patterns for common malicious code
    malicious_patterns = [
        r'import\s+subprocess',
        r'system\("',
        r'exec\(',
        r'os\.system',
    ]

    # Load custom malicious patterns from the file
    custom_patterns = load_custom_patterns_from_file('malicious_library/MALlib.txt')

    # Add custom patterns to the list
    malicious_patterns.extend(custom_patterns)

    for pattern in malicious_patterns:
        if re.search(pattern, code):
            print("Potential malicious code found:")
            print(code)
            return True

    return False

def remove_malicious_code(code):
    # Remove detected malicious code
    cleaned_code = re.sub(r'import\s+subprocess', '', code)
    cleaned_code = re.sub(r'system\("', '', cleaned_code)
    cleaned_code = re.sub(r'exec\(', '', cleaned_code)
    cleaned_code = re.sub(r'os\.system', '', cleaned_code)

    return cleaned_code

# Create the malicious library if it doesn't exist
if not os.path.exists('malicious_library/MALlib.txt'):
    create_malicious_library()

# Sample code to be scanned
code_to_scan = """
import subprocess
print("Hello, world!")
"""

if scan_for_malicious_code(code_to_scan):
    cleaned_code = remove_malicious_code(code_to_scan)
    print("Malicious code removed:")
    print(cleaned_code)
else:
    print("No malicious code detected.")

