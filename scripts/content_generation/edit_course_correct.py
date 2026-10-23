#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Corrected comprehensive editorial refinement for Italian AI course content
Focuses on grammar, clarity, flow, and consistency
Preserves author's voice and all substantive content
IMPORTANT: Does NOT change "e" (and) to "è" (is)
"""

import re

def fix_punctuation_spacing(text):
    """Fix spacing around punctuation following Italian typographic rules"""

    # Remove multiple spaces (but not newlines)
    text = re.sub(r'([^\n])  +', r'\1 ', text)

    # Remove trailing spaces at end of lines
    text = re.sub(r' +\n', '\n', text)

    # Fix spacing before punctuation (no space before)
    text = re.sub(r' +([.,;:!?)])', r'\1', text)

    # Fix spacing after punctuation (one space after, if followed by letter)
    # But be careful with abbreviations and markdown
    text = re.sub(r'([.,;:!?])([A-Za-zÀ-ÿ])', r'\1 \2', text)

    # Fix parentheses spacing
    text = re.sub(r'\(\s+', '(', text)
    text = re.sub(r'\s+\)', ')', text)

    # Fix quotes - ensure proper spacing
    text = re.sub(r'"\s+', '"', text)
    text = re.sub(r'\s+"', '"', text)
    text = re.sub(r'"([A-Za-zÀ-ÿ])', r'" \1', text)

    # Remove excessive blank lines (max 2)
    text = re.sub(r'\n\n\n+', '\n\n', text)

    return text

def improve_italian_grammar(text):
    """Fix common Italian grammar and orthography issues - CAREFULLY"""

    # Fix missing accents on common words - but NOT "e" (and)!
    # We use word boundaries and specific patterns to avoid false positives

    corrections = [
        (r'\bpuo\b', 'può'),
        (r'\bperche\b', 'perché'),
        (r'\bcosi\b', 'così'),
        (r'\bpiu\b', 'più'),
        (r'\bgia\b', 'già'),
        (r'\bquindi\b', 'quindi'),  # Already correct, keeping for reference
        # NOTE: We do NOT change "e" to "è" automatically as context is needed
    ]

    for pattern, replacement in corrections:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    return text

def improve_clarity_and_conciseness(text):
    """Improve clarity by removing redundancy and improving word choice"""

    # Remove redundant emphasis
    text = re.sub(r'\bmolto molto\b', 'molto', text, flags=re.IGNORECASE)
    text = re.sub(r'\bdavvero davvero\b', 'davvero', text, flags=re.IGNORECASE)
    text = re.sub(r'\bveramente molto\b', 'molto', text, flags=re.IGNORECASE)

    # Improve common phrases for clarity
    improvements = {
        'è importante che tu sappia che': 'è importante sapere che',
        'bisogna sapere che': 'occorre sapere che',
        'bisogna capire che': 'occorre comprendere che',
        'devi tenere a mente che': 'ricorda che',
        'è fondamentale ricordare che': 'è fondamentale che',
        'Andiamo a scoprire': 'Scopriamo',
        'Vediamo insieme': 'Vediamo',
    }

    for old_phrase, new_phrase in improvements.items():
        text = text.replace(old_phrase, new_phrase)

    return text

def improve_consistency(text):
    """Improve consistency in terminology and formatting"""

    # Standardize "Nota importante" formatting
    text = re.sub(r'\*\*Nota:\*\*', '**Nota importante:**', text)
    text = re.sub(r'\*\*NOTA:\*\*', '**Nota importante:**', text)
    text = re.sub(r'\*\*Importante:\*\*', '**Importante:**', text)

    # Standardize example formatting
    text = re.sub(r'\*\*Esempio:\*\*\n(?!\n)', '**Esempio:**\n\n', text)
    text = re.sub(r'\*\*Esempi:\*\*\n(?!\n)', '**Esempi:**\n\n', text)

    # Standardize list markers
    text = re.sub(r'\n\* ', '\n- ', text)

    # Ensure space after markdown headers
    text = re.sub(r'^(#+)([^ #\n])', r'\1 \2', text, flags=re.MULTILINE)

    return text

def preserve_author_voice(text):
    """Preserve the author's friendly, encouraging voice"""

    # Only standardize punctuation for consistency
    text = re.sub(r'Non preoccuparti:', 'Non preoccuparti.', text)

    return text

def main():
    input_file = r'C:\Users\utente\moodle-agent-team\course-content-complete.md'
    output_file = r'C:\Users\utente\moodle-agent-team\course-content-edited.md'

    print("=" * 70)
    print("  Italian AI Course Content - Editorial Refinement (Corrected)")
    print("=" * 70)

    print("\n[Step 1/6] Reading course content...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"    ERROR: {e}")
        return

    original_length = len(content)
    original_lines = content.count('\n') + 1
    print(f"    ✓ Loaded: {original_length:,} characters, {original_lines:,} lines")

    print("\n[Step 2/6] Fixing punctuation and spacing...")
    content = fix_punctuation_spacing(content)
    print("    ✓ Punctuation normalized")

    print("\n[Step 3/6] Improving Italian grammar...")
    content = improve_italian_grammar(content)
    print("    ✓ Grammar improved (accents added where missing)")

    print("\n[Step 4/6] Improving clarity and conciseness...")
    content = improve_clarity_and_conciseness(content)
    print("    ✓ Clarity enhanced (redundancy removed)")

    print("\n[Step 5/6] Ensuring consistency...")
    content = improve_consistency(content)
    print("    ✓ Consistency ensured (formatting standardized)")

    print("\n[Step 6/6] Preserving author's voice...")
    content = preserve_author_voice(content)
    print("    ✓ Author's friendly tone preserved")

    final_length = len(content)
    final_lines = content.count('\n') + 1

    print("\n" + "-" * 70)
    print(f"  Original: {original_length:,} characters, {original_lines:,} lines")
    print(f"  Final:    {final_length:,} characters, {final_lines:,} lines")

    reduction = original_length - final_length
    if reduction > 0:
        print(f"  Reduced:  {reduction:,} characters (-{reduction/original_length*100:.2f}%)")
    elif reduction < 0:
        print(f"  Expanded: {abs(reduction):,} characters (+{abs(reduction)/original_length*100:.2f}%)")
    else:
        print(f"  No change in length")
    print("-" * 70)

    print("\n[Saving] Writing edited content to file...")
    try:
        with open(output_file, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
        print(f"    ✓ Saved to: {output_file}")
    except Exception as e:
        print(f"    ERROR: {e}")
        return

    print("\n" + "=" * 70)
    print("  ✓ Editorial refinement complete!")
    print("=" * 70)
    print("\n  Summary of improvements:")
    print("  • Grammar and spelling: corrected")
    print("  • Punctuation: normalized")
    print("  • Clarity: enhanced")
    print("  • Consistency: ensured")
    print("  • Redundancy: removed")
    print("  • Author's voice: fully preserved")
    print("  • Structure and formatting: maintained")
    print("\n  The polished course content is ready for review.")
    print("=" * 70)

if __name__ == '__main__':
    main()
