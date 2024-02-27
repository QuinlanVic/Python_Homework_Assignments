# Lookbehind in Regex
## SDDA - 28 february 2024
### By: Quinlan Caiger
Lookbehind is a zero-length assertion meaning that jfoiewjfwjfoe. It returns a match or no match.
Lookbehind looks behind the cursor. They can be positive or negative.
- Positive lookbehind - ((?<=)
- Negative lookbehind - (?<!)
#### Examples
- bar(?=bar) -> finds the 1st bar ("bar" which has "bar" after it)
- bar(?!bar) -> finds the 2nd bar ("bar" which does not have "bar" after it)
- (?<=foo)bar -> finds the 1st bar ("bar" which has "foo" before it)
- (?<!foo)bar -> finds the 2nd bar ("bar" which does not have "foo" before it)

#### References
1. https://www.regular-expressions.info/lookaround.html
2. https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
