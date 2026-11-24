from pathlib import Path
import cairosvg

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT/'docs'
DOCS.mkdir(exist_ok=True)

system_svg = r'''<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="970" viewBox="0 0 1500 970">
<defs>
 <marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#52677f"/></marker>
 <marker id="bluearr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#2864c8"/></marker>
 <style>
 .title{font:700 30px Arial;fill:#17283b}.sub{font:16px Arial;fill:#6a7b8e}.head{font:700 18px Arial;fill:#20364c}.body{font:15px Arial;fill:#526579}.tiny{font:700 13px Arial;fill:#ffffff}.line{stroke:#52677f;stroke-width:3;fill:none;marker-end:url(#arr)}.blue{stroke:#2864c8;stroke-width:3;fill:none;marker-end:url(#bluearr)}
 </style>
</defs>
<rect width="1500" height="970" fill="#f4f7fb"/>
<text x="55" y="62" class="title">Northstar Operations — system architecture</text>
<text x="55" y="94" class="sub">Local, rule-based simulation of progressive mixed-initiative layout adaptation</text>
<!-- user -->
<rect x="55" y="180" width="230" height="125" rx="18" fill="#fff" stroke="#cbd7e5" stroke-width="2"/>
<text x="82" y="222" class="head">User interaction</text><text x="82" y="255" class="body">Focus a monitoring panel</text><text x="82" y="280" class="body">Accept / reject / undo</text>
<!-- logger -->
<rect x="375" y="180" width="245" height="125" rx="18" fill="#eaf1ff" stroke="#8eb1ef" stroke-width="2"/>
<text x="402" y="222" class="head">Interaction logger</text><text x="402" y="255" class="body">Per-session focus counts</text><text x="402" y="280" class="body">Layout action history</text>
<!-- store -->
<rect x="720" y="180" width="260" height="125" rx="18" fill="#eaf7f4" stroke="#7dbbac" stroke-width="2"/>
<text x="747" y="222" class="head">Local preference store</text><text x="747" y="255" class="body">Accepted / rejected changes</text><text x="747" y="280" class="body">Browser localStorage</text>
<!-- policy -->
<rect x="1080" y="180" width="350" height="125" rx="18" fill="#fff5e7" stroke="#e9b86c" stroke-width="2"/>
<text x="1107" y="222" class="head">Adaptation policy engine</text><text x="1107" y="255" class="body">Deterministic rules, not trained ML</text><text x="1107" y="280" class="body">Two focuses + acceptance history</text>
<!-- connectors top -->
<path d="M285 242 H375" class="line"/><path d="M620 242 H720" class="line"/><path d="M980 242 H1080" class="line"/>
<!-- decision box -->
<path d="M1255 305 V385" class="line"/>
<polygon points="1255,385 1400,465 1255,545 1110,465" fill="#fff" stroke="#d5a34f" stroke-width="2"/>
<text x="1255" y="453" text-anchor="middle" class="head">Decision</text><text x="1255" y="480" text-anchor="middle" class="body">Auto enabled and</text><text x="1255" y="503" text-anchor="middle" class="body">2 accepts already?</text>
<!-- recommendation -->
<rect x="720" y="405" width="300" height="145" rx="18" fill="#fff" stroke="#8eb1ef" stroke-width="2"/>
<text x="747" y="447" class="head">Recommendation state</text><text x="747" y="480" class="body">Explain observed focus pattern</text><text x="747" y="505" class="body">Ask user to apply or keep</text><text x="747" y="530" class="body">Implemented</text>
<!-- automatic -->
<rect x="1080" y="625" width="350" height="125" rx="18" fill="#e8f7f2" stroke="#79b8a8" stroke-width="2"/>
<text x="1107" y="667" class="head">Automatic low-risk change</text><text x="1107" y="700" class="body">Reorder one panel only</text><text x="1107" y="725" class="body">Undo remains available · Implemented</text>
<!-- dashboard -->
<rect x="375" y="625" width="340" height="125" rx="18" fill="#fff" stroke="#8eb1ef" stroke-width="2"/>
<text x="402" y="667" class="head">Dashboard renderer</text><text x="402" y="700" class="body">Four illustrative monitoring panels</text><text x="402" y="725" class="body">Reorders the visual layout · Implemented</text>
<!-- policy flow -->
<path d="M1110 465 H1020" class="blue"/><text x="1058" y="445" text-anchor="middle" class="body">No / new preference</text>
<path d="M1255 545 V625" class="blue"/><text x="1290" y="590" class="body">Yes</text>
<path d="M720 500 C680 535 650 570 650 625" class="blue"/><text x="650" y="575" class="body" text-anchor="middle">If accepted</text>
<!-- renderer feedback loops -->
<path d="M1080 687 H715" class="blue"/><path d="M545 625 V540 H190 V305" class="line"/>
<text x="845" y="671" class="body" text-anchor="middle">Render updated layout</text>
<text x="235" y="515" class="body">Feedback / undo</text>
<!-- labels -->
<rect x="720" y="790" width="710" height="78" rx="14" fill="#fff" stroke="#9aa9b8" stroke-width="2" stroke-dasharray="8 6"/>
<text x="745" y="822" class="head">Planned extensions</text><text x="745" y="848" class="body">Task-context signals · editable preferences · panel locks · longitudinal user evaluation</text>
<rect x="55" y="892" width="17" height="17" rx="4" fill="#eaf1ff" stroke="#8eb1ef"/><text x="82" y="906" class="body">Implemented in prototype</text>
<rect x="365" y="892" width="17" height="17" rx="4" fill="#fff5e7" stroke="#e9b86c"/><text x="392" y="906" class="body">Simulated rule-based decision logic</text>
<rect x="720" y="892" width="17" height="17" rx="4" fill="#fff" stroke="#9aa9b8" stroke-dasharray="4 3"/><text x="747" y="906" class="body">Planned, not implemented</text>
<text x="55" y="944" class="sub">No cloud service, trained model, database server or live equipment connection is included in the current scope.</text>
</svg>'''
(DOCS/'system-architecture.svg').write_text(system_svg, encoding='utf-8')
cairosvg.svg2png(bytestring=system_svg.encode(), write_to=str(DOCS/'system-architecture.png'), output_width=1500, output_height=970)

