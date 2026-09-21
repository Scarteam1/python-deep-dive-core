import sys
import re

def main():
    if len(sys.argv) < 2:
        return
    milestone = sys.argv[1]
    m = int(milestone)
    total = 161
    
    # Calculate blocks perfectly based on a 10-point scale
    green_count = int(round((m / total) * 10))
    purple_count = 10 - green_count
    bar = '??' * green_count + '??' * purple_count
    
    # Read the file
    with open('README.md', 'r', encoding='utf-8') as f_in:
        content = f_in.read()
        
    # Surgically replace the scrambled bar and match the text layout
    updated = re.sub(r'Current Progress:\s*.*?\s*\d+ / 161', f'Current Progress: {bar} {milestone} / 161', content)
    updated = re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-{milestone})', updated)
    
    # Write it back cleanly in raw UTF-8 format
    with open('README.md', 'w', encoding='utf-8') as f_out:
        f_out.write(updated)

if __name__ == '__main__':
    main()
