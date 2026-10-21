(() => {
  'use strict';

  const C = window.COURSE;
  if (!C) {
    console.error("COURSE data not loaded.");
    return;
  }

  const $ = id => document.getElementById(id);
  const esc = val => String(val ?? '').replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));

  // LocalStorage state management
  const STORAGE_KEY = 'aip-c01-masterclass-v2';
  const store = {
    get() {
      try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
      catch { return {}; }
    },
    save() {
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }
      catch {}
    }
  };

  const domainNames = {
    0: 'Foundations & Strategy',
    1: 'Domain 1: Models & Data (31%)',
    2: 'Domain 2: Implementation (26%)',
    3: 'Domain 3: Security & Governance (20%)',
    4: 'Domain 4: Optimization (12%)',
    5: 'Domain 5: Testing & Evaluation (11%)'
  };

  const domainColors = {
    0: 'var(--d0-accent)',
    1: 'var(--d1-accent)',
    2: 'var(--d2-accent)',
    3: 'var(--d3-accent)',
    4: 'var(--d4-accent)',
    5: 'var(--d5-accent)'
  };

  let state = Object.assign({
    mode: 'slides', // slides | treatise | mock | quizzes | recalls | skills | references
    currentId: 'core-001',
    layer: 'intuition', // intuition | architecture | api | traps | rule
    learned: {},
    weak: {},
    answers: {},
    mockAnswers: {},
    mockDone: false,
    mockDeadline: 0,
    theme: 'dark'
  }, store.get());

  // Master item lookup
  const coreMap = new Map(C.core.map(s => [s.id, s]));
  const quizMap = new Map(C.quizzes.map(q => [q.id, q]));
  const refMap = new Map(C.references.map(r => [r.id, r]));

  let currentItem = coreMap.get(state.currentId) || C.core[0];
  let visibleItems = [];
  let lightboxZoom = 100;

  // Initialize theme
  document.body.className = `theme-${state.theme} mode-${state.mode}`;

  /* ==========================================================================
     Item Filtering & Navigation List
     ========================================================================== */
  function getFilteredItems() {
    const term = $('search-input').value.trim().toLowerCase();
    const domainFilter = $('domain-select').value;
    
    let pool = [];
    if (state.mode === 'slides' || state.mode === 'treatise') {
      pool = C.core;
    } else if (state.mode === 'mock') {
      pool = C.mock.map(id => quizMap.get(id)).filter(Boolean);
    } else if (state.mode === 'quizzes') {
      pool = C.quizzes;
    } else if (state.mode === 'recalls') {
      pool = C.recalls.map((r, i) => ({ ...r, id: `recall-${i}`, title: r.question }));
    } else if (state.mode === 'skills') {
      pool = C.skills.map(s => ({ ...s, title: `Skill ${s.id}: ${s.description}` }));
    } else if (state.mode === 'references') {
      pool = C.references;
    }

    return pool.filter(item => {
      const matchDomain = domainFilter === 'all' || String(item.domain) === domainFilter;
      if (!matchDomain) return false;
      if (!term) return true;
      const haystack = (item.title + ' ' + (item.lead || '') + ' ' + (item.points || []).join(' ') + ' ' + (item.text || '')).toLowerCase();
      return haystack.includes(term);
    });
  }

  function updateSidebarList() {
    visibleItems = getFilteredItems();
    $('item-count-badge').textContent = `${visibleItems.length} items`;

    const frag = document.createDocumentFragment();
    visibleItems.forEach(item => {
      const btn = document.createElement('button');
      btn.className = `nav-item-btn ${item.id === currentItem.id ? 'active' : ''} ${state.learned[item.id] ? 'learned' : ''} ${state.weak[item.id] ? 'weak' : ''}`;
      
      const icon = document.createElement('span');
      icon.className = 'status-icon';
      icon.textContent = state.learned[item.id] ? '✓' : state.weak[item.id] ? '★' : '•';
      
      const text = document.createElement('span');
      text.textContent = item.displayTitle || item.title;
      
      btn.appendChild(icon);
      btn.appendChild(text);
      btn.onclick = () => selectItem(item.id);
      frag.appendChild(btn);
    });

    $('nav-item-list').replaceChildren(frag);
    updateProgressStats();
  }

  function updateProgressStats() {
    const totalCore = C.core.length;
    const learnedCount = C.core.filter(s => state.learned[s.id]).length;
    const pct = Math.round((learnedCount / totalCore) * 100);
    $('progress-bar-fill').style.width = `${pct}%`;
    $('progress-text').textContent = `${learnedCount} of ${totalCore} slides learned (${pct}%)`;
  }

  function selectItem(id) {
    let target = coreMap.get(id) || quizMap.get(id) || refMap.get(id) || visibleItems.find(x => x.id === id);
    if (!target) return;
    currentItem = target;
    state.currentId = id;
    store.save();

    updateSidebarList();
    renderMainView();

    // On mobile, close sidebar after pick
    if (window.innerWidth <= 860) {
      $('sidebar').classList.remove('open');
    }
  }

  /* ==========================================================================
     Mode Switching
     ========================================================================== */
  function switchMode(newMode) {
    state.mode = newMode;
    document.body.className = `theme-${state.theme} mode-${state.mode}`;
    document.querySelectorAll('.mode-tab').forEach(tab => {
      tab.classList.toggle('active', tab.dataset.mode === newMode);
    });
    store.save();
    
    // Default to first item of new mode if current isn't in pool
    updateSidebarList();
    if (visibleItems.length > 0 && !visibleItems.some(x => x.id === currentItem.id)) {
      selectItem(visibleItems[0].id);
    } else {
      renderMainView();
    }
  }

  /* ==========================================================================
     View Rendering Engines
     ========================================================================== */
  function renderMainView() {
    const s = currentItem;
    const stage = $('slide-stage');
    const d = s.domain ?? 0;
    
    // Set dynamic domain accent
    document.documentElement.style.setProperty('--accent-active', domainColors[d] || 'var(--d1-accent)');
    $('breadcrumb-domain').textContent = domainNames[d] || `Domain ${d}`;
    $('breadcrumb-domain').style.borderColor = domainColors[d];
    $('breadcrumb-domain').style.color = domainColors[d];

    const idx = visibleItems.findIndex(x => x.id === s.id);
    $('breadcrumb-title').textContent = idx >= 0 ? `Item ${idx + 1} of ${visibleItems.length}` : s.id;
    $('slide-number-display').textContent = idx >= 0 ? `${idx + 1} / ${visibleItems.length}` : s.id;
    $('btn-prev-slide').disabled = idx <= 0;
    $('btn-next-slide').disabled = idx < 0 || idx >= visibleItems.length - 1;

    // Action status buttons
    $('btn-mark-learned').classList.toggle('active-learned', !!state.learned[s.id]);
    $('btn-mark-learned').textContent = state.learned[s.id] ? '✓ Learned' : 'Mark Learned';
    $('btn-mark-review').classList.toggle('active-review', !!state.weak[s.id]);
    $('btn-mark-review').textContent = state.weak[s.id] ? '★ In Review' : 'Review Later';

    // Toolbar layer pills visibility (only active for slides & treatise)
    const showLayers = state.mode === 'slides' || state.mode === 'treatise';
    document.querySelectorAll('.layer-pill').forEach(pill => {
      pill.style.display = showLayers ? 'inline-block' : 'none';
      pill.classList.toggle('active', pill.dataset.layer === state.layer);
    });

    if (state.mode === 'slides') {
      stage.innerHTML = renderSlideDeck(s);
      attachSlideEvents(s);
    } else if (state.mode === 'treatise') {
      stage.innerHTML = renderVisualTreatise();
      attachTreatiseEvents();
    } else if (state.mode === 'mock' || state.mode === 'quizzes') {
      stage.innerHTML = renderQuizStage(s);
      attachQuizEvents(s);
    } else if (state.mode === 'recalls') {
      stage.innerHTML = renderRecallStage(s);
      attachRecallEvents(s);
    } else if (state.mode === 'skills') {
      stage.innerHTML = renderSkillStage(s);
    } else if (state.mode === 'references') {
      stage.innerHTML = renderReferenceStage(s);
    }
  }

  /* --------------------------------------------------------------------------
     1. Slide Deck Presentation Renderer
     -------------------------------------------------------------------------- */
  function renderSlideDeck(s) {
    const rd = s.russianDoll || {};
    const layerContent = {
      intuition: { badge: 'Layer 1: First Principle', label: 'Intuitive Mental Model', text: rd.intuition || s.lead },
      architecture: { badge: 'Layer 2: Architecture', label: 'System Data Flow & Mechanics', text: rd.architecture || 'Examine the architecture diagram on the right.' },
      api: { badge: 'Layer 3: Exact APIs & Code', label: 'boto3 Calls, Payloads & Config', text: rd.api || 'Review AWS SDK signatures and parameters.' },
      traps: { badge: 'Layer 4: Amazon Traps & Limits', label: 'Exam Distractors & Edge Cases', text: rd.traps || s.trap },
      rule: { badge: 'Layer 5: 2-Day Exam Rule', label: 'Rapid Scenario Decision Rule', text: rd.examRule || 'Pick option matching all constraints.' }
    }[state.layer] || { badge: 'Insight', label: 'Teaching', text: s.lead };

    const hasImage = !!s.image;
    const linkedCount = (s.linkedQuizzes || []).length;

    return `
      <article class="slide-deck-frame" id="slide">
        <header class="slide-header">
          <div class="slide-title-line">
            <h1 class="slide-main-title">${esc(s.title)}</h1>
            ${s.skills?.length ? `<span class="slide-skills-pill">Skill ${esc(s.skills.join(', '))}</span>` : ''}
          </div>
          <p class="slide-lead-text">${esc(s.lead)}</p>
        </header>

        <div class="slide-grid-split ${hasImage ? '' : 'no-image'}">
          <!-- Left Content Column -->
          <div class="slide-core-content">
            <!-- Teaching Points -->
            <div class="teaching-points-box">
              <div class="teaching-points-title">Core Principles & Requirements</div>
              <ul class="points-list">
                ${(s.points || []).map(p => `<li>${esc(p)}</li>`).join('')}
              </ul>
            </div>

            <!-- Active Russian Doll Layer -->
            <div class="russian-doll-card">
              <div class="rd-layer-header">
                <span class="rd-layer-badge">${esc(layerContent.badge)}</span>
                <span class="rd-layer-label">${esc(layerContent.label)}</span>
              </div>
              <div class="rd-layer-body">${esc(layerContent.text)}</div>
            </div>

            <!-- Amazon Exam Trap -->
            <div class="trap-callout">
              <div class="trap-icon">⚠️</div>
              <div class="trap-text">
                <strong>Amazon Exam Trap & Distractor Pattern:</strong>
                ${esc(s.trap)}
              </div>
            </div>

            <!-- Active Self-Check Recall -->
            <details class="recall-accordion">
              <summary class="recall-summary">${esc(s.question)}</summary>
              <div class="recall-content">
                <p><strong>AWS Answer & Rationale:</strong> ${esc(s.answer)}</p>
              </div>
            </details>

            <!-- Test Button -->
            <div class="slide-action-bar">
              ${linkedCount ? `
                <button id="btn-open-linked-quiz" class="btn-open-quiz">
                  <span>⚡ Test This Concept in Question Bank (${linkedCount} questions)</span>
                </button>
              ` : ''}
            </div>
          </div>

          <!-- Right Diagram Column -->
          ${hasImage ? `
            <div class="slide-diagram-card">
              <div class="diagram-header">
                <span class="diagram-badge">Architecture & System Flow</span>
                <button id="btn-zoom-main" class="btn-zoom-diagram" title="Enlarge Diagram (Z)">🔍 Lightbox Zoom</button>
              </div>
              <div class="diagram-figure-wrapper" id="diagram-click-target">
                <img src="${esc(s.image)}" alt="${esc(s.title)} Architecture Diagram">
              </div>
            </div>
          ` : ''}
        </div>
      </article>
    `;
  }

  function attachSlideEvents(s) {
    const zoomBtn = $('btn-zoom-main');
    const target = $('diagram-click-target');
    if (zoomBtn && s.image) zoomBtn.onclick = () => openLightbox(s.image, s.title);
    if (target && s.image) target.onclick = () => openLightbox(s.image, s.title);

    const quizBtn = $('btn-open-linked-quiz');
    if (quizBtn && s.linkedQuizzes?.length) {
      quizBtn.onclick = () => openQuizDrawer(s.linkedQuizzes[0]);
    }
  }

  /* --------------------------------------------------------------------------
     2. Visual Treatise (Scrollable Long-Form Masterclass)
     -------------------------------------------------------------------------- */
  function renderVisualTreatise() {
    let currentDomain = -1;
    let html = `<div class="treatise-container">`;

    C.core.forEach(s => {
      const d = s.domain ?? 0;
      if (d !== currentDomain) {
        currentDomain = d;
        html += `
          <div class="treatise-domain-divider" id="treatise-domain-${d}">
            <h2 class="treatise-domain-title" style="color: ${domainColors[d]}">${domainNames[d]}</h2>
            <p class="treatise-domain-lead">Comprehensive technical deep dive covering official AWS AIP-C01 blueprint requirements.</p>
          </div>
        `;
      }

      const rd = s.russianDoll || {};
      html += `
        <article class="treatise-section-card" id="treatise-${s.id}">
          <header class="treatise-section-header">
            <span class="domain-tag" style="color: ${domainColors[d]}; border-color: ${domainColors[d]}">${domainNames[d]} · ${s.id}</span>
            <h3 class="treatise-section-title">${esc(s.title)}</h3>
            <p class="treatise-section-lead">${esc(s.lead)}</p>
          </header>

          ${s.image ? `
            <div class="treatise-diagram-box" onclick="window.openLightbox('${esc(s.image)}', '${esc(s.title)}')">
              <img src="${esc(s.image)}" alt="${esc(s.title)}">
              <div class="treatise-diagram-caption">Figure: ${esc(s.title)} (Click to enlarge)</div>
            </div>
          ` : ''}

          <div class="teaching-points-box">
            <div class="teaching-points-title">Architectural Principles</div>
            <ul class="points-list">
              ${(s.points || []).map(p => `<li>${esc(p)}</li>`).join('')}
            </ul>
          </div>

          <div class="treatise-rd-layers">
            <div class="treatise-layer-row"><div class="treatise-layer-name">Layer 1: First Principle Intuition</div><div class="treatise-layer-text">${esc(rd.intuition || s.lead)}</div></div>
            <div class="treatise-layer-row"><div class="treatise-layer-name">Layer 2: AWS Architecture Flow</div><div class="treatise-layer-text">${esc(rd.architecture || 'See system diagram.')}</div></div>
            <div class="treatise-layer-row"><div class="treatise-layer-name">Layer 3: Exact APIs & Code</div><div class="treatise-layer-text"><code>${esc(rd.api || 'boto3 bedrock-runtime invocation')}</code></div></div>
            <div class="treatise-layer-row"><div class="treatise-layer-name">Layer 4: Amazon Traps & Limits</div><div class="treatise-layer-text">${esc(rd.traps || s.trap)}</div></div>
            <div class="treatise-layer-row"><div class="treatise-layer-name">Layer 5: 2-Day Exam Decision Rule</div><div class="treatise-layer-text"><strong>${esc(rd.examRule || 'Match all constraints.')}</strong></div></div>
          </div>

          <div class="trap-callout">
            <div class="trap-icon">⚠️</div>
            <div class="trap-text"><strong>Exam Alert:</strong> ${esc(s.trap)}</div>
          </div>
        </article>
      `;
    });

    html += `</div>`;
    return html;
  }

  function attachTreatiseEvents() {
    // Treatise internal event handling
  }

  /* --------------------------------------------------------------------------
     3. Practice Quiz & Mock Exam Stage Renderer
     -------------------------------------------------------------------------- */
  function renderQuizStage(q) {
    const isMock = state.mode === 'mock';
    const storeTarget = isMock ? state.mockAnswers : state.answers;
    const saved = storeTarget[q.id] || { selected: [], checked: false };
    const selected = saved.selected || [];
    const checked = isMock ? state.mockDone : !!saved.checked;
    const correctCount = q.options.filter(o => o.correct).length;

    return `
      <div class="quiz-stage-container">
        <div class="quiz-card">
          <div class="quiz-meta-line">
            <span class="quiz-domain-tag">${esc(domainNames[q.domain] || `Domain ${q.domain}`)}</span>
            ${q.topic ? `<span class="quiz-topic-tag" style="background:rgba(59,130,246,0.12);color:var(--accent-active);padding:2px 8px;border-radius:4px;font-size:0.8rem;font-weight:600;">📌 ${esc(q.topic)}</span>` : ''}
            ${q.difficulty ? `<span class="quiz-diff-tag" style="background:rgba(16,185,129,0.12);color:#10b981;padding:2px 8px;border-radius:4px;font-size:0.8rem;font-weight:600;">${esc(q.difficulty)}</span>` : ''}
            <span class="quiz-instruction-text">${correctCount > 1 ? `Select ${correctCount} responses.` : 'Select one response.'}</span>
          </div>

          ${q.questionNumber ? `<h3 class="quiz-number-title" style="font-size:1.15rem;font-weight:800;color:var(--text-primary);margin:10px 0 6px 0;">Question ${q.questionNumber}${q.topic ? ` · ${esc(q.topic)}` : ''}</h3>` : ''}
          <div class="quiz-stem-text" style="text-align:justify;line-height:1.55;margin-bottom:16px;">${esc(q.cleanStem || q.title)}</div>

          <fieldset class="options-fieldset">
            ${q.options.map((o, i) => {
              const isPicked = selected.includes(i);
              let optionClass = '';
              if (checked) {
                if (o.correct) optionClass = 'correct';
                else if (isPicked) optionClass = 'wrong';
              }
              return `
                <label class="quiz-option-label ${optionClass}">
                  <input type="${correctCount > 1 ? 'checkbox' : 'radio'}" name="quiz-ans" value="${i}" ${isPicked ? 'checked' : ''} ${checked ? 'disabled' : ''}>
                  <span><strong>${String.fromCharCode(65 + i)}.</strong> ${esc(o.text)}</span>
                </label>
              `;
            }).join('')}
          </fieldset>

          <div class="quiz-actions-row">
            ${!isMock && !checked ? `<button id="btn-check-quiz" class="btn-primary">Check Answer</button>` : ''}
            ${!isMock && checked ? `<button id="btn-retry-quiz" class="btn-secondary">Try Again</button>` : ''}
            ${isMock && !state.mockDeadline && !state.mockDone ? `<button id="btn-start-mock" class="btn-primary">Start 180-Minute Mock Timer</button>` : ''}
            ${isMock && !state.mockDone ? `<button id="btn-finish-mock" class="btn-secondary">Finish & Score Exam</button>` : ''}
            ${isMock && state.mockDone ? `<button id="btn-reset-mock" class="btn-secondary">Restart Mock</button>` : ''}
          </div>

          ${checked ? renderFeedbackBox(q, selected) : ''}
        </div>
      </div>
    `;
  }

  function renderFeedbackBox(q, selected) {
    const correctIdxs = q.options.map((o, i) => o.correct ? i : -1).filter(i => i >= 0);
    const pass = correctIdxs.length === selected.length && correctIdxs.every(i => selected.includes(i));

    return `
      <div class="quiz-feedback-box">
        <h3 class="feedback-result-title ${pass ? 'pass' : 'fail'}">
          ${pass ? '✓ Correct! Direct hit on AWS exam blueprint.' : '✗ Incorrect. Review the official rationale below.'}
        </h3>
        <p><strong>Correct Answer:</strong> ${correctIdxs.map(i => String.fromCharCode(65 + i)).join(', ')}</p>
        <div class="feedback-rationale-text">
          <strong>Official AWS Rationale:</strong><br>${esc(q.answer)}
        </div>
      </div>
    `;
  }

  function attachQuizEvents(q) {
    const isMock = state.mode === 'mock';
    const storeTarget = isMock ? state.mockAnswers : state.answers;

    document.querySelectorAll('input[name="quiz-ans"]').forEach(input => {
      input.onchange = () => {
        const picked = [...document.querySelectorAll('input[name="quiz-ans"]:checked')].map(el => +el.value);
        storeTarget[q.id] = { selected: picked, checked: false };
        store.save();
      };
    });

    const checkBtn = $('btn-check-quiz');
    if (checkBtn) {
      checkBtn.onclick = () => {
        const picked = [...document.querySelectorAll('input[name="quiz-ans"]:checked')].map(el => +el.value);
        if (!picked.length) return;
        storeTarget[q.id] = { selected: picked, checked: true };
        const key = q.options.map((o, i) => o.correct ? i : -1).filter(i => i >= 0);
        if (picked.length !== key.length || !key.every(i => picked.includes(i))) {
          state.weak[q.id] = true;
        } else {
          state.learned[q.id] = true;
        }
        store.save();
        renderMainView();
        updateSidebarList();
      };
    }

    const retryBtn = $('btn-retry-quiz');
    if (retryBtn) {
      retryBtn.onclick = () => {
        delete storeTarget[q.id];
        store.save();
        renderMainView();
      };
    }

    const startMockBtn = $('btn-start-mock');
    if (startMockBtn) {
      startMockBtn.onclick = () => {
        state.mockDeadline = Date.now() + 180 * 60 * 1000;
        store.save();
        updateTimer();
        renderMainView();
      };
    }

    const finishMockBtn = $('btn-finish-mock');
    if (finishMockBtn) {
      finishMockBtn.onclick = finishMockExam;
    }

    const resetMockBtn = $('btn-reset-mock');
    if (resetMockBtn) {
      resetMockBtn.onclick = () => {
        state.mockAnswers = {};
        state.mockDone = false;
        state.mockDeadline = 0;
        store.save();
        selectItem(C.mock[0]);
      };
    }
  }

  function finishMockExam() {
    state.mockDone = true;
    state.mockDeadline = 0;
    store.save();
    renderMainView();
    updateSidebarList();
  }

  /* --------------------------------------------------------------------------
     4. Recall Cards, Skills, and References
     -------------------------------------------------------------------------- */
  function renderRecallStage(r) {
    return `
      <div class="quiz-stage-container">
        <div class="quiz-card">
          <span class="quiz-domain-tag">${domainNames[r.domain] || `Domain ${r.domain}`}</span>
          <h2 class="quiz-stem-text">${esc(r.question)}</h2>
          <details class="recall-accordion" style="margin-top: 16px;">
            <summary class="recall-summary">Reveal Master Answer</summary>
            <div class="recall-content">
              <p>${esc(r.answer)}</p>
            </div>
          </details>
        </div>
      </div>
    `;
  }
  function attachRecallEvents(r) {}

  function renderSkillStage(s) {
    return `
      <div class="quiz-stage-container">
        <div class="quiz-card">
          <span class="quiz-domain-tag">Domain ${s.domain} Skill</span>
          <h2 class="quiz-stem-text">Skill ${esc(s.id)}: ${esc(s.description)}</h2>
          <div class="teaching-points-box" style="margin-top: 20px;">
            <div class="teaching-points-title">Core Lessons Teaching This Skill:</div>
            <ul class="points-list">
              ${(s.slides || []).map(id => `
                <li><button class="nav-item-btn" style="display:inline;padding:2px 8px;" onclick="window.COURSE_APP.selectItem('${esc(id)}')">${esc(coreMap.get(id)?.title || id)}</button></li>
              `).join('')}
            </ul>
          </div>
        </div>
      </div>
    `;
  }

  function renderReferenceStage(r) {
    return `
      <div class="quiz-stage-container" style="max-width: 1000px;">
        <div class="quiz-card">
          <span class="quiz-domain-tag">${r.volume} · Section</span>
          <h2 class="quiz-stem-text">${esc(r.title)}</h2>
          <div class="treatise-layer-text" style="margin-top: 20px; font-size: 1.05rem; line-height: 1.6;">
            ${r.html}
          </div>
        </div>
      </div>
    `;
  }

  /* ==========================================================================
     Lightbox & Modal Management
     ========================================================================== */
  function openLightbox(imgSrc, title) {
    const lb = $('diagram-lightbox');
    $('lightbox-image').src = imgSrc;
    $('lightbox-title').textContent = title || 'Architecture Diagram';
    lightboxZoom = 100;
    $('lightbox-image').style.transform = `scale(1)`;
    $('lightbox-zoom-level').textContent = '100%';
    lb.hidden = false;
  }

  function closeLightbox() {
    $('diagram-lightbox').hidden = true;
    $('lightbox-image').src = '';
  }

  function openQuizDrawer(qid) {
    const q = quizMap.get(qid);
    if (!q) return;
    const drawer = $('quiz-drawer');
    $('quiz-drawer-title').textContent = q.displayTitle || q.title;
    $('quiz-drawer-body').innerHTML = renderQuizStage(q);
    attachQuizEvents(q);
    drawer.hidden = false;
  }

  function closeQuizDrawer() {
    $('quiz-drawer').hidden = true;
  }

  /* ==========================================================================
     Event Handlers & Keyboard Shortcuts
     ========================================================================== */
  // Top nav mode clicks
  document.querySelectorAll('.mode-tab').forEach(tab => {
    tab.onclick = () => switchMode(tab.dataset.mode);
  });

  // Layer pills click
  document.querySelectorAll('.layer-pill').forEach(pill => {
    pill.onclick = () => {
      state.layer = pill.dataset.layer;
      store.save();
      renderMainView();
    };
  });

  // Prev / Next slide
  $('btn-prev-slide').onclick = () => {
    const idx = visibleItems.findIndex(x => x.id === currentItem.id);
    if (idx > 0) selectItem(visibleItems[idx - 1].id);
  };
  $('btn-next-slide').onclick = () => {
    const idx = visibleItems.findIndex(x => x.id === currentItem.id);
    if (idx >= 0 && idx + 1 < visibleItems.length) selectItem(visibleItems[idx + 1].id);
  };

  // Actions
  $('btn-mark-learned').onclick = () => {
    state.learned[currentItem.id] = !state.learned[currentItem.id];
    if (state.learned[currentItem.id]) delete state.weak[currentItem.id];
    store.save();
    renderMainView();
    updateSidebarList();
  };

  $('btn-mark-review').onclick = () => {
    state.weak[currentItem.id] = !state.weak[currentItem.id];
    store.save();
    renderMainView();
    updateSidebarList();
  };

  // Search & Filter
  $('search-input').oninput = () => updateSidebarList();
  $('domain-select').onchange = () => updateSidebarList();

  // Theme toggle
  $('btn-theme').onclick = () => {
    state.theme = state.theme === 'dark' ? 'light' : 'dark';
    document.body.className = `theme-${state.theme} mode-${state.mode}`;
    store.save();
  };

  // Fullscreen
  $('btn-fullscreen').onclick = () => {
    if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {});
    else document.exitFullscreen().catch(() => {});
  };

  // Mobile drawer toggle
  $('btn-sidebar-toggle').onclick = () => {
    $('sidebar').classList.toggle('open');
  };

  // Lightbox controls
  $('lightbox-close').onclick = closeLightbox;
  $('lightbox-zoom-in').onclick = () => {
    lightboxZoom = Math.min(300, lightboxZoom + 25);
    $('lightbox-image').style.transform = `scale(${lightboxZoom / 100})`;
    $('lightbox-zoom-level').textContent = `${lightboxZoom}%`;
  };
  $('lightbox-zoom-out').onclick = () => {
    lightboxZoom = Math.max(50, lightboxZoom - 25);
    $('lightbox-image').style.transform = `scale(${lightboxZoom / 100})`;
    $('lightbox-zoom-level').textContent = `${lightboxZoom}%`;
  };
  $('lightbox-zoom-reset').onclick = () => {
    lightboxZoom = 100;
    $('lightbox-image').style.transform = `scale(1)`;
    $('lightbox-zoom-level').textContent = `100%`;
  };

  $('quiz-drawer-close').onclick = closeQuizDrawer;

  // Keyboard navigation
  document.addEventListener('keydown', e => {
    if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;

    if (e.key === 'ArrowRight' || e.key === ' ') {
      $('btn-next-slide').click();
      e.preventDefault();
    } else if (e.key === 'ArrowLeft') {
      $('btn-prev-slide').click();
      e.preventDefault();
    } else if (e.key === 'f' || e.key === 'F') {
      $('btn-fullscreen').click();
    } else if (e.key === 'q' || e.key === 'Q') {
      if (currentItem.linkedQuizzes?.length) openQuizDrawer(currentItem.linkedQuizzes[0]);
    } else if (e.key === 'l' || e.key === 'L') {
      $('btn-mark-learned').click();
    } else if (e.key === 'r' || e.key === 'R') {
      $('btn-mark-review').click();
    } else if (e.key === 'm' || e.key === 'M') {
      $('btn-sidebar-toggle').click();
    } else if (e.key === '1') {
      $('btn-layer-intuition').click();
    } else if (e.key === '2') {
      $('btn-layer-architecture').click();
    } else if (e.key === '3') {
      $('btn-layer-api').click();
    } else if (e.key === '4') {
      $('btn-layer-traps').click();
    } else if (e.key === '5') {
      $('btn-layer-rule').click();
    } else if (e.key === 'Escape') {
      closeLightbox();
      closeQuizDrawer();
      $('sidebar').classList.remove('open');
    }
  });

  function updateTimer() {
    if (state.mode !== 'mock') {
      $('timer-display').textContent = '';
      return;
    }
    if (state.mockDone) {
      $('timer-display').textContent = 'Reviewing Results';
      return;
    }
    if (!state.mockDeadline) {
      $('timer-display').textContent = '180:00 Ready';
      return;
    }
    const left = Math.max(0, Math.ceil((state.mockDeadline - Date.now()) / 1000));
    const h = Math.floor(left / 3600);
    const m = Math.floor((left % 3600) / 60);
    const s = left % 60;
    $('timer-display').textContent = `⏱️ ${h}:${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
    if (left === 0) finishMockExam();
  }

  // Mock countdown timer loop
  setInterval(updateTimer, 1000);

  function go(id, targetMode) {
    if (targetMode && targetMode !== state.mode) {
      switchMode(targetMode);
    }
    if (id) {
      selectItem(id);
    }
  }

  // Expose global app object
  window.COURSE_APP = {
    go,
    selectItem,
    switchMode,
    openLightbox,
    getState: () => structuredClone(state)
  };
  window.openLightbox = openLightbox;

  // Initialize
  updateSidebarList();
  renderMainView();
})();
