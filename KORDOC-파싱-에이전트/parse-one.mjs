import { readFile, writeFile, mkdir, access } from 'node:fs/promises';
import path from 'node:path';
import { createHash } from 'node:crypto';
import { parse } from 'kordoc';

const [inputArg, outputArg, ...extra] = process.argv.slice(2);
if (!inputArg || !outputArg || extra.length || path.extname(inputArg).toLowerCase() !== '.pdf') {
  throw new Error('Usage: node parse-one.mjs <one.pdf> <output-directory>');
}
const input = path.resolve(inputArg);
const output = path.resolve(outputArg);
const data = await readFile(input);
if (!data.subarray(0, 1024).includes(Buffer.from('%PDF-'))) throw new Error('Not a PDF');
const sha256 = createHash('sha256').update(data).digest('hex');
const runPath = path.join(output, 'run.json');
try {
  const prior = JSON.parse(await readFile(runPath, 'utf8'));
  if (prior.sha256 === sha256 && prior.status === 'parsed') {
    console.log(JSON.stringify({ status: 'reused', output }));
    process.exit(0);
  }
  throw new Error('An earlier run exists. Do not overwrite or retry without an explicit new request.');
} catch (e) { if (e.code !== 'ENOENT') throw e; }
await mkdir(output, { recursive: true });
for (const filename of ['parsed.md', 'parsed.json']) {
  try { await access(path.join(output, filename)); throw new Error('Output already exists: ' + filename); }
  catch (e) { if (e.code !== 'ENOENT') throw e; }
}
const pkg = JSON.parse(await readFile(new URL('./node_modules/kordoc/package.json', import.meta.url), 'utf8'));
const options = { ocr: false, formulaOcr: false, scriptTags: true };
process.env.KORDOC_OFFLINE = '1';
const record = { input, sha256, engine: 'kordoc', version: pkg.version, source: 'https://github.com/chrisryugj/kordoc', options, parseAttempts: 1, startedAt: new Date().toISOString(), status: 'started' };
await writeFile(runPath, JSON.stringify(record, null, 2), { flag: 'wx' });
try {
  const result = await parse(input, options);
  if (!result.success) throw new Error(JSON.stringify(result));
  const images = [];
  for (const item of result.images || []) {
    const filename = item.filename;
    if (path.basename(filename) !== filename) throw new Error('Unsafe image filename');
    await writeFile(path.join(output, filename), item.data, { flag: 'wx' });
    images.push({ filename, mimeType: item.mimeType, bytes: item.data.length });
  }
  await writeFile(path.join(output, 'parsed.md'), result.markdown, { flag: 'wx', encoding: 'utf8' });
  await writeFile(path.join(output, 'parsed.json'), JSON.stringify({ ...result, images }, null, 2), { flag: 'wx', encoding: 'utf8' });
  Object.assign(record, { status: 'parsed', finishedAt: new Date().toISOString(), pageCount: result.pageCount ?? result.metadata?.pageCount, markdownChars: result.markdown.length });
  await writeFile(runPath, JSON.stringify(record, null, 2));
  console.log(JSON.stringify(record));
} catch (e) {
  await writeFile(runPath, JSON.stringify({ ...record, status: 'failed', error: String(e), finishedAt: new Date().toISOString() }, null, 2));
  throw e;
}
