"""Generates index.html (dashboard) + PROGRESS_REPORT.md from one data list.
Run: python build.py
"""
import html, json, os, datetime

OUT = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-09-29"

# status: live | working | progress | blocked | parked | done | archive
# src: 'hermes' (built/worked on in Hermes sessions) | 'folder' (found in F:\ only, not inspected in depth)
P = [
 dict(name="CPU RUSH", cat="Education / Games", src="hermes", status="live", pct=85,
      desc="Interactive OS teaching game. 7 modes: scheduler, page replacement, disk, allocation, deadlock (Banker's), virtual memory, file systems.",
      path=r"C:\Users\MAHESH\OneDrive\Documents\ChatGPT\OS", port=3000, local="http://127.0.0.1:3000/",
      gh="https://github.com/maheshbasavaraj/cpu-rush", last="2026-09-28",
      done="All 7 modes start and return correct puzzle payloads (verify.js all-green); README + GitHub push done; HIT/MISS + controls UI fix.",
      todo="Gameplay/grading not verified end-to-end for every mode; server can serve stale code; no public deploy yet."),
 dict(name="DSDS - Data Structure Design Studio", cat="Education / Games", src="hermes", status="live", pct=90,
      desc="Learn data structures by choosing under constraints: story, pick A-D, score 1-5 with feedback. FastAPI web app, 6-step progressive track.",
      path=r"F:\AI Projects\dsds", port=8000, local="http://127.0.0.1:8000/",
      gh="https://github.com/maheshbasavaraj/dsds", last="2026-08-07",
      done="Web app, tests, Dockerfile, render.yaml, GitHub repo, DEPLOY.md.",
      todo="Render deploy not live (dsds.onrender.com returns 404). Students need a public HTTPS URL."),
 dict(name="Alien Shooter 3D", cat="Games", src="hermes", status="progress", pct=70,
      desc="Three.js 3D shooter built from original game data files: 24 monsters, 10 weapons, campaign + survive modes. Later p5.js remake (index2.html).",
      path=r"F:\AI Projects\alien-shooter-3d", port=8081, local="http://127.0.0.1:8081/index2.html",
      gh="", last="2026-07-06",
      done="Built Jun 8; 5 improvement iterations (sound, reload, hit flash, damage numbers); empty-landscape/no-enemies bug worked on.",
      todo="Session on 29 Sep: add a new gameplay level to the original GameTop Alien Shooter install (in progress). No git repo."),
 dict(name="Kannada Dub (YouTube EN to Kn audio)", cat="AI / Media", src="hermes", status="blocked", pct=65,
      desc="Pipeline: download, ASR (faster-whisper), translate, IndicF5 TTS, mix. Dubbing stays local by choice.",
      path=r"F:\AI Projects\kannada-dub", port=None, local="",
      gh="", last="2026-09-25",
      done="Stages s1 (download/audio split) working; pipeline, docs, verify.py, refs and models in place.",
      todo="GPU ASR crashed on 23 Sep: cublas64_12.dll not found (CUDA runtime). Re-run to confirm whether fixed since."),
 dict(name="Unclutter (OpenRouter provider)", cat="AI Tools", src="hermes", status="progress", pct=60,
      desc="Jev-based browser extension (WXT/TypeScript). Adding OpenRouter as a model provider.",
      path=r"F:\AI Projects\unclutter\unclutter", port=None, local="",
      gh="", last="2026-09-28",
      done="Provider code (lib/providers.ts, lib/model.ts) reviewed and extended in the 28 Sep session.",
      todo="18 uncommitted changes; not confirmed built and tested end-to-end."),
 dict(name="JEV Mail Classifier", cat="AI Tools", src="hermes", status="parked", pct=70,
      desc="Email triage with Jev + OpenRouter. 8 categories (spam, security, receipt, academic, action, personal, newsletter, promotion) with thresholds and actions.",
      path=r"F:\AI Projects\JEVMAIL\jev-mail-classifier", port=None, local="",
      gh="https://github.com/parth-kp/jev-mail-classifier", last="2026-09-21",
      done="config.suggested.yaml built and tested with real Jev calls on subject lines.",
      todo="Parked. Needs IMAP_USERNAME / IMAP_PASSWORD in .env, merge categories into config.yaml, run jev-mail run --dry-run."),
 dict(name="Learning Platform (Game Forge + DSDS + SWE Quiz)", cat="Education / Games", src="hermes", status="progress", pct=75,
      desc="One FastAPI origin hosting three learning modules, Docker compose, single student URL.",
      path=r"F:\AI Projects\project-platform", port=None, local="",
      gh="", last="2026-08-27",
      done="Platform app, hub, Dockerfile, docker-compose, DEPLOY.md, all three modules vendored in.",
      todo="Not deployed publicly; not run in this session (needs Docker Desktop: docker compose up --build, then localhost:8080)."),
 dict(name="Game Forge (Educational Game MCP)", cat="Education / Games", src="hermes", status="working", pct=80,
      desc="MCP server that builds single-file educational browser games. Tools: build_game_prompt, save_game, list_games, review_checklist.",
      path=r"F:\AI Projects\project-platform\game_MCP", port=None, local="",
      gh="https://github.com/maheshbasavaraj/game_MCP", last="2026-08-05",
      done="System prompt, MCP tools, 5 sample games (factorial, fibonacci, fraction-catch, tower-of-hanoi, verify-pipeline), Ollama driver.",
      todo="Run with: python app.py (port 8000, so stop DSDS first or change port)."),
 dict(name="BIOE3 Bio-AI Proposal (DBT-BIRAC)", cat="Research / Writing", src="hermes", status="done", pct=100,
      desc="Full proposal draft for the DBT-BIRAC Bio-AI call: hub-and-spoke consortium, work packages, budget, risks, verified arXiv citations.",
      path=r"F:\AI Projects\BIOE3_BioAI_Proposal", port=None, local="",
      gh="", last="2026-06-19",
      done="Proposal, budget template, quick reference, research notes; supporting arXiv pulls in dbt_birac_bioai/.",
      todo="Call deadline was 30 Jun 2026 (passed). Partner names/PI details were placeholders."),
 dict(name="Socratic Instructor Playbook (OS)", cat="Research / Writing", src="hermes", status="done", pct=100,
      desc="Socratic instructor playbook for an OS syllabus, matched to the structure of the MLOps playbook example.",
      path=r"C:\Users\MAHESH\OneDrive\Documents\ChatGPT\OS", port=None, local="",
      gh="https://github.com/maheshbasavaraj/cpu-rush", last="2026-09-28",
      done="Playbook built; README with syllabus map pushed to GitHub.", todo="None known."),
 dict(name="Agentic-Q paper (revised)", cat="Research / Writing", src="hermes", status="done", pct=90,
      desc="Academic paper polish: reviewer-comment revision and AI-detector humanization.",
      path=r"F:\AI Projects\agentic-q", port=None, local="",
      gh="", last="2026-07-23",
      done="Revised + final DOCX/DOCM, reviewer comment JSONs, rendered output.", todo="Turnitin AI % target (<=30%) not confirmed here."),
 dict(name="Agentic AI - Saksham / FDP", cat="Teaching / FDP", src="hermes", status="working", pct=70,
      desc="Agentic AI faculty-development workspace: App (agents, workflows), game-mcp, patent-prior-art-mcp, Teacher (DSATM-FDP batch 1).",
      path=r"F:\Agentic AI saksham", port=None, local="",
      gh="https://github.com/maheshbasavaraj/Agentic-AI-saksham", last="2026-07-31",
      done="App, MCP servers, Teacher material; private GitHub repo.", todo="Uses fdp\\Scripts\\python.exe. Not run in this session."),
 dict(name="Pi Ad Blocker", cat="AI / Vision", src="folder", status="archive", pct=50,
      desc="Ad-blocker experiments (benchmarks, configs, demo_advanced.py, video checks).",
      path=r"F:\AI Projects\pi-ad-blocker", port=None, local="", gh="", last="2026-06-10",
      done="Code and benchmarks present.", todo="Status not verified; folder inspected only by name."),
 dict(name="Meme Gen / AR Ad Blocker", cat="AI / Vision", src="folder", status="archive", pct=50,
      desc="Meme generator and AR ad-blocker tries (try -1 to Try4, speckit, gemini chat log).",
      path=r"F:\AI Projects\MEME GEN", port=None, local="", gh="", last="2026-09-01",
      done="Multiple attempts kept.", todo="Status not verified."),
 dict(name="Patenter", cat="Research / Writing", src="folder", status="archive", pct=50,
      desc="Patent drafting workspace (forms, DSATM patent, antigravity version).",
      path=r"F:\AI Projects\patenter", port=None, local="", gh="", last="2026-04-26",
      done="Drafts and forms present.", todo="Status not verified."),
 dict(name="PPT Generator", cat="Tools", src="folder", status="archive", pct=60,
      desc="Generates PPT from a given video.", path=r"F:\AI Projects\pptgen", port=None, local="",
      gh="https://github.com/maheshbasavaraj/PPTGenerator", last="2026-04-27",
      done="app.py, main.py, generator, sample output.", todo="Status not verified."),
 dict(name="Certificate Generator", cat="Tools", src="folder", status="archive", pct=80,
      desc="Bulk certificate PDFs from a student list.", path=r"F:\AI Projects\CertificateGen", port=None, local="",
      gh="", last="2026-04-26", done="cert_gen.py with generated certificate PDFs.", todo="Status not verified."),
 dict(name="VTU Marks Extractor", cat="Tools", src="folder", status="done", pct=90,
      desc="Extracts marks from result PDFs into an Excel sheet for the whole class.",
      path=r"F:\AI Projects\MARKS extractor", port=None, local="",
      gh="https://github.com/maheshbasavaraj/VTU-Marks-extracter", last="2026-04-26",
      done="Built exe (dist/build), extracted_marks.xlsx produced.", todo="Status not verified beyond outputs."),
 dict(name="Doc Gen (QP generator)", cat="Tools", src="folder", status="archive", pct=60,
      desc="Question-paper DOCX generator (Deep Learning BCD601).", path=r"F:\AI Projects\Doc gen", port=None, local="",
      gh="", last="2026-04-26", done="generator.py + sample QP.", todo="Status not verified."),
 dict(name="Extropic / Thermodynamic Computing", cat="Research / Writing", src="folder", status="archive", pct=50,
      desc="Papers on thermodynamic computing for fusion energy.", path=r"F:\AI Projects\extropic", port=None, local="",
      gh="", last="2026-04-26", done="Two DOCX drafts, paper.pdf, thrml source.", todo="Status not verified."),
 dict(name="Articles (AI patent white paper, VR edu survey)", cat="Research / Writing", src="folder", status="archive", pct=60,
      desc="White paper and survey drafts.", path=r"F:\AI Projects\Articles", port=None, local="",
      gh="", last="2026-08-20", done="AI_Patent_White_Paper_2025, decentralized VR edu survey, extropic.", todo="Status not verified."),
 dict(name="Lab (Agentic AI, AIML, GenAI)", cat="Teaching / FDP", src="folder", status="archive", pct=60,
      desc="Lab manuals and programs.", path=r"F:\AI Projects\lab", port=None, local="",
      gh="https://github.com/maheshbasavaraj/GENAI_LAB", last="2026-04-26", done="Three lab folders.", todo="Status not verified."),
 dict(name="Quiz / SET / ButterCloud Quiz", cat="Education / Games", src="folder", status="archive", pct=60,
      desc="ButterCloud quiz app with several backups.", path=r"F:\AI Projects\SET", port=None, local="",
      gh="https://github.com/maheshbasavaraj/SWE_QUIZ", last="2026-04-27", done="App + backups.", todo="Status not verified."),
 dict(name="YouTube Channel content", cat="AI / Media", src="folder", status="archive", pct=40,
      desc="Story scripts and prompts, sample video.", path=r"F:\AI Projects\youtube channel", port=None, local="",
      gh="", last="2026-04-27", done="Scripts and one MP4.", todo="Status not verified."),
 dict(name="Agent (Telegram to WhatsApp)", cat="AI Tools", src="folder", status="archive", pct=50,
      desc="Agent scripts incl. telegram_to_whatsapp_agent.py.", path=r"F:\AI Projects\Agent", port=None, local="",
      gh="https://github.com/maheshbasavaraj/Agent_fdp", last="2026-04-26", done="Scripts + README.", todo="Status not verified."),
 dict(name="Face Recognition / Anti-Spoofing", cat="AI / Vision", src="folder", status="archive", pct=50,
      desc="Face recognition with Silent-Face-Anti-Spoofing.", path=r"F:\face recog", port=None, local="",
      gh="", last="2026-06-04", done="Student face data and spoof repo.", todo="Status not verified."),
 dict(name="CI/CD demos (CICD, mlops-cicd)", cat="DevOps", src="folder", status="done", pct=90,
      desc="CI/CD demo with train.py and tests; MLOps pipeline.", path=r"F:\CICD", port=None, local="",
      gh="https://github.com/maheshbasavaraj/mlops-cicd", last="2026-09-01", done="Repos pushed (CICD, CI, cd, mlops-cicd).", todo="None known."),
 dict(name="ComfyUI + Wan2GP (media gen)", cat="AI / Media", src="folder", status="working", pct=60,
      desc="Local image/video generation installs.", path=r"F:\comfiUI", port=None, local="",
      gh="", last="2026-05-28", done="ComfyUI-Easy-Install; Wan2GP in F:\\WANGP.", todo="Status not verified."),
]

