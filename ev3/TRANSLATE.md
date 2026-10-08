# EV3 docs HTML → Japanese translation rules (temporary file, not deployed)

You are translating generated HTML documentation pages for the LEGO EV3 MicroPython docs (a mirror of pybricks.com/ev3-micropython) into natural, careful Japanese.

All work is inside the `ev3/` directory — STATIC HTML FILES ONLY (there is no .rst source; the built HTML is the artifact being translated and deployed). NEVER touch anything outside `ev3/` and only the files assigned to you. Delete this file before pushing.

## Translation rules (follow strictly)

1. Translate all VISIBLE text in the main content section: h1-h4, p, li, td, th, dt, dd, figcaption, blockquote, admonition bodies, table contents, `<title>`. Sidebar `<a>` link texts that are page titles: keep them consistent — use the natural Japanese title for pages you own; for pages owned by others, translate the link text to the obvious Japanese equivalent.
2. Natural, careful Japanese for hardware-hobbyist readers — rewrite for clarity where a literal translation would be awkward. です・ます style consistent with the rest of the site (e.g. 「モーターを接続するポート。」).
3. KEEP IN ENGLISH: API/class/method/parameter names and signatures, code, product names (LEGO, MINDSTORMS, EV3 Brick, EV3, MicroPython, ev3dev, VS Code, Bluetooth, Wi-Fi, SD card, Linux, Windows, macOS, PuTTY, firmware), file names/paths, commands, URLs, identifiers inside `<code>`/`<span class="pre">` literals. Short simple terms that Japanese hobbyists use in English may stay.
4. DO NOT translate: tag structure, attributes, ids, classes, hrefs, `<pre>` code bodies (except comments — see #5), genindex.html, py-modindex.html, search.html, searchindex.js, `_sources/`, `_static/`, `_images/`.
5. Inside `<pre>` code blocks: translate ONLY Python `#` comments to Japanese. NEVER translate code, and NEVER translate string literals shown on the EV3 brick display (the brick screen only renders Latin text — Japanese strings would break on the device). Keep program output strings English.
6. Inline markup is already rendered HTML — keep all tags exactly as they are and only change the human text inside. Do not restructure HTML, do not reformat/indent, do not "clean up". Minimal diffs per file.
7. Sidebar nav captions, breadcrumb, search placeholder, Next/Previous buttons are already translated — do not touch `<nav>`/footer chrome.
8. External links (lego.com PDFs, ev3dev.org, github.com/pybricks/...) stay external — do NOT rewrite URLs.
9. Where docs tell the user to use English UI (VS Code buttons, menus), keep English UI names; a short Japanese gloss in parens is fine, e.g. 「File」メニュー.

## Verification (must all pass before commit)

- `python3 -c "from html.parser import HTMLParser; HTMLParser().feed(open('FILE',encoding='utf8').read())"` for every edited file (well-formed check).
- No leftover English PROSE: run this per edited file —
  `python3 -c "import re,html; s=open('FILE',encoding='utf8').read(); t=re.sub(r'<(script|style)[^>]*>.*?</\\1>','',s,flags=re.S); t=re.sub(r'<[^>]+>','\n',t); t=html.unescape(t); print('\n'.join(l.strip() for l in t.split('\n') if len(l.strip())>15 and not l.strip().startswith(('pybricks','import','from','def ','class ')) and not any(ord(c)>0x3000 for c in l)))"`
  Remaining lines should only be identifiers, commands, code, product names, or proper nouns — NOT prose sentences.
- `git diff` review your own changes before committing.

## Commit

`git add ev3/ && git rm ev3/TRANSLATE.md && git commit -m "ev3: <対象名>を日本語化"` then `git push -u origin <your branch>`. Do NOT open a PR, do NOT merge, do NOT create other sessions.
