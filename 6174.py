TARGETS = {3: 495, 4: 6174}


def validate(x):
    x = x.strip()
    if not x.isdecimal():
        return "Please enter numbers only."
    if len(x) not in TARGETS:
        return "Please enter a 3 or 4 digit number."
    if len(set(x)) == 1:
        return "All digits can't be the same. Please enter a valid number."
    return None


def kaprekar(x):
    x = x.strip()
    size = len(x)
    target = TARGETS[size]
    iterations = 0
    diff = 0
    steps = []

    while diff != target:
        digits = sorted(x)
        number1 = int("".join(digits))
        number2 = int("".join(reversed(digits)))
        diff = number2 - number1
        iterations += 1
        steps.append(f"{number2} - {number1} = {diff}")
        x = str(diff).zfill(size)

    return steps, iterations
