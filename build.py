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
# ============================================================
#  Renderer: Mission-control dashboard (single-file, no deps)
# ============================================================
import json as _json
import datetime as _dt
import math as _math
import hashlib
import colorsys
import random as _rndlib

# ---------- colour helpers (cover art) ----------
def _hex2hsl(hx):
    hx = hx.lstrip("#")
    r, g, b = (int(hx[i:i + 2], 16) / 255 for i in (0, 2, 4))
    return colorsys.rgb_to_hls(r, g, b)


def _hsl(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h % 1.0, l, s)
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))


# ---------- generated cover art (deterministic per project) ----------
FAMILY = {
    "Education / Games": "sky", "Games": "sky", "Teaching / FDP": "sky",
    "AI / Media": "wave", "AI / Vision": "cell",
    "AI Tools": "flow", "DevOps": "flow",
    "Tools": "code", "Research / Writing": "code",
}


def _rng(name):
    seed = int(hashlib.md5(name.encode("utf-8")).hexdigest()[:8], 16)
    r = _rndlib.Random(seed)
    return r


def cover_svg(p, w=420, h=156):
    """Unique inline SVG cover for one project - no external images, no network."""
    col = STATUS[p["status"]][1]
    hue, _, _ = _hex2hsl(col)
    # keep the status family, but rotate per project so same-status covers differ
    rot = (_rng(p["name"] + "|rot").random() - 0.5) * 0.34
    hue = (hue + rot) % 1.0
    r = _rng(p["name"])
    deep = _hsl(hue, 0.55, 0.045)
    mid = _hsl((hue + 0.08) % 1.0, 0.50, 0.10)
    hi = _hsl((hue + 0.13) % 1.0, 0.72, 0.30)
    acc = _hsl(hue, 0.90, 0.66)
    acc2 = _hsl((hue + 0.55) % 1.0, 0.85, 0.70)
    # a true-status-colour highlight keeps every card reading as its real status
    flag = col
    gid = "cg" + hashlib.md5(f"{p['name']}|{w}x{h}".encode()).hexdigest()[:8]
    out = [f'<svg class="coverart" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">',
           f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">'
           f'<stop offset="0%" stop-color="{mid}"/><stop offset="55%" stop-color="{deep}"/>'
           f'<stop offset="100%" stop-color="{hi}"/></linearGradient>'
           f'<radialGradient id="{gid}s" cx="18%" cy="12%" r="80%">'
           f'<stop offset="0%" stop-color="{acc}" stop-opacity=".34"/>'
           f'<stop offset="100%" stop-color="{acc}" stop-opacity="0"/></radialGradient></defs>',
           f'<rect width="{w}" height="{h}" fill="url(#{gid})"/>',
           f'<rect width="{w}" height="{h}" fill="url(#{gid}s)"/>']

    # star dust, shared by every family
    for _ in range(int(r.uniform(26, 44))):
        x, y = round(r.uniform(0, w), 1), round(r.uniform(0, h), 1)
        rr = round(r.uniform(0.4, 1.5), 2)
        o = round(r.uniform(0.10, 0.55), 2)
        out.append(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="#fff" opacity="{o}"/>')

    fam = FAMILY.get(p["cat"], "code")
    # per-project structural variant, so two projects in one family never compose alike
    vseed = _rng(p["name"] + "|var")
    layout = vseed.choice(["center", "left", "right", "full", "band"])

    if fam == "sky":  # skyline / orbital ring / radar sweep
        if layout == "center":
            mx, my = w * 0.5, h * 0.42
            mr = 26
            out.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{mr}" fill="{acc}" opacity=".26"/>')
            out.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{mr * 0.62:.1f}" fill="{acc}" opacity=".30"/>')
            out.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{mr * 0.30:.1f}" fill="{acc2}" opacity=".55"/>')
            for rr, op in ((mr * 1.7, .22), (mr * 2.3, .14), (mr * 3.0, .08)):
                out.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="{rr:.1f}" fill="none" '
                           f'stroke="{acc}" stroke-width="1" opacity="{op}"/>')
            bx = 0
            while bx < w:
                bw = round(r.uniform(14, 34), 1)
                bh = round(r.uniform(14, 48), 1)
                out.append(f'<rect x="{bx}" y="{round(h - bh, 1)}" width="{bw}" height="{bh}" '
                           f'fill="#02040c" opacity="{round(r.uniform(0.45, 0.8), 2)}"/>')
                bx += bw + round(r.uniform(3, 9), 1)
        elif layout == "left":
            mx, my, mr = round(r.uniform(w * 0.24, w * 0.34), 1), round(r.uniform(30, 50), 1), round(r.uniform(20, 30), 1)
            out.append(f'<circle cx="{mx}" cy="{my}" r="{mr}" fill="{acc}" opacity=".24"/>')
            out.append(f'<circle cx="{mx}" cy="{my}" r="{round(mr * 0.34, 1)}" fill="{acc2}" opacity=".6"/>')
            bx = 0
            while bx < w:
                bw = round(r.uniform(16, 40), 1)
                bh = round(r.uniform(20, 66), 1)
                out.append(f'<rect x="{bx}" y="{round(h - bh, 1)}" width="{bw}" height="{bh}" '
                           f'fill="#02040c" opacity="{round(r.uniform(0.45, 0.82), 2)}"/>')
                for wy in range(int(h - bh) + 8, h - 4, 11):
                    for wx in range(int(bx) + 5, int(bx + bw) - 4, 9):
                        if r.random() < 0.32:
                            out.append(f'<rect x="{wx}" y="{wy}" width="3" height="4" fill="{flag}" opacity=".5"/>')
                bx += bw + round(r.uniform(3, 11), 1)
            out.append(f'<rect x="0" y="{h - 2}" width="{w}" height="2" fill="{flag}" opacity=".5"/>')
        else:  # radar sweep
            cx, cy = w * 0.5, h * 1.02
            for rr in (h * 0.45, h * 0.75, h * 1.05, h * 1.35):
                out.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{rr:.1f}" fill="none" '
                           f'stroke="{acc}" stroke-width="1" opacity=".26"/>')
            out.append(f'<path d="M{cx:.1f} {cy:.1f} L{cx - h * 0.7:.1f} {cy - h * 0.95:.1f} Z" fill="{acc}" opacity=".12"/>')
            for k in range(9):
                ang = r.uniform(-2.5, -0.65)
                px = cx + _math.cos(ang) * h * r.uniform(0.5, 1.3)
                py = cy + _math.sin(ang) * h * r.uniform(0.5, 1.3)
                if -20 < px < w + 20 and -20 < py < h + 20:
                    out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{round(r.uniform(2, 5), 1)}" '
                               f'fill="{acc2}" opacity="{round(r.uniform(0.3, 0.8), 2)}"/>')
            out.append(f'<rect x="0" y="0" width="{w}" height="2" fill="{flag}" opacity=".4"/>')

    elif fam == "wave":  # audio / spectrum bars
        n = 30
        bw = (w - 30) / n
        for i in range(n):
            env = _math.sin(_math.pi * (i / (n - 1)))
            bh = max(4, (h * 0.74) * env * r.uniform(0.28, 1.0))
            x = 15 + i * bw
            c = acc if i % 3 == 0 else (acc2 if i % 5 == 0 else hi)
            out.append(f'<rect x="{round(x, 1)}" y="{round((h - bh) / 2, 1)}" width="{round(bw * 0.56, 1)}" '
                       f'height="{round(bh, 1)}" rx="{round(bw * 0.28, 1)}" fill="{c}" '
                       f'opacity="{round(0.35 + 0.5 * env, 2)}"/>')
        out.append(f'<circle cx="{round(w * 0.5, 1)}" cy="{round(h * 0.5, 1)}" r="3.4" fill="#fff" opacity=".7"/>')

    elif fam == "cell":  # molecular lattice
        nodes = [(round(r.uniform(28, w - 28), 1), round(r.uniform(26, h - 22), 1)) for _ in range(11)]
        for i, (x1, y1) in enumerate(nodes):
            for x2, y2 in nodes[i + 1:]:
                d = _math.hypot(x1 - x2, y1 - y2)
                if d < 96:
                    out.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{acc}" '
                               f'stroke-width="1" opacity="{round(0.5 - d / 240, 2)}"/>')
        for i, (x, y) in enumerate(nodes):
            rr = round(r.uniform(4.5, 11), 1)
            out.append(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{acc if i % 2 else acc2}" '
                       f'opacity="{round(r.uniform(0.45, 0.9), 2)}"/>')
            out.append(f'<circle cx="{x}" cy="{y}" r="{round(rr * 2.1, 1)}" fill="none" stroke="{acc}" '
                       f'stroke-width=".8" opacity=".25"/>')

    elif fam == "flow":  # pipeline / node graph
        rows, per = 3, 4
        grid = {}
        for ry in range(rows):
            row = {}
            for cxi in range(per):
                if r.random() < 0.22:
                    continue
                row[cxi] = (34 + cxi * ((w - 68) / (per - 1)),
                            30 + ry * ((h - 60) / (rows - 1)))
            grid[ry] = row
        for ry in sorted(grid):
            row = grid[ry]
            ks = sorted(row)
            for a, b in zip(ks, ks[1:]):
                x1, y1 = row[a]
                x2, y2 = row[b]
                mx2 = (x1 + x2) / 2
                out.append(f'<path d="M{x1:.1f} {y1:.1f} C{mx2:.1f} {y1:.1f} {mx2:.1f} {y2:.1f} {x2:.1f} {y2:.1f}" '
                           f'fill="none" stroke="{acc}" stroke-width="1.4" opacity=".45"/>')
            for cxi in ks:
                x, y = row[cxi]
                out.append(f'<rect x="{x - 11:.1f}" y="{y - 8:.1f}" width="22" height="16" rx="5" '
                           f'fill="#02040c" stroke="{acc2}" stroke-width="1.3" opacity=".9"/>')
                out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6" fill="{acc2}"/>')

    else:  # code / research: three distinct compositions
        if layout == "center":
            bw2, bh2 = w * 0.62, h * 0.70
            bx2, by2 = (w - bw2) / 2, (h - bh2) / 2
            out.append(f'<rect x="{bx2:.1f}" y="{by2:.1f}" width="{bw2:.1f}" height="{bh2:.1f}" rx="10" '
                       f'fill="#03060f" opacity=".72" stroke="{acc}" stroke-opacity=".28"/>')
            out.append(f'<rect x="{bx2:.1f}" y="{by2:.1f}" width="{bw2:.1f}" height="16" rx="10" '
                       f'fill="{hi}" opacity=".5"/>')
            for cxx in (bx2 + 13, bx2 + 25, bx2 + 37):
                out.append(f'<circle cx="{cxx:.1f}" cy="{by2 + 8:.1f}" r="3.1" fill="{acc2}" opacity=".8"/>')
            yy = by2 + 27
            while yy < by2 + bh2 - 8:
                lw = (bw2 - 46) * r.uniform(0.22, 0.94)
                c = acc if r.random() < 0.5 else (acc2 if r.random() < 0.4 else hi)
                out.append(f'<rect x="{bx2 + 40:.1f}" y="{yy:.1f}" width="{lw:.1f}" height="4.4" rx="2.2" '
                           f'fill="{c}" opacity="{round(r.uniform(0.4, 0.92), 2)}"/>')
                yy += 11.5
        elif layout == "left":
            # stacked document sheets, fanned
            for k in range(3):
                ox = 18 + k * 15
                oy = (h - 96) / 2 + k * 6
                out.append(f'<rect x="{ox}" y="{oy:.1f}" width="{w * 0.56:.1f}" height="96" rx="8" '
                           f'fill="#03060f" opacity="{0.42 + 0.2 * k:.2f}" '
                           f'stroke="{(acc if k == 2 else acc2)}" stroke-opacity="{0.22 + 0.16 * k:.2f}"/>')
            for k in range(7):
                yy = (h - 96) / 2 + 12 + 16 + k * 10
                lw = (w * 0.56 - 52) * r.uniform(0.35, 1.0)
                out.append(f'<rect x="{18 + 2 * 15 + 16}" y="{yy:.1f}" width="{lw:.1f}" height="4" rx="2" '
                           f'fill="{acc if k % 3 else acc2}" opacity="{round(r.uniform(0.5, 0.95), 2)}"/>')
            for k in range(5):
                out.append(f'<circle cx="{w - 30 - k * 17}" cy="{h * 0.5:.1f}" r="{round(r.uniform(3, 6), 1)}" '
                           f'fill="{acc2}" opacity="{round(r.uniform(0.3, 0.7), 2)}"/>')
        else:
            # terminal on the left + progress chart on the right
            tw = w * 0.50
            out.append(f'<rect x="18" y="{h * 0.16:.1f}" width="{tw:.1f}" height="{h * 0.68:.1f}" rx="9" '
                       f'fill="#03060f" opacity=".68" stroke="{acc}" stroke-opacity=".26"/>')
            for k in range(6):
                yy = h * 0.16 + 16 + k * 12
                lw = (tw - 34) * r.uniform(0.25, 0.92)
                out.append(f'<rect x="30" y="{yy:.1f}" width="{lw:.1f}" height="4" rx="2" '
                           f'fill="{acc2 if k % 2 else acc}" opacity="{round(r.uniform(0.45, 0.9), 2)}"/>')
            bx3, by3 = w * 0.63, h * 0.76
            npt = 6
            for k in range(npt):
                bhh = r.uniform(0.18, 1.0) * h * 0.44
                xx = bx3 + k * ((w - bx3 - 24) / npt)
                out.append(f'<rect x="{xx:.1f}" y="{by3 - bhh:.1f}" width="{(w - bx3 - 24) / npt * 0.6:.1f}" '
                           f'height="{bhh:.1f}" rx="3" fill="{acc if k % 2 else hi}" '
                           f'opacity="{round(r.uniform(0.4, 0.85), 2)}"/>')
            out.append(f'<line x1="{bx3 - 6:.1f}" y1="{by3 + 2:.1f}" x2="{w - 20:.1f}" y2="{by3 + 2:.1f}" '
                       f'stroke="{acc}" stroke-width="1.2" opacity=".55"/>')

    out.append('</svg>')
    return "".join(out)

