# Lookbehind (and lookahead) in Regex
## SDDA - 28 february 2024
### By: Quinlan Caiger
Lookbehind alongside lookahead are known as lookarounds and are zero-length assertions meaning that they do not consume any characters in the string and return a true or false value depending on if there is a match. They check if a regular expression can be matched towards the left (lookbehind) or right (lookahead) of the current cursor position.

### Definitions
- Look ahead positive (?=)
  - Find expression A where expression B follows:
  - A(?=B)

- Look ahead negative (?!)
  > Find expression A where expression B does not follow:
  - A(?!B)

- Look behind positive (?<=)
  > Find expression A where expression B precedes:
  - (?<=B)A

- Look behind negative (?<!)
  > Find expression A where expression B does not precede:
  - (?<!B)A

### Examples
**Input string = "foobarbarfoo"**
- Look ahead positive (?=)
  - bar(?=bar) -> foo**bar**barfoo
  - finds the 1st bar ("bar" which has "bar" after it)
- Look ahead negative (?!)
  - bar(?!bar) -> foobar**bar**foo
  - finds the 2nd bar ("bar" which does not have "bar" after it)
- Look behind positive (?<=)
  - (?<=foo)bar -> foo**bar**barfoo
  - finds the 1st bar ("bar" which has "foo" before it)
- Look behind negative (?<!)
  - (?<!foo)bar -> foobar**bar**foo
  - finds the 2nd bar ("bar" which does not have "foo" before it)

#### References
1. https://www.regular-expressions.info/lookaround.html
2. https://stackoverflow.com/questions/2973436/regex-lookahead-lookbehind-and-atomic-groups
