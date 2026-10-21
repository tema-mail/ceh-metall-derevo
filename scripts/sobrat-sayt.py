# Сборка публичной версии для GitHub Pages: site/index.html (отчёт) + site/<прототип>.html
# Ссылки отчёта на прототипы-артефакты заменяются на соседние страницы. Всё с noindex.
import json, os, re, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
site = os.path.join(ROOT, 'site'); shutil.rmtree(site, ignore_errors=True); os.makedirs(site)
html = open(os.path.join(ROOT, 'otchet/index.html')).read()
links = json.load(open(os.path.join(ROOT, 'otchet/prototipy.json')))
names = {'leto': 'leto.html', 'kupol': 'kupola.html', 'loft': 'loft.html'}
for k, url in links.items():
    html = html.replace(url, names[k])
head = '<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="robots" content="noindex,nofollow">\n'
m = re.search(r'</style>\n', html)
html = head + html[:m.end()] + '</head>\n<body>\n' + html[m.end():] + '\n</body>\n</html>\n'
open(os.path.join(site, 'index.html'), 'w').write(html)
for f in names.values():
    shutil.copy(os.path.join(ROOT, 'prototipy', f), os.path.join(site, f))
open(os.path.join(site, 'robots.txt'), 'w').write('User-agent: *\nDisallow: /\n')
print('ok', sorted(os.listdir(site)))
