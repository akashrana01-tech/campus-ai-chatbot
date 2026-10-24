/**
 * CampusAI - Student Chatbot Controller
 * Handles conversation state, real-time message rendering,
 * suggested chips, mobile sidebar, and markdown parsing.
 */

document.addEventListener('DOMContentLoaded', () => {
  const chatMessages = document.getElementById('chatMessages');
  const chatForm = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const sendBtn = document.getElementById('sendBtn');
  const charCounter = document.getElementById('charCounter');
  const typingIndicator = document.getElementById('typingIndicator');
  const dynamicChipsContainer = document.getElementById('dynamicChipsContainer');
  const clearChatBtn = document.getElementById('clearChatBtn');
  const headerClearBtn = document.getElementById('headerClearBtn');

  // Sidebar toggle elements
  const chatSidebar = document.getElementById('chatSidebar');
  const sidebarToggleBtn = document.getElementById('chatSidebarToggleBtn');
  const sidebarCloseBtn = document.getElementById('sidebarCloseBtn');
  const sidebarBackdrop = document.getElementById('sidebarBackdrop');

  // Session ID Management
  let sessionId = localStorage.getItem('campusai_session_id');
  if (!sessionId) {
    sessionId = 'session_' + Math.random().toString(36).substring(2, 15) + Date.now().toString(36);
    localStorage.setItem('campusai_session_id', sessionId);
  }

  // Auto-scroll helper
  function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Format timestamp (e.g. "5:24 PM")
  function getCurrentTime() {
    return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }

  // Safe HTML Escaping for User Strings
  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // Safe Markdown Formatter (Bold, Bullet Points, Numbered Lists, Links, Paragraphs)
  function formatMarkdown(text) {
    if (!text) return '';

    // First escape HTML entities
    let escaped = escapeHtml(text);

    // Markdown bold: **text** -> <strong>text</strong>
    escaped = escaped.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Markdown italic: *text* -> <em>text</em>
    escaped = escaped.replace(/\*(.*?)\*/g, '<em>$1</em>');

    // Markdown link: [text](url) -> <a href="url" target="_blank">text</a>
    escaped = escaped.replace(/\[(.*?)\]\((.*?)\)/g, (match, title, url) => {
      // Validate url safety (http, https, mailto, tel)
      if (/^(https?:|mailto:|tel:)/i.test(url.trim())) {
        return `<a href="${url.trim()}" target="_blank" rel="noopener noreferrer">${title}</a>`;
      }
      return title;
    });

    // Split lines for list and paragraph processing
    const lines = escaped.split('\n');
    let html = '';
    let inList = false;

    for (let i = 0; i < lines.length; i++) {
      const line = lines[i].trim();

      if (line.startsWith('- ') || line.startsWith('* ')) {
        if (!inList) {
          html += '<ul>';
          inList = true;
        }
        html += `<li>${line.substring(2)}</li>`;
      } else {
        if (inList) {
          html += '</ul>';
          inList = false;
        }
        if (line) {
          html += `<p>${line}</p>`;
        }
      }
    }

    if (inList) {
      html += '</ul>';
    }

    return html;
  }

  // Append User Message to UI
  function appendUserMessage(text) {
    const wrapper = document.createElement('div');
    wrapper.className = 'message-wrapper user-wrapper';
    wrapper.innerHTML = `
      <div class="avatar-bubble user-avatar">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
      </div>
      <div class="message-content-block">
        <div class="message-meta">
          <span class="message-time">${getCurrentTime()}</span>
          <span class="message-author">You</span>
        </div>
        <div class="message-bubble user-bubble">
          <p>${escapeHtml(text)}</p>
        </div>
      </div>
    `;
    chatMessages.appendChild(wrapper);
    scrollToBottom();
  }

  // Append Assistant Message to UI
  function appendAssistantMessage(data) {
    const wrapper = document.createElement('div');
    wrapper.className = 'message-wrapper assistant-wrapper';

    // Source badge text & class
    let badgeHtml = '<span class="message-badge verified-badge">Verified FAQ</span>';
    if (data.source === 'ai') {
      badgeHtml = '<span class="message-badge ai-badge">Gemini AI</span>';
    } else if (data.source === 'fallback') {
      badgeHtml = '<span class="message-badge fallback-badge">Admin Notice</span>';
    } else if (data.source === 'greeting') {
      badgeHtml = '<span class="message-badge verified-badge">CampusAI</span>';
    }

    const formattedContent = formatMarkdown(data.response);
    const copyId = 'copy_' + Math.random().toString(36).substring(2, 9);

    wrapper.innerHTML = `
      <div class="avatar-bubble bot-avatar">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>
      </div>
      <div class="message-content-block">
        <div class="message-meta">
          <span class="message-author">CampusAI</span>
          <span class="message-time">${getCurrentTime()}</span>
          ${badgeHtml}
        </div>
        <div class="message-bubble bot-bubble">
          ${formattedContent}
        </div>
        <div class="message-actions-bar">
          <button class="copy-btn" id="${copyId}">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span>Copy Answer</span>
          </button>
        </div>
      </div>
    `;

    chatMessages.appendChild(wrapper);

    // Setup copy button
    const copyBtn = document.getElementById(copyId);
    if (copyBtn) {
      copyBtn.addEventListener('click', () => copyToClipboard(data.response, copyBtn));
    }

    // Render suggestions
    if (data.suggestions && data.suggestions.length > 0) {
      renderSuggestions(data.suggestions);
    }

    scrollToBottom();
  }

  // Render Suggested Question Chips
  function renderSuggestions(suggestions) {
    dynamicChipsContainer.innerHTML = '';
    suggestions.forEach(query => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'chip-btn';
      btn.textContent = query;
      btn.addEventListener('click', () => {
        chatInput.value = query;
        sendMessage(query);
      });
      dynamicChipsContainer.appendChild(btn);
    });
  }

  // Send Message Logic
  async function sendMessage(text) {
    const message = (text || chatInput.value || '').trim();
    if (!message) return;

    appendUserMessage(message);
    chatInput.value = '';
    chatInput.style.height = 'auto';
    charCounter.textContent = '0/600';
    sendBtn.disabled = true;

    // Show Typing Indicator
    typingIndicator.style.display = 'flex';
    scrollToBottom();

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: message,
          session_id: sessionId,
        }),
      });

      const data = await response.json();

      typingIndicator.style.display = 'none';
      sendBtn.disabled = false;

      if (response.ok && data.success) {
        appendAssistantMessage(data);
      } else {
        appendAssistantMessage({
          response: data.error || 'I encountered an unexpected issue connecting to the knowledge base. Please try asking again in a moment.',
          source: 'fallback',
          suggestions: ['What are the college fees?', 'What courses are offered?']
        });
      }
    } catch (err) {
      typingIndicator.style.display = 'none';
      sendBtn.disabled = false;
      appendAssistantMessage({
        response: 'Unable to reach CampusAI service right now. Please check your internet connection or try again.',
        source: 'fallback',
        suggestions: ['How can I contact the college office?']
      });
    }
  }

  // Chat Form Submit Event
  chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    sendMessage();
  });

  // Enter to send (Shift+Enter for newline)
  chatInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  });

  // Character counter & auto-resize input
  chatInput.addEventListener('input', () => {
    charCounter.textContent = `${chatInput.value.length}/600`;
    chatInput.style.height = 'auto';
    chatInput.style.height = Math.min(chatInput.scrollHeight, 120) + 'px';
  });

  // Delegate initial chip buttons
  document.addEventListener('click', (e) => {
    const chip = e.target.closest('.chip-btn, .topic-chip-btn');
    if (chip && chip.dataset.query) {
      sendMessage(chip.dataset.query);
      closeSidebar();
    }
  });

  // Reset / Clear Chat Handler
  function resetConversation() {
    if (confirm('Are you sure you want to clear your current chat history?')) {
      // Clear all except welcome message
      const welcome = document.getElementById('welcomeMessage');
      chatMessages.innerHTML = '';
      if (welcome) {
        chatMessages.appendChild(welcome);
      }
      dynamicChipsContainer.innerHTML = '';
      sessionId = 'session_' + Math.random().toString(36).substring(2, 15) + Date.now().toString(36);
      localStorage.setItem('campusai_session_id', sessionId);
      showToast('Chat history cleared', 'info');
    }
  }

  if (clearChatBtn) clearChatBtn.addEventListener('click', resetConversation);
  if (headerClearBtn) headerClearBtn.addEventListener('click', resetConversation);

  // Mobile Sidebar Toggle
  function openSidebar() {
    chatSidebar.classList.add('open');
    sidebarBackdrop.classList.add('open');
  }

  function closeSidebar() {
    chatSidebar.classList.remove('open');
    sidebarBackdrop.classList.remove('open');
  }

  if (sidebarToggleBtn) sidebarToggleBtn.addEventListener('click', openSidebar);
  if (sidebarCloseBtn) sidebarCloseBtn.addEventListener('click', closeSidebar);
  if (sidebarBackdrop) sidebarBackdrop.addEventListener('click', closeSidebar);

  // Check URL query parameters (e.g. /chat?q=What+are+the+fees)
  const metaQuery = document.querySelector('meta[name="initial-query"]')?.getAttribute('content');
  const urlParamQuery = new URLSearchParams(window.location.search).get('q');
  const autoQuery = metaQuery || urlParamQuery;

  if (autoQuery && autoQuery.trim()) {
    chatInput.value = autoQuery.trim();
    setTimeout(() => {
      sendMessage(autoQuery.trim());
    }, 400);
  }
});
