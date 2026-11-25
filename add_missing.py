import sys
with open('C:/Project/Mark-LV-main/ui.py', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()
idx_end = content.find('def paintEvent(self, _):', content.find('def _paint_core'))
idx_end -= 5
missing = open('C:/Project/Mark-LV-main/core_append.txt', 'r', encoding='utf-8').read()
content = content[:idx_end] + missing + content[idx_end:]
with open('C:/Project/Mark-LV-main/ui.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('SUCCESS')
