#!/usr/bin/env python3
"""
Fix Moodle backup by adding missing essential XML files
"""

import os
import zipfile
import tempfile
import shutil

def create_missing_xml_files(extract_dir):
    """Create missing XML files required by Moodle"""

    # files.xml - Required for file management
    files_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<files>
</files>'''

    # roles.xml - Required for role definitions
    roles_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<roles>
  <role_overrides>
  </role_overrides>
  <role_assignments>
  </role_assignments>
</roles>'''

    # scales.xml - Required for grading scales
    scales_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<scales_definition>
</scales_definition>'''

    # outcomes.xml - Required for learning outcomes
    outcomes_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<outcomes_definition>
</outcomes_definition>'''

    # questions.xml - Required for question bank
    questions_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<question_categories>
</question_categories>'''

    # gradebook.xml - Required for gradebook
    gradebook_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<gradebook>
  <attributes>
    <grade_categories>
    </grade_categories>
    <grade_items>
    </grade_items>
    <grade_letters>
    </grade_letters>
    <grade_settings>
    </grade_settings>
  </attributes>
</gradebook>'''

    # completion.xml - For activity completion
    completion_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<course_completion>
  <enabled>1</enabled>
  <completions>
  </completions>
</course_completion>'''

    # groups.xml - For group management
    groups_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<groups>
  <groupings>
  </groupings>
</groups>'''

    # Write all files
    with open(os.path.join(extract_dir, 'files.xml'), 'w', encoding='utf-8') as f:
        f.write(files_xml)

    with open(os.path.join(extract_dir, 'roles.xml'), 'w', encoding='utf-8') as f:
        f.write(roles_xml)

    with open(os.path.join(extract_dir, 'scales.xml'), 'w', encoding='utf-8') as f:
        f.write(scales_xml)

    with open(os.path.join(extract_dir, 'outcomes.xml'), 'w', encoding='utf-8') as f:
        f.write(outcomes_xml)

    with open(os.path.join(extract_dir, 'questions.xml'), 'w', encoding='utf-8') as f:
        f.write(questions_xml)

    with open(os.path.join(extract_dir, 'gradebook.xml'), 'w', encoding='utf-8') as f:
        f.write(gradebook_xml)

    with open(os.path.join(extract_dir, 'completion.xml'), 'w', encoding='utf-8') as f:
        f.write(completion_xml)

    with open(os.path.join(extract_dir, 'groups.xml'), 'w', encoding='utf-8') as f:
        f.write(groups_xml)

    print("[OK] Created missing XML files")

def fix_backup(input_mbz, output_mbz):
    """Fix the Moodle backup by adding missing files"""

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        extract_dir = os.path.join(temp_dir, 'backup')
        os.makedirs(extract_dir)

        # Extract existing backup
        print(f"Extracting {input_mbz}...")
        with zipfile.ZipFile(input_mbz, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        # Add missing files
        print("Adding missing XML files...")
        create_missing_xml_files(extract_dir)

        # Create new backup
        print(f"Creating fixed backup: {output_mbz}...")
        with zipfile.ZipFile(output_mbz, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(extract_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, extract_dir)
                    zipf.write(file_path, arcname)

        print(f"[OK] Fixed backup created: {output_mbz}")
        print(f"[OK] File size: {os.path.getsize(output_mbz) / 1024:.1f} KB")

if __name__ == '__main__':
    input_file = 'AI-Principianti-backup.mbz'
    output_file = 'AI-Principianti-FIXED.mbz'

    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found")
        exit(1)

    fix_backup(input_file, output_file)
    print("\n[OK] Done! Use AI-Principianti-FIXED.mbz to import into Moodle")
