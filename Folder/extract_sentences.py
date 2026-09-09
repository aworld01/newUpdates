"""
Extract English-Hindi sentence pairs from a text file into a dictionary.

Expected file format: sentences alternate as
    English sentence
    Hindi sentence
    <blank line>
    English sentence
    Hindi sentence
    <blank line>
    ...

Blank/extra empty lines are ignored, and lines are simply paired up
two-at-a-time in the order they appear (first non-empty line = English,
second non-empty line = Hindi).
"""

import json
import sys


def extract_sentence_pairs(input_path):
    """Read the file and return a dict mapping English -> Hindi sentences."""
    with open(input_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]

    # Drop empty lines entirely, then pair them up two-by-two
    non_empty_lines = [line for line in lines if line]

    sentence_dict = {}
    skipped = []

    for i in range(0, len(non_empty_lines) - 1, 2):
        english = non_empty_lines[i]
        hindi = non_empty_lines[i + 1]
        sentence_dict[english] = hindi

    # If there's an odd one out at the end, note it instead of silently dropping it
    if len(non_empty_lines) % 2 != 0:
        skipped.append(non_empty_lines[-1])

    return sentence_dict, skipped


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "daily_use_sentences.txt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "sentence_dict.json"

    sentence_dict, skipped = extract_sentence_pairs(input_path)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(sentence_dict, f, ensure_ascii=False, indent=2)

    print(f"Extracted {len(sentence_dict)} English-Hindi sentence pairs.")
    print(f"Saved to {output_path}")

    if skipped:
        print(f"Warning: {len(skipped)} unpaired line(s) skipped: {skipped}")


if __name__ == "__main__":
    main()