e = html.escape
_today = _dt.date.fromisoformat(TODAY)


def age_days(s):
    try:
        return (_today - _dt.date.fromisoformat(s)).days
    except Exception:
        return None


def furl(p):
    return "file:///" + p.replace("\\", "/").replace(" ", "%20")


def rel_days(n):
    if n is None:
        return "unknown"
    if n <= 0:
        return "today"
    if n == 1:
        return "1 day ago"
    if n < 30:
        return f"{n} days ago"
    if n < 365:
        return f"{n // 30} mo ago"
    return f"{n // 365} yr ago"


# ---- derived ----
counts = {k: sum(1 for p in P if p["status"] == k) for k in STATUS}
avg = round(sum(p["pct"] for p in P) / len(P))
hermes_n = sum(1 for p in P if p["src"] == "hermes")
folder_n = len(P) - hermes_n
avg_hermes = round(sum(p["pct"] for p in P if p["src"] == "hermes") / max(1, hermes_n))
gh_n = sum(1 for p in P if p["gh"])
run_n = sum(1 for p in P if p["port"])
shipped = counts["done"] + counts["live"]
blocked_n = counts["blocked"] + counts["parked"]
today_n = sum(1 for p in P if (age_days(p["last"]) or 99) <= 7)
cats = sorted({p["cat"] for p in P})

# ---- cards (grid view) ----
def card(p, i):
    lab, col = STATUS[p["status"]]
    ad = age_days(p["last"])
    links = [f'<a class="lnk" href="{e(furl(p["path"]))}" title="{e(p["path"])}">\U0001F4C1 Folder</a>']
    if p["local"]:
        links.insert(0, f'<a class="lnk go" href="{e(p["local"])}" target="_blank" rel="noopener">▶ Launch</a>')
    if p["gh"]:
        links.append(f'<a class="lnk gh" href="{e(p["gh"])}" target="_blank" rel="noopener">★ GitHub</a>')
    ping = (f'<span class="dot" id="ping{i}"><i></i><b>checking…</b></span>') if p["port"] else ""
    origin = '<span class="orig h">◆ built in Hermes</span>' if p["src"] == "hermes" else '<span class="orig f">▢ found on F:</span>'
    hay = e((p["name"] + " " + p["desc"] + " " + p["cat"] + " " + p["done"] + " " + p["todo"]).lower())
    port = f' data-port="{p["port"]}"' if p["port"] else ""
    return f'''<article class="card" data-i="{i}" data-status="{p["status"]}" data-src="{p["src"]}" data-cat="{e(p["cat"])}" data-pct="{p["pct"]}" data-age="{ad if ad is not None else 9999}" data-hay="{hay}"{port} style="--c:{col}">
  <div class="glow"></div>
  <div class="cover">{cover_svg(p)}<span class="cvr-cat">{e(p["cat"])}</span></div>
  <header><h3>{e(p["name"])}</h3><span class="st">{lab}</span></header>
  <div class="meta"><span class="cat">{e(p["cat"])}</span>{origin}<span class="ago">{rel_days(ad)}</span>{ping}</div>
  <p class="desc">{e(p["desc"])}</p>
  <div class="pctrow"><b>{p["pct"]}<sup>%</sup></b><div class="bar"><i style="width:0" data-w="{p["pct"]}"></i></div></div>
  <details><summary>Progress report</summary>
    <p><em class="k">Done</em>{e(p["done"])}</p>
    <p><em class="k">Next</em>{e(p["todo"])}</p>
    <p class="path" data-path="{e(p["path"])}">{e(p["path"])} <span class="cp">copy</span></p>
  </details>
  <nav>{"".join(links)}</nav>
</article>'''

cards_html = "\n".join(card(p, i) for i, p in enumerate(P))


# ---- board (kanban) view ----
def bcard(p):
    lab, col = STATUS[p["status"]]
    links = []
    if p["local"]:
        links.append(f'<a class="lnk go" href="{e(p["local"])}" target="_blank" rel="noopener">▶</a>')
    if p["gh"]:
        links.append(f'<a class="lnk gh" href="{e(p["gh"])}" target="_blank" rel="noopener">★</a>')
    links.append(f'<a class="lnk" href="{e(furl(p["path"]))}" title="open folder">\U0001F4C1</a>')
    ad = age_days(p["last"])
    return (f'<div class="bcard" style="--c:{col}"><div class="bcov">{cover_svg(p, 260, 74)}</div>'
            f'<div class="btop"><b>{e(p["name"])}</b>'
            f'<span class="mini">{p["pct"]}%</span></div>'
            f'<div class="bar sm"><i style="width:{p["pct"]}%"></i></div>'
            f'<div class="bmeta">{e(p["cat"])} · {rel_days(ad)}</div>'
            f'<nav>{"".join(links)}</nav></div>')

cols = ""
for k in ["live", "working", "progress", "blocked", "parked", "done", "archive"]:
    if not counts[k]:
        continue
    lab, col = STATUS[k]
    items = "".join(bcard(p) for p in P if p["status"] == k)
    cols += (f'<div class="bcol" style="--c:{col}"><div class="bhead"><span class="bdot"></span>'
             f'<b>{lab}</b><span class="bcount">{counts[k]}</span></div>{items}</div>')
