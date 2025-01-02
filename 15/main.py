import re

# Quantifiers
# *: Matches 0 or more occurrences. -> a* "", "a", "aa"
# +: Matches 1 or more occurrences.
# ?: Matches 0 or 1 occurrence (makes it optional). "", "a"
# {n}: Matches exactly n occurrences. a{3} -> "aaa"
# {n,}: Matches n or more occurrences. "a{2,} "aa", "aaa"
# {n,m}: Matches between n and m occurrences. a{2,4}, "aa", "aaa", "aaaa"

# QWD123 -> Moraju biti 3 slova i pracena sa 3 broja

bonus_codes = "ABC123, tom255, bonus455, bonus22"

pattern = r"\b[A-Za-z]{3}\d{3}\b"

product_codes=re.findall(pattern, bonus_codes)
print(product_codes)

# Vezba
username = "toma1992"
username_pattern = r"[a-zA-Z]{1,5}\d{2,}"
match = re.match(username_pattern, username)

if match:
    print(match.group())

