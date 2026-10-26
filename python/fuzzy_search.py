'''
n: how many maches to return (default = 3)
cutoff: minimum similarity score (0-1)
Defalt =0.6
'''
from difflib import get_close_matches

user_input = "how you?"
source_texts = ["Hello", "How are you?", "Hi"]

match = get_close_matches(user_input, source_texts, n=1, cutoff=0.6)

print(match)