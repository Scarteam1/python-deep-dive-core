import sys
import re

def main():
    # If no number argument was passed, default to 61
    milestone = "61"
    if len(sys.argv) > 1:
        milestone = sys.argv[1]  # FIX: Explicitly target the first input string word index
        
    m = int(milestone)
    total = 161
    
    # Precision 20-character metric grid
    max_blocks = 20
    green_count = int(round((m / total) * max_blocks))
    gray_count = max_blocks - green_count
    
    # Use hex codes to completely bypass local environment translation bugs
    green_square = "\U0001F7E9"
    dark_square = "\U00002B1B"
    bar_string = green_square * green_count + dark_square * gray_count
    
    with open('README.md', 'r', encoding='utf-8', errors='ignore') as f_in:
        content = f_in.read()
        
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if "Current Progress:" in line:
            lines[i] = f'  * **Current Progress:** {bar_string} {milestone} / 161 Lectures Completed'
        if "(Lectures 31-" in line:
            lines[i] = re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-{milestone})', line)
            
    with open('README.md', 'w', encoding='utf-8', newline='\r\n') as f_out:
        f_out.write("\n".join(lines))

if __name__ == "__main__":
    main()
