# Gaps for the Muse video prompt

## Muse limits

- Muse length or duration limits: Not in source.
- Muse scene count limit: Not in source.

## Prompts not found

- The linked session https://claude.ai/code/session_017BHx4Ro7SEm2QNzZ4MpV1o: the transcript was not readable. Its prompts are not in this prompt.
- Prompts that the user calls "created in this repo": no file in the repo is a Muse or video prompt. The repo has prompt-named slide and diagram assets. Those are listed in prompt-sources.md. If the user means other prompt files, send the paths and the prompt will be updated.

## Units with no visual in the prompt

- Q1 to Q8 and Q12 to Q13: the prompt gives these units one shared scene or none. Only Q5, Q7, Q9, Q10, Q11, and Q14 to Q16 have a dedicated scene.
- G1 to G4 and H3: the prompt uses one card each. The prompt does not add an official AWS diagram for these units.
- P6: the prompt names the ML basics in one panel. The guide states the XGBoost facts only in this unit.

## Guide topics without a prompt scene

- Part 1 and Part 1B to Part 1C: covered by scenes 2 to 6 at topic level only.
- Part 8B console steps: covered by scene 8 at topic level only.
- Part 8C glossary: no scene. The glossary is for reference, not for video.
- Part 8D and Part 8A3: no scene in this prompt. Add them if the video must show them.

## Official diagrams

- Part 8A7 has 18 official AWS diagrams. The prompt uses them in scene 33 only.
- Most units have no official AWS diagram in the guide. Scenes that name a diagram use a schematic instead.
- Source credits are not in the video. The source list is in the guide, not in the video.

## Facts not checked in this pass

- The prompt uses guide facts. It was not checked against each official page again in this pass.
- Facts from units Q1 to Q8 and P1 to P6 were not re-read in this pass.

## Checks not run

- Watermark checks: not run. The video is not uploaded.
- The Anthropic Sans font: not installed. Scene text uses Inter.

## Video course branch not found

- Branch claude/muse-video-course: not on origin for aws-aip-c01-study-guide. `git ls-remote origin` lists no such ref. Tip 7126031d is not in this repo.
- Not used because not found: the FINAL RUN brief (Parts 1 to 8), video-course/examples/README.md (32 example types), QC.md, CRITICS.md, CRITICS-R2.md, pilot-work/next-run/, and the two NEXT RUN prompts.
- muse-prompt.md is still the first version. It has not been rewritten to the brief. muse-prompt-v1.md is the same text.
- AIF-C01 dependency: the coordinator's relay says the session uses AIF-C01 domain weights. This prompt does not use them. The guide's domain weights are 31, 26, 20, 12, and 11 percent.

## FINAL RUN brief: pending

- The FINAL RUN brief, Parts 1 to 8 of the AWS-P1 video course, is not in this repo or on origin. Branch claude/muse-video-course is not on origin.
- Pending: the user may upload the brief or name the repo that holds it.
- muse-prompt.md is the working copy. It has the practice frames added. The brief's method is not applied.

## Practice exams: verification not run

- The 450 practice questions from Practice Exams 1 to 6 are not checked against official AWS pages. No question has a verified note.
- Each question maps to a guide unit by keyword match. The mapping is rough and was not reviewed. See practice-exams-all.md for each unit count.
- 45 questions have no unit match. They sit in the practice group.
- No stem repeats across the six exams. A near-duplicate check found no pairs above 0.85 similarity.
- Exam text is in /mnt/project-files only. It is not in the public repo.

## Video prompt length

- The 450-question prompt is superseded. The current muse-prompt.md is the 43-scene curriculum-only file, about 21,114 characters.
- Superseded: Muse length and input limits: Not in source. The prompt may not fit one Muse run.
- Superseded: If one run fails, run Parts 1, 2, and 3 in order. Each part has about 150 questions.
- Superseded: The summary version with 31 frames is muse-prompt-summary.md.

## Dash and semicolon handling in exam text

- Em dashes and en dashes in exam text were replaced with a comma and a space.
- Semicolons in exam text were kept. They are part of the exam wording.

## Lost text: 35-scene Muse prompt

- The first version of muse-prompt.md had 35 scenes. Its text was overwritten during a rewrite. The first match of the end marker fell in the instruction line, which cut the head of the file.
- muse-prompt-v1.md was deleted by mistake. It held the 35-scene text.
- Neither version is recovered.
- The current muse-prompt.md has 43 scenes. It was rebuilt from session records. Its wording may differ from the lost text.
- Correction to the "Muse prompt is still the first version" note above: muse-prompt-v1.md no longer exists, so it cannot be the same text.
