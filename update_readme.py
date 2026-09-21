import sys
import re

def main():
    if len(sys.argv) < 2:
        return
    milestone = sys.argv[1]
    m = int(milestone)
    
    # Calculate blocks perfectly based on a 10-point scale
    green_count = int(round((m / 161) * 10))
    purple_count = 10 - green_count
    bar = '??' * green_count + '??' * purple_count
    
    # Read the current README file contents
    with open('README.md', 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()
        
    # Overwrite the visual tracker lines safely
    for i, line in enumerate(lines):
        if "Current Progress:" in line:
            lines[i] = f'- Current Progress: {bar} {milestone} / 161 Lectures Completed\n'
        if "Engineering Focus:" in line and "(Lectures 31-" in line:
            lines[i] = re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-{milestone})', line)
            
    # Write back the pristine layout in raw UTF-8 format
    with open('README.md', 'w', encoding='utf-8') as f_out:
        f_out.write(''.join(lines))

if __name__ == '__main__':
    main()
