import pypdf, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

if len(sys.argv) < 2:
    print("Usage: python extract_pdf.py <path-to-pdf> [max_pages] [max_chars]")
    sys.exit(1)

fname = sys.argv[1]
max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else 15
max_chars = int(sys.argv[3]) if len(sys.argv) > 3 else 12000

if not os.path.exists(fname):
    print(f"File not found: {fname}", file=sys.stderr)
    sys.exit(1)

reader = pypdf.PdfReader(fname)
text = ''
for page in reader.pages[:max_pages]:
    t = page.extract_text()
    if t:
        text += t + '\n'
    if len(text) > max_chars:
        break

print(text[:max_chars])
