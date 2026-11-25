# ZION SCRIPT syntax (v0.1)

## Output and variables

Use show to display a value. Assign a variable with name be value or the familiar Python-style name = value form.

\`\`\`zion
show "Hello!"
answer be 42
score = answer + 8
show score
\`\`\`

show replaces the older Say spelling. The old Say and Store value as name forms remain accepted for compatibility with early examples.

## Operators and expressions

ZION expressions use Python syntax and precedence. Supported operators include arithmetic (+ - * / // % **), comparisons (== != < <= > >=), boolean (and or not), bitwise (& | ^ ~ << >>), identity (is, is not), membership (in, not in), assignment operators (=, +=, -=, etc.), calls, attributes, indexing and slicing.

\`\`\`zion
base be 5
power = base ** 3
remainder = power % 4
is_valid = power >= 100 and remainder != 0
show is_valid
\`\`\`

Friendly comparison phrases are also supported in conditions, such as If score is greater than or equal to 50.

## Conditions and repetition

\`\`\`zion
if score >= 50
    show "You passed"
otherwise
    show "Try again"
end if

repeat 3 times
    show "Hello"
end repeat
\`\`\`

## Existing beginner commands

The early prototype's Ask, list commands, For each, and simple no-argument function commands remain available.

## Python interoperability

Python-compatible statements such as import math, result = math.sqrt(81), and method calls can be used. The transpiler validates generated Python syntax but does not sandbox execution. Only run code you trust.

## Current limitations

This is an early transpiler, not a fully independent reimplementation of Python. ZION-specific blocks currently cover conditions and repeat/foreach loops; advanced constructs can be supplied as Python-compatible statements where supported.
