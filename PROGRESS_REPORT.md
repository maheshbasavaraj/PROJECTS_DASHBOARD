# Projects Progress Report (2026-09-29)

28 projects tracked; 12 built/worked in Hermes; average progress 68% (estimate).

| Project | Status | % | Done | Open / next |
|---|---|---|---|---|
| CPU RUSH | Live | 85% | All 7 modes start and return correct puzzle payloads (verify.js all-green); README + GitHub push done; HIT/MISS + controls UI fix. | Gameplay/grading not verified end-to-end for every mode; server can serve stale code; no public deploy yet. |
| DSDS - Data Structure Design Studio | Live | 90% | Web app, tests, Dockerfile, render.yaml, GitHub repo, DEPLOY.md. | Render deploy not live (dsds.onrender.com returns 404). Students need a public HTTPS URL. |
| Alien Shooter 3D | In progress | 70% | Built Jun 8; 5 improvement iterations (sound, reload, hit flash, damage numbers); empty-landscape/no-enemies bug worked on. | Session on 29 Sep: add a new gameplay level to the original GameTop Alien Shooter install (in progress). No git repo. |
| Kannada Dub (YouTube EN to Kn audio) | Blocked | 65% | Stages s1 (download/audio split) working; pipeline, docs, verify.py, refs and models in place. | GPU ASR crashed on 23 Sep: cublas64_12.dll not found (CUDA runtime). Re-run to confirm whether fixed since. |
| Unclutter (OpenRouter provider) | In progress | 60% | Provider code (lib/providers.ts, lib/model.ts) reviewed and extended in the 28 Sep session. | 18 uncommitted changes; not confirmed built and tested end-to-end. |
| JEV Mail Classifier | Parked | 70% | config.suggested.yaml built and tested with real Jev calls on subject lines. | Parked. Needs IMAP_USERNAME / IMAP_PASSWORD in .env, merge categories into config.yaml, run jev-mail run --dry-run. |
| Learning Platform (Game Forge + DSDS + SWE Quiz) | In progress | 75% | Platform app, hub, Dockerfile, docker-compose, DEPLOY.md, all three modules vendored in. | Not deployed publicly; not run in this session (needs Docker Desktop: docker compose up --build, then localhost:8080). |
| Game Forge (Educational Game MCP) | Working | 80% | System prompt, MCP tools, 5 sample games (factorial, fibonacci, fraction-catch, tower-of-hanoi, verify-pipeline), Ollama driver. | Run with: python app.py (port 8000, so stop DSDS first or change port). |
| BIOE3 Bio-AI Proposal (DBT-BIRAC) | Done | 100% | Proposal, budget template, quick reference, research notes; supporting arXiv pulls in dbt_birac_bioai/. | Call deadline was 30 Jun 2026 (passed). Partner names/PI details were placeholders. |
| Socratic Instructor Playbook (OS) | Done | 100% | Playbook built; README with syllabus map pushed to GitHub. | None known. |
| Agentic-Q paper (revised) | Done | 90% | Revised + final DOCX/DOCM, reviewer comment JSONs, rendered output. | Turnitin AI % target (<=30%) not confirmed here. |
| Agentic AI - Saksham / FDP | Working | 70% | App, MCP servers, Teacher material; private GitHub repo. | Uses fdp\Scripts\python.exe. Not run in this session. |
| Pi Ad Blocker | Archived / unverified | 50% | Code and benchmarks present. | Status not verified; folder inspected only by name. |
| Meme Gen / AR Ad Blocker | Archived / unverified | 50% | Multiple attempts kept. | Status not verified. |
| Patenter | Archived / unverified | 50% | Drafts and forms present. | Status not verified. |
| PPT Generator | Archived / unverified | 60% | app.py, main.py, generator, sample output. | Status not verified. |
| Certificate Generator | Archived / unverified | 80% | cert_gen.py with generated certificate PDFs. | Status not verified. |
| VTU Marks Extractor | Done | 90% | Built exe (dist/build), extracted_marks.xlsx produced. | Status not verified beyond outputs. |
| Doc Gen (QP generator) | Archived / unverified | 60% | generator.py + sample QP. | Status not verified. |
| Extropic / Thermodynamic Computing | Archived / unverified | 50% | Two DOCX drafts, paper.pdf, thrml source. | Status not verified. |
| Articles (AI patent white paper, VR edu survey) | Archived / unverified | 60% | AI_Patent_White_Paper_2025, decentralized VR edu survey, extropic. | Status not verified. |
| Lab (Agentic AI, AIML, GenAI) | Archived / unverified | 60% | Three lab folders. | Status not verified. |
| Quiz / SET / ButterCloud Quiz | Archived / unverified | 60% | App + backups. | Status not verified. |
| YouTube Channel content | Archived / unverified | 40% | Scripts and one MP4. | Status not verified. |
| Agent (Telegram to WhatsApp) | Archived / unverified | 50% | Scripts + README. | Status not verified. |
| Face Recognition / Anti-Spoofing | Archived / unverified | 50% | Student face data and spoof repo. | Status not verified. |
| CI/CD demos (CICD, mlops-cicd) | Done | 90% | Repos pushed (CICD, CI, cd, mlops-cicd). | None known. |
| ComfyUI + Wan2GP (media gen) | Working | 60% | ComfyUI-Easy-Install; Wan2GP in F:\WANGP. | Status not verified. |

_Archived/unverified entries were identified by folder name, contents and dates only._
