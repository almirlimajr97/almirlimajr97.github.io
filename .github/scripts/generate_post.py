import os, re

title   = os.environ.get('POST_TITLE', '')
date    = os.environ.get('POST_DATE', '')
content = os.environ.get('POST_CONTENT', '')
ack     = os.environ.get('POST_ACK', '').strip()
pdf     = os.environ.get('POST_PDF', '').strip()
slug    = os.environ.get('POST_SLUG', '').strip()

if not slug:
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

def md_inline(text):
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
                  r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    return text

def md_to_body(text):
    lines = text.split('\n')
    html = []
    para = []
    def flush():
        if para:
            html.append('<p>' + md_inline(' '.join(para)) + '</p>')
            para.clear()
    for line in lines:
        line = line.rstrip()
        if line.startswith('## '):
            flush(); html.append('<h2>' + md_inline(line[3:]) + '</h2>')
        elif line.startswith('### '):
            flush(); html.append('<h3>' + md_inline(line[4:]) + '</h3>')
        elif line == '':
            flush()
        else:
            para.append(line)
    flush()
    return '\n      '.join(html)

body_html = md_to_body(content)
ack_html  = md_inline(ack) if ack else ''

pdf_block = ''
if pdf:
    pdf_block = (
        '\n      <div class="pdf-wrap">'
        '\n        <iframe src="/files/' + pdf + '" title="' + title + '"></iframe>'
        '\n      </div>'
        '\n      <a class="download-link" href="/files/' + pdf + '" target="_blank" rel="noopener">'
        '\n        📥 Download the paper (PDF)'
        '\n      </a>'
    )

ack_block = ''
if ack_html:
    ack_block = (
        '\n    <div class="ack-box">'
        '\n      ' + ack_html +
        '\n    </div>'
    )

template = open('.github/scripts/post_template.html').read()
result = (template
    .replace('{{TITLE}}', title)
    .replace('{{DATE}}', date)
    .replace('{{BODY}}', body_html)
    .replace('{{ACK_BLOCK}}', ack_block)
    .replace('{{PDF_BLOCK}}', pdf_block)
)

filepath = 'posts/' + slug + '.html'
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(result)
print('Created:', filepath)
