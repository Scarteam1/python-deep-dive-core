import sys
import re

def main():
    if len(sys.argv) < 2: return
    milestone = sys.argv[1]
    m = int(milestone)
    total = 161
    
    # Advanced Linux Smooth-Loading Math (Total width of 15 characters)
    max_blocks = 15
    fractional_symbols = [" ", "▏", "▎", "▍", "▌", "▋", "▊", "▉", "█"]
    
    raw_score = (m / total) * max_blocks
    full_blocks = int(raw_score)
    remainder = raw_score - full_blocks
    symbol_index = int(remainder * 8)
    
    # Assemble the high-fidelity telemetry bar
    bar_string = "█" * full_blocks
    if full_blocks < max_blocks:
        bar_string += fractional_symbols[symbol_index]
        bar_string += " " * (max_blocks - full_blocks - 1)
        
    # Wrap it in clean markdown syntax accents
    final_bar = f"`|{bar_string}|`"
    
    with open('README.md', 'r', encoding='utf-8', errors='ignore') as f_in:
        lines = f_in.readlines()
        
    for i, line in enumerate(lines):
        if "Current Progress:" in line:
            lines[i] = f'  * **Current Progress:** {final_bar} {milestone} / 161 Lectures Completed\n'
        if "(Lectures 31-" in line:
            lines[i] = re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-{milestone})', line)
            
    with open('README.md', 'w', encoding='utf-8', newline='\r\n') as f_out:
        f_out.write("".join(lines))

if __name__ == "__main__":
    main()