board_html = f'<div class="board">{cols}</div>'


# ---- table view ----
def trow(p):
    lab, col = STATUS[p["status"]]
    ln = ""
    if p["local"]:
        ln += f'<a class="lnk go" href="{e(p["local"])}" target="_blank" rel="noopener">▶ app</a> '
    if p["gh"]:
        ln += f'<a class="lnk gh" href="{e(p["gh"])}" target="_blank" rel="noopener">★ repo</a>'
    ad = age_days(p["last"])
    return (f'<tr data-hay="{e((p["name"] + " " + p["desc"] + " " + p["cat"]).lower())}"'
            f' data-status="{p["status"]}" data-src="{p["src"]}" data-cat="{e(p["cat"])}"'
            f' data-pct="{p["pct"]}" data-age="{ad if ad is not None else 9999}">'
            f'<td><b>{e(p["name"])}</b><small>{e(p["path"])}</small></td>'
            f'<td><span class="st" style="--c:{col}">{lab}</span></td>'
            f'<td><div class="bar sm" style="--c:{col}"><i style="width:{p["pct"]}%"></i></div><b>{p["pct"]}%</b></td>'
            f'<td>{e(p["cat"])}</td><td>{rel_days(ad)}</td>'
            f'<td class="lnkcell">{ln}</td></tr>')


rows = "\n".join(trow(p) for p in P)
table_html = ('<div class="tablewrap"><table><thead><tr><th>Project</th><th>Status</th><th>Progress</th>'
              '<th>Category</th><th>Last change</th><th>Links</th></tr></thead><tbody>'
              + rows + '</tbody></table></div>')


# ---- KPI tiles ----
def ring(value, total, color, label, sub):
    r, sw = 34, 7
    circ = 2 * _math.pi * r
    off = circ * (1 - (value / total if total else 0))
    return f'''<div class="kpi" style="--c:{color}">
  <svg viewBox="0 0 84 84" class="ring"><circle cx="42" cy="42" r="{r}" class="trk"/><circle cx="42" cy="42" r="{r}" class="val" stroke="{color}" style="stroke-dasharray:{circ:.1f};stroke-dashoffset:{off:.1f}"/></svg>
  <div class="ktx"><b data-count="{value}">{value}</b><span>{label}</span><small>{sub}</small></div></div>'''

kpis = "".join([
    ring(len(P), max(len(P), 40), "#7dd3fc", "projects tracked", f"{hermes_n} built in Hermes · {folder_n} found on disk"),
    ring(shipped, len(P), "#34d399", "shipped or live", f"{round(100*shipped/len(P))}% of the estate"),
    ring(round(avg), 100, "#a78bfa", f"avg {avg}% complete", f"Hermes work sits at {avg_hermes}%"),
    ring(blocked_n, len(P), "#f87171", "blocked or parked", "need a decision to move"),
])

stat_tiles = f'''<div class="stats">
  <div class="stat"><b id="liveN">–</b><span>local servers answering</span><small>live ping, refreshes every 12s</small></div>
  <div class="stat"><b>{today_n}</b><span>changed in the last 7 days</span><small>freshly touched</small></div>
  <div class="stat"><b>{gh_n}</b><span>pushed to GitHub</span><small>remote copies exist</small></div>
  <div class="stat"><b>{run_n}</b><span>launchable with one click</span><small>start and open the app</small></div>
</div>'''

chips = "".join(
    f'<button class="chip" data-f="{k}" style="--c:{STATUS[k][1]}"><b>{counts[k]}</b><span>{STATUS[k][0]}</span></button>'
    for k in STATUS if counts[k])
chip_cats = "".join(f'<button class="chip cat" data-c="{e(c)}" style="--c:#94a3b8"><b>{sum(1 for p in P if p["cat"] == c)}</b><span>{e(c)}</span></button>'
                    for c in cats)

# ---- donut (status distribution) ----
R, SW = 52, 13
C = 2 * _math.pi * R
segs, acc = "", 0.0
for k in STATUS:
    if not counts[k]:
        continue
    frac = counts[k] / len(P)
    segs += (f'<circle class="seg" cx="60" cy="60" r="{R}" fill="none" stroke="{STATUS[k][1]}" '
             f'stroke-width="{SW}" stroke-dasharray="{frac*C:.2f} {C:.2f}" stroke-dashoffset="{-acc*C:.2f}" '
             f'stroke-linecap="butt"><title>{e(STATUS[k][0])}: {counts[k]}</title></circle>')
    acc += frac
donut = (f'<div class="donut"><svg viewBox="0 0 120 120">{segs}'
         f'<circle cx="60" cy="60" r="38" fill="none" class="trk"/>'
         f'<text x="60" y="56" class="dnum">{avg}%</text><text x="60" y="70" class="dlab">avg done</text></svg>'
         f'<ul class="legend">' + "".join(
             f'<li style="--c:{STATUS[k][1]}"><i></i>{e(STATUS[k][0])}<b>{counts[k]}</b></li>'
             for k in STATUS if counts[k]) + '</ul></div>')

# ---- activity sparkline (real last-change dates) ----
months = []
y, mo = _today.year, _today.month
for _ in range(11, -1, -1):
    m = mo - _
    yy = y
    while m <= 0:
        m += 12
        yy -= 1
    months.append((yy, m))
mcount = []
for (yy, m) in months:
    mcount.append(sum(1 for p in P if p["last"].startswith(f"{yy:04d}-{m:02d}")))
peak = max(mcount) or 1
pts = []
for idx, v in enumerate(mcount):
    x = 6 + idx * (248 / 11)
    yv = 74 - (v / peak) * 58
    pts.append(f"{x:.1f},{yv:.1f}")
spark = (f'<svg class="spark" viewBox="0 0 262 84" preserveAspectRatio="none">'
         f'<polyline points="{" ".join(pts)}" class="line"/>'
         + "".join(f'<circle cx="{6 + i*(248/11):.1f}" cy="{74 - (v/peak)*58:.1f}" r="2.6" class="pt"><title>{mcount[i]} touched in {months[i][0]}-{months[i][1]:02d}</title></circle>'
                   for i, v in enumerate(mcount)) +
         f'<text x="6" y="82" class="ax">{months[0][0]}-{months[0][1]:02d}</text>'
         f'<text x="254" y="82" class="ax end">{months[-1][0]}-{months[-1][1]:02d}</text>'
         f'<text x="6" y="10" class="ax">peak {peak}/month</text></svg>')

# ---- payload for the JS modal ----
payload = []
for p in P:
    lab, col = STATUS[p["status"]]
    payload.append({
        "n": p["name"], "c": p["cat"], "s": lab, "sc": p["status"], "col": col, "pct": p["pct"],
        "d": p["desc"], "done": p["done"], "todo": p["todo"], "path": p["path"],
        "last": p["last"], "ago": rel_days(age_days(p["last"])),
        "local": p["local"], "gh": p["gh"], "port": p["port"],
        "src": "Built in Hermes" if p["src"] == "hermes" else "Found on F: drive",
        "cover": cover_svg(p, 700, 200),
        "fam": FAMILY.get(p["cat"], "code"),
    })
data_js = _json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c")

