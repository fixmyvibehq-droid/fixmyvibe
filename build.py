#!/usr/bin/env python3
"""Build the FixMyVibe site into ./public.

Reads every Markdown fix in content/fixes, renders the home page, one page per
fix, a 404 page, sitemap.xml and robots.txt. Needs Python 3 with the
`markdown` and `PyYAML` packages:  pip install markdown pyyaml

Run:  python3 build.py
Then commit the public/ folder; the host serves it as plain files.
"""
import datetime
import html
import json
import pathlib
import re
import shutil

import markdown
import yaml

ROOT = pathlib.Path(__file__).parent
CONTENT = ROOT / 'content' / 'fixes'
OUT = ROOT / 'public'
SITE = 'https://fixmyvibe.org'
CATEGORY_ORDER = ['Deploy & environment', 'Build', 'Database & auth', 'Payments', 'Frontend', 'APIs', 'AI APIs']

e = html.escape


LIST_ITEM = re.compile(r'^\s*(?:[-*+]|\d+\.)\s')


def blank_before_lists(text):
    """Python-Markdown needs a blank line before a list; GitHub doesn't. Add one."""
    lines, out = text.split('\n'), []
    for i, line in enumerate(lines):
        prev = out[-1] if out else ''
        if LIST_ITEM.match(line) and prev.strip() and not LIST_ITEM.match(prev) and not prev.startswith(' '):
            out.append('')
        out.append(line)
    return '\n'.join(out)


def render_markdown(body):
    # Fix pages never use raw HTML, so treat "<" as text. This keeps prompt
    # placeholders like <paste the error> visible instead of vanishing as tags.
    md = markdown.Markdown(extensions=['extra', 'sane_lists'])
    md.preprocessors.deregister('html_block')
    md.inlinePatterns.deregister('html')
    return md.convert(body)


def load_fixes():
    keywords = json.loads((ROOT / 'data' / 'keywords.json').read_text())
    fixes = []
    for path in sorted(CONTENT.glob('*.md')):
        raw = path.read_text()
        _, front, body = raw.split('---', 2)
        body = blank_before_lists(body)
        meta = yaml.safe_load(front)
        slug = path.stem
        checked = meta['last_checked']
        if isinstance(checked, str):
            checked = datetime.date.fromisoformat(checked)
        fixes.append({
            'slug': slug,
            'title': meta['title'],
            'heading': meta['heading'],
            'error': meta['error'],
            'category': meta['category'],
            'tools': meta.get('tools', []),
            'checked': checked,
            'html': render_markdown(body),
            'keywords': keywords.get(slug, []),
        })
    return sorted(fixes, key=lambda f: f['title'].lower())


