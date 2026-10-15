import json,re,sys
STAND={1:'WkxUsh',2:'UNmMYT',3:'TdzrkC',4:'Usxwx9',5:'SAUnJU'}
def strip_ids(o):
    if isinstance(o,dict):
        return {k:strip_ids(v) for k,v in o.items() if k not in ('id','data_id','template_id')}
    if isinstance(o,list): return [strip_ids(x) for x in o]
    return o
def fix_p(m):
    tag=m.group(0)
    s=re.search(r'style="([^"]*)"',tag) or re.search(r"style='([^']*)'",tag)
    st=s.group(1) if s else ''
    add=[]
    if 'line-height' not in st: add.append('line-height:1.6')
    if 'font-size' not in st: add.append('font-size:16px')
    if not add: return tag
    q='"' if (s and s.group(0).startswith('style="')) or not s else "'"
    new=st.rstrip('; ')+(';' if st.strip() else '')+';'.join(add)
    if s: return tag.replace(s.group(0),'style=%s%s%s'%(q,new,q))
    return tag[:-1]+' style="%s">'%new
def fix_html(h):
    h=re.sub(r'<p\b[^>]*>',fix_p,h)
    if '<table' in h:
        h=h.replace('padding:12px 10px;','padding:10px 6px;word-break:normal;overflow-wrap:normal;')
        h=h.replace('font-size:14px;line-height:1.4','font-size:13px;line-height:1.4')
    # trust row / eyebrow-style tiny caps: ease letter spacing
    h=h.replace('font-size:10px; font-weight:600; letter-spacing:2px','font-size:10px; font-weight:600; letter-spacing:1px')
    h=h.replace('font-size:10px;font-weight:600;letter-spacing:2px;text-transform:uppercase;line-height:1.5','font-size:10px;font-weight:600;letter-spacing:1px;text-transform:uppercase;line-height:1.5')
    return h
def walk(o):
    if isinstance(o,dict):
        st=o.get('styles')
        if o.get('type')=='section' and isinstance(o.get('data',{}).get('styles'),dict):
            s=o['data']['styles']
            for k in ('inner_padding_left','inner_padding_right'):
                if isinstance(s.get(k),int) and s[k]>24: s[k]=24
        if o.get('type') in ('text','html') and isinstance(o.get('data',{}).get('content'),str):
            o['data']['content']=fix_html(o['data']['content'])
        for v in o.values(): walk(v)
    elif isinstance(o,list):
        for v in o: walk(v)
if __name__=="__main__":
 for i in range(1,6):
     d=json.load(open(f'e{i}.json'))['result']['data']['attributes']['definition']
     d=strip_ids(d); walk(d)
     json.dump({"data":{"type":"template","id":STAND[i],"attributes":{"definition":d}}},open(f'up{i}.json','w'))
     print(i, len(json.dumps(d)))
