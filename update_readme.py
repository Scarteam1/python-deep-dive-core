import sys
import re

def main():
    if len(sys.argv) < 2: return
    milestone = sys.argv[1]
    m = int(milestone)
    total = 161
    
    # Slim 20-Character Precision Grid
    max_blocks = 20
    
    # Calculate exact filled segments
    green_count = int(round((m / total) * max_blocks))
    gray_count = max_blocks - green_count
    
    # Build the colorful slim telemetry string
    bar_string = "??" * green_count + "⬛" * gray_count
    
    with open('README.md', 'r', encoding='utf-8', errors='ignore') as f_in:
        lines = f_in.readlines()
        
    for i, line in enumerate(lines):
        if "Current Progress:" in line:
            lines[i] = f'  * **Current Progress:** {bar_string} {milestone} / 161 Lectures Completed\n'
        if "(Lectures 31-" in line:
            lines[i] = re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-{milestone})', line)
            
    with open('README.md', 'w', encoding='utf-8', newline='\r\n') as f_out:
        f_out.write("".join(lines))

if __name__ == "__main__":
    main()