# Three-row storyboard illustration (3 states per scenario)
W,H=1500,1040
parts=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><style>
.title{{font:700 29px Arial;fill:#17283b}}.rowtitle{{font:700 19px Arial;fill:#20364c}}.step{{font:700 14px Arial;fill:#fff}}.txt{{font:15px Arial;fill:#506276}}.small{{font:13px Arial;fill:#708095}}.paneltitle{{font:700 14px Arial;fill:#24384d}}.paneltxt{{font:12px Arial;fill:#728196}}.btn{{font:700 12px Arial;fill:#fff}}.box{{fill:#fff;stroke:#d7e0ea;stroke-width:2}}.arrow{{stroke:#8192a5;stroke-width:3;fill:none;marker-end:url(#arr)}}
</style><marker id="arr" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#8192a5"/></marker></defs>
<rect width="100%" height="100%" fill="#f4f7fb"/>
<text x="50" y="55" class="title">Progressive adaptive dashboard — interaction storyboards</text>
<text x="50" y="85" class="small">Illustrated sequences based on the implemented browser prototype</text>
''']

def txt(x,y,cls,s):
    return f'<text x="{x}" y="{y}" class="{cls}">{s}</text>'
def card(x,y,w,h,head,body,fill='#ffffff',stroke='#d7e0ea'):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" fill="{fill}" stroke="{stroke}" stroke-width="2"/>' + txt(x+16,y+27,'paneltitle',head) + txt(x+16,y+47,'paneltxt',body)
def button(x,y,label,blue=False):
    fill='#2864c8' if blue else '#65778c'
    return f'<rect x="{x}" y="{y}" width="{len(label)*7+26}" height="30" rx="7" fill="{fill}"/>' + txt(x+13,y+20,'btn',label)
# helpers per row
row_specs=[
    ('1  Recommendation and acceptance','A new user has not yet established a stable preference. The system asks before it changes the layout.'),
    ('2  Rejection and stability','The user decides the suggestion is not useful. The layout remains unchanged and the prompt is suppressed for that session.'),
    ('3  Learned automation and recovery','After two accepted recommendations, the same low-risk change is applied automatically in a later session. Undo remains available.')
]
start_y=120
for idx,(title,desc) in enumerate(row_specs):
    y=start_y+idx*300
    parts.append(txt(50,y,'rowtitle',title))
    parts.append(txt(50,y+25,'small',desc))
    xs=[50,545,1040]
    # step cards
    for n,x in enumerate(xs):
        parts.append(f'<rect x="{x}" y="{y+45}" width="410" height="205" rx="16" class="box"/>')
        parts.append(f'<circle cx="{x+26}" cy="{y+72}" r="15" fill="#2864c8"/><text x="{x+26}" y="{y+77}" text-anchor="middle" class="step">{n+1}</text>')
    parts.append(f'<path d="M460 {y+150} H530" class="arrow"/><path d="M955 {y+150} H1025" class="arrow"/>')
    if idx==0:
        parts += [txt(95,y+120,'paneltitle','User action'),txt(95,y+147,'txt','Focus “Maintenance queue” twice.'),card(95,y+157,300,52,'Maintenance queue','Focused 2 times this session','#f7faff','#b6cafa'),
                  txt(590,y+120,'paneltitle','System response'),txt(590,y+147,'txt','Explains the observed pattern.'),card(590,y+157,300,52,'Move Maintenance queue to top?','Apply or keep current layout','#f7faff','#b6cafa'),
                  txt(1085,y+120,'paneltitle','User control'),txt(1085,y+147,'txt','Accepts the suggestion.'),card(1085,y+157,300,52,'Layout updated','Maintenance queue moves to first','#eaf7f4','#94cbbb')]
    elif idx==1:
        parts += [txt(95,y+120,'paneltitle','User action'),txt(95,y+147,'txt','Focus “Throughput” twice.'),card(95,y+157,300,52,'Throughput','Focused 2 times this session','#f7faff','#b6cafa'),
                  txt(590,y+120,'paneltitle','System response'),txt(590,y+147,'txt','Offers a reasoned recommendation.'),card(590,y+157,300,52,'Move Throughput to top?','No change has happened yet','#f7faff','#b6cafa'),
                  txt(1085,y+120,'paneltitle','User control'),txt(1085,y+147,'txt','Chooses “Keep current layout”.'),card(1085,y+157,300,52,'Suggestion dismissed','Existing panel order is preserved','#fff6e7','#edc47e')]
    else:
        parts += [txt(95,y+120,'paneltitle','Learning across sessions'),txt(95,y+147,'txt','Two earlier suggestions were accepted.'),card(95,y+157,300,52,'Preference learned','Same low-risk change accepted twice','#eaf7f4','#94cbbb'),
                  txt(590,y+120,'paneltitle','Automatic response'),txt(590,y+147,'txt','Next session: same focus pattern.'),card(590,y+157,300,52,'Automatic adjustment','Panel moves to first position','#eaf7f4','#94cbbb'),
                  txt(1085,y+120,'paneltitle','Recovery and control'),txt(1085,y+147,'txt','Uses Undo or pauses automation.'),card(1085,y+157,300,52,'Layout restored','Future change requires confirmation','#f7faff','#b6cafa')]
parts.append('<text x="50" y="1010" class="small">All values and operational panels are illustrative. Storyboards describe prototype behaviour, not a deployed industrial system.</text></svg>')
story_svg=''.join(parts)
(DOCS/'interaction-storyboards.svg').write_text(story_svg,encoding='utf-8')
cairosvg.svg2png(bytestring=story_svg.encode(), write_to=str(DOCS/'interaction-storyboards.png'), output_width=W, output_height=H)
print('Created diagrams')
