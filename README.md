# Kaprekar Routine

A small program that runs Kaprekar's routine on 3 and 4 digit numbers, available as a Python command-line script and as a web page.

## What is the Kaprekar routine?

1. Take a number and arrange its digits in descending order, then in ascending order.
2. Subtract the smaller number from the larger one.
3. Repeat with the result (keeping leading zeros) until it stops changing.

Every valid 4 digit number reaches **6174** in at most 7 steps, and every valid 3 digit number reaches **495**.

## Features

- Accepts 3 or 4 digit numbers
- Leading zeros allowed (`0123` counts as a 4 digit number)
- Rejects non-numeric input without crashing
- Rejects numbers whose digits are all the same (`1111`, `222`), since they give 0 and never reach the target
- Prints every step and the total number of iterations

## Project structure

```
kaprekar.py   Python command-line version
index.html    Web version (HTML, CSS and JavaScript in one file)
README.md     This file
```

## Running the Python version

Requires Python 3.6 or newer. No extra packages are needed.

```
python kaprekar.py
```

Example session:

```
Enter a 3 or 4 digit number: 0123
Original number was 0123
3210 - 123 = 3087
8730 - 378 = 8352
8532 - 2358 = 6174
Number of iterations: 3
```

## Running the web version

Open `index.html` in any browser. Type a number and press **Calculate** or Enter. The page shows each step and the iteration count, and works offline apart from the Google Fonts stylesheet.

### Publishing it

The web version is a single static file, so it can be hosted for free:

- **GitHub Pages:** push the project to a repository, then go to Settings → Pages and select the branch.
- **Netlify Drop:** drag the folder onto the Netlify Drop page.
- **Cloudflare Pages:** connect the repository or upload the folder.

Keep the file named `index.html` so hosts serve it as the home page.

## How it works

For each step the program:

1. Sorts the digits of the current number.
2. Builds the ascending number (`number1`) and the descending number (`number2`).
3. Computes `diff = number2 - number1`.
4. Pads `diff` back to the original length with leading zeros (`zfill` in Python, `padStart` in JavaScript).
5. Stops when `diff` equals the target (495 for 3 digits, 6174 for 4 digits).

## Why only 3 and 4 digits?

These lengths have a single fixed point, so the loop always ends at a known target. Two-digit numbers instead fall into a repeating cycle (09 → 81 → 63 → 27 → 45 → 09) and have no fixed point, so they are not supported.

## Possible improvements

- Ask "Try another number?" and repeat
- Run all valid numbers and chart how many steps each takes
- Save the steps to a file
- Wrap the logic in functions and add tests
