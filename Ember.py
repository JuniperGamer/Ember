import re

# Welcome to Ember!
# Ember detects and removes code based off code given

# This is a framework and not an actual program.

def scan_for_malicious_code(code):
    # Define patterns for common malicious code
    malicious_patterns = [
        r'import\s+subprocess',
        r'system\("',
        r'exec\(',
        r'os\.system',
    ]
    
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