TPL = r'''<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Mission Control — Mahesh's Projects</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{
  --bg:#060912; --bg2:#0a0f1e; --card:rgba(19,26,46,.72); --card2:rgba(13,18,34,.86);
  --bd:rgba(120,140,190,.16); --bd2:rgba(120,140,190,.30);
  --fg:#e8edfb; --mu:#8d9ab9; --ac:#7dd3fc; --ac2:#a78bfa;
  --shadow:0 24px 60px -20px rgba(0,0,0,.85);
  --r:18px; --ease:cubic-bezier(.2,.9,.25,1);
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;background:var(--bg);color:var(--fg);
  font:15px/1.6 'Space Grotesk',system-ui,Segoe UI,sans-serif;
  -webkit-font-smoothing:antialiased;overflow-x:hidden;
}
#bg{position:fixed;inset:0;z-index:0;pointer-events:none}
#neb{position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;pointer-events:none;overflow:hidden}
#bg{position:fixed;inset:0;z-index:0;pointer-events:none}
/* deep space base + nebula blooms */
#neb::after{content:'';position:absolute;inset:0;background:
  radial-gradient(1250px 700px at 8% -14%,rgba(56,189,248,.40),transparent 62%),
  radial-gradient(1050px 620px at 94% -8%,rgba(167,139,250,.38),transparent 62%),
  radial-gradient(950px 680px at 82% 84%,rgba(236,72,153,.24),transparent 64%),
  radial-gradient(1150px 760px at 20% 100%,rgba(52,211,153,.22),transparent 64%),
  radial-gradient(780px 460px at 52% 36%,rgba(14,165,233,.20),transparent 66%),
  radial-gradient(600px 380px at 62% 58%,rgba(99,102,241,.18),transparent 66%),
  linear-gradient(180deg,#04060f 0%,#070c1c 30%,#050a16 60%,#04060f 100%)}
/* slow-drifting aurora ribbons */
#neb::before{content:'';position:absolute;inset:-25%;opacity:1;
  background:
    conic-gradient(from 210deg at 22% 32%,transparent 0deg,rgba(56,189,248,.50) 60deg,transparent 130deg),
    conic-gradient(from 20deg at 78% 26%,transparent 0deg,rgba(167,139,250,.48) 70deg,transparent 140deg),
    conic-gradient(from 130deg at 52% 82%,transparent 0deg,rgba(16,185,129,.36) 80deg,transparent 150deg),
    conic-gradient(from 300deg at 62% 56%,transparent 0deg,rgba(236,72,153,.32) 65deg,transparent 135deg),
    conic-gradient(from 90deg at 8% 74%,transparent 0deg,rgba(99,102,241,.30) 60deg,transparent 132deg);
  filter:blur(58px);animation:drift 64s ease-in-out infinite alternate}
@keyframes drift{
  0%{transform:translate3d(-2.5%,-1.5%,0) rotate(0deg) scale(1)}
  50%{transform:translate3d(2.5%,2%,0) rotate(6deg) scale(1.07)}
  100%{transform:translate3d(-1.5%,2.5%,0) rotate(-5deg) scale(1.04)}}
/* perspective grid + vignette, above the aurora */
body::before{content:'';position:fixed;inset:0;z-index:1;pointer-events:none;
  background-image:
    linear-gradient(rgba(160,200,255,.075) 1px,transparent 1px),
    linear-gradient(90deg,rgba(160,200,255,.075) 1px,transparent 1px);
  background-size:58px 58px;
  -webkit-mask-image:radial-gradient(ellipse 85% 62% at 50% 16%,#000,transparent 78%);
  mask-image:radial-gradient(ellipse 85% 62% at 50% 16%,#000,transparent 78%)}
body::after{content:'';position:fixed;inset:0;z-index:1;pointer-events:none;
  background:radial-gradient(ellipse 130% 95% at 50% 45%,transparent 55%,rgba(3,5,14,.42) 100%)}
.wrap{position:relative;z-index:2;max-width:1460px;margin:0 auto;padding:0 24px 90px}
a{color:inherit}
.mono{font-family:'JetBrains Mono',Consolas,monospace}

/* ---------- header ---------- */
header.top{padding:56px 0 26px;display:flex;flex-wrap:wrap;gap:20px;align-items:flex-end;justify-content:space-between}
.brand{display:flex;align-items:center;gap:14px}
.orb{position:relative;width:64px;height:64px;flex:0 0 64px;display:grid;place-items:center}
.orb .ring{position:absolute;border-radius:50%;border:1px solid rgba(125,211,252,.30)}
.orb .r1{inset:0;animation:spin 14s linear infinite;border-style:dashed}
.orb .r2{inset:9px;border-color:rgba(167,139,250,.34);animation:spin 9s linear infinite reverse;border-style:dotted}
.orb .core{width:30px;height:30px;border-radius:10px;display:grid;place-items:center;font-size:15px;
  background:linear-gradient(140deg,#7dd3fc,#a78bfa 55%,#34d399);color:#060912;
  box-shadow:0 8px 24px -6px rgba(125,211,252,.8)}
.orb .sat{position:absolute;width:6px;height:6px;border-radius:50%}
.orb .s1{background:#7dd3fc;box-shadow:0 0 10px #7dd3fc;animation:orb 6s linear infinite}
.orb .s2{background:#a78bfa;box-shadow:0 0 10px #a78bfa;animation:orb 9s linear infinite reverse}
.orb .s3{background:#34d399;box-shadow:0 0 10px #34d399;animation:orb 12s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
@keyframes orb{from{transform:rotate(0deg) translateX(32px) rotate(0deg)}
  to{transform:rotate(360deg) translateX(32px) rotate(-360deg)}}
.mark{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;font-size:22px;
  background:linear-gradient(140deg,#7dd3fc,#a78bfa 55%,#34d399);color:#060912;font-weight:700;
  box-shadow:0 10px 30px -8px rgba(125,211,252,.7);animation:bob 5s var(--ease) infinite}
@keyframes bob{0%,100%{transform:translateY(0) rotate(0)}50%{transform:translateY(-6px) rotate(-6deg)}}
h1{margin:0;font-size:clamp(30px,4.4vw,52px);line-height:1.02;letter-spacing:-.03em;font-weight:700}
h1 .grad{background:linear-gradient(100deg,#7dd3fc,#a78bfa 45%,#34d399);-webkit-background-clip:text;background-clip:text;color:transparent}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:11.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--mu);margin-bottom:6px}
.sub{color:var(--mu);margin:10px 0 0;max-width:60ch}
.hero-pills{display:flex;gap:9px;flex-wrap:wrap;margin-top:16px}
.hp{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;color:#c3cee6;padding:7px 13px;
  border-radius:999px;background:rgba(17,24,48,.9);border:1px solid var(--bd);box-shadow:0 8px 22px -14px #000}
.dotc{width:8px;height:8px;border-radius:50%;background:var(--c);box-shadow:0 0 9px var(--c);
  animation:bp 2.6s var(--ease) infinite}
@keyframes bp{0%,100%{transform:scale(1);opacity:1}50%{transform:scale(1.35);opacity:.6}}
.hbtns{display:flex;gap:10px;flex-wrap:wrap}
.btn{appearance:none;cursor:pointer;font:inherit;font-size:13px;font-weight:600;color:var(--fg);
  background:var(--card);border:1px solid var(--bd2);padding:9px 15px;border-radius:12px;
  display:inline-flex;align-items:center;gap:8px;transition:.18s var(--ease)}
.btn:hover{border-color:var(--ac);transform:translateY(-2px);box-shadow:0 10px 26px -12px rgba(125,211,252,.8)}
.btn.accent{background:linear-gradient(120deg,rgba(125,211,252,.22),rgba(167,139,250,.22));border-color:rgba(125,211,252,.5)}
.btn kbd{font:11px/1 'JetBrains Mono',monospace;background:rgba(255,255,255,.08);border:1px solid var(--bd2);
  border-radius:5px;padding:3px 6px;color:var(--mu)}

/* ---------- marquee ---------- */
.ticker{border-top:1px solid var(--bd);border-bottom:1px solid var(--bd);margin:22px 0 30px;overflow:hidden;
  background:linear-gradient(90deg,transparent,rgba(125,211,252,.05),transparent)}
.ticker .t{display:inline-flex;gap:44px;padding:9px 0;white-space:nowrap;animation:slide 44s linear infinite}
@keyframes slide{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.ticker b{font-size:12px;font-family:'JetBrains Mono',monospace;color:var(--mu);font-weight:400;letter-spacing:.04em}
.ticker b em{color:var(--ac);font-style:normal}

/* ---------- kpis ---------- */
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin-bottom:14px}
.kpi{display:flex;align-items:center;gap:14px;padding:16px 18px;border-radius:var(--r);
  background:#0e1530;position:relative;overflow:hidden;
  transition:.2s var(--ease)}
.kpi:hover{transform:translateY(-3px);border-color:var(--c)}
.kpi::after{content:'';position:absolute;inset:auto 0 0 0;height:2px;background:linear-gradient(90deg,var(--c),transparent)}
.ring{width:70px;height:70px;flex:0 0 70px;transform:rotate(-90deg)}
.ring .trk{fill:none;stroke:rgba(255,255,255,.07);stroke-width:8}
.ring .val{fill:none;stroke-width:8;stroke-linecap:round;filter:drop-shadow(0 0 6px currentColor);
  animation:draw 1.5s var(--ease) both}
@keyframes draw{from{stroke-dashoffset:999}}
.ktx b{display:block;font-size:27px;line-height:1;letter-spacing:-.02em}
.ktx span{display:block;color:var(--mu);font-size:13px;margin-top:4px}
.ktx small{display:block;color:#6c7a99;font-size:11.5px;margin-top:3px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px;margin-bottom:30px}
.stat{padding:14px 16px;border-radius:14px;background:#0c1226;border:1px solid var(--bd)}
.stat b{display:block;font-size:23px;color:var(--ac)}
.stat span{display:block;font-size:13px}
.stat small{display:block;color:#6c7a99;font-size:11.5px;margin-top:2px}

/* ---------- controls ---------- */
.controls{position:sticky;top:0;z-index:30;padding:14px 0 12px;margin-bottom:6px;
  background:linear-gradient(180deg,#060912 62%,rgba(6,9,18,.9) 88%,rgba(6,9,18,0))}
.searchrow{display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.search{position:relative;flex:1;min-width:250px}
.search input{width:100%;padding:11px 14px 11px 40px;border-radius:13px;border:1px solid var(--bd2);
  background:var(--card2);color:var(--fg);font:inherit;font-size:14px;outline:none;transition:.18s}
.search input:focus{border-color:var(--ac);box-shadow:0 0 0 4px rgba(125,211,252,.12)}
.search svg{position:absolute;left:13px;top:50%;transform:translateY(-50%);opacity:.55}
.seg{display:flex;background:var(--card2);border:1px solid var(--bd2);border-radius:12px;padding:3px;gap:2px}
.seg button{appearance:none;border:0;background:transparent;color:var(--mu);font:inherit;font-size:13px;font-weight:600;
  padding:7px 14px;border-radius:9px;cursor:pointer;transition:.16s var(--ease)}
.seg button.on{background:linear-gradient(120deg,rgba(125,211,252,.24),rgba(167,139,250,.24));color:var(--fg);
  box-shadow:inset 0 0 0 1px rgba(125,211,252,.35)}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
.chip{appearance:none;cursor:pointer;font:inherit;display:inline-flex;align-items:center;gap:7px;padding:6px 12px;
  border-radius:999px;background:var(--card2);border:1px solid var(--bd);color:var(--mu);font-size:12.5px;
  transition:.16s var(--ease)}
.chip b{color:var(--c);font-family:'JetBrains Mono',monospace;font-size:11.5px}
.chip:hover{border-color:var(--c);color:var(--fg);transform:translateY(-1px)}
.chip.on{background:color-mix(in srgb,var(--c) 16%,transparent);border-color:var(--c);color:var(--fg);
  box-shadow:0 0 0 1px color-mix(in srgb,var(--c) 40%,transparent)}
.chip.cat b{color:var(--ac2)}
.catlab{font:11px/1 'JetBrains Mono',monospace;letter-spacing:.18em;text-transform:uppercase;color:#5c688a;
  align-self:center;margin-right:2px}
.resultline{display:flex;justify-content:space-between;align-items:center;color:var(--mu);font-size:12.5px;
  font-family:'JetBrains Mono',monospace;padding:8px 2px 12px}

/* ---------- grid ---------- */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(370px,1fr));gap:16px}
.card{position:relative;padding:18px;border-radius:var(--r);background:var(--card);border:1px solid var(--bd);
  display:flex;flex-direction:column;gap:9px;overflow:hidden;
  transition:transform .25s var(--ease),border-color .25s,box-shadow .25s;cursor:pointer;
  animation:pop .5s var(--ease) backwards;animation-delay:min(calc(var(--d,0)*22ms),600ms)}
@keyframes pop{from{opacity:0;transform:translateY(12px) scale(.99)}}
.card::before{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;background:var(--c);opacity:.85}
.cover{position:relative;height:118px;margin:-18px -18px 4px;border-radius:0;overflow:hidden;
  border-bottom:1px solid var(--bd);flex:0 0 auto}
.cover .coverart{width:100%;height:100%;display:block;opacity:.92;transition:transform .5s var(--ease),opacity .3s}
.card:hover .cover .coverart{transform:scale(1.06);opacity:1}
.cover::after{content:'';position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(180deg,rgba(4,7,17,.10) 0%,rgba(4,7,17,0) 42%,#0d1428 99%)}
.cvr-cat{position:absolute;left:12px;bottom:10px;z-index:2;font:600 9.5px/1 'JetBrains Mono',monospace;
  letter-spacing:.14em;text-transform:uppercase;color:#cfe0f7;background:rgba(4,8,18,.55);
  border:1px solid rgba(160,190,255,.22);border-radius:999px;padding:4px 9px;backdrop-filter:blur(3px)}
/* board tile cover */
.bcov{height:58px;margin:0 -11px 9px;overflow:hidden;position:relative}
.bcov .coverart{width:100%;height:100%;display:block;opacity:.85}
.bcov::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,transparent 30%,rgba(19,26,46,.96) 100%)}
/* modal hero */
.mhero{position:relative;height:150px;margin:-26px -26px 0;overflow:hidden}
.mhero .coverart{width:100%;height:100%;display:block}
.mhero::after{content:'';position:absolute;inset:0;
  background:linear-gradient(180deg,transparent 20%,rgba(20,27,48,.98) 96%)}
.card:hover{transform:translateY(-5px);border-color:color-mix(in srgb,var(--c) 55%,transparent);
  box-shadow:0 26px 50px -26px rgba(0,0,0,.95),0 0 0 1px color-mix(in srgb,var(--c) 22%,transparent)}
.glow{position:absolute;inset:0;opacity:0;transition:opacity .3s;pointer-events:none;
  background:radial-gradient(360px circle at var(--mx,50%) var(--my,0%),color-mix(in srgb,var(--c) 16%,transparent),transparent 60%)}
.card:hover .glow{opacity:1}
.card header{display:flex;justify-content:space-between;gap:10px;align-items:flex-start}
.card h3{margin:0;font-size:17px;letter-spacing:-.01em;line-height:1.25}
.st{flex:0 0 auto;font-size:11px;font-weight:600;letter-spacing:.04em;padding:3px 10px;border-radius:999px;
  background:color-mix(in srgb,var(--c) 16%,transparent);color:var(--c);
  border:1px solid color-mix(in srgb,var(--c) 45%,transparent);white-space:nowrap}
.meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:11.5px;color:var(--mu)}
.meta .cat,.meta .orig{padding:2px 8px;border-radius:6px;background:rgba(255,255,255,.05);border:1px solid var(--bd)}
.meta .orig.h{color:#7dd3fc}.meta .orig.f{color:#94a3b8}
.meta .ago{font-family:'JetBrains Mono',monospace;font-size:11px}
.dot{display:inline-flex;align-items:center;gap:5px;font-family:'JetBrains Mono',monospace;font-size:11px}
.dot i{width:7px;height:7px;border-radius:50%;background:#64748b;transition:.3s}
.dot.up{color:#34d399}.dot.up i{background:#34d399;box-shadow:0 0 0 0 rgba(52,211,153,.6);animation:pulse 2s infinite}
.dot.down{color:#f87171}.dot.down i{background:#f87171}
@keyframes pulse{70%{box-shadow:0 0 0 8px rgba(52,211,153,0)}100%{box-shadow:0 0 0 0 rgba(52,211,153,0)}}
.desc{margin:0;color:#c3cee6;font-size:14px;line-height:1.55;flex:1}
.pctrow{display:flex;align-items:center;gap:12px}
.pctrow b{font:600 20px/1 'JetBrains Mono',monospace;color:var(--c);min-width:56px}
.pctrow sup{font-size:11px;opacity:.7}
.bar{flex:1;height:7px;border-radius:99px;background:rgba(255,255,255,.07);overflow:hidden}
.bar i{display:block;height:100%;border-radius:99px;background:linear-gradient(90deg,var(--c),color-mix(in srgb,var(--c) 45%,#fff));
  box-shadow:0 0 14px -2px var(--c);width:0;transition:width 1.2s var(--ease)}
.bar.sm{height:5px;flex:0 0 90px;display:inline-block;vertical-align:middle}
details{background:rgba(0,0,0,.24);border:1px solid var(--bd);border-radius:11px;padding:8px 12px}
summary{cursor:pointer;color:var(--ac);font-size:12.5px;font-weight:600;list-style:none;user-select:none}
summary::-webkit-details-marker{display:none}
summary::before{content:'▸ ';transition:.2s}
details[open] summary::before{content:'▾ '}
details p{margin:9px 0 0;font-size:13px;color:#b9c4dc;line-height:1.55}
em.k{display:inline-block;font-style:normal;font:600 10px/1 'JetBrains Mono',monospace;letter-spacing:.1em;
  text-transform:uppercase;color:var(--mu);margin-right:8px;padding:3px 6px;border-radius:5px;background:rgba(255,255,255,.05)}
em.k.k2{color:#fca5a5}
.path{font-family:'JetBrains Mono',monospace;font-size:11px;color:#7b88a8;word-break:break-all}
.cp{cursor:pointer;color:var(--ac);border:1px solid var(--bd2);border-radius:5px;padding:1px 6px;margin-left:4px;font-size:10px}
nav{display:flex;gap:8px;flex-wrap:wrap;margin-top:2px}
.lnk{font-size:12px;font-weight:600;text-decoration:none;color:var(--mu);padding:6px 11px;border-radius:9px;
  border:1px solid var(--bd);background:rgba(255,255,255,.03);transition:.16s var(--ease)}
.lnk:hover{color:var(--fg);border-color:var(--bd2);transform:translateY(-2px);background:rgba(255,255,255,.07)}
.lnk.go{color:#06202e;background:linear-gradient(120deg,#7dd3fc,#a78bfa);border-color:transparent}
.lnk.go:hover{box-shadow:0 10px 24px -10px rgba(125,211,252,.9)}
.lnk.gh{color:#d8b4fe}

/* ---------- board ---------- */
.board{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(250px,1fr);gap:14px;overflow-x:auto;padding-bottom:14px}
.bcol{background:rgba(8,12,24,.6);border:1px solid var(--bd);border-radius:var(--r);padding:12px;min-height:180px}
.bhead{display:flex;align-items:center;gap:8px;padding:2px 4px 12px;font-size:13px}
.bhead .bdot{width:9px;height:9px;border-radius:50%;background:var(--c);box-shadow:0 0 12px var(--c)}
.bhead .bcount{margin-left:auto;font:11px/1 'JetBrains Mono',monospace;color:var(--mu);
  background:rgba(255,255,255,.06);padding:3px 7px;border-radius:6px}
.bcard{background:#0e1530;border:1px solid var(--bd);border-left:2px solid var(--c);border-radius:12px;
  padding:0 11px 11px;margin-bottom:9px;transition:.18s var(--ease);cursor:pointer;position:relative}
.bcard:hover{transform:translateX(3px);border-color:var(--c);background:rgba(255,255,255,.04)}
.btop{display:flex;justify-content:space-between;gap:8px;align-items:baseline;font-size:13.5px;margin-bottom:7px}
.mini{font:11px/1 'JetBrains Mono',monospace;color:var(--c)}
.bmeta{font-size:11px;color:#6f7c9c;margin-top:7px}
.bcard nav{margin-top:9px;gap:6px}
.bcard .lnk{padding:3px 9px;font-size:11px}

/* ---------- table ---------- */
.tablewrap{overflow-x:auto;border:1px solid var(--bd);border-radius:var(--r);background:var(--card2)}
table{width:100%;border-collapse:collapse;font-size:13.5px;min-width:820px}
th,td{padding:11px 13px;text-align:left;border-bottom:1px solid var(--bd);vertical-align:middle}
th{font:600 11px/1 'JetBrains Mono',monospace;letter-spacing:.12em;text-transform:uppercase;color:var(--mu);
  background:#0c1224;position:sticky;top:0}
tbody tr{transition:.14s}
tbody tr:hover{background:rgba(125,211,252,.06)}
td b{display:block}
td small{display:block;font-family:'JetBrains Mono',monospace;font-size:10.5px;color:#6f7c9c;word-break:break-all;max-width:280px}
td b + .bar{display:inline-block}
.lnkcell{white-space:nowrap}
.lnkcell .lnk{padding:4px 9px;font-size:11px;display:inline-block;margin-right:4px}

/* ---------- analytics ---------- */
.analytics{display:grid;grid-template-columns:1fr 1.4fr;gap:16px;margin:34px 0 8px}
.panel{padding:18px;border-radius:var(--r);background:#0e1530;border:1px solid rgba(120,140,190,.22)}
.panel h3{margin:0 0 4px;font-size:15px}
.panel .cap{color:var(--mu);font-size:12.5px;margin:0 0 14px}
.donut{display:flex;align-items:center;gap:18px;flex-wrap:wrap}
.donut svg{width:150px;height:150px;flex:0 0 150px}
.seg{transition:.2s}
.donut .seg:hover{opacity:.75;transform:scale(1.03);transform-origin:60px 60px}
.donut .trk{stroke:rgba(255,255,255,.05)}
.dnum{fill:var(--fg);font:600 20px 'Space Grotesk',sans-serif;text-anchor:middle}
.dlab{fill:var(--mu);font:9px 'JetBrains Mono',monospace;text-anchor:middle;letter-spacing:.1em}
.legend{list-style:none;margin:0;padding:0;flex:1;min-width:170px;display:grid;gap:6px}
.legend li{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--mu)}
.legend i{width:9px;height:9px;border-radius:3px;background:var(--c);box-shadow:0 0 8px var(--c)}
.legend b{margin-left:auto;font-family:'JetBrains Mono',monospace;color:var(--fg);font-weight:500}
.spark{width:100%;height:110px;overflow:visible}
.spark .line{fill:none;stroke:url(#g1);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;
  filter:drop-shadow(0 0 6px rgba(125,211,252,.6));stroke-dasharray:400;stroke-dashoffset:400;animation:drawline 2s var(--ease) .3s forwards}
@keyframes drawline{to{stroke-dashoffset:0}}
.spark .pt{fill:#a78bfa;stroke:#0b1020;stroke-width:1.5}
.spark .ax{fill:#5c688a;font:9px 'JetBrains Mono',monospace}
.spark .ax.end{text-anchor:end}

/* ---------- modal ---------- */
.modal{position:fixed;inset:0;z-index:100;display:none;place-items:center;padding:24px;
  background:rgba(3,5,12,.88)}
.modal.on{display:grid;animation:fade .22s var(--ease)}
@keyframes fade{from{opacity:0}}
.sheet{width:min(680px,100%);max-height:86vh;overflow:auto;border-radius:22px;padding:26px;
  background:linear-gradient(180deg,rgba(20,27,48,.98),rgba(10,14,28,.98));
  border:1px solid var(--bd2);box-shadow:var(--shadow);animation:rise .28s var(--ease);position:relative}
@keyframes rise{from{transform:translateY(22px) scale(.97);opacity:0}}
.sheet::before{content:'';position:absolute;left:0;right:0;top:0;height:3px;border-radius:22px 22px 0 0;
  background:linear-gradient(90deg,var(--ac),var(--ac2),#34d399)}
.sheet{padding-top:0}
.sheet h2{margin:18px 0 6px;font-size:24px;letter-spacing:-.02em;padding-right:34px}
.sheet .rowmeta{display:flex;flex-wrap:wrap;gap:7px;align-items:center;margin-bottom:16px;font-size:12px;color:var(--mu)}
.x{position:absolute;top:18px;right:18px;width:32px;height:32px;border-radius:9px;cursor:pointer;
  border:1px solid var(--bd2);background:rgba(255,255,255,.05);color:var(--fg);font-size:15px;line-height:1}
.x:hover{background:rgba(248,113,113,.2);border-color:#f87171}
.sheet .bigpct{display:flex;align-items:center;gap:16px;padding:14px 16px;border-radius:14px;
  background:rgba(255,255,255,.04);border:1px solid var(--bd);margin-bottom:16px}
.sheet .bigpct b{font:700 34px/1 'JetBrains Mono',monospace;color:var(--c)}
.sheet .cols2{display:grid;grid-template-columns:1fr 1fr;gap:14px}
@media(max-width:640px){.sheet .cols2{grid-template-columns:1fr}.analytics{grid-template-columns:1fr}}
.sheet .blk{background:rgba(0,0,0,.26);border:1px solid var(--bd);border-radius:13px;padding:13px 15px;font-size:13.5px;line-height:1.6;color:#c3cee6}
.sheet .blk h4{margin:0 0 7px;font:600 10.5px/1 'JetBrains Mono',monospace;letter-spacing:.14em;text-transform:uppercase;color:var(--mu)}
.sheet .code{font-family:'JetBrains Mono',monospace;font-size:11.5px;color:#93a1c2;word-break:break-all;
  background:rgba(0,0,0,.35);border:1px solid var(--bd);border-radius:10px;padding:11px;margin-top:14px}

/* ---------- palette ---------- */
.pal{position:fixed;inset:0;z-index:120;display:none;place-items:start center;padding:14vh 20px 20px;
  background:rgba(3,5,12,.9)}
.pal.on{display:grid;animation:fade .18s}
.palbox{width:min(620px,100%);border-radius:18px;overflow:hidden;background:linear-gradient(180deg,rgba(22,29,52,.99),rgba(10,14,28,.99));
  border:1px solid var(--bd2);box-shadow:var(--shadow)}
.palin{width:100%;padding:16px 18px;border:0;background:transparent;color:var(--fg);font:15px 'Space Grotesk',sans-serif;outline:none}
.pallist{max-height:46vh;overflow:auto;border-top:1px solid var(--bd)}
.pali{padding:10px 18px;display:flex;align-items:center;gap:10px;cursor:pointer;font-size:13.5px;border-left:2px solid transparent}
.pali .em{width:8px;height:8px;border-radius:50%;background:var(--c);box-shadow:0 0 8px var(--c)}
.pali .stt{margin-left:auto;font:10.5px/1 'JetBrains Mono',monospace;color:var(--mu)}
.pali.sel{background:rgba(125,211,252,.12);border-left-color:var(--ac)}
.palfoot{padding:8px 18px;border-top:1px solid var(--bd);color:#5c688a;font:11px/1.6 'JetBrains Mono',monospace}

/* ---------- toast + footer ---------- */
#toast{position:fixed;left:50%;bottom:28px;transform:translate(-50%,20px);z-index:200;opacity:0;
  padding:10px 18px;border-radius:12px;background:rgba(20,27,48,.97);border:1px solid var(--bd2);
  font-size:13px;box-shadow:var(--shadow);transition:.25s var(--ease);pointer-events:none}
#toast.on{opacity:1;transform:translate(-50%,0)}
footer{margin-top:46px;padding-top:22px;border-top:1px solid var(--bd);color:#5c688a;font-size:12.5px;
  display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;align-items:flex-start}
footer b{color:var(--mu)}
canvas#fx{position:fixed;inset:0;z-index:150;pointer-events:none}
@media (prefers-reduced-motion:reduce){*{animation-duration:.01ms !important;transition-duration:.01ms !important}}
</style></head>
<body>
<div id="neb" aria-hidden="true"></div>
<canvas id="bg"></canvas>
<div class="wrap">

  <header class="top">
    <div>
      <div class="brand">
        <div class="orb" aria-hidden="true"><span class="ring r1"></span><span class="ring r2"></span>
          <span class="core">◈</span><span class="sat s1"></span><span class="sat s2"></span><span class="sat s3"></span></div>
        <div>
          <div class="eyebrow">Mahesh · build log · __TODAY__</div>
          <h1>Mission <span class="grad">Control</span></h1>
        </div>
      </div>
      <p class="sub">Every project built with Hermes plus everything parked on the F: drive — live status, honest progress, and the next move for each one.</p>
      <div class="hero-pills">
        <span class="hp"><i class="dotc" style="--c:#34d399"></i>__SL__ shipping</span>
        <span class="hp"><i class="dotc" style="--c:#7dd3fc"></i>__NWK__ active in progress</span>
        <span class="hp"><i class="dotc" style="--c:#f87171"></i>__NB__ need a decision</span>
        <span class="hp"><i class="dotc" style="--c:#f59e0b"></i>__NT__ touched this week</span>
      </div>
    </div>
    <div class="hbtns">
      <button class="btn accent" id="palBtn">Search everything <kbd>Ctrl</kbd><kbd>K</kbd></button>
      <button class="btn" id="repBtn">Progress report <kbd>R</kbd></button>
    </div>
  </header>

  <div class="ticker"><div class="t" id="tick"></div></div>

  <div class="kpis">__KPIS__</div>
  <div class="stats">__STATS__</div>

  <div class="analytics">
    <div class="panel"><h3>Where the work sits</h3><p class="cap">Status mix across all __NP__ tracked projects.</p>__DONUT__</div>
    <div class="panel"><h3>Activity, last 12 months</h3><p class="cap">Projects touched per month, straight from real file dates.</p>
      <svg class="spark" viewBox="0 0 262 84" preserveAspectRatio="none"><defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#7dd3fc"/><stop offset="60%" stop-color="#a78bfa"/><stop offset="100%" stop-color="#34d399"/></linearGradient></defs>__SPARK__</svg>
      <div class="resultline"><span>__NH__ built or worked in Hermes</span><span>__NF__ discovered on disk</span></div>
    </div>
  </div>

  <div class="controls">
    <div class="searchrow">
      <div class="search">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/></svg>
        <input id="q" type="search" placeholder="Filter projects, folders, blockers…" autocomplete="off">
      </div>
      <div class="seg" id="views">
        <button data-v="grid" class="on">▦ Grid</button>
        <button data-v="board">▥ Board</button>
        <button data-v="table">☰ Table</button>
      </div>
      <div class="seg" id="sorts">
        <button data-s="name" class="on">A–Z</button>
        <button data-s="pct">Progress</button>
        <button data-s="age">Freshest</button>
      </div>
    </div>
    <div class="chips" id="chips">
      <button class="chip on" data-f="all" style="--c:#7dd3fc"><b>__NP__</b><span>Everything</span></button>
      <button class="chip" data-f="hermes" style="--c:#7dd3fc"><b>__NH__</b><span>Built in Hermes</span></button>
      __CHIPS__
    </div>
    <div class="chips" id="catchips"><span class="catlab">Category</span>__CATCHIPS__</div>
    <div class="resultline"><span id="rline">__NP__ projects</span><span id="liveLine">live ping every 12s · Ctrl+K command palette</span></div>
  </div>

  <section id="viewGrid" class="grid">__CARDS__</section>
  <section id="viewBoard" hidden>__BOARD__</section>
  <section id="viewTable" hidden>__TABLE__</section>

  <div class="analytics" id="repBlock">
    <div class="panel"><h3>Progress report</h3><p class="cap">Same data, dense view — sortable in the Table tab.</p>
      <p style="font-size:13px;color:#b9c4dc;line-height:1.7">__NOTE__</p>
    </div>
    <div class="panel"><h3>How to read this</h3><p class="cap">Honesty rules baked into the numbers.</p>
      <ul style="margin:0;padding-left:18px;color:#b9c4dc;font-size:13.5px;line-height:1.8">
        <li><b>Live / Working / In progress / Blocked / Parked / Done</b> come from real Hermes sessions and verified checks.</li>
        <li><b>Archived · unverified</b> entries were identified by folder name, contents and last-modified date only — their progress % is a guess.</li>
        <li><b>Progress %</b> is an estimate of completeness, not a metric anyone measured.</li>
        <li><b>Green dots</b> are real HTTP pings to your local servers, refreshed live.</li>
      </ul>
    </div>
  </div>

  <footer>
    <div><b>__NP__ projects</b> · __NH__ built in Hermes · __NG__ pushed to GitHub · average __AVG__% complete · generated __TODAY__<br>
    Statuses from session history and verified checks; archived entries are name-and-date guesses.</div>
    <div class="mono">◈ built by Hermes · <span id="clock"></span></div>
  </footer>
</div>

<canvas id="fx"></canvas>
<div id="toast"></div>

<div class="modal" id="modal"><div class="sheet" id="sheet">
  <div class="mhero" id="mHero"></div>
  <button class="x" id="mx">✕</button>
  <h2 id="mName"></h2>
  <div class="rowmeta" id="mMeta"></div>
  <div class="bigpct" id="mPct"></div>
  <p style="color:#c3cee6;font-size:14.5px;line-height:1.65" id="mDesc"></p>
  <div class="cols2" style="margin-top:16px">
    <div class="blk"><h4>Done</h4><div id="mDone"></div></div>
    <div class="blk"><h4>Open / next</h4><div id="mTodo"></div></div>
  </div>
  <div class="code" id="mPath"></div>
  <nav id="mNav" style="margin-top:16px"></nav>
</div></div>

<div class="pal" id="pal"><div class="palbox">
  <input class="palin" id="palq" placeholder="Jump to a project, status or category…" autocomplete="off">
  <div class="pallist" id="pallist"></div>
  <div class="palfoot">↑ ↓ to move · ↵ to open · esc to close</div>
</div></div>

<script>
const DATA = __DATA__;
const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
const cards=$$('#viewGrid .card');
cards.forEach((c,n)=>c.style.setProperty('--d',n));

/* ---------- toast ---------- */
let tt; const toast=m=>{const t=$('#toast');t.textContent=m;t.classList.add('on');clearTimeout(tt);tt=setTimeout(()=>t.classList.remove('on'),1900)};

/* ---------- confetti on card open ---------- */
const fx=$('#fx'),fxc=fx.getContext('2d');let parts=[],raf=null;
function sizeFx(){fx.width=innerWidth*devicePixelRatio;fx.height=innerHeight*devicePixelRatio;fxc.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0)}
sizeFx(); addEventListener('resize',sizeFx);
function burst(x,y,color){
  for(let i=0;i<26;i++){const a=Math.random()*Math.PI*2,s=1+Math.random()*5;
    parts.push({x,y,vx:Math.cos(a)*s,vy:Math.sin(a)*s-1.6,life:1,c:color||['#7dd3fc','#a78bfa','#34d399','#fca5a5'][i%4],r:2+Math.random()*3})}
  if(!raf) raf=requestAnimationFrame(step)
}
function step(){
  fxc.clearRect(0,0,fx.width,fx.height);
  parts=parts.filter(p=>p.life>0);
  parts.forEach(p=>{p.x+=p.vx;p.y+=p.vy;p.vy+=0.14;p.life-=0.022;
    fxc.globalAlpha=Math.max(0,p.life);fxc.fillStyle=p.c;
    fxc.beginPath();fxc.arc(p.x,p.y,p.r,0,6.283);fxc.fill()});
  fxc.globalAlpha=1;
  if(parts.length) raf=requestAnimationFrame(step); else {raf=null;fxc.clearRect(0,0,fx.width,fx.height)}
}

/* ---------- background constellation ---------- */
const bg=$('#bg'),bgc=bg.getContext('2d');let W,H,pts=[];
const LINK2=17000;
function sizeBg(){W=bg.width=innerWidth;H=bg.height=innerHeight;bgc.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);
  const n=Math.min(78,Math.round(W*H/26000));
  pts=Array.from({length:n},()=>({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.16,vy:(Math.random()-.5)*.16,r:Math.random()*1.5+.4}))}
sizeBg(); addEventListener('resize',sizeBg);
let lastDraw=0;
(function loop(t){
  requestAnimationFrame(loop);
  if(t-lastDraw<33) return;          // ~30fps cap
  lastDraw=t;
  bgc.clearRect(0,0,W,H);
  for(const p of pts){p.x+=p.vx;p.y+=p.vy;
    if(p.x<0||p.x>W)p.vx*=-1; if(p.y<0||p.y>H)p.vy*=-1;
    bgc.beginPath();bgc.fillStyle='rgba(160,190,255,.5)';bgc.arc(p.x,p.y,p.r,0,6.283);bgc.fill()}
  for(let i=0;i<pts.length;i++)for(let j=i+1;j<pts.length;j++){
    const a=pts[i],b=pts[j],dx=a.x-b.x,dy=a.y-b.y,d2=dx*dx+dy*dy;
    if(d2<LINK2){bgc.strokeStyle='rgba(125,211,252,'+(0.14*(1-d2/LINK2))+')';
      bgc.beginPath();bgc.moveTo(a.x,a.y);bgc.lineTo(b.x,b.y);bgc.stroke()}}
})();
</script>
<script>
/* ================= behaviour ================= */
const ALL=[...DATA];
let filter='all',cat='all',q='',sort='name',view='grid';

const orderCards=()=>{
  const g=$('#viewGrid');
  const arr=[...g.children].sort((a,b)=>{
    if(sort==='pct') return +b.dataset.pct-+a.dataset.pct;
    if(sort==='age') return +a.dataset.age-+b.dataset.age;
    return a.querySelector('h3').textContent.localeCompare(b.querySelector('h3').textContent);
  });
  arr.forEach(c=>g.appendChild(c));
};
const matches=el=>{
  const f = filter==='all' ? true : filter==='hermes' ? el.dataset.src==='hermes' : el.dataset.status===filter;
  const c = cat==='all' || el.dataset.cat===cat;
  const t = !q || el.dataset.hay.includes(q);
  return f&&c&&t;
};
function apply(){
  let n=0;
  $$('#viewGrid .card').forEach(c=>{const ok=matches(c);c.style.display=ok?'':'none';if(ok)n++});
  $$('#viewTable tbody tr').forEach(r=>{const f=filter==='all'?true:filter==='hermes'?r.dataset.src==='hermes':r.dataset.status===filter;
    const c=cat==='all'||r.dataset.cat===cat;const t=!q||r.dataset.hay.includes(q);
    r.style.display=(f&&c&&t)?'':'none'});
  $('#rline').textContent = (q||cat!=='all'||filter!=='all') ? n+' of '+DATA.length+' projects shown' : DATA.length+' projects';
  drawBar();
}
const drawBar=()=>$$('#viewGrid .card').forEach(c=>{if(c.style.display!=='none'){const i=c.querySelector('.bar i');i.style.width=i.dataset.w+'%'}});
$('#q').addEventListener('input',e=>{q=e.target.value.trim().toLowerCase();apply()});
$$('#chips .chip').forEach(b=>b.onclick=()=>{
  $$('#chips .chip').forEach(x=>{if(x.dataset.f)x.classList.remove('on')});
  b.classList.add('on');filter=b.dataset.f;apply()});
$$('#catchips .chip').forEach(b=>b.onclick=()=>{
  const on=b.classList.contains('on');
  $$('#catchips .chip').forEach(x=>x.classList.remove('on'));
  if(on){cat='all'}else{b.classList.add('on');cat=b.dataset.c}
  apply()});
$$('#views button').forEach(b=>b.onclick=()=>{
  $$('#views button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
  view=b.dataset.v;
  $('#viewGrid').hidden = view!=='grid';
  $('#viewBoard').hidden = view!=='board';
  $('#viewTable').hidden = view!=='table';
  if(view==='grid') requestAnimationFrame(drawBar);
  localStorage.setItem('pd.view',view);
});
$$('#sorts button').forEach(b=>b.onclick=()=>{
  $$('#sorts button').forEach(x=>x.classList.remove('on'));b.classList.add('on');
  sort=b.dataset.s;orderCards();requestAnimationFrame(drawBar);localStorage.setItem('pd.sort',sort)});
const savedView=localStorage.getItem('pd.view'); if(savedView)$(`#views button[data-v="${savedView}"]`)?.click();
const savedSort=localStorage.getItem('pd.sort'); if(savedSort)$(`#sorts button[data-s="${savedSort}"]`)?.click();
else $('#sorts button[data-s="name"]').click();

/* card spotlight */
$$('#viewGrid .card').forEach(c=>c.addEventListener('pointermove',ev=>{
  const r=c.getBoundingClientRect();
  c.style.setProperty('--mx',((ev.clientX-r.left)/r.width*100)+'%');
  c.style.setProperty('--my',((ev.clientY-r.top)/r.height*100)+'%')}));

/* copy path */
document.addEventListener('click',e=>{
  const cp=e.target.closest('.cp');
  if(cp){e.stopPropagation();const p=cp.parentElement.dataset.path;
    navigator.clipboard?.writeText(p).then(()=>toast('Copied folder path'),()=>toast(p));return}
  if(e.target.closest('a')) e.stopPropagation();
});

/* ---------- modal ---------- */
const openM=i=>{
  const p=ALL[i];if(!p)return;
  $('#mHero').innerHTML=p.cover||'';
  $('#mName').textContent=p.n;
  $('#mMeta').innerHTML=`<span class="st" style="--c:${p.col}">${p.s}</span><span class="cat">${p.c}</span><span>${p.src}</span><span>last change ${p.ago}</span>${p.port?`<span>port :${p.port}</span>`:''}`;
  $('#mPct').innerHTML=`<b style="--c:${p.col};color:${p.col}">${p.pct}<sup style="font-size:15px">%</sup></b>
    <div style="flex:1"><div class="bar" style="--c:${p.col}"><i style="width:${p.pct}%"></i></div>
    <small style="color:var(--mu);font-size:12px">progress, estimated</small></div>`;
  $('#mDesc').textContent=p.d;
  $('#mDone').textContent=p.done; $('#mTodo').textContent=p.todo;
  $('#mPath').innerHTML=p.path+' <span class="cp" style="cursor:pointer">copy</span>';
  let nav='';
  if(p.local) nav+=`<a class="lnk go" href="${p.local}" target="_blank" rel="noopener">▶ Launch app</a>`;
  if(p.gh) nav+=`<a class="lnk gh" href="${p.gh}" target="_blank" rel="noopener">★ Open repository</a>`;
  nav+=`<a class="lnk" href="file:///${p.path.replace(/\\/g,'/').replace(/ /g,'%20')}">📁 Open folder</a>`;
  $('#mNav').innerHTML=nav;
  $('#modal').classList.add('on'); document.body.style.overflow='hidden';
  const r=$('#viewGrid .card[data-i="'+i+'"]');
  if(r){const b=r.getBoundingClientRect();burst(b.left+b.width/2,b.top+40,r.style.getPropertyValue('--c'))}
  setTimeout(()=>$('#mx').focus(),30);
};
const closeM=()=>{$('#modal').classList.remove('on');document.body.style.overflow=''};
$('#mx').onclick=closeM;
$('#modal').onclick=e=>{if(e.target.id==='modal')closeM()};
$('#viewGrid').addEventListener('click',e=>{const c=e.target.closest('.card');if(c)openM(+c.dataset.i)});
$('#viewBoard').addEventListener('click',e=>{const c=e.target.closest('.bcard');if(!c)return;
  const n=c.querySelector('.btop b').textContent;const i=ALL.findIndex(x=>x.n===n);if(i>=0)openM(i)});
$('#repBtn').onclick=()=>$('#repBlock').scrollIntoView({behavior:'smooth',block:'center'});

/* ---------- command palette ---------- */
const pal=$('#pal'),palq=$('#palq'),pallist=$('#pallist');let sel=0,rows=[];
function buildPal(){
  const t=palq.value.trim().toLowerCase();
  rows=[];
  ALL.forEach((p,i)=>{if(!t||(p.n+p.c+p.s+p.d).toLowerCase().includes(t))rows.push({t:p.n,sub:p.c,st:p.s,c:p.col,i})});
  pallist.innerHTML=rows.slice(0,40).map((r,k)=>`<div class="pali ${k===sel?'sel':''}" data-k="${k}" style="--c:${r.c}"><span class="em"></span>${r.t}<span class="stt">${r.st} · ${r.sub}</span></div>`).join('')
    ||'<div class="pali">no match</div>';
}
function openPal(){pal.classList.add('on');palq.value='';sel=0;buildPal();setTimeout(()=>palq.focus(),20)}
function closePal(){pal.classList.remove('on')}
$('#palBtn').onclick=openPal;
pal.onclick=e=>{if(e.target.id==='pal')closePal()};
palq.addEventListener('input',()=>{sel=0;buildPal()});
pallist.addEventListener('click',e=>{const r=e.target.closest('.pali');if(!r||!rows[+r.dataset.k])return;closePal();openM(rows[+r.dataset.k].i)});
addEventListener('keydown',e=>{
  if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();pal.classList.contains('on')?closePal():openPal();return}
  if(e.key==='Escape'){closePal();closeM();return}
  if(pal.classList.contains('on')){
    if(e.key==='ArrowDown'){e.preventDefault();sel=Math.min(sel+1,Math.min(39,rows.length-1));buildPal()}
    if(e.key==='ArrowUp'){e.preventDefault();sel=Math.max(sel-1,0);buildPal()}
    if(e.key==='Enter'&&rows[sel]){closePal();openM(rows[sel].i)}
  } else if(e.key==='/'&&document.activeElement.tagName!=='INPUT'){e.preventDefault();openPal()}
  else if(e.key.toLowerCase()==='r'&&!e.ctrlKey&&!e.metaKey&&document.activeElement.tagName!=='INPUT'){$('#repBlock').scrollIntoView({behavior:'smooth'})}
});

/* ---------- ticker ---------- */
const t1=ALL.filter(p=>p.todo&&p.todo!=='None known.').map(p=>'<b><em>▸ '+p.n.split(' - ')[0]+'</em> — '+p.todo.replace(/"/g,'')+'</b>').join('');
$('#tick').innerHTML=t1+t1;

/* ---------- live ping ---------- */
let up=0,tot=0;
async function ping(){
  up=0;tot=0;
  await Promise.all(cards.filter(c=>c.dataset.port!==undefined).map(async c=>{
    tot++;const el=$('#ping'+c.dataset.i);
    try{const ctl=new AbortController();const to=setTimeout(()=>ctl.abort(),2200);
      await fetch('http://127.0.0.1:'+c.dataset.port+'/',{mode:'no-cors',signal:ctl.signal});
      clearTimeout(to);el.className='dot up';el.querySelector('b').textContent='UP :'+c.dataset.port;up++}
    catch(_){el.className='dot down';el.querySelector('b').textContent='offline'}
  }));
  $('#liveN').textContent=up+'/'+tot;
  $('#liveLine').textContent = tot? (up? up+' of '+tot+' local servers answering' : 'no local servers answering — start one from a card') : 'no launchable servers in this set';
}
ping();setInterval(ping,12000);

/* ---------- clock + reveal ---------- */
setInterval(()=>{$('#clock').textContent=new Date().toLocaleTimeString()},1000);
$('#clock').textContent=new Date().toLocaleTimeString();
orderCards();
requestAnimationFrame(drawBar);
setTimeout(drawBar,120);

/* safety net: if animations were skipped/paused, never leave a card invisible */
const reveal=()=>cards.forEach(c=>{if(parseFloat(getComputedStyle(c).opacity)<0.02){
  c.style.animation='none';c.style.opacity='1';c.style.transform='none';}});
[1200,2200,3600].forEach(t=>setTimeout(reveal,t));
addEventListener('pageshow',reveal);
setTimeout(reveal,6000);
</script>
</body></html>'''

