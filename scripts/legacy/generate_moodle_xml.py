#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Moodle XML Course Backup Generator
Converts markdown course content to Moodle-compatible XML backup format
"""

import re
import html
import hashlib
import time
from datetime import datetime
from xml.sax.saxutils import escape
import markdown2

class MoodleXMLGenerator:
    def __init__(self, course_name, short_name, category, summary):
        self.course_name = course_name
        self.short_name = short_name
        self.category = category
        self.summary = summary
        self.activity_id = 1
        self.section_id = 1
        self.module_id = 1
        self.timestamp = int(time.time())
        self.activities = []
        self.sections = []

    def generate_id(self):
        """Generate unique activity ID"""
        current_id = self.activity_id
        self.activity_id += 1
        return current_id

    def generate_module_id(self):
        """Generate unique module ID"""
        current_id = self.module_id
        self.module_id += 1
        return current_id

    def markdown_to_html(self, md_content):
        """Convert markdown to HTML"""
        if not md_content:
            return ""
        # Convert markdown to HTML
        html_content = markdown2.markdown(md_content, extras=[
            "fenced-code-blocks",
            "tables",
            "break-on-newline",
            "code-friendly"
        ])
        return html_content

    def escape_xml(self, text):
        """Escape special XML characters"""
        if not text:
            return ""
        # First escape basic XML entities
        text = escape(text)
        return text

    def create_cdata(self, content):
        """Wrap content in CDATA section"""
        if not content:
            return "<![CDATA[]]>"
        # Escape any existing CDATA end sequences
        content = content.replace("]]>", "]]]]><![CDATA[>")
        return f"<![CDATA[{content}]]>"

    def create_page_activity(self, name, content, section_num):
        """Create a page activity"""
        activity_id = self.generate_id()
        module_id = self.generate_module_id()

        html_content = self.markdown_to_html(content)

        activity = {
            'type': 'page',
            'id': activity_id,
            'moduleid': module_id,
            'name': name,
            'content': html_content,
            'section': section_num
        }

        self.activities.append(activity)
        return activity_id, module_id

    def create_quiz_activity(self, name, questions, section_num):
        """Create a quiz activity"""
        activity_id = self.generate_id()
        module_id = self.generate_module_id()

        activity = {
            'type': 'quiz',
            'id': activity_id,
            'moduleid': module_id,
            'name': name,
            'questions': questions,
            'section': section_num
        }

        self.activities.append(activity)
        return activity_id, module_id

    def create_forum_activity(self, name, intro, section_num):
        """Create a forum activity"""
        activity_id = self.generate_id()
        module_id = self.generate_module_id()

        html_intro = self.markdown_to_html(intro)

        activity = {
            'type': 'forum',
            'id': activity_id,
            'moduleid': module_id,
            'name': name,
            'intro': html_intro,
            'section': section_num
        }

        self.activities.append(activity)
        return activity_id, module_id

    def create_assignment_activity(self, name, instructions, section_num):
        """Create an assignment activity"""
        activity_id = self.generate_id()
        module_id = self.generate_module_id()

        html_instructions = self.markdown_to_html(instructions)

        activity = {
            'type': 'assign',
            'id': activity_id,
            'moduleid': module_id,
            'name': name,
            'intro': html_instructions,
            'section': section_num
        }

        self.activities.append(activity)
        return activity_id, module_id

    def create_label_activity(self, content, section_num):
        """Create a label resource"""
        activity_id = self.generate_id()
        module_id = self.generate_module_id()

        html_content = self.markdown_to_html(content)

        activity = {
            'type': 'label',
            'id': activity_id,
            'moduleid': module_id,
            'intro': html_content,
            'section': section_num
        }

        self.activities.append(activity)
        return activity_id, module_id

    def generate_moodle_backup_xml(self):
        """Generate complete Moodle backup XML"""

        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<moodle_backup>\n'
        xml += '  <information>\n'
        xml += f'    <name>{self.escape_xml(self.course_name)}</name>\n'
        xml += f'    <moodle_version>2023100900</moodle_version>\n'
        xml += f'    <moodle_release>4.3</moodle_release>\n'
        xml += f'    <backup_version>2023100900</backup_version>\n'
        xml += f'    <backup_release>4.3</backup_release>\n'
        xml += f'    <backup_date>{self.timestamp}</backup_date>\n'
        xml += f'    <mnet_remoteusers>0</mnet_remoteusers>\n'
        xml += f'    <include_files>1</include_files>\n'
        xml += f'    <include_file_references_to_external_content>0</include_file_references_to_external_content>\n'
        xml += f'    <original_wwwroot>https://moodle.example.com</original_wwwroot>\n'
        xml += f'    <original_site_identifier_hash>generated_{hashlib.md5(str(self.timestamp).encode()).hexdigest()}</original_site_identifier_hash>\n'
        xml += f'    <original_course_id>1</original_course_id>\n'
        xml += f'    <original_course_fullname>{self.escape_xml(self.course_name)}</original_course_fullname>\n'
        xml += f'    <original_course_shortname>{self.escape_xml(self.short_name)}</original_course_shortname>\n'
        xml += f'    <original_course_startdate>{self.timestamp}</original_course_startdate>\n'
        xml += f'    <original_course_enddate>0</original_course_enddate>\n'
        xml += f'    <original_course_contextid>2</original_course_contextid>\n'
        xml += f'    <original_system_contextid>1</original_system_contextid>\n'
        xml += '    <type>course</type>\n'
        xml += '    <format>topics</format>\n'
        xml += '    <interactive>1</interactive>\n'
        xml += '    <mode>10</mode>\n'
        xml += '    <execution>1</execution>\n'
        xml += '    <executiontime>0</executiontime>\n'
        xml += '  </information>\n'

        # Details section
        xml += '  <details>\n'
        xml += '    <detail backup_id="' + hashlib.md5(str(self.timestamp).encode()).hexdigest() + '" type="course" format="topics" interactive="1" mode="10" execution="1" executiontime="0">\n'
        xml += '      <activities>\n'

        # Add all activities
        for activity in self.activities:
            xml += f'        <activity moduleid="{activity["moduleid"]}" sectionid="{activity["section"]}" modulename="{activity["type"]}" title="{self.escape_xml(activity["name"] if "name" in activity else "Label")}" directory="activities/{activity["type"]}_{activity["id"]}">\n'
            xml += '        </activity>\n'

        xml += '      </activities>\n'
        xml += '      <sections>\n'

        # Add sections
        for i in range(11):  # Section 0 (general) + 10 topic sections
            section_title = f"Modulo {i}" if i > 0 else "Generale"
            xml += f'        <section sectionid="{i}" title="{section_title}" directory="sections/section_{i}">\n'
            xml += '        </section>\n'

        xml += '      </sections>\n'
        xml += '      <course courseid="1" contextid="2" directory="course">\n'
        xml += '      </course>\n'
        xml += '    </detail>\n'
        xml += '  </details>\n'

        # Contents section
        xml += '  <contents>\n'
        xml += '    <activities>\n'

        for activity in self.activities:
            xml += f'      <activity moduleid="{activity["moduleid"]}" sectionid="{activity["section"]}" modulename="{activity["type"]}" directory="activities/{activity["type"]}_{activity["id"]}">\n'
            xml += f'        <title>{self.escape_xml(activity.get("name", "Label"))}</title>\n'
            xml += '      </activity>\n'

        xml += '    </activities>\n'
        xml += '    <sections>\n'

        for i in range(11):
            section_title = f"Modulo {i}" if i > 0 else "Generale"
            xml += f'      <section sectionid="{i}" directory="sections/section_{i}">\n'
            xml += f'        <title>{section_title}</title>\n'
            xml += '      </section>\n'

        xml += '    </sections>\n'
        xml += '    <course courseid="1" contextid="2" directory="course">\n'
        xml += f'      <shortname>{self.escape_xml(self.short_name)}</shortname>\n'
        xml += f'      <fullname>{self.escape_xml(self.course_name)}</fullname>\n'
        xml += f'      <category>{self.escape_xml(self.category)}</category>\n'
        xml += f'      <summary>{self.create_cdata(self.summary)}</summary>\n'
        xml += '    </course>\n'
        xml += '  </contents>\n'

        xml += '</moodle_backup>\n'

        return xml

    def generate_course_xml(self):
        """Generate the course/course.xml file"""
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<course id="1" contextid="2">\n'
        xml += f'  <shortname>{self.escape_xml(self.short_name)}</shortname>\n'
        xml += f'  <fullname>{self.escape_xml(self.course_name)}</fullname>\n'
        xml += f'  <idnumber></idnumber>\n'
        xml += f'  <summary>{self.create_cdata(self.summary)}</summary>\n'
        xml += f'  <summaryformat>1</summaryformat>\n'
        xml += f'  <format>topics</format>\n'
        xml += f'  <showgrades>1</showgrades>\n'
        xml += f'  <newsitems>5</newsitems>\n'
        xml += f'  <startdate>{self.timestamp}</startdate>\n'
        xml += f'  <enddate>0</enddate>\n'
        xml += f'  <marker>0</marker>\n'
        xml += f'  <maxbytes>0</maxbytes>\n'
        xml += f'  <legacyfiles>0</legacyfiles>\n'
        xml += f'  <showreports>0</showreports>\n'
        xml += f'  <visible>1</visible>\n'
        xml += f'  <groupmode>0</groupmode>\n'
        xml += f'  <groupmodeforce>0</groupmodeforce>\n'
        xml += f'  <defaultgroupingid>0</defaultgroupingid>\n'
        xml += f'  <lang></lang>\n'
        xml += f'  <theme></theme>\n'
        xml += f'  <timecreated>{self.timestamp}</timecreated>\n'
        xml += f'  <timemodified>{self.timestamp}</timemodified>\n'
        xml += f'  <requested>0</requested>\n'
        xml += f'  <enablecompletion>1</enablecompletion>\n'
        xml += f'  <completionnotify>0</completionnotify>\n'
        xml += f'  <hiddensections>0</hiddensections>\n'
        xml += f'  <coursedisplay>0</coursedisplay>\n'
        xml += f'  <category id="1" name="{self.escape_xml(self.category)}" />\n'
        xml += '</course>\n'

        return xml


def parse_course_content(file_path):
    """Parse the markdown course content file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by module sections
    modules = []

    # Find all module headers
    module_pattern = r'^# Modulo (\d+): (.+)$'

    current_module = None
    current_content = []

    lines = content.split('\n')

    for line in lines:
        match = re.match(module_pattern, line)
        if match:
            # Save previous module
            if current_module:
                modules.append({
                    'number': current_module['number'],
                    'title': current_module['title'],
                    'content': '\n'.join(current_content)
                })

            # Start new module
            current_module = {
                'number': int(match.group(1)),
                'title': match.group(2)
            }
            current_content = [line]
        else:
            if current_module:
                current_content.append(line)

    # Don't forget the last module
    if current_module:
        modules.append({
            'number': current_module['number'],
            'title': current_module['title'],
            'content': '\n'.join(current_content)
        })

    return modules


