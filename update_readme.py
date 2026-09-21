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
    
    # Read the current README file
    with open('README.md', 'r', encoding='utf-8') as f_in:
        content = f_in.read()
        
    # Reset the entire progress line cleanly to bypass scrambled characters
    # This matches exactly the title indicator header block on your portfolio
    pattern = r'#+ ?? Milestone Tracking Dashboard.*?
\s*•\s*Current Progress:.*?
'
    replacement = f'## ?? Milestone Tracking Dashboard\n\n* **Current Progress:** {bar} {milestone} / 161 Lectures Completed\n'
    
    # If the markdown header doesn't use the emoji, search for standard fallback lines
    if "Milestone Tracking Dashboard" in content:
        # Surgical line-by-line replacement to clear old question marks completely
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if "Current Progress:" in line:
                lines[i] = f'* **Current Progress:** {bar} {milestone} / 161 Lectures Completed'
            if "(Lectures 31-" in line:
                lines[i] = re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-{milestone})', line)
        updated = '\n'.join(lines)
    else:
        updated = re.sub(pattern, replacement, content, flags=re.DOTALL)
        updated = re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-{milestone})', updated)
    
    # Write it back cleanly in raw UTF-8 format
    with open('README.md', 'w', encoding='utf-8') as f_out:
        f_out.write(updated)

if __name__ == '__main__':
    main()
