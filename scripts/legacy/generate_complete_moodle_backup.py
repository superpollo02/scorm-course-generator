#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete Moodle Backup Package Generator
Creates a full Moodle backup structure with all necessary XML files
"""

import os
import re
import html
import hashlib
import time
import zipfile
from datetime import datetime
from xml.sax.saxutils import escape
import markdown2

class CompleteMoodleBackup:
    def __init__(self, course_name, short_name, category, summary, output_dir):
        self.course_name = course_name
        self.short_name = short_name
        self.category = category
        self.summary = summary
        self.output_dir = output_dir
        self.activity_id = 1
        self.section_id = 0
        self.module_id = 1
        self.timestamp = int(time.time())
        self.backup_id = hashlib.md5(str(self.timestamp).encode()).hexdigest()
        self.activities = []
        self.sections_data = {}

        # Create output directory structure
        self.setup_directories()

    def setup_directories(self):
        """Create directory structure for Moodle backup"""
        dirs = [
            self.output_dir,
            os.path.join(self.output_dir, 'activities'),
            os.path.join(self.output_dir, 'sections'),
            os.path.join(self.output_dir, 'course'),
        ]
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)

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
        return escape(text)

    def create_cdata(self, content):
        """Wrap content in CDATA section"""
        if not content:
            return "<![CDATA[]]>"
        content = content.replace("]]>", "]]]]><![CDATA[>")
        return f"<![CDATA[{content}]]>"

    def create_page_activity(self, name, content, section_num):
        """Create a page activity with XML file"""
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
        self.create_page_xml(activity)
        return activity_id, module_id

    def create_page_xml(self, activity):
        """Generate XML file for page activity"""
        activity_dir = os.path.join(self.output_dir, 'activities', f"page_{activity['id']}")
        os.makedirs(activity_dir, exist_ok=True)

        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<activity id="' + str(activity['id']) + '" moduleid="' + str(activity['moduleid']) + '" modulename="page" contextid="' + str(activity['id'] + 100) + '">\n'
        xml += '  <page id="' + str(activity['id']) + '">\n'
        xml += f'    <name>{self.escape_xml(activity["name"])}</name>\n'
        xml += f'    <intro>{self.create_cdata("")}</intro>\n'
        xml += f'    <introformat>1</introformat>\n'
        xml += f'    <content>{self.create_cdata(activity["content"])}</content>\n'
        xml += f'    <contentformat>1</contentformat>\n'
        xml += f'    <legacyfiles>0</legacyfiles>\n'
        xml += f'    <legacyfileslast>$@NULL@$</legacyfileslast>\n'
        xml += f'    <display>5</display>\n'
        xml += f'    <displayoptions>a:1:{{s:12:"printheading";s:1:"1";}}</displayoptions>\n'
        xml += f'    <revision>1</revision>\n'
        xml += f'    <timemodified>{self.timestamp}</timemodified>\n'
        xml += '  </page>\n'
        xml += '</activity>\n'

        with open(os.path.join(activity_dir, 'page.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

        # Create module.xml
        self.create_module_xml(activity_dir, activity)

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
        self.create_quiz_xml(activity)
        return activity_id, module_id

    def create_quiz_xml(self, activity):
        """Generate XML file for quiz activity"""
        activity_dir = os.path.join(self.output_dir, 'activities', f"quiz_{activity['id']}")
        os.makedirs(activity_dir, exist_ok=True)

        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<activity id="' + str(activity['id']) + '" moduleid="' + str(activity['moduleid']) + '" modulename="quiz" contextid="' + str(activity['id'] + 100) + '">\n'
        xml += '  <quiz id="' + str(activity['id']) + '">\n'
        xml += f'    <name>{self.escape_xml(activity["name"])}</name>\n'
        xml += f'    <intro>{self.create_cdata(self.markdown_to_html(activity["questions"]))}</intro>\n'
        xml += f'    <introformat>1</introformat>\n'
        xml += f'    <timeopen>0</timeopen>\n'
        xml += f'    <timeclose>0</timeclose>\n'
        xml += f'    <timelimit>0</timelimit>\n'
        xml += f'    <overduehandling>autosubmit</overduehandling>\n'
        xml += f'    <graceperiod>0</graceperiod>\n'
        xml += f'    <preferredbehaviour>deferredfeedback</preferredbehaviour>\n'
        xml += f'    <attempts>0</attempts>\n'
        xml += f'    <attemptonlast>0</attemptonlast>\n'
        xml += f'    <grademethod>1</grademethod>\n'
        xml += f'    <decimalpoints>2</decimalpoints>\n'
        xml += f'    <questiondecimalpoints>-1</questiondecimalpoints>\n'
        xml += f'    <reviewattempt>69888</reviewattempt>\n'
        xml += f'    <reviewcorrectness>69888</reviewcorrectness>\n'
        xml += f'    <reviewmarks>69888</reviewmarks>\n'
        xml += f'    <reviewspecificfeedback>69888</reviewspecificfeedback>\n'
        xml += f'    <reviewgeneralfeedback>69888</reviewgeneralfeedback>\n'
        xml += f'    <reviewrightanswer>69888</reviewrightanswer>\n'
        xml += f'    <reviewoverallfeedback>69888</reviewoverallfeedback>\n'
        xml += f'    <questionsperpage>1</questionsperpage>\n'
        xml += f'    <navmethod>free</navmethod>\n'
        xml += f'    <shuffleanswers>1</shuffleanswers>\n'
        xml += f'    <sumgrades>0</sumgrades>\n'
        xml += f'    <grade>10</grade>\n'
        xml += f'    <timecreated>{self.timestamp}</timecreated>\n'
        xml += f'    <timemodified>{self.timestamp}</timemodified>\n'
        xml += '  </quiz>\n'
        xml += '</activity>\n'

        with open(os.path.join(activity_dir, 'quiz.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

        self.create_module_xml(activity_dir, activity)

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
        self.create_forum_xml(activity)
        return activity_id, module_id

    def create_forum_xml(self, activity):
        """Generate XML file for forum activity"""
        activity_dir = os.path.join(self.output_dir, 'activities', f"forum_{activity['id']}")
        os.makedirs(activity_dir, exist_ok=True)

        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<activity id="' + str(activity['id']) + '" moduleid="' + str(activity['moduleid']) + '" modulename="forum" contextid="' + str(activity['id'] + 100) + '">\n'
        xml += '  <forum id="' + str(activity['id']) + '">\n'
        xml += f'    <type>general</type>\n'
        xml += f'    <name>{self.escape_xml(activity["name"])}</name>\n'
        xml += f'    <intro>{self.create_cdata(activity["intro"])}</intro>\n'
        xml += f'    <introformat>1</introformat>\n'
        xml += f'    <assessed>0</assessed>\n'
        xml += f'    <assesstimestart>0</assesstimestart>\n'
        xml += f'    <assesstimefinish>0</assesstimefinish>\n'
        xml += f'    <scale>0</scale>\n'
        xml += f'    <maxbytes>0</maxbytes>\n'
        xml += f'    <maxattachments>1</maxattachments>\n'
        xml += f'    <forcesubscribe>1</forcesubscribe>\n'
        xml += f'    <trackingtype>1</trackingtype>\n'
        xml += f'    <rsstype>0</rsstype>\n'
        xml += f'    <rssarticles>0</rssarticles>\n'
        xml += f'    <timemodified>{self.timestamp}</timemodified>\n'
        xml += f'    <warnafter>0</warnafter>\n'
        xml += f'    <blockafter>0</blockafter>\n'
        xml += f'    <blockperiod>0</blockperiod>\n'
        xml += f'    <completiondiscussions>0</completiondiscussions>\n'
        xml += f'    <completionreplies>0</completionreplies>\n'
        xml += f'    <completionposts>0</completionposts>\n'
        xml += '  </forum>\n'
        xml += '</activity>\n'

        with open(os.path.join(activity_dir, 'forum.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

        self.create_module_xml(activity_dir, activity)

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
        self.create_assignment_xml(activity)
        return activity_id, module_id

    def create_assignment_xml(self, activity):
        """Generate XML file for assignment activity"""
        activity_dir = os.path.join(self.output_dir, 'activities', f"assign_{activity['id']}")
        os.makedirs(activity_dir, exist_ok=True)

        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<activity id="' + str(activity['id']) + '" moduleid="' + str(activity['moduleid']) + '" modulename="assign" contextid="' + str(activity['id'] + 100) + '">\n'
        xml += '  <assign id="' + str(activity['id']) + '">\n'
        xml += f'    <name>{self.escape_xml(activity["name"])}</name>\n'
        xml += f'    <intro>{self.create_cdata(activity["intro"])}</intro>\n'
        xml += f'    <introformat>1</introformat>\n'
        xml += f'    <alwaysshowdescription>1</alwaysshowdescription>\n'
        xml += f'    <submissiondrafts>0</submissiondrafts>\n'
        xml += f'    <sendnotifications>0</sendnotifications>\n'
        xml += f'    <sendlatenotifications>0</sendlatenotifications>\n'
        xml += f'    <duedate>0</duedate>\n'
        xml += f'    <cutoffdate>0</cutoffdate>\n'
        xml += f'    <gradingduedate>0</gradingduedate>\n'
        xml += f'    <allowsubmissionsfromdate>0</allowsubmissionsfromdate>\n'
        xml += f'    <grade>100</grade>\n'
        xml += f'    <timemodified>{self.timestamp}</timemodified>\n'
        xml += f'    <requiresubmissionstatement>0</requiresubmissionstatement>\n'
        xml += f'    <completionsubmit>0</completionsubmit>\n'
        xml += f'    <teamsubmission>0</teamsubmission>\n'
        xml += f'    <requireallteammemberssubmit>0</requireallteammemberssubmit>\n'
        xml += f'    <teamsubmissiongroupingid>0</teamsubmissiongroupingid>\n'
        xml += f'    <blindmarking>0</blindmarking>\n'
        xml += f'    <hidegrader>0</hidegrader>\n'
        xml += f'    <revealidentities>0</revealidentities>\n'
        xml += f'    <attemptreopenmethod>none</attemptreopenmethod>\n'
        xml += f'    <maxattempts>-1</maxattempts>\n'
        xml += f'    <markingworkflow>0</markingworkflow>\n'
        xml += f'    <markingallocation>0</markingallocation>\n'
        xml += '  </assign>\n'
        xml += '</activity>\n'

        with open(os.path.join(activity_dir, 'assign.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

        self.create_module_xml(activity_dir, activity)

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
            'section': section_num,
            'name': 'Label'
        }

        self.activities.append(activity)
        self.create_label_xml(activity)
        return activity_id, module_id

    def create_label_xml(self, activity):
        """Generate XML file for label activity"""
        activity_dir = os.path.join(self.output_dir, 'activities', f"label_{activity['id']}")
        os.makedirs(activity_dir, exist_ok=True)

        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<activity id="' + str(activity['id']) + '" moduleid="' + str(activity['moduleid']) + '" modulename="label" contextid="' + str(activity['id'] + 100) + '">\n'
        xml += '  <label id="' + str(activity['id']) + '">\n'
        xml += f'    <name>Label</name>\n'
        xml += f'    <intro>{self.create_cdata(activity["intro"])}</intro>\n'
        xml += f'    <introformat>1</introformat>\n'
        xml += f'    <timemodified>{self.timestamp}</timemodified>\n'
        xml += '  </label>\n'
        xml += '</activity>\n'

        with open(os.path.join(activity_dir, 'label.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

        self.create_module_xml(activity_dir, activity)

    def create_module_xml(self, activity_dir, activity):
        """Create module.xml file for an activity"""
        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<module id="' + str(activity['moduleid']) + '" version="2023100900">\n'
        xml += f'  <modulename>{activity["type"]}</modulename>\n'
        xml += f'  <sectionid>{activity["section"]}</sectionid>\n'
        xml += f'  <sectionnumber>{activity["section"]}</sectionnumber>\n'
        xml += f'  <idnumber></idnumber>\n'
        xml += f'  <added>{self.timestamp}</added>\n'
        xml += f'  <score>0</score>\n'
        xml += f'  <indent>0</indent>\n'
        xml += f'  <visible>1</visible>\n'
        xml += f'  <visibleoncoursepage>1</visibleoncoursepage>\n'
        xml += f'  <visibleold>1</visibleold>\n'
        xml += f'  <groupmode>0</groupmode>\n'
        xml += f'  <groupingid>0</groupingid>\n'
        xml += f'  <completion>0</completion>\n'
        xml += f'  <completiongradeitemnumber>$@NULL@$</completiongradeitemnumber>\n'
        xml += f'  <completionview>0</completionview>\n'
        xml += f'  <completionexpected>0</completionexpected>\n'
        xml += f'  <availability>$@NULL@$</availability>\n'
        xml += f'  <showdescription>0</showdescription>\n'
        xml += '</module>\n'

        with open(os.path.join(activity_dir, 'module.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

    def create_section_xml(self, section_num, section_title, sequence):
        """Create section XML file"""
        section_dir = os.path.join(self.output_dir, 'sections', f'section_{section_num}')
        os.makedirs(section_dir, exist_ok=True)

        xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml += '<section id="' + str(section_num) + '">\n'
        xml += f'  <number>{section_num}</number>\n'
        xml += f'  <name>{self.escape_xml(section_title)}</name>\n'
        xml += f'  <summary>{self.create_cdata("")}</summary>\n'
        xml += f'  <summaryformat>1</summaryformat>\n'
        xml += f'  <sequence>{",".join(map(str, sequence))}</sequence>\n'
        xml += f'  <visible>1</visible>\n'
        xml += f'  <availabilityjson>$@NULL@$</availabilityjson>\n'
        xml += f'  <timemodified>{self.timestamp}</timemodified>\n'
        xml += '</section>\n'

        with open(os.path.join(section_dir, 'section.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

    def create_course_xml(self):
        """Create course.xml file"""
        course_dir = os.path.join(self.output_dir, 'course')

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
        xml += f'  <category id="1">\n'
        xml += f'    <name>{self.escape_xml(self.category)}</name>\n'
        xml += f'    <description>$@NULL@$</description>\n'
        xml += f'  </category>\n'
        xml += '</course>\n'

        with open(os.path.join(course_dir, 'course.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

    def create_moodle_backup_xml(self):
        """Create main moodle_backup.xml file"""
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
        xml += f'    <original_site_identifier_hash>generated_{self.backup_id}</original_site_identifier_hash>\n'
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
        xml += f'    <detail backup_id="{self.backup_id}" type="course" format="topics" interactive="1" mode="10" execution="1" executiontime="0">\n'
        xml += '      <activities>\n'

        for activity in self.activities:
            xml += f'        <activity moduleid="{activity["moduleid"]}" sectionid="{activity["section"]}" modulename="{activity["type"]}" title="{self.escape_xml(activity.get("name", "Label"))}" directory="activities/{activity["type"]}_{activity["id"]}">\n'
            xml += '        </activity>\n'

        xml += '      </activities>\n'
        xml += '      <sections>\n'

        for i in range(11):
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
        xml += '    </course>\n'
        xml += '  </contents>\n'

        xml += '</moodle_backup>\n'

        with open(os.path.join(self.output_dir, 'moodle_backup.xml'), 'w', encoding='utf-8') as f:
            f.write(xml)

    def finalize_backup(self):
        """Create section XMLs and finalize backup structure"""
        # Group activities by section
        sections = {}
        for activity in self.activities:
            section_num = activity['section']
            if section_num not in sections:
                sections[section_num] = []
            sections[section_num].append(activity['moduleid'])

        # Create section XMLs
        for i in range(11):
            section_title = f"Modulo {i}" if i > 0 else "Generale"
            sequence = sections.get(i, [])
            self.create_section_xml(i, section_title, sequence)

        # Create course XML
        self.create_course_xml()

        # Create main moodle_backup.xml
        self.create_moodle_backup_xml()


def parse_course_content(file_path):
    """Parse the markdown course content file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    modules = []
    module_pattern = r'^# Modulo (\d+): (.+)$'
    current_module = None
    current_content = []
    lines = content.split('\n')

    for line in lines:
        match = re.match(module_pattern, line)
        if match:
            if current_module:
                modules.append({
                    'number': current_module['number'],
                    'title': current_module['title'],
                    'content': '\n'.join(current_content)
                })
            current_module = {
                'number': int(match.group(1)),
                'title': match.group(2)
            }
            current_content = [line]
        else:
            if current_module:
                current_content.append(line)

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

    sections = re.split(r'^## ', module_content, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue

        if 'Attività' in section or 'Attivita' in section or 'Quiz' in section:
            if 'Quiz' in section:
                quiz_match = re.search(r'^(.+?)\n', section)
                if quiz_match:
                    quiz_title = quiz_match.group(1).strip()
                    activities['quizzes'].append({
                        'name': quiz_title,
                        'content': section
                    })
            elif 'Discussione' in section or 'Forum' in section or 'Progetto - Risolvi' in section:
                forum_match = re.search(r'^(.+?)\n', section)
                if forum_match:
                    forum_title = forum_match.group(1).strip()
                    activities['forums'].append({
                        'name': forum_title,
                        'content': section
                    })
            else:
                assign_match = re.search(r'^(.+?)\n', section)
                if assign_match:
                    assign_title = assign_match.group(1).strip()
                    activities['assignments'].append({
                        'name': assign_title,
                        'content': section
                    })
        elif 'Introduzione al Modulo' in section:
            activities['labels'].append({
                'content': section
            })
        elif 'Riepilogo' in section:
            page_match = re.search(r'^(.+?)\n', section)
            if page_match:
                page_title = page_match.group(1).strip()
                activities['pages'].append({
                    'name': page_title,
                    'content': section
                })
        else:
            page_match = re.search(r'^(.+?)\n', section)
            if page_match:
                page_title = page_match.group(1).strip()
                if len(page_title) > 3 and not page_title.startswith('#'):
                    activities['pages'].append({
                        'name': page_title,
                        'content': section
                    })

    return activities


def main():
    """Main function"""
    course_info = {
        'name': 'Introduzione all\'Intelligenza Artificiale per Principianti',
        'short_name': 'AI-Principianti',
        'category': 'Technology / AI',
        'summary': 'Corso introduttivo all\'intelligenza artificiale per principianti. Impara le nozioni base dell\'AI per farne un uso razionale ed efficiente.'
    }

    output_dir = r'C:\Users\utente\moodle-agent-team\moodle_backup'

    # Create backup generator
    backup = CompleteMoodleBackup(
        course_info['name'],
        course_info['short_name'],
        course_info['category'],
        course_info['summary'],
        output_dir
    )

    # Parse course content
    print("Parsing course content...")
    input_file = r'C:\Users\utente\moodle-agent-team\course-content-edited.md'
    modules = parse_course_content(input_file)
    print(f"Found {len(modules)} modules\n")

    # Process each module
    for module in modules:
        section_num = module['number']
        print(f"Processing Module {section_num}: {module['title']}")

        activities = extract_activities_from_module(module['content'])

        if activities['labels']:
            for label in activities['labels']:
                backup.create_label_activity(label['content'], section_num)
                print(f"  - Created label (introduction)")

        for page in activities['pages']:
            backup.create_page_activity(page['name'], page['content'], section_num)
            print(f"  - Created page: {page['name'][:50]}...")

        for quiz in activities['quizzes']:
            backup.create_quiz_activity(quiz['name'], quiz['content'], section_num)
            print(f"  - Created quiz: {quiz['name'][:50]}...")

        for forum in activities['forums']:
            backup.create_forum_activity(forum['name'], forum['content'], section_num)
            print(f"  - Created forum: {forum['name'][:50]}...")

        for assignment in activities['assignments']:
            backup.create_assignment_activity(assignment['name'], assignment['content'], section_num)
            print(f"  - Created assignment: {assignment['name'][:50]}...")

    print("\n\nFinalizing backup structure...")
    backup.finalize_backup()

    # Create ZIP file (MBZ format)
    print("Creating MBZ (ZIP) archive...")
    mbz_file = r'C:\Users\utente\moodle-agent-team\AI-Principianti-backup.mbz'
    with zipfile.ZipFile(mbz_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(output_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, output_dir)
                zipf.write(file_path, arcname)

    # Statistics
    activity_types = {}
    for activity in backup.activities:
        atype = activity['type']
        activity_types[atype] = activity_types.get(atype, 0) + 1

    print(f"\n{'='*60}")
    print(f"MOODLE BACKUP GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"Course: {course_info['name']}")
    print(f"Short name: {course_info['short_name']}")
    print(f"Modules parsed: {len(modules)}")
    print(f"Total activities created: {len(backup.activities)}")
    print(f"\nActivities by type:")
    for atype, count in sorted(activity_types.items()):
        print(f"  - {atype}: {count}")
    print(f"\nOutput directory: {output_dir}")
    print(f"MBZ file: {mbz_file}")
    print(f"\n{'='*60}")
    print(f"The MBZ file is ready to be imported into Moodle 4.x")
    print(f"{'='*60}\n")

    return mbz_file, len(modules), len(backup.activities), activity_types


if __name__ == '__main__':
    main()
