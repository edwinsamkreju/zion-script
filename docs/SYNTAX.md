# ZION SCRIPT syntax (v0.1)

## Output and variables
```text
Say "Hello!"
Store 42 as answer
Say answer
```

## Input
```text
Ask "What is your name?" and store the answer as name
Say name
```

## Arithmetic
```text
Add 4 and 5
Subtract 3 from 10
Multiply 6 and 7
Divide 20 by 4
Say result
```
Arithmetic commands place their answer in `result`.

## Conditions
```text
If score is greater than or equal to 50
    Say "You passed"
Otherwise
    Say "Try again"
End if
```

## Repetition
```text
Repeat 3 times
    Say "Hello"
End repeat
```

## Lists
```text
Create a list called colours
Add "Blue" to colours
For each colour in colours
    Say colour
End for
```

## Functions
```text
Create a function called welcome
    Say "Welcome!"
End function
Run welcome
```

## Comments
A line beginning with `#` is a comment.

## Current limitations
Function parameters, return values, list indexing and dictionary commands are not implemented yet. Expressions currently use Python expression syntax plus friendly comparison phrases. ZION is not an arbitrary natural-language parser.
