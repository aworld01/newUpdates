import argparse

ap = argparse.ArgumentParser(
description=f"This is a tutorial on ArgumentParser"
)

ap.add_argument("n1",
type=int,
help="please enter a positive number.")

args = ap.parse_args()

result = args.n1

print(f'You have entered: {result}')