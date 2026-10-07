"""Collect evidence for one review; never reparse or modify KORDOC output."""
import collections
import datetime
import hashlib
import json
import pathlib
import re
import sys
import unicodedata
from pypdf import PdfReader
import pypdfium2 as pdfium

out = pathlib.Path(sys.argv[1]).resolve()
marker = out / 'review-run.json'
with marker.open('x', encoding='utf-8') as f:
    json.dump({'reviewCount': 1, 'startedAt': datetime.datetime.now(datetime.timezone.utc).isoformat()}, f)
run = json.loads((out / 'run.json').read_text(encoding='utf-8'))
source = pathlib.Path(run['input'])
assert hashlib.sha256(source.read_bytes()).hexdigest() == run['sha256'], 'Source changed'
result = json.loads((out / 'parsed.json').read_text(encoding='utf-8'))
reader = PdfReader(source)
texts = [p.extract_text() or '' for p in reader.pages]
pages = {p['pageNumber']: p['markdown'] for p in result.get('pages', [])}

def words(text):
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'(\w)-\s*\n\s*(\w)', r'\1\2', text)
    return collections.Counter(re.findall(r'[a-z0-9]+', text.lower()))

def coverage(ref, actual):
    counts = words(ref)
    return round(sum((counts & words(actual)).values()) / max(1, sum(counts.values())), 4)

per_page = [{'page': i + 1, 'source_chars': len(t), 'parsed_chars': len(pages.get(i + 1, '')), 'token_overlap': coverage(t, pages.get(i + 1, ''))} for i, t in enumerate(texts)]
table_candidates = [i + 1 for i, t in enumerate(texts) if re.search(r'Table\s*1\s*:', t, re.I)]
sample = sorted(set([1, table_candidates[0] if table_candidates else max(1, len(texts)//2), len(texts)]))
doc = pdfium.PdfDocument(str(source))
previews = out / '검수표본'
previews.mkdir(exist_ok=True)
for n in sample:
    page = doc[n - 1]
    bitmap = page.render(scale=1.4)
    bitmap.to_pil().save(previews / f'original-page-{n}.png')
    bitmap.close()
    page.close()
doc.close()
evidence = {
    'reviewCount': 1, 'source_pages': len(texts), 'kordoc_pages': result.get('pageCount', result.get('metadata', {}).get('pageCount')),
    'output_page_numbers': sorted(pages), 'sample_pages': sample,
    'document_token_overlap': coverage('\n'.join(texts), result['markdown']),
    'metric_note': 'Reference is pypdf text, not ground truth. Token overlap cannot establish reading order, table fidelity, or semantic accuracy.',
    'replacement_characters': result['markdown'].count('\ufffd'),
    'warnings': result.get('warnings', []), 'qualitySummary': result.get('qualitySummary'),
    'block_types': dict(collections.Counter(b['type'] for b in result.get('blocks', []))),
    'per_page': per_page,
}
(out / '검수자료.json').write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding='utf-8')
(previews / '표본파싱문.md').write_text('\n\n'.join(f'# PDF {n}쪽\n\n{pages.get(n, "[페이지 출력 없음]")}' for n in sample), encoding='utf-8')
print(json.dumps(evidence, ensure_ascii=False, indent=2))
