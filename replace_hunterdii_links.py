import re
from pathlib import Path
path = Path('app.py')
text = path.read_text(encoding='utf-8')
new_link = 'https://github.com/Washim629/AI-resume-Analyzer'
updated = re.sub(r'https://github\.com/Hunterdii[^"\s>]*', new_link, text)
path.write_text(updated, encoding='utf-8')
print('Updated Hunterdii GitHub links to', new_link)