def extract_activities_from_module(module_content):
    """Extract different types of activities from module content"""
    activities = {
        'pages': [],
        'quizzes': [],
        'forums': [],
        'assignments': [],
        'labels': []
    }

    # Split content into sections
    sections = re.split(r'^## ', module_content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        # Check if it's an activity section
        if 'Attività' in section or 'Quiz' in section:
            # Extract quiz activities
            if 'Quiz' in section:
                quiz_match = re.search(r'^(.+?)\n', section)
                if quiz_match:
                    quiz_title = quiz_match.group(1).strip()
                    activities['quizzes'].append({
                        'name': quiz_title,
                        'content': section
                    })
            # Extract discussion/forum activities
            elif 'Discussione' in section or 'Forum' in section:
                forum_match = re.search(r'^(.+?)\n', section)
                if forum_match:
                    forum_title = forum_match.group(1).strip()
                    activities['forums'].append({
                        'name': forum_title,
                        'content': section
                    })
            # Extract assignment activities
            elif 'Esercizio' in section or 'Progetto' in section or 'Case Study' in section or 'Lab' in section:
                assign_match = re.search(r'^(.+?)\n', section)
                if assign_match:
                    assign_title = assign_match.group(1).strip()
                    activities['assignments'].append({
                        'name': assign_title,
                        'content': section
                    })
        elif 'Introduzione al Modulo' in section:
            # Module introduction as label
            activities['labels'].append({
                'content': section
            })
        elif 'Riepilogo' in section:
            # Summary as page
            page_match = re.search(r'^(.+?)\n', section)
            if page_match:
                page_title = page_match.group(1).strip()
                activities['pages'].append({
                    'name': page_title,
                    'content': section
                })
        else:
            # Regular content sections as pages
            page_match = re.search(r'^(.+?)\n', section)
            if page_match:
                page_title = page_match.group(1).strip()
                # Skip if title is too short or looks like a fragment
                if len(page_title) > 3 and not page_title.startswith('#'):
                    activities['pages'].append({
                        'name': page_title,
                        'content': section
                    })

    return activities


def main():
    """Main function to generate Moodle XML"""

    # Course information
    course_info = {
        'name': 'Introduzione all\'Intelligenza Artificiale per Principianti',
        'short_name': 'AI-Principianti',
        'category': 'Technology / AI',
        'summary': 'Corso introduttivo all\'intelligenza artificiale per principianti. Impara le nozioni base dell\'AI per farne un uso razionale ed efficiente.'
    }

    # Initialize generator
    generator = MoodleXMLGenerator(
        course_info['name'],
        course_info['short_name'],
        course_info['category'],
        course_info['summary']
    )

    # Parse course content
    print("Parsing course content...")
    input_file = r'C:\Users\utente\moodle-agent-team\course-content-edited.md'
    modules = parse_course_content(input_file)

    print(f"Found {len(modules)} modules")

    # Process each module
    for module in modules:
        section_num = module['number']
        print(f"\nProcessing Module {section_num}: {module['title']}")

        # Extract activities from module content
        activities = extract_activities_from_module(module['content'])

        # Create label for module introduction
        if activities['labels']:
            for label in activities['labels']:
                generator.create_label_activity(label['content'], section_num)
                print(f"  - Created label (introduction)")

        # Create page activities
        for page in activities['pages']:
            generator.create_page_activity(page['name'], page['content'], section_num)
            print(f"  - Created page: {page['name'][:50]}...")

        # Create quiz activities
        for quiz in activities['quizzes']:
            generator.create_quiz_activity(quiz['name'], quiz['content'], section_num)
            print(f"  - Created quiz: {quiz['name'][:50]}...")

        # Create forum activities
        for forum in activities['forums']:
            generator.create_forum_activity(forum['name'], forum['content'], section_num)
            print(f"  - Created forum: {forum['name'][:50]}...")

        # Create assignment activities
        for assignment in activities['assignments']:
            generator.create_assignment_activity(assignment['name'], assignment['content'], section_num)
            print(f"  - Created assignment: {assignment['name'][:50]}...")

    # Generate XML files
    print("\n\nGenerating Moodle XML files...")

    # Generate main backup XML
    moodle_backup_xml = generator.generate_moodle_backup_xml()

    # Write to file
    output_file = r'C:\Users\utente\moodle-agent-team\moodle-backup.xml'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(moodle_backup_xml)

    print(f"\n[OK] Moodle backup XML generated: {output_file}")

    # Generate course.xml
    course_xml = generator.generate_course_xml()
    course_xml_file = r'C:\Users\utente\moodle-agent-team\moodle-course.xml'
    with open(course_xml_file, 'w', encoding='utf-8') as f:
        f.write(course_xml)

    print(f"[OK] Course XML generated: {course_xml_file}")

    # Statistics
    print(f"\n{'='*60}")
    print(f"GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Course: {course_info['name']}")
    print(f"Short name: {course_info['short_name']}")
    print(f"Modules: {len(modules)}")
    print(f"Total activities created: {len(generator.activities)}")

    # Count by type
    activity_types = {}
    for activity in generator.activities:
        atype = activity['type']
        activity_types[atype] = activity_types.get(atype, 0) + 1

    print(f"\nActivities by type:")
    for atype, count in sorted(activity_types.items()):
        print(f"  - {atype}: {count}")

    print(f"\n{'='*60}")

    return output_file, course_xml_file, len(modules), len(generator.activities), activity_types


if __name__ == '__main__':
    main()
