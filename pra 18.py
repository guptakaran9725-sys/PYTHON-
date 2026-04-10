# PRACTICAL 18: Demonstrating Regular Expressions

import re

text = "My email is vahib123@example.com and my phone number is +91-9876543210."

print("Original Text:", text)

# 1. re.search() - Find first match
match = re.search(r"\d{10}", text)
if match:
    print("\nSearch for 10-digit number:", match.group())

# 2. re.findall() - Find all matches
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
print("Find all emails:", emails)

# 3. re.match() - Match at beginning of string
match_start = re.match(r"My", text)
print("Match at start:", match_start.group() if match_start else "No match")

# 4. re.split() - Split string by pattern
split_text = re.split(r"\s", text)
print("Split by spaces:", split_text)

# 5. re.sub() - Replace pattern
masked_text = re.sub(r"\d{10}", "XXXXXXXXXX", text)
print("Replace phone number:", masked_text)

# 6. Character classes
digits = re.findall(r"\d", text)
print("All digits:", digits)

# 7. Anchors (^ for start, $ for end)
start_check = re.findall(r"^My", text)
end_check = re.findall(r"\.$", text)
print("Starts with 'My':", start_check)
print("Ends with '.':", end_check)

# 8. Quantifiers
numbers = re.findall(r"\d{2,}", text)
print("Numbers with 2 or more digits:", numbers)

# 9. Groups
phone_match = re.search(r"(\+91)-(\d{10})", text)
if phone_match:
    print("Country Code:", phone_match.group(1))
    print("Phone Number:", phone_match.group(2))