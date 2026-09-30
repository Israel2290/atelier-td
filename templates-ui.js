(() => {
  const templates = window.ATELIER_TEMPLATES || [];
  const layout = document.getElementById('appLayout');
  const examView = document.getElementById('examView');
  const templatesView = document.getElementById('templatesView');
  const grid = document.getElementById('templateGrid');
  const searchInput = document.getElementById('templateSearch');
  const languageFilter = document.getElementById('templateLanguage');
  const categoryFilter = document.getElementById('templateCategory');
  const typeFilter = document.getElementById('templateType');
  const stateFilter = document.getElementById('templateState');
  const toast = document.getElementById('templateToast');
  let toastTimer;

  const priorityOrder = { essential: 0, frequent: 1, complementary: 2 };
  const priorityLabel = {
    essential: ['🔥 Essentiel', 'priority-essential'],
    frequent: ['Fréquent', 'priority-frequent'],
    complementary: ['Complémentaire', 'priority-complementary']
  };
  const normalize = value => String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase('fr');
  const savedTemplates = () => progress.__templates || {};
  const questionById = new Map(questions.map(question => [question.id, question]));

  function populateFilters() {
    const categories = [...new Set(templates.map(template => template.category))].sort((a, b) => a.localeCompare(b, 'fr'));
    const types = [...new Set(templates.map(template => template.type))].sort((a, b) => a.localeCompare(b, 'fr'));
    categoryFilter.innerHTML = '<option value="">Toutes les catégories</option>' + categories.map(value => `<option>${escapeHTML(value)}</option>`).join('');
    typeFilter.innerHTML = '<option value="">Tous les types</option>' + types.map(value => `<option>${escapeHTML(value)}</option>`).join('');
  }

  function codeSection(template, field, heading, value) {
    const id = `${template.id}-${field}`;
    return `<section class="template-section">
      <h3>${heading}</h3>
      <div class="template-code-wrap">
        <textarea class="template-code" id="code-${escapeHTML(id)}" data-template-code="${escapeHTML(id)}" aria-label="${heading} : ${escapeHTML(template.title)}" spellcheck="false">${escapeHTML(value)}</textarea>
        <div class="template-code-actions">
          <button type="button" data-copy-code="${escapeHTML(id)}">Copier</button>
          <button type="button" data-reset-code="${escapeHTML(id)}">Réinitialiser</button>
        </div>
      </div>
    </section>`;
  }

  function copyWithSelection(value) {
    const temporary = document.createElement('textarea');
    temporary.value = value;
    temporary.setAttribute('readonly', '');
    temporary.style.position = 'fixed';
    temporary.style.opacity = '0';
    document.body.appendChild(temporary);
    temporary.select();
    const copied = document.execCommand('copy');
    temporary.remove();
    if (!copied) throw new Error('Copie indisponible');
  }

  function renderTemplate(template) {
    const saved = savedTemplates()[template.id] || {};
    const [priorityText, priorityClass] = priorityLabel[template.priority] || priorityLabel.complementary;
    const relatedQuestions = (template.examIds || []).map(id => questionById.get(id)).filter(Boolean);
    const relatedLinks = relatedQuestions.length
      ? `<div class="template-links"><span class="toolbar-label">Templates utiles pour :</span>${relatedQuestions.slice(0, 3).map(question => `<button type="button" data-related-question="${escapeHTML(question.id)}" title="${escapeHTML(question.prompt)}">${escapeHTML(question.section)}</button>`).join('')}${relatedQuestions.length > 3 ? `<span class="source-caption">+ ${relatedQuestions.length - 3} exercices</span>` : ''}</div>`
      : '';
    const points = values => `<ul class="template-points">${values.map(value => `<li>${escapeHTML(value)}</li>`).join('')}</ul>`;
    return `<article class="template-card" data-template-card="${escapeHTML(template.id)}">
      <div class="template-card-head">
        <div><h2>${escapeHTML(template.title)}</h2><div class="template-badges"><span class="template-badge">${escapeHTML(template.language)}</span><span class="template-badge">${escapeHTML(template.category)}</span><span class="template-badge">${escapeHTML(template.type)}</span><span class="template-badge ${priorityClass}">${priorityText}</span></div></div>
      </div>
      <p>${escapeHTML(template.description)}</p>
      ${codeSection(template, 'syntax', 'Syntaxe minimale', template.syntax)}
      ${codeSection(template, 'example', 'Exemple complet', template.example)}
      <section class="template-section"><h3>À retenir</h3>${points(template.remember)}</section>
      <section class="template-section"><h3>Pièges fréquents</h3>${points(template.pitfalls)}</section>
      <section class="template-section"><h3>Dans une épreuve</h3><p>${escapeHTML(template.exercise)}</p></section>
      ${relatedLinks}
      <div class="template-status" aria-label="Mémorisation">
        <button type="button" data-template-state="review" data-template-id="${escapeHTML(template.id)}" aria-pressed="${saved.state === 'review'}">À revoir</button>
        <button type="button" data-template-state="known" data-template-id="${escapeHTML(template.id)}" aria-pressed="${saved.state === 'known'}">Maîtrisé</button>
        <button type="button" data-template-state="favorite" data-template-id="${escapeHTML(template.id)}" aria-pressed="${Boolean(saved.favorite)}">Favori</button>
      </div>
    </article>`;
  }

  function searchableText(template) {
    const linkedQuestions = (template.examIds || []).map(id => questionById.get(id)?.prompt || '').join(' ');
    return normalize([
      template.title, template.language, template.category, template.type, template.description,
      template.syntax, template.example, template.exercise, ...(template.tags || []),
      ...(template.remember || []), ...(template.pitfalls || []), linkedQuestions
    ].join(' '));
  }

  function searchRelevance(template, terms) {
    const title = normalize(template.title);
    const tags = normalize((template.tags || []).join(' '));
    return terms.reduce((score, term) => score
      + (title === term ? 30 : title.startsWith(term) ? 20 : title.includes(term) ? 12 : 0)
      + (tags.includes(term) ? 6 : 0), 0);
  }

  function renderTemplates() {
    const terms = normalize(searchInput.value).split(/\s+/).filter(Boolean);
    const selectedLanguage = languageFilter.value;
    const selectedCategory = categoryFilter.value;
    const selectedType = typeFilter.value;
    const selectedState = stateFilter.value;
    const saved = savedTemplates();
    const shown = templates.filter(template => {
      const state = saved[template.id] || {};
      const text = searchableText(template);
      return (!selectedLanguage || template.language === selectedLanguage)
        && (!selectedCategory || template.category === selectedCategory)
        && (!selectedType || template.type === selectedType)
        && (!selectedState || (selectedState === 'favorite' ? state.favorite : state.state === selectedState))
        && terms.every(term => text.includes(term));
    }).sort((a, b) => searchRelevance(b, terms) - searchRelevance(a, terms) || (priorityOrder[a.priority] ?? 3) - (priorityOrder[b.priority] ?? 3) || a.title.localeCompare(b.title, 'fr'));

    document.getElementById('templateCount').textContent = templates.length;
    document.getElementById('templateResultCount').textContent = `${shown.length} modèle${shown.length === 1 ? '' : 's'} affiché${shown.length === 1 ? '' : 's'}`;
    if (!shown.length) {
      const isCpp = selectedLanguage === 'C++';
      grid.innerHTML = `<div class="template-empty">${isCpp ? 'Aucun sujet fourni ne demande du C++ ; aucun modèle C++ n’a donc été ajouté.' : 'Aucun template ne correspond à cette recherche. Modifie les mots ou les filtres.'}</div>`;
      return;
    }
    const groups = new Map();
    shown.forEach(template => {
      if (!groups.has(template.category)) groups.set(template.category, []);
      groups.get(template.category).push(template);
    });
    grid.innerHTML = [...groups.entries()].map(([category, categoryTemplates]) => `<section class="template-category-group" aria-label="Catégorie ${escapeHTML(category)}"><div class="template-category-heading"><h2>${escapeHTML(category)}</h2><span>${categoryTemplates.length} fiche${categoryTemplates.length === 1 ? '' : 's'}</span></div><div class="template-category-cards">${categoryTemplates.map(renderTemplate).join('')}</div></section>`).join('');
    grid.querySelectorAll('[data-template-code]').forEach(code => { code.dataset.original = code.value; });
    grid.querySelectorAll('[data-template-state]').forEach(button => button.addEventListener('click', () => {
      const id = button.dataset.templateId;
      const existing = savedTemplates()[id] || {};
      const next = { ...existing };
      if (button.dataset.templateState === 'favorite') next.favorite = !existing.favorite;
      else next.state = button.dataset.templateState;
      progress.__templates = { ...savedTemplates(), [id]: next };
      saveProgress();
      renderTemplates();
    }));
    grid.querySelectorAll('[data-copy-code]').forEach(button => button.addEventListener('click', async () => {
      const code = grid.querySelector(`[data-template-code="${CSS.escape(button.dataset.copyCode)}"]`);
      if (!code) return;
      try {
        if (navigator.clipboard?.writeText) {
          try {
            await navigator.clipboard.writeText(code.value);
          } catch {
            copyWithSelection(code.value);
          }
        } else {
          copyWithSelection(code.value);
        }
        button.textContent = 'Copié !';
        showToast('Code copié');
        window.setTimeout(() => { if (button.isConnected) button.textContent = 'Copier'; }, 1500);
      } catch {
        showToast('Copie indisponible dans ce navigateur');
      }
    }));
    grid.querySelectorAll('[data-reset-code]').forEach(button => button.addEventListener('click', () => {
      const code = grid.querySelector(`[data-template-code="${CSS.escape(button.dataset.resetCode)}"]`);
      if (code) code.value = code.dataset.original;
    }));
    grid.querySelectorAll('[data-related-question]').forEach(button => button.addEventListener('click', () => openRelatedQuestion(button.dataset.relatedQuestion)));
  }

  function showToast(message) {
    toast.textContent = message;
    toast.hidden = false;
    window.clearTimeout(toastTimer);
    toastTimer = window.setTimeout(() => { toast.hidden = true; }, 1500);
  }

  function setView(view) {
    const isTemplates = view === 'templates';
    layout.dataset.view = view;
    examView.hidden = isTemplates;
    templatesView.hidden = !isTemplates;
    document.querySelectorAll('[data-view-target]').forEach(button => {
      const active = button.dataset.viewTarget === view;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    if (isTemplates) renderTemplates();
    else renderQuestion();
  }

  function openRelatedQuestion(questionId) {
    const question = questionById.get(questionId);
    if (!question) return;
    activeExam = question.source;
    document.getElementById('examFilter').value = question.source;
    activeSubject = 'Toutes';
    activeMode = 'all';
    document.querySelectorAll('.mode-button').forEach(button => button.classList.toggle('selected', button.dataset.mode === 'all'));
    setView('exams');
    updateVisibleQuestions();
    currentIndex = visibleQuestions.findIndex(item => item.id === questionId);
    selectedOption = null;
    renderQuestion();
  }

  function addRelatedTemplates() {
    if (layout.dataset.view !== 'exams') return;
    const question = visibleQuestions[currentIndex];
    if (!question) return;
    const related = templates.filter(template => (template.examIds || []).includes(question.id));
    if (!related.length) return;
    const heading = document.querySelector('#questionCard h2');
    if (!heading) return;
    const links = document.createElement('div');
    links.className = 'template-links exam-template-links';
    links.innerHTML = `<span class="toolbar-label">Templates utiles :</span>${related.map(template => `<button type="button" data-open-template="${escapeHTML(template.id)}">${escapeHTML(template.title)}</button>`).join('')}`;
    heading.insertAdjacentElement('afterend', links);
    links.querySelectorAll('[data-open-template]').forEach(button => button.addEventListener('click', () => {
      const template = templates.find(item => item.id === button.dataset.openTemplate);
      setView('templates');
      searchInput.value = template?.title || '';
      languageFilter.value = template?.language || '';
      categoryFilter.value = '';
      typeFilter.value = '';
      stateFilter.value = '';
      renderTemplates();
    }));
  }

  populateFilters();
  searchInput.addEventListener('input', renderTemplates);
  [languageFilter, categoryFilter, typeFilter, stateFilter].forEach(filter => filter.addEventListener('change', renderTemplates));
  document.querySelectorAll('[data-view-target]').forEach(button => button.addEventListener('click', () => setView(button.dataset.viewTarget)));

  const renderExamQuestion = renderQuestion;
  renderQuestion = function () {
    renderExamQuestion();
    addRelatedTemplates();
  };
  renderQuestion();
})();
