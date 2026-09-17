#!/usr/bin/env python3
import hashlib, json, re, sys, urllib.request
from pathlib import Path

EXPECTED_SHA1 = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
URL = "https://raw.githubusercontent.com/justhop90-bot/TheByzantineShadow/main/ShadowSource.per"
OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "shadow-source-rule-index.json")
RAW = Path("ShadowSource.per")

raw = urllib.request.urlopen(URL, timeout=30).read()
sha1 = hashlib.sha1(raw).hexdigest()
if sha1 != EXPECTED_SHA1:
    raise SystemExit(f"SHA1 MISMATCH: got {sha1}, expected {EXPECTED_SHA1}")
RAW.write_bytes(raw)
text = raw.decode("utf-8")

# Mask comments/strings while preserving byte length/newlines so offsets remain exact.
def mask_source(s):
    out = list(s)
    i = 0
    n = len(s)
    in_str = False
    escaped = False
    while i < n:
        c = s[i]
        if in_str:
            if c == "\\" and not escaped:
                out[i] = " "
                escaped = True
            elif c == '"' and not escaped:
                out[i] = " "
                in_str = False
                escaped = False
            else:
                if c != "\n" and c != "\r": out[i] = " "
                escaped = False
            i += 1
            continue
        if c == '"':
            out[i] = " "
            in_str = True
            i += 1
            continue
        if c == ';':
            while i < n and s[i] not in "\r\n":
                out[i] = " "
                i += 1
            continue
        i += 1
    return ''.join(out)

masked = mask_source(text)
starts = [m.start() for m in re.finditer(r'\(defrule\b', masked)]

def matching_end(start):
    depth = 0
    for i in range(start, len(masked)):
        c = masked[i]
        if c == '(':
            depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0:
                return i + 1
    raise ValueError(f"unbalanced rule starting at byte/char {start}")

def line_no(pos):
    return text.count('\n', 0, pos) + 1

def byte_offset(pos):
    return len(text[:pos].encode('utf-8'))

def normalize(body):
    body = re.sub(r'\s+', ' ', body).strip()
    m = re.match(r'^\(defrule\s*(.*?)\s*=>\s*(.*?)\)$', body, re.S)
    if not m:
        return {"predicate": body, "actions": ""}
    return {"predicate": m.group(1).strip(), "actions": m.group(2).strip()}

rules = []
for ordinal, start in enumerate(starts, 1):
    end = matching_end(start)
    body = text[start:end]
    norm = normalize(body)
    jumps = re.findall(r'\(up-jump-rule\s+([^\)]+)\)', body)
    refs = []
    tokens = [
        'gl-build-progress','gl-current-build-item','gl-progression-pause',
        'gl-strategy','SPLIT','set-escrow-percentage','up-modify-escrow',
        'release-escrow','disable-self','up-jump-rule',
        'building-type-count','building-type-count-total','research-completed',
        'research-status','can-build-with-escrow','can-research-with-escrow',
        'can-train-with-escrow'
    ]
    for t in tokens:
        if re.search(r'\b' + re.escape(t) + r'\b', body): refs.append(t)
    rules.append({
        'ordinal': ordinal,
        'byte_start': byte_offset(start),
        'byte_end_exclusive': byte_offset(end),
        'source_line_start': line_no(start),
        'source_line_end': line_no(end),
        'jump_targets_raw': jumps,
        'keywords': refs,
        'predicate': norm['predicate'],
        'actions': norm['actions']
    })

# Explicit fall-through is source-order successor; jump target interpretation is retained raw
# because AoE2 UP jump semantics must be resolved against the donor's actual rule numbering.
for r in rules:
    r['fall_through_ordinal'] = r['ordinal'] + 1 if r['ordinal'] < len(rules) else None

payload = {
    'source_url': URL,
    'expected_sha1': EXPECTED_SHA1,
    'actual_sha1': sha1,
    'byte_length': len(raw),
    'decoded_char_length': len(text),
    'line_count': text.count('\n') + 1,
    'defrule_count': len(rules),
    'rules': rules,
}
OUT.write_text(json.dumps(payload, indent=2), encoding='utf-8')
print(json.dumps({k: payload[k] for k in payload if k != 'rules'}, indent=2))
