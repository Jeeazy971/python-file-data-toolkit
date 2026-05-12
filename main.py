from pathlib import Path

input_folder = Path("input_files")
reports_folder = Path("reports")

input_folder.mkdir(exist_ok=True)
reports_folder.mkdir(exist_ok=True)

if input_folder.is_dir() and reports_folder.is_dir():
    notes_path = input_folder / "notes.txt"
    tasks_path = input_folder / "tasks.txt"
    readme_path = input_folder / "readme.md"
    errors_path = input_folder / "errors.log"
    draft_path = input_folder / "draft.TXT"

    notes_content = """Python notes
Pathlib is useful
Files can be read"""

    tasks_content = """Tasks
Practice pathlib
Review exceptions
Generate report"""

    readme_content = """# README
This file should be ignored by the text report."""

    errors_content = """INFO: all good
WARNING: low disk space"""

    draft_content = """Draft
This uppercase extension should still be accepted"""

    notes_path.write_text(notes_content, encoding="utf-8")
    tasks_path.write_text(tasks_content, encoding="utf-8")
    readme_path.write_text(readme_content, encoding="utf-8")
    errors_path.write_text(errors_content, encoding="utf-8")
    draft_path.write_text(draft_content, encoding="utf-8")

    report_path = reports_folder / "text_files_report.txt"

    text_files_count = 0
    report_content = "Text files report\n"
    report_content += "-----------------\n"

    for item in input_folder.iterdir():
        if item.is_file() and item.suffix.lower() == ".txt":
            content = item.read_text(encoding="utf-8")
            lines_count = len(content.splitlines())
            text_files_count += 1

            report_content += f"File: {item.name}\n"
            report_content += f"Path: {item}\n"
            report_content += f"Lines: {lines_count}\n"
            report_content += "Content:\n"
            report_content += f"{content}\n"
            report_content += "\n"

    report_content += f"Total text files: {text_files_count}"

    report_path.write_text(report_content, encoding="utf-8")

    report = report_path.read_text(encoding="utf-8")
    print(report)
else:
    print("Required folders were not created.")