STATUS = {
 "live": ("Live", "#22c55e"), "working": ("Working", "#38bdf8"), "progress": ("In progress", "#f59e0b"),
 "blocked": ("Blocked", "#ef4444"), "parked": ("Parked", "#a78bfa"), "done": ("Done", "#10b981"),
 "archive": ("Archived / unverified", "#94a3b8"),
}
e = html.escape

def furl(p):
    return "file:///" + p.replace("\\", "/").replace(" ", "%20")

def card(i, p):
    lab, col = STATUS[p["status"]]
    links = [f'<a href="{e(furl(p["path"]))}">Folder</a>']
    if p["local"]:
        links.insert(0, f'<a class="go" href="{e(p["local"])}" target="_blank">Open live</a>')
    if p["gh"]:
        links.append(f'<a href="{e(p["gh"])}" target="_blank">GitHub</a>')
    ping = f' data-port="{p["port"]}" data-url="{e(p["local"])}"' if p["port"] else ""
    pill = f'<span class="ping" id="ping{i}">checking...</span>' if p["port"] else ""
    origin = "built in Hermes" if p["src"] == "hermes" else "found in F: folders"
    return f'''<article class="card" data-status="{p["status"]}" data-src="{p["src"]}" data-cat="{e(p["cat"])}" data-q="{e((p["name"]+" "+p["desc"]+" "+p["cat"]).lower())}"{ping} data-i="{i}">
<header><h3>{e(p["name"])}</h3><span class="st" style="--c:{col}">{lab}</span></header>
<p class="meta">{e(p["cat"])} &middot; last change {p["last"]} &middot; {origin} {pill}</p>
<p>{e(p["desc"])}</p>
<div class="bar"><i style="width:{p["pct"]}%;background:{col}"></i></div><small>{p["pct"]}% (estimate)</small>
<details><summary>Progress report</summary><p><b>Done:</b> {e(p["done"])}</p><p><b>Open / next:</b> {e(p["todo"])}</p><p class="path">{e(p["path"])}</p></details>
<nav>{" ".join(links)}</nav></article>'''

cards = "\n".join(card(i, p) for i, p in enumerate(P))
counts = {k: sum(1 for p in P if p["status"] == k) for k in STATUS}
chips = "".join(f'<button class="chip" data-f="{k}"><b style="color:{STATUS[k][1]}">{counts[k]}</b> {STATUS[k][0]}</button>' for k in STATUS if counts[k])
avg = round(sum(p["pct"] for p in P) / len(P))
hermes_n = sum(1 for p in P if p["src"] == "hermes")

rows = "\n".join(
    f'<tr><td>{e(p["name"])}</td><td><span class="st" style="--c:{STATUS[p["status"]][1]}">{STATUS[p["status"]][0]}</span></td><td>{p["pct"]}%</td><td>{e(p["done"])}</td><td>{e(p["todo"])}</td></tr>'
    for p in P)

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mahesh - Projects Dashboard</title>
<style>
:root{{--bg:#0b1020;--card:#131a2e;--bd:#25304d;--fg:#e6eaf5;--mu:#8b97b5;--ac:#6ea8fe}}
*{{box-sizing:border-box}}body{{margin:0;font:14px/1.5 system-ui,Segoe UI,sans-serif;background:var(--bg);color:var(--fg)}}
.wrap{{max-width:1300px;margin:0 auto;padding:24px}}h1{{margin:0 0 4px;font-size:26px}}.sub{{color:var(--mu);margin-bottom:18px}}
.kpis{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin-bottom:18px}}
.kpi{{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:14px}}.kpi b{{font-size:26px;display:block}}.kpi span{{color:var(--mu)}}
.tools{{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px;align-items:center}}
input[type=search]{{flex:1;min-width:220px;padding:9px 12px;border-radius:10px;border:1px solid var(--bd);background:var(--card);color:var(--fg)}}
.chip{{background:var(--card);color:var(--fg);border:1px solid var(--bd);border-radius:999px;padding:6px 12px;cursor:pointer}}.chip.on{{border-color:var(--ac);background:#1b2748}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(360px,1fr));gap:14px}}
.card{{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:6px}}
.card header{{display:flex;justify-content:space-between;gap:8px;align-items:flex-start}}.card h3{{margin:0;font-size:16px}}
.st{{background:color-mix(in srgb,var(--c) 18%,transparent);color:var(--c);border:1px solid var(--c);padding:1px 9px;border-radius:999px;font-size:12px;white-space:nowrap}}
.meta{{color:var(--mu);font-size:12px;margin:0}}.card p{{margin:2px 0}}
.bar{{height:7px;background:#0d1326;border-radius:6px;overflow:hidden;margin-top:4px}}.bar i{{display:block;height:100%}}small{{color:var(--mu)}}
details{{background:#0f1730;border-radius:8px;padding:6px 10px}}summary{{cursor:pointer;color:var(--ac)}}.path{{font-family:Consolas,monospace;font-size:12px;color:var(--mu);word-break:break-all}}
nav{{margin-top:auto;display:flex;gap:8px;flex-wrap:wrap;padding-top:6px}}nav a{{color:var(--ac);border:1px solid var(--bd);border-radius:8px;padding:4px 10px;text-decoration:none}}nav a.go{{background:var(--ac);color:#06122b;border-color:var(--ac);font-weight:600}}
.ping{{font-weight:600}}.ping.up{{color:#22c55e}}.ping.down{{color:#ef4444}}
h2{{margin:34px 0 10px}}table{{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--bd);border-radius:12px;overflow:hidden}}
th,td{{text-align:left;padding:8px 10px;border-bottom:1px solid var(--bd);vertical-align:top;font-size:13px}}th{{background:#0f1730;color:var(--mu)}}
.note{{color:var(--mu);font-size:12px;margin-top:20px}}
</style></head><body><div class="wrap">
<h1>Projects Dashboard</h1>
<div class="sub">Everything built in Hermes + everything under F:\\AI Projects. Generated {TODAY}. Live badges ping your local servers when you open this page.</div>
<div class="kpis">
<div class="kpi"><b>{len(P)}</b><span>projects tracked</span></div>
<div class="kpi"><b>{hermes_n}</b><span>built/worked in Hermes</span></div>
<div class="kpi"><b id="liveN">-</b><span>servers up right now</span></div>
<div class="kpi"><b>{avg}%</b><span>average progress (estimate)</span></div>
<div class="kpi"><b>{counts["blocked"]+counts["parked"]}</b><span>blocked / parked</span></div>
</div>
<div class="tools"><input type="search" id="q" placeholder="Search projects...">
<button class="chip on" data-f="all">All</button><button class="chip" data-f="hermes">Built in Hermes</button>{chips}</div>
<section class="grid" id="grid">
{cards}
</section>
<h2>Progress report</h2>
<table><thead><tr><th>Project</th><th>Status</th><th>Progress</th><th>Done</th><th>Open / next</th></tr></thead><tbody>
{rows}
</tbody></table>
<p class="note">Method: "Built in Hermes" statuses come from your Hermes session history and verified checks. "Archived / unverified" entries were only identified by folder name, contents and last-modified date; their progress % is a rough guess. Folder dates are top-level modification times.</p>
</div>
<script>
const cards=[...document.querySelectorAll('.card')];let f='all',q='';
function apply(){{cards.forEach(c=>{{const okF=f==='all'||c.dataset.status===f||(f==='hermes'&&c.dataset.src==='hermes');
c.style.display=(okF&&c.dataset.q.includes(q))?'':'none'}})}}
document.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));b.classList.add('on');f=b.dataset.f;apply()}});
document.getElementById('q').oninput=e=>{{q=e.target.value.toLowerCase();apply()}};
let up=0,total=0;
async function ping(){{up=0;total=0;await Promise.all(cards.filter(c=>c.dataset.port).map(async c=>{{total++;const el=document.getElementById('ping'+c.dataset.i);
try{{const ctl=new AbortController();setTimeout(()=>ctl.abort(),2500);await fetch('http://127.0.0.1:'+c.dataset.port+'/',{{mode:'no-cors',signal:ctl.signal}});
el.textContent='UP :'+c.dataset.port;el.className='ping up';up++}}catch(_){{el.textContent='DOWN :'+c.dataset.port;el.className='ping down'}}}}));
document.getElementById('liveN').textContent=up+'/'+total}}
ping();setInterval(ping,15000);
</script></body></html>'''

open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)

md = [f"# Projects Progress Report ({TODAY})\n", f"{len(P)} projects tracked; {hermes_n} built/worked in Hermes; average progress {avg}% (estimate).\n",
      "| Project | Status | % | Done | Open / next |", "|---|---|---|---|---|"]
for p in P:
    md.append(f'| {p["name"]} | {STATUS[p["status"]][0]} | {p["pct"]}% | {p["done"]} | {p["todo"]} |')
md.append("\n_Archived/unverified entries were identified by folder name, contents and dates only._\n")
open(os.path.join(OUT, "PROGRESS_REPORT.md"), "w", encoding="utf-8").write("\n".join(md))
print("ok", len(P), "projects; counts", counts)
