import json, re, glob

file = glob.glob("*.srt")[0]

def translate_srt_partial(srt_filename, json_filename, output_filename):
    # Load the translation dictionary
    with open(json_filename, 'r', encoding='utf-8') as f:
        trans_dict = json.load(f)

    # Sort dictionary keys by length in descending order for greedy phrase matching
    sorted_keys = sorted(trans_dict.keys(), key=len, reverse=True)

    with open(srt_filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse SRT blocks
    raw_blocks = re.split(r'\n\s*\n', content.strip())
    blocks = []
    for b in raw_blocks:
        lines = b.strip().split('\n')
        if len(lines) >= 3:
            match = re.match(r'([\d:,]+)\s*-->\s*([\d:,]+)', lines[1])
            start_time = match.group(1) if match else ""
            end_time = match.group(2) if match else ""
            text = ' '.join(lines[2:])
            blocks.append({'start': start_time, 'end': end_time, 'text': text})

    # Group broken lines across blocks into complete sentences
    sentences = []
    not_matched_sentences = []
    current_group_times = []
    current_text_parts = []

    for block in blocks:
        if not current_group_times:
            current_group_times = [block['start'], block['end']]
        else:
            current_group_times[1] = block['end']

        current_text_parts.append(block['text'])
        combined_text = ' '.join(current_text_parts)
        combined_text_normalized = re.sub(r'\s+', ' ', combined_text).strip()

        # Check if sentence is complete (ends with . ? !) or if it's the last block
        if re.search(r'[.?!]$', combined_text_normalized) or block == blocks[-1]:
            # Apply partial/phrase translation using dictionary keys
            translated_text = combined_text_normalized
            matched = False
            for key in sorted_keys:
                if key in translated_text:
                    translated_text = translated_text.replace(key, trans_dict[key])
                    matched = True

            sentences.append({
                'start': current_group_times[0],
                'end': current_group_times[1],
                'text': translated_text
            })

            # Track sentences that had no dictionary matches
            if not matched:
                not_matched_sentences.append(combined_text_normalized)

            current_group_times = []
            current_text_parts = []

    # Write the translated and merged subtitles to the output file
    with open(output_filename, 'w', encoding='utf-8') as f:
        for i, item in enumerate(sentences, 1):
            f.write(f"{i}\n{item['start']} --> {item['end']}\n{item['text']}\n\n")

    # Automatically create and write unmatched sentences to not_matched.txt if any exist
    if not_matched_sentences:
        with open('not_matched.txt', 'w', encoding='utf-8') as f:
            for text in not_matched_sentences:
                f.write(text + '\n\n')

if __name__ == '__main__':
    translate_srt_partial(file, 'dict.json', 'subt2.srt')