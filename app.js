// Main companion app logic
document.addEventListener("DOMContentLoaded", () => {
  // Elements
  const searchInput = document.getElementById("search-input");
  const chapterSelect = document.getElementById("chapter-select");
  const typePills = document.querySelectorAll(".type-pills .pill");
  const scriptsList = document.getElementById("scripts-list");
  const scriptsCount = document.getElementById("scripts-count");
  
  const viewerPanel = document.getElementById("viewer-panel");
  const emptyState = document.getElementById("empty-state");
  const viewerContent = document.getElementById("viewer-content");
  
  const scriptTitle = document.getElementById("script-title");
  const scriptFilename = document.getElementById("script-filename");
  const scriptChapterBadge = document.getElementById("script-chapter-badge");
  const scriptTypeBadge = document.getElementById("script-type-badge");
  const scriptDescription = document.getElementById("script-description");
  const scriptDescriptionContainer = document.getElementById("script-description-container");
  const codeBlock = document.getElementById("code-block");
  
  const btnCopyCode = document.getElementById("btn-copy-code");
  const btnRunCodelab = document.getElementById("btn-run-codelab");
  const copiedToast = document.getElementById("copied-toast");
  
  const btnShowAbout = document.getElementById("btn-show-about");
  const btnCloseModal = document.getElementById("btn-close-modal");
  const aboutModal = document.getElementById("about-modal");

  // State
  let selectedScript = null;
  let currentTypeFilter = "all";

  // Check if SCRIPTS_DATA is available
  if (typeof SCRIPTS_DATA === "undefined") {
    console.error("SCRIPTS_DATA is not defined. Please run compile_scripts.py first.");
    return;
  }

  // Populate Chapter Select Dropdown
  const chapters = [...new Set(SCRIPTS_DATA.map(s => s.chapter))].sort((a, b) => a - b);
  chapters.forEach(ch => {
    const opt = document.createElement("option");
    opt.value = ch;
    opt.textContent = `Chapter ${ch}`;
    chapterSelect.appendChild(opt);
  });

  // Base64 helper
  function encodeBase64(str) {
    try {
      return btoa(String.fromCharCode(...new TextEncoder().encode(str)));
    } catch (e) {
      console.error("Base64 encoding failed:", e);
      return "";
    }
  }

  // Simple python code syntax highlighter
  function highlightPython(code) {
    // Simple regex highlighter
    let esc = code
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

    // Keywords
    const keywords = /\b(def|class|return|if|else|elif|for|while|try|except|import|from|as|in|is|not|and|or|print|input|with|pass|lambda|True|False|None)\b/g;
    esc = esc.replace(keywords, '<span class="token-keyword">$1</span>');

    // Comments
    esc = esc.replace(/(#.*)/g, '<span class="token-comment">$1</span>');

    // Strings (double and single quote)
    esc = esc.replace(/("(?:\\"|[^"])*")/g, '<span class="token-string">$1</span>');
    esc = esc.replace(/('(?:\\'|[^'])*')/g, '<span class="token-string">$1</span>');

    // Numbers
    esc = esc.replace(/\b(\d+)\b/g, '<span class="token-number">$1</span>');

    return esc;
  }

  // Style Injection for highlighting tokens
  const style = document.createElement('style');
  style.innerHTML = `
    .token-keyword { color: #F43F5E; font-weight: bold; }
    .token-comment { color: #6B7280; font-style: italic; }
    .token-string { color: #10B981; }
    .token-number { color: #F59E0B; }
  `;
  document.head.appendChild(style);

  // Render Scripts List based on filters
  function renderList() {
    const query = searchInput.value.toLowerCase().trim();
    const selectedChapter = chapterSelect.value;
    
    const filtered = SCRIPTS_DATA.filter(script => {
      // Chapter filter
      if (selectedChapter !== "all" && script.chapter.toString() !== selectedChapter) {
        return false;
      }
      
      // Type filter
      if (currentTypeFilter !== "all" && script.type !== currentTypeFilter) {
        return false;
      }
      
      // Search query filter
      if (query) {
        const inName = script.name.toLowerCase().includes(query);
        const inFilename = script.filename.toLowerCase().includes(query);
        const inCode = script.code.toLowerCase().includes(query);
        const inDesc = script.description.toLowerCase().includes(query);
        return inName || inFilename || inCode || inDesc;
      }
      
      return true;
    });

    // Update count
    scriptsCount.textContent = `${filtered.length} Script${filtered.length === 1 ? '' : 's'}`;

    // Clear list
    scriptsList.innerHTML = "";

    if (filtered.length === 0) {
      scriptsList.innerHTML = `<li class="empty-list-message" style="color: var(--text-muted); font-size: 0.9rem; padding: 1rem; text-align: center;">No scripts found</li>`;
      return;
    }

    // Populate list
    filtered.forEach(script => {
      const li = document.createElement("li");
      li.className = `script-item ${selectedScript === script ? 'selected' : ''}`;
      
      let badgeClass = "badge-other";
      if (script.type === "example") badgeClass = "badge-example";
      else if (script.type === "challenge") badgeClass = "badge-challenge";
      else if (script.type === "answer") badgeClass = "badge-answer";

      li.innerHTML = `
        <div class="script-item-meta">
          <span class="script-item-chapter">Chapter ${script.chapter}</span>
          <span class="badge ${badgeClass}" style="font-size: 0.65rem; padding: 0.1rem 0.4rem;">${script.type}</span>
        </div>
        <div class="script-item-name">${script.name}</div>
        <div class="script-item-desc">${script.description || script.filename}</div>
      `;

      li.addEventListener("click", () => {
        selectScript(script);
        // Highlight active item
        document.querySelectorAll(".script-item").forEach(item => item.classList.remove("selected"));
        li.classList.add("selected");
      });

      scriptsList.appendChild(li);
    });
  }

  // Select and view script details
  function selectScript(script) {
    selectedScript = script;
    
    // Switch states
    emptyState.classList.add("hidden");
    viewerContent.classList.remove("hidden");
    
    // Update headers and content
    scriptTitle.textContent = script.name;
    scriptFilename.textContent = script.filename;
    scriptChapterBadge.textContent = `Chapter ${script.chapter}`;
    scriptTypeBadge.textContent = script.type;
    
    // Set badge classes
    scriptTypeBadge.className = "badge";
    if (script.type === "example") scriptTypeBadge.classList.add("badge-example");
    else if (script.type === "challenge") scriptTypeBadge.classList.add("badge-challenge");
    else if (script.type === "answer") scriptTypeBadge.classList.add("badge-answer");
    else scriptTypeBadge.classList.add("badge-other");

    // Handle description
    if (script.description) {
      scriptDescriptionContainer.classList.remove("hidden");
      scriptDescription.textContent = script.description;
    } else {
      scriptDescriptionContainer.classList.add("hidden");
    }

    // Display code
    codeBlock.innerHTML = highlightPython(script.code);

    // Prepare link to pythoncopy
    const base64Code = encodeBase64(script.code);
    btnRunCodelab.href = `https://jamesabela.github.io/jsfun/pythoncopy.html?code=${base64Code}&theme=dark`;
  }

  // Copy code to clipboard
  btnCopyCode.addEventListener("click", () => {
    if (!selectedScript) return;
    navigator.clipboard.writeText(selectedScript.code).then(() => {
      copiedToast.classList.add("show");
      setTimeout(() => {
        copiedToast.classList.remove("show");
      }, 2000);
    });
  });

  // Event Listeners for Filters
  searchInput.addEventListener("input", renderList);
  chapterSelect.addEventListener("change", renderList);
  
  typePills.forEach(pill => {
    pill.addEventListener("click", () => {
      typePills.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");
      currentTypeFilter = pill.getAttribute("data-type");
      renderList();
    });
  });

  // Modal actions
  btnShowAbout.addEventListener("click", (e) => {
    e.preventDefault();
    aboutModal.classList.remove("hidden");
  });
  btnCloseModal.addEventListener("click", () => {
    aboutModal.classList.add("hidden");
  });
  aboutModal.addEventListener("click", (e) => {
    if (e.target === aboutModal) {
      aboutModal.classList.add("hidden");
    }
  });

  // Initial render
  renderList();
});