def page(title, description, path, body, scripts=''):
    canonical = SITE + path
    year = datetime.date.today().year
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{canonical}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="FixMyVibe">
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@fixmyvibehq">
<meta name="theme-color" content="#0e0f0c">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,700;12..96,800&family=JetBrains+Mono:wght@400;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
</head>
<body>
<header class="site-header"><div class="wrap">
<a class="logo" href="/">{{✓}} fixmyvibe</a>
<nav class="nav" aria-label="Main"><a href="/#doctor">Error Doctor</a><a href="/#library">Fixes</a><a href="https://x.com/fixmyvibehq" rel="noopener">X</a></nav>
</div></header>
<main>
{body}
</main>
<footer class="site-footer"><div class="wrap">
<span>© {year} FixMyVibe. Fixes are checked against official docs, but always test before you ship.</span>
<span class="footer-links"><a href="/tools/">Tools we recommend</a><a href="/disclosure/">Affiliate disclosure</a><a href="https://x.com/fixmyvibehq" rel="noopener">@fixmyvibehq</a></span>
</div></footer>
{scripts}
</body>
</html>
'''


DOCTOR_JS = '''<script>
(function () {
  var index = JSON.parse(document.getElementById('fix-index').textContent);
  var form = document.getElementById('doctor-form');
  var input = document.getElementById('doctor-input');
  var out = document.getElementById('doctor-results');
  function words(s) { return s.toLowerCase().match(/[a-z0-9_.-]{4,}/g) || []; }
  function score(text, fix) {
    var s = 0;
    if (text.indexOf(fix.error.toLowerCase()) !== -1) s += 20;
    fix.phrases.forEach(function (p) { if (p && text.indexOf(p) !== -1) s += p.split(/\\s+/).length + 1; });
    var errWords = {};
    words(fix.error).forEach(function (w) { errWords[w] = true; });
    var seen = {};
    words(text).forEach(function (w) { if (errWords[w] && !seen[w]) { seen[w] = true; s += 1; } });
    return s;
  }
  function link(fix, top) {
    var a = document.createElement('a');
    a.className = top ? 'result top' : 'result';
    a.href = '/fix/' + fix.slug + '/';
    var strong = document.createElement('strong');
    strong.textContent = fix.title;
    var span = document.createElement('span');
    span.textContent = fix.category;
    a.appendChild(strong); a.appendChild(span);
    return a;
  }
  form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var text = input.value.toLowerCase().trim();
    out.innerHTML = '';
    if (!text) return;
    var ranked = index.map(function (f) { return { f: f, s: score(text, f) }; })
      .filter(function (r) { return r.s >= 3; })
      .sort(function (a, b) { return b.s - a.s; })
      .slice(0, 3);
    if (!ranked.length) {
      var p = document.createElement('p');
      p.className = 'hint';
      p.textContent = "No match yet. We're adding fixes every week. Send this error to @fixmyvibehq on X and we'll write one.";
      out.appendChild(p);
      return;
    }
    ranked.forEach(function (r, i) { out.appendChild(link(r.f, i === 0)); });
  });
})();
</script>'''

COPY_JS = '''<script>
document.querySelectorAll('.article blockquote').forEach(function (quote) {
  var text = quote.innerText.trim();
  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'btn copy-btn';
  btn.textContent = 'Copy';
  btn.setAttribute('aria-label', 'Copy prompt');
  btn.addEventListener('click', function () {
    navigator.clipboard.writeText(text).then(function () { btn.textContent = 'Copied'; },
      function () { btn.textContent = 'Select & copy'; });
    setTimeout(function () { btn.textContent = 'Copy'; }, 2000);
  });
  quote.appendChild(btn);
});
</script>'''


def build_home(fixes):
    cats = sorted({f['category'] for f in fixes},
                  key=lambda c: CATEGORY_ORDER.index(c) if c in CATEGORY_ORDER else 99)
    sections = []
    for cat in cats:
        items = ''.join(
            f'<li><a href="/fix/{f["slug"]}/">{e(f["title"])}<code>{e(f["error"])}</code></a></li>'
            for f in fixes if f['category'] == cat)
        sections.append(f'<div class="category"><h3>{e(cat)}</h3><ul class="fix-list">{items}</ul></div>')
    index = [{
        'slug': f['slug'], 'title': f['heading'], 'error': f['error'], 'category': f['category'],
        'phrases': [p.lower() for p in [f['error'], f['title'], *f['keywords']]],
    } for f in fixes]
    index_json = json.dumps(index).replace('</', '<\\/')
    body = f'''<section class="wrap hero">
<h1>Your vibe-coded app broke.<br><span>Let’s fix it.</span></h1>
<p>Plain-English fixes for the errors AI coding tools leave behind. Every fix ends with a prompt you paste straight into your AI.</p>
</section>
<section class="wrap" id="doctor" aria-labelledby="doctor-title">
<form class="doctor" id="doctor-form">
<label id="doctor-title" for="doctor-input">Error Doctor · paste your error message</label>
<textarea id="doctor-input" name="error" placeholder="e.g. Error: supabaseUrl is required." spellcheck="false"></textarea>
<div class="doctor-row"><button class="btn" type="submit">Find my fix</button><span class="hint">Runs in your browser. Nothing you paste is sent anywhere.</span></div>
<div class="results" id="doctor-results" aria-live="polite"></div>
</form>
</section>
<section class="wrap" id="library" aria-labelledby="library-title">
<h2 class="section-title" id="library-title">Fix library</h2>
<p class="section-sub">{len(fixes)} fixes and growing. New ones added every week. Starting a new project? See <a href="/tools/">the tools we recommend</a>.</p>
{''.join(sections)}
</section>
<section class="wrap"><div class="kit">
<div><h2>Launch Kit, coming soon</h2><p>A pre-launch checklist for auth, secrets, payments and SEO, with a fix prompt for every item and rule files that stop AI tools making these mistakes in the first place.</p></div>
<a class="btn" href="https://x.com/fixmyvibehq" rel="noopener">Follow for launch</a>
</div></section>
<script type="application/json" id="fix-index">{index_json}</script>'''
    return page('FixMyVibe: fixes for broken vibe-coded apps',
                'Your vibe-coded app broke? Paste the error and get a plain-English fix plus a prompt to paste into Cursor, Lovable, Bolt, Replit or Claude Code.',
                '/', body, DOCTOR_JS)


def load_tools():
    return json.loads((ROOT / 'data' / 'tools.json').read_text())


def aff_link(tool, text, cls='btn'):
    rel = 'sponsored nofollow noopener' if tool['affiliate'] else 'noopener'
    return f'<a class="{cls}" href="{e(tool["url"])}" rel="{rel}">{e(text)}</a>'


AFF_NOTE = ('<span class="aff-note">Affiliate link: we may earn a commission at no cost to you. '
            '<a href="/disclosure/">Details</a></span>')


def tool_box(f, tools):
    """A short note under a fix that's tagged with a tool we have an affiliate link for."""
    for t in tools:
        if t['affiliate'] and any(m in f['tools'] for m in t['match']):
            return (f'<aside class="aff-box"><p><strong>Starting your next project?</strong> '
                    f'{e(t.get("pitch", t["about"]))}</p>'
                    f'<div class="aff-row">{aff_link(t, "Try " + t["name"], "btn ghost")}{AFF_NOTE}</div></aside>')
    return ''


def build_tools(tools):
    cards = []
    for t in tools:
        note = AFF_NOTE if t['affiliate'] else ''
        cards.append(f'''<li class="tool-card">
