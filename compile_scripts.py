import os
import json
import re

def parse_chapter_number(dir_name):
    match = re.search(r'Chapter_(\d+)', dir_name)
    if match:
        return int(match.group(1))
    return 999

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    scripts_data = []

    # Get all Chapter directories
    chapters_dirs = []
    for entry in os.listdir(base_dir):
        entry_path = os.path.join(base_dir, entry)
        if os.path.isdir(entry_path) and entry.startswith("Chapter_"):
            chapters_dirs.append(entry)
            
    # Sort chapters numerically
    chapters_dirs.sort(key=parse_chapter_number)

    for ch_dir in chapters_dirs:
        ch_num = parse_chapter_number(ch_dir)
        ch_path = os.path.join(base_dir, ch_dir)
        
        # Get all Python files in the chapter directory
        py_files = [f for f in os.listdir(ch_path) if f.endswith(".py")]
        py_files.sort(key=natural_sort_key)
        
        for f in py_files:
            file_path = os.path.join(ch_path, f)
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file_content:
                code = file_content.read()
            
            # Determine script type and clean name
            # Filename patterns:
            # - CH3_answer1.py -> Answer 1
            # - ch3_example1.py -> Example 1
            # - Ch12_challenge1.py -> Challenge 1
            # - CH3_answer_investigation.py -> Answer Investigation
            
            lower_f = f.lower()
            script_type = "other"
            name = f
            
            if "example" in lower_f:
                script_type = "example"
                match = re.search(r'example(\d+)', lower_f)
                name = f"Example {match.group(1)}" if match else f"Example ({f})"
            elif "answer" in lower_f:
                script_type = "answer"
                if "investigation" in lower_f:
                    name = "Answer: Investigation"
                else:
                    match = re.search(r'answer(\d+)', lower_f)
                    name = f"Answer {match.group(1)}" if match else f"Answer ({f})"
            elif "challenge" in lower_f:
                script_type = "challenge"
                match = re.search(r'challenge(\d+)', lower_f)
                name = f"Challenge {match.group(1)}" if match else f"Challenge ({f})"
                
            # Extract simple description from initial comment lines
            description = ""
            lines = code.split("\n")
            comment_lines = []
            for line in lines:
                stripped = line.strip()
                if stripped.startswith("#"):
                    # Avoid lines like '# Learn More', '# Input', '# Output', '# "test"'
                    if not any(keyword in stripped for keyword in ["# Learn More", "# Input", "# Output", "# \""]):
                        comment_lines.append(stripped.lstrip("#").strip())
                elif stripped == "":
                    continue
                else:
                    # Non-comment line, stop extracting
                    break
            
            if comment_lines:
                description = " ".join(comment_lines)
            
            scripts_data.append({
                "chapter": ch_num,
                "filename": f,
                "type": script_type,
                "name": name,
                "code": code,
                "description": description
            })
            
    # Write to scripts_data.js
    js_content = f"// Automatically generated scripts data\nconst SCRIPTS_DATA = {json.dumps(scripts_data, indent=2)};\n"
    output_path = os.path.join(base_dir, "scripts_data.js")
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(js_content)
        
    print(f"Successfully compiled {len(scripts_data)} scripts into {output_path}")

if __name__ == "__main__":
    main()
