"""MkDocs hook: inject an estimated reading time under each lesson's title.

Counts the words in the page's Markdown and prints a friendly
"⏱️ X min read" line just after the first H1. Skipped on the homepage
and on section index (README) pages so only real lessons are tagged.
"""

import re

WORDS_PER_MINUTE = 200

_H1 = re.compile(r"^#\s+.*$", re.MULTILINE)
_CODE_FENCE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE = re.compile(r"`[^`]*`")
_WORD = re.compile(r"[A-Za-z0-9']+")


def on_page_markdown(markdown, page, config, files):
    if page.is_homepage:
        return markdown

    # Skip section landing pages (the course README/index pages).
    src = page.file.src_uri.lower()
    if src.endswith("readme.md") or src.endswith("index.md"):
        return markdown

    text = _CODE_FENCE.sub(" ", markdown)
    text = _INLINE_CODE.sub(" ", text)
    words = len(_WORD.findall(text))
    if words == 0:
        return markdown

    minutes = max(1, round(words / WORDS_PER_MINUTE))
    badge = f'\n\n<p class="reading-time">⏱️ {minutes} min read</p>\n'

    match = _H1.search(markdown)
    if not match:
        return badge + markdown

    end = match.end()
    return markdown[:end] + badge + markdown[end:]