def rep():
    return (f"{len(P)} projects tracked, {hermes_n} of them built or worked on inside Hermes. "
            f"Average progress sits at {avg}% (an estimate, not a measurement), and {today_n} projects "
            f"changed in the last seven days. {blocked_n} are blocked or parked and need a decision, not more code. "
            f"Every card links straight to the folder, the running app, or the repository — and the green dot "
            f"next to a port is a real HTTP ping, not a guess.")


page = (TPL
        .replace("__TODAY__", e(TODAY)).replace("__NP__", str(len(P)))
        .replace("__SL__", str(shipped))
        .replace("__NWK__", str(counts["working"] + counts["progress"] + counts["live"]))
        .replace("__NB__", str(blocked_n)).replace("__NT__", str(today_n))
        .replace("__NH__", str(hermes_n)).replace("__NF__", str(folder_n))
        .replace("__NG__", str(gh_n)).replace("__AVG__", str(avg))
        .replace("__KPIS__", kpis).replace("__STATS__", stat_tiles)
        .replace("__DONUT__", donut).replace("__SPARK__", spark)
        .replace("__CHIPS__", chips).replace("__CATCHIPS__", chip_cats)
        .replace("__CARDS__", cards_html).replace("__BOARD__", board_html)
        .replace("__TABLE__", table_html).replace("__DATA__", data_js)
        .replace("__NOTE__", e(rep())))

open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(page)

md = [f"# Projects Progress Report ({TODAY})\n",
      f"{len(P)} projects tracked; {hermes_n} built/worked in Hermes; average progress {avg}% (estimate).\n",
      "| Project | Status | % | Done | Open / next |", "|---|---|---|---|---|"]
for p in P:
    md.append(f'| {p["name"]} | {STATUS[p["status"]][0]} | {p["pct"]}% | {p["done"]} | {p["todo"]} |')
md.append("\n_Archived/unverified entries were identified by folder name, contents and dates only._\n")
open(os.path.join(OUT, "PROGRESS_REPORT.md"), "w", encoding="utf-8").write("\n".join(md))
print("ok", len(P), "projects;", counts, "| avg", avg, "| hermes", hermes_n, "| gh", gh_n, "| bytes", len(page))
