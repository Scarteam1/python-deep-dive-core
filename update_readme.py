import sys

def main():
    milestone = "60"
    if len(sys.argv) > 1:
        milestone = sys.argv[1]
        
    m = int(milestone)
    
    # Calculate progress blocks perfectly (6 green, 4 purple for lecture 60)
    green_count = int(round((m / 161) * 10))
    purple_count = 10 - green_count
    bar = '??' * green_count + '??' * purple_count
    
    with open('README.md', 'r', encoding='utf-8') as f_in:
        content = f_in.read()
        
    # Standardize and cleanly rewrite the progress section line-by-line
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if "Current Progress:" in line:
            lines[i] = f'  * **Current Progress:** {bar} {milestone} / 161 Lectures Completed'
        if "(Lectures 31-" in line:
            import re
            lines[i] = re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-{milestone})', line)
            
    with open('README.md', 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(lines))

if __name__ == '__main__':
    main()
