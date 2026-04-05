import re

with open('docs/gallery.py', 'r') as f:
    content = f.read()

# Match blocks that start with `        # html.Section([` and end with `        # ], style={'padding': '20px'}),`
pattern = re.compile(r'\n\s*# html\.Section\(\[\n.*?# \], style=\{\'padding\': \'20px\'\}\),\n', re.DOTALL)

cleaned = re.sub(pattern, '\n', content)

with open('docs/gallery.py', 'w') as f:
    f.write(cleaned)

