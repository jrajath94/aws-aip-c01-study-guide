# Prompt sources for the Muse video prompt

## Prompts from the linked session

- Session: https://claude.ai/code/session_017BHx4Ro7SEm2QNzZ4MpV1o
- Status: Not read. The session record was available as metadata only. Its title is "Explainer videos for interview prep". Its transcript and prompt text were not readable from this session.
- Prompts used from this session: none.

## Prompt-named files in this repo

These files are slide and diagram assets. They are not Muse prompts. The video prompt uses their topics, not their text.

| Path | Used for |
|---|---|
| slides/aip-c01/project/slides/d1-t16-prompts.html | Domain 1 prompt topic, scene 10 and scene 14 context |
| slides/aip-c01/project/slides/d2-prompt-mgmt.html | Domain 2 prompt management topic, scene 15 context |
| slides/aip-c01/project/slides/d3-prompt-attacks.html | Domain 3 prompt attack topic, scene 17 context |
| slides/aip-c01/project/slides/d4-prompt-cache.html | Domain 4 prompt caching topic, scene 22 |
| assets/img/mermaid/27-prompt-caching.mmd | Prompt caching diagram, scene 22 |
| assets/img/mermaid/36-prompt-compression.mmd | Prompt compression, not in the guide, not used |
| assets/img/mermaid/60-prompt-flows.mmd | Prompt flows, not in the guide, not used |
| assets/img/mermaid/69-prompt-management.mmd | Prompt management, scene 15 context |
| assets/img/mermaid/71-prompt-attack-taxonomy.mmd | Prompt attack taxonomy, scene 17 context |
| assets/img/ste100/aip-prompt-caching.svg | Prompt caching visual, scene 22 |
| assets/img/ste100/aip-prompt-cache-hit.svg | Cache hit visual, scene 22 |
| assets/img/ste100/aip-prompt-lifecycle.svg | Prompt lifecycle, not in the guide, not used |

## Branch copies

The branch origin/cursor/visual-treatise-3ba5 has the same prompt-named assets listed above. It has no separate Muse prompt file.

## Guide sources for the scenes

The scene facts come from the guide, article version 22, in slides/aip-c01/article/index.html. The scene list names each unit ID. Each unit names its official AWS page in the guide.

## AWS-P1 video course branch

- Branch: claude/muse-video-course, tip 7126031d, per the coordinator relay.
- Status: not on origin in this repo. Not read.
- Files not used: FINAL RUN brief (Parts 1 to 8), video-course/examples/README.md, QC.md, CRITICS.md, CRITICS-R2.md, pilot-work/next-run/.

## Practice exam uploads

- Six files: Practice Exam 1 to 6, AIP-C01, uploaded to this session.
- Read by extracting the window.__QUIZ_DATA__ JSON in each file. Each file has 75 questions.
- Output: /mnt/project-files/aip-c01-exams/practice-exams-all.md and practice-exams-all.json.
- Used in the video prompt: first question of each unit group, in the practice exam frames section of muse-prompt.md.
