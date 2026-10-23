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

    # Fix spacing around punctuation (but preserve line breaks)
    text = re.sub(r'  +', ' ', text)  # Multiple spaces to single (not newlines)
    text = re.sub(r' +\n', '\n', text)  # Remove trailing spaces before newlines
    text = re.sub(r'\n\n\n+', '\n\n', text)  # Max 2 consecutive newlines

    # Fix punctuation spacing (Italian rules) - careful not to affect markdown
    text = re.sub(r' +([.,;:!?)])', r'\1', text)  # No space before punctuation
    text = re.sub(r'([.,;:!?])([A-Za-zÀ-ÿ])', r'\1 \2', text)  # Space after punctuation

    # Fix quotation marks spacing
    text = re.sub(r'"\s+', '"', text)
    text = re.sub(r'\s+"', '"', text)

    # Improve specific phrases for clarity and conciseness
    improvements = {
        'è importante notare che': 'è importante considerare che',
        'bisogna sapere che': 'occorre sapere che',
        'devi tenere a mente che': 'ricorda che',
        'è fondamentale ricordare che': 'è fondamentale che',
        'Non preoccuparti:': 'Non preoccuparti.',
        'Non preoccuparti se': 'Non preoccuparti:',
        'Andiamo a scoprire': 'Scopriamo',
        'Vediamo insieme': 'Vediamo',
    }

    for old, new in improvements.items():
        text = text.replace(old, new)

    # Fix common typos and missing accents
    text = re.sub(r'\bpuo\b', 'può', text)
    text = re.sub(r'\bperche\b', 'perché', text)
    text = re.sub(r'\bcosi\b', 'così', text)
    text = re.sub(r'\bpiu\b', 'più', text)

    return text

def improve_structure(text):
    """Improve document structure and formatting"""

    # Ensure space after # in headers
    text = re.sub(r'^(#+)([^ #\n])', r'\1 \2', text, flags=re.MULTILINE)

    # Standardize "Note important" formatting
    text = re.sub(r'\*\*Nota:\*\*', '**Nota importante:**', text)
    text = re.sub(r'\*\*Importante:\*\*', '**Importante:**', text)
    text = re.sub(r'\*\*IMPORTANTE:\*\*', '**Importante:**', text)

    # Ensure consistent example formatting
    text = re.sub(r'\*\*Esempio:\*\*\s*\n', '**Esempio:**\n\n', text)
    text = re.sub(r'\*\*Esempi:\*\*\s*\n', '**Esempi:**\n\n', text)

    # Improve consistency in list formatting
    text = re.sub(r'\n- \*\*', '\n- **', text)
    text = re.sub(r'\n\* \*\*', '\n- **', text)

    return text

def improve_clarity(text):
    """Improve clarity and remove redundancy"""

    # Remove double emphasis (very very -> very)
    text = re.sub(r'\bmolto molto\b', 'molto', text)
    text = re.sub(r'\bdavvero davvero\b', 'davvero', text)
    text = re.sub(r'\bveramente molto\b', 'molto', text)

    # Improve clarity of common phrases
    clarity_improvements = {
        'è importante che tu sappia che': 'è importante sapere che',
        'devi sapere che': 'ricorda che',
        'bisogna capire che': 'occorre comprendere che',
        'è necessario comprendere che': 'è fondamentale comprendere che',
    }

    for old, new in clarity_improvements.items():
        text = text.replace(old, new)

    return text

def main():
    input_file = r'C:\Users\utente\moodle-agent-team\course-content-complete.md'
    output_file = r'C:\Users\utente\moodle-agent-team\course-content-edited.md'

    print("Reading course content...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_lines = content.count('\n')
    print(f"Original: {len(content)} characters, {original_lines} lines")

    print("Applying editorial improvements...")
    content = polish_italian_text(content)
    content = improve_structure(content)
    content = improve_clarity(content)

    final_lines = content.count('\n')
    print(f"Final: {len(content)} characters, {final_lines} lines")

    print("Saving edited content...")
    with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)

    print(f"\nEdited content saved to: {output_file}")
    print("Editorial review complete!")

if __name__ == '__main__':
    main()
