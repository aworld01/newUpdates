import re, glob

file = glob.glob("*.srt")[0]

def srt2txt(srt_filename, txt_filename):
    with open(srt_filename, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the SRT file into individual subtitle blocks
    blocks = re.split(r'\n\s*\n', content.strip())
    transcript_lines = []

    for block in blocks:
        lines = block.strip().split('\n')
        if len(lines) >= 3:
            text_lines = lines[2:]
            # Join wrapped lines within the same subtitle cue with a space
            text_block = ' '.join(text_lines)
            transcript_lines.append(text_block)

    # Combine all blocks into a continuous text stream
    full_text = ' '.join(transcript_lines)
    full_text = re.sub(r'\s+', ' ', full_text)

    # Split lines only at periods (.), keeping the period; otherwise join everything
    sentences = re.split(r'(?<=[.?])\s+', full_text)
    cleaned_sentences = [s.strip() for s in sentences if s.strip()]

    # Write the result to the output file with double newlines separating each sentence/turn
    with open(txt_filename, 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(cleaned_sentences))

if __name__ == '__main__':
    srt2txt(file, 'clean_data.txt')
    
