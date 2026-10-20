import json
import re

def translate_and_merge_srt(srt_filename, json_filename, output_filename):
    # Load the translation dictionary
    with open(json_filename, 'r', encoding='utf-8') as f:
        trans_dict = json.load(f)

    with open(srt_filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse SRT blocks
    raw_blocks = re.split(r'\n\s*\n', content.strip())
    blocks = []
    for b in raw_blocks:
        lines = b.strip().split('\n')
        if len(lines) >= 3:
            time_line = lines[1]
            text = ' '.join(lines[2:])
            blocks.append({'time_line': time_line, 'text': text})

    # Group broken lines across blocks into complete sentences
    sentences = []
    current_group_times = []
    current_text_parts = []

    for block in blocks:
        match = re.match(r'([\d:,]+)\s*-->\s*([\d:,]+)', block['time_line'])
        if match:
            start_time = match.group(1)
            end_time = match.group(2)
        else:
            start_time, end_time = "", ""

        if not current_group_times:
            current_group_times = [start_time, end_time]
        else:
            current_group_times[1] = end_time

        current_text_parts.append(block['text'])
        combined_text = ' '.join(current_text_parts)
        combined_text_normalized = re.sub(r'\s+', ' ', combined_text).strip()

        # Check if sentence is complete (ends with . ? !) or if it's the last block
        if re.search(r'[.?!]$', combined_text_normalized) or block == blocks[-1]:
            # Translate using dictionary if available, otherwise keep original text
            translated_text = trans_dict.get(combined_text_normalized, combined_text_normalized)
            sentences.append({
                'start': current_group_times[0],
                'end': current_group_times[1],
                'text': translated_text
            })
            current_group_times = []
            current_text_parts = []

    # Write the translated and merged subtitles to the output file
    with open(output_filename, 'w', encoding='utf-8') as f:
        for i, item in enumerate(sentences, 1):
            f.write(f"{i}\n{item['start']} --> {item['end']}\n{item['text']}\n\n")

if __name__ == '__main__':
    translate_and_merge_srt('subt1.srt', 'dict.json', 'subt2.srt')