<h2>{e(t["name"])}</h2>
<p class="tool-for">{e(t["for"])}</p>
<p>{e(t["about"])}</p>
<div class="aff-row">{aff_link(t, "Visit " + t["name"], "btn ghost")}{note}</div>
</li>''')
    body = f'''<div class="wrap narrow article">
<p class="crumb"><a href="/">Home</a> / Tools</p>
<h1>Tools we recommend</h1>
<p>The tools we'd pick for a first app, and the ones our fixes come up against most. Some links are affiliate links and are marked; they never change what we recommend.</p>
<ul class="tool-list">{''.join(cards)}</ul>
</div>'''
    return page('Tools we recommend for vibe coding | FixMyVibe',
                'The AI app builders, databases, payments and hosting we recommend for building your first app.',
                '/tools/', body)


def build_disclosure():
    body = '''<div class="wrap narrow article">
<p class="crumb"><a href="/">Home</a> / Disclosure</p>
<h1>Affiliate disclosure</h1>
<p>FixMyVibe is free to use. To keep it that way, some links on this site are affiliate links. If you click one and later pay for that product, we may earn a commission. It costs you nothing extra.</p>
<h2>How we handle this</h2>
<ul>
<li>Affiliate links are always marked next to the link.</li>
<li>We only link a tool where it genuinely fits the problem or page.</li>
<li>Commissions never change our fixes. If a tool causes a problem, we say so.</li>
<li>We also recommend tools we earn nothing from.</li>
</ul>
<p>Questions? Message <a href="https://x.com/fixmyvibehq" rel="noopener">@fixmyvibehq</a> on X.</p>
</div>'''
    return page('Affiliate disclosure | FixMyVibe', 'How FixMyVibe uses affiliate links.', '/disclosure/', body)


def build_fix(f, tools):
    checked = f['checked'].strftime('%-d %b %Y')
    tool_names = ' · '.join(f['tools'])
    description = (f'How to fix "{f["error"]}" in apps built with {", ".join(f["tools"][:3])}. '
                   'Plain-English cause, step-by-step fix and a copy-paste prompt for your AI.')
    body = f'''<div class="wrap narrow article">
<p class="crumb"><a href="/#library">Fixes</a> / {e(f["category"])}</p>
<h1>{e(f["heading"])}</h1>
<div class="fix-error">{e(f["error"])}</div>
<p class="meta">{e(tool_names)} · last checked {checked}</p>
<article>{f["html"]}</article>
{tool_box(f, tools)}
<p style="margin-top: 48px"><a class="btn ghost" href="/#doctor">Got a different error? Try Error Doctor</a></p>
</div>'''
    return page(f'{f["title"]}: how to fix it | FixMyVibe', description, f'/fix/{f["slug"]}/', body, COPY_JS)


def build_404():
    body = '''<section class="wrap hero"><h1>404: this page<br><span>didn’t deploy.</span></h1>
<p>Ironic, we know. <a href="/">Head back to the fix library</a> or paste your error into Error Doctor.</p></section>'''
    return page('Page not found | FixMyVibe', "This page doesn't exist.", '/404', body)


def main():
    fixes = load_fixes()
    tools = load_tools()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / 'fix').mkdir(parents=True)
    for asset in (ROOT / 'assets').iterdir():
        shutil.copy(asset, OUT / asset.name)
    (OUT / 'index.html').write_text(build_home(fixes))
    (OUT / '404.html').write_text(build_404())
    for name, html_text in (('tools', build_tools(tools)), ('disclosure', build_disclosure())):
        (OUT / name).mkdir()
        (OUT / name / 'index.html').write_text(html_text)
    for f in fixes:
        d = OUT / 'fix' / f['slug']
        d.mkdir()
        (d / 'index.html').write_text(build_fix(f, tools))
    urls = ([f'{SITE}/', f'{SITE}/tools/', f'{SITE}/disclosure/']
            + [f'{SITE}/fix/{f["slug"]}/' for f in fixes])
    (OUT / 'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + ''.join(f'<url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    (OUT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n')
    print(f'Built {len(fixes)} fix pages into {OUT}')


if __name__ == '__main__':
    main()
