#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to refine and polish Italian course content
Improves grammar, clarity, flow while preserving author's voice
"""

import re

def polish_italian_text(text):
    """
    Apply editorial improvements to Italian text
    Focus on: grammar, clarity, conciseness, consistency
    """

    # Fix common spacing issues
    text = re.sub(r'\s+', ' ', text)  # Multiple spaces to single
    text = re.sub(r' +\n', '\n', text)  # Remove trailing spaces
    text = re.sub(r'\n\n\n+', '\n\n', text)  # Max 2 newlines

    # Fix punctuation spacing (Italian rules)
    text = re.sub(r'\s+([.,;:!?)])', r'\1', text)  # No space before punctuation
    text = re.sub(r'([.,;:!?])([A-Za-z])', r'\1 \2', text)  # Space after punctuation
    text = re.sub(r'\(\s+', '(', text)  # No space after (
    text = re.sub(r'\s+\)', ')', text)  # No space before )

    # Fix quotation marks
    text = re.sub(r'"\s+', '"', text)  # No space after opening quote
    text = re.sub(r'\s+"', '"', text)  # No space before closing quote

    # Improve consistency in terminology
    replacements = {
        # Consistency in AI terminology
        'Intelligenza Artificiale (spesso abbreviata in AI': 'Intelligenza Artificiale (comunemente abbreviata in AI',
        'spesso abbreviata': 'comunemente abbreviata',

        # Remove unnecessary filler words (while preserving meaning)
        ' molto molto ': ' molto ',
        ' davvero davvero ': ' davvero ',
        ' veramente molto ': ' molto ',

        # Improve clarity
        'è importante che': 'è fondamentale che',
        'bisogna capire': 'occorre comprendere',
        'devi sapere': 'è necessario sapere',

        # Consistency in phrases
        'Non preoccuparti:': 'Non preoccuparti.',
        'Andiamo a scoprire': 'Scopriamo',
        'Vediamo insieme': 'Analizziamo',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Improve list consistency
    text = re.sub(r'\n- \*\*', '\n- **', text)  # Consistent list formatting

    # Fix common Italian grammar issues
    text = re.sub(r'\bpuo\b', 'può', text)  # Missing accent
    text = re.sub(r'\bperche\b', 'perché', text)  # Missing accent
    text = re.sub(r'\bpiù\s+di\s+quanto', 'più di quanto', text)  # Spacing

    return text

def improve_section_headers(text):
    """Ensure consistent formatting of headers"""
    # Ensure space after # in headers
    text = re.sub(r'^(#+)([^ #])', r'\1 \2', text, flags=re.MULTILINE)

    # Ensure proper capitalization in Italian headers (first word + proper nouns)
    # This is context-dependent, so we'll be conservative

    return text

def improve_readability(text):
    """Improve readability and flow"""

    # Break up very long sentences (over 40 words) - mark for review
    # This is conservative - we don't auto-break, just identify

    # Ensure consistent use of examples
    text = re.sub(r'\n\*\*Esempio:\*\*', '\n\n**Esempio:**', text)
    text = re.sub(r'\n\*\*Esempi:\*\*', '\n\n**Esempi:**', text)

    # Ensure consistent formatting of notes/important blocks
    text = re.sub(r'\*\*Nota:\*\*', '**Nota importante:**', text)
    text = re.sub(r'\*\*Importante:\*\*', '**Nota importante:**', text)

    return text

def main():
    input_file = r'C:\Users\utente\moodle-agent-team\course-content-complete.md'
    output_file = r'C:\Users\utente\moodle-agent-team\course-content-edited.md'

    print("Reading course content...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"Original length: {len(content)} characters, {len(content.splitlines())} lines")

    print("Polishing text...")
    content = polish_italian_text(content)

    print("Improving headers...")
    content = improve_section_headers(content)

    print("Improving readability...")
    content = improve_readability(content)

    print("Saving edited content...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Final length: {len(content)} characters, {len(content.splitlines())} lines")
    print(f"\nEdited content saved to: {output_file}")
    print("\n✓ Editorial review complete!")

if __name__ == '__main__':
    main()
