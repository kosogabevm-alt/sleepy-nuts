P={'メイプル':('#e8590c',['ジェット','チェンバー']),'はれ':('#d6336c',['フェニックス','ネオン','レイズ']),'ふかみ':('#1c7ed6',['フェイド','ソーヴァ']),'ストリング':('#7048e8',['オーメン','ハーバー']),'しー':('#2b8a3e',['サイファー','キルジョイ','セージ'])}
ORDER=list(P)
# plans: map -> list of (label, {player: agent}, memo)
def pl(**k): return k
MAPS=[
 ('アセント',[('メイン',pl(メイプル='ジェット',はれ='フェニックス',ふかみ='ソーヴァ',ストリング='オーメン',しー='キルジョイ'))],'プロ定番に近い形（キルジョイ→サイファー版がプロで最多、100 Thieves 4-0）'),
 ('ヘイヴン',[('メイン',pl(メイプル='ジェット',はれ='フェニックス',ふかみ='ソーヴァ',ストリング='オーメン',しー='キルジョイ'))],'プロではヘイヴンのジェット採用は少なめ（勝率30%）'),
 ('スプリット',[('A案',pl(メイプル='チェンバー',はれ='ネオン',ふかみ='フェイド',ストリング='オーメン',しー='セージ')),('B案',pl(メイプル='ジェット',はれ='レイズ',ふかみ='スカイ※',ストリング='オーメン',しー='サイファー'))],'プロはオーメン＋ヴァイパーのスモーク2枚が基本 ／ ※スカイは担当外'),
 ('ロータス',[('メイン',pl(メイプル='ジェット',はれ='フェニックス',ふかみ='フェイド',ストリング='オーメン',しー='サイファー'))],'プロはレイズ採用が主流（Team Liquid：ジェット・レイズ・フェイド・オーメン・サイファーで5勝2敗）'),
 ('サンセット',[('A案',pl(メイプル='ジェット',はれ='フェニックス',ふかみ='ソーヴァ',ストリング='オーメン',しー='サイファー')),('B案',pl(メイプル='チェンバー',はれ='ネオン',ふかみ='ソーヴァ',ストリング='オーメン',しー='セージ'))],'B案はプロで8勝3敗（LOUD 5-1）'),
 ('アビス',[('メイン',pl(メイプル='ジェット',はれ='フェニックス',ふかみ='ソーヴァ',ストリング='ハーバー / オーメン',しー='サイファー'))],'ハーバー版は100 Thievesが同じ構成で勝利。ハーバー推奨'),
 ('サミット',[('A案',pl(メイプル='チェンバー',はれ='ネオン',ふかみ='ソーヴァ',ストリング='ハーバー / オーメン',しー='セージ')),('B案',pl(メイプル='ジェット',はれ='フェニックス',ふかみ='ソーヴァ',ストリング='オーメン / ハーバー',しー='サイファー'))],'A案はソーヴァ→フェイド、オーメンでプロ定番（9勝5敗、LOUD・Gen.G）'),
]
def chip(p,a): c=P[p][0]; return f'<span class="ag" style="--c:{c}">{a}</span>'
th=''.join(f'<th style="--c:{P[p][0]}"><span class="pn">{p}</span><small>{"・".join(P[p][1])}</small></th>' for p in ORDER)
rows=''
for m,plans,memo in MAPS:
    for i,(lab,a) in enumerate(plans):
        rows+='<tr>'+(f'<td class="map" rowspan="{len(plans)}">{m}</td>' if i==0 else '')+f'<td class="lab">{lab}</td>'+''.join(f'<td>{chip(p,a[p])}</td>' for p in ORDER)+(f'<td class="memo" rowspan="{len(plans)}">{memo}</td>' if i==0 else '')+'</tr>'
cards=''
for m,plans,memo in MAPS:
    body=''
    for lab,a in plans:
        body+=f'<div class="plan"><span class="pl">{lab}</span>'+''.join(f'<div class="li"><span class="who" style="--c:{P[p][0]}">{p}</span>{a[p]}</div>' for p in ORDER)+'</div>'
    cards+=f'<div class="card"><h3>{m}</h3>{body}<p class="m">{memo}</p></div>'
roster=''.join(f'<div class="r" style="--c:{P[p][0]}"><b>{p}</b><span>{"・".join(P[p][1])}</span></div>' for p in ORDER)
html=f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><style>
@page{{size:A4 landscape;margin:12mm}}
body{{font-family:"IPAPGothic","IPAGothic",sans-serif;color:#222;margin:0}}
h1{{font-size:20px;margin:0 0 4px}} .sub{{color:#666;font-size:10px;margin:0 0 10px}}
h2{{font-size:14px;border-left:5px solid #333;padding-left:8px;margin:14px 0 8px}}
.roster{{display:flex;gap:8px;margin-bottom:6px}} .r{{flex:1;border:2px solid var(--c);border-radius:8px;padding:5px 8px;font-size:11px}} .r b{{color:var(--c);font-size:13px;display:block}}
table{{border-collapse:collapse;width:100%;font-size:13px}} th,td{{border:1px solid #ccc;padding:8px 5px;text-align:center;vertical-align:middle}}
th{{background:var(--c,#444);color:#fff}} th small{{display:block;font-weight:normal;font-size:8.5px;opacity:.9}} .pn{{font-size:12px}}
td.map{{font-weight:bold;font-size:13px;background:#f3f3f3}} td.lab{{font-size:10px;color:#555}} td.memo{{text-align:left;font-size:10.5px;color:#555;width:23%}}
.ag{{display:inline-block;border:1.5px solid var(--c);color:var(--c);border-radius:12px;padding:2px 8px;font-weight:bold}}
.cards{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}} .card{{border:1px solid #ccc;border-radius:8px;padding:8px;break-inside:avoid}}
.card h3{{margin:0 0 6px;font-size:14px}} .plan{{margin-bottom:6px}} .pl{{font-size:9px;background:#eee;border-radius:4px;padding:1px 6px}}
.li{{font-size:13px;margin:4px 0}} .who{{display:inline-block;width:56px;font-size:9.5px;color:#fff;background:var(--c);border-radius:4px;text-align:center;margin-right:6px;padding:1px 0}}
.m{{font-size:8.5px;color:#666;margin:4px 0 0;border-top:1px dashed #ddd;padding-top:4px}}
.pb{{page-break-before:always}}
</style></head><body>
<h1>マップ別 構成表（担当プレイヤー別）</h1><p class="sub">メモ欄はVCT 2026（Pacific・EMEA・Americas ステージ2＋Champions上海）のプロ試合データより</p>
<h2>担当キャラ</h2><div class="roster">{roster}</div>
<h2>マップ × プレイヤー表</h2>
<table><tr><th style="--c:#444">マップ</th><th style="--c:#444">案</th>{th}<th style="--c:#444">メモ（プロデータ）</th></tr>{rows}</table>
<div class="pb"></div><h1>マップ別 構成一覧</h1><p class="sub">左の色ラベル＝担当プレイヤー</p>
<div class="cards">{cards}</div>
</body></html>'''
open('team_comps.html','w').write(html)
