import sys, re
def main():
    if len(sys.argv) < 2: return
    m = int(sys.argv[1])
    g = int(round((m/161)*10))
    bar = "🟩"*g + "🟪"*(10-g)
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i, l in enumerate(lines):
        if "Current Progress:" in l:
            lines[i] = f"  * **Current Progress:** {bar} {m} / 161 Lectures Completed\n"
        if "(Lectures 31-" in l:
            lines[i] = re.sub(r"\(Lectures 31-\d+\)", f"(Lectures 31-{m})", l)
    with open("README.md", "w", encoding="utf-8", newline="\r\n") as f:
        f.write("".join(lines))
if __name__=="__main__": main()
