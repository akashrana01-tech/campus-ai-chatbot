/**
 * CampusAI Group 2 - Student Chatbot Controller
 * Distinct Emerald & Amber Academic Interface
 * Features:
 * - Real-time conversational exchange with persistent SQLite logging
 * - Dual-tier response rendering (Local 3NF DB vs. Google Gemini AI)
 * - Category quick-filter tabs for instant topic discovery
 * - Web Speech API Speech-to-Text (Microphone voice input)
 * - Web Speech API Text-to-Speech (Audio answer playback)
 * - Interactive response rating (Helpful / Unhelpful)
 * - One-click answer copying with visual toast feedback
 * - Mobile responsive drawer & auto-expanding textarea
 */

document.addEventListener('DOMContentLoaded', () => {
  const chatMessages = document.getElementById('chatMessages');
  const chatForm = document.getElementById('chatForm');
  const chatInput = document.getElementById('chatInput');
  const sendBtn = document.getElementById('sendBtn');
  const micBtn = document.getElementById('micBtn');
  const charCounter = document.getElementById('charCounter');
  const typingIndicator = document.getElementById('typingIndicator');
  const dynamicChipsContainer = document.getElementById('dynamicChipsContainer');
  const clearChatBtn = document.getElementById('clearChatBtn');
  const headerClearBtn = document.getElementById('headerClearBtn');
  const chatCategoryBar = document.getElementById('chatCategoryBar');

  // Sidebar toggle elements
  const chatSidebar = document.getElementById('chatSidebar');
  const sidebarToggleBtn = document.getElementById('chatSidebarToggleBtn');
  const sidebarCloseBtn = document.getElementById('sidebarCloseBtn');
  const sidebarBackdrop = document.getElementById('sidebarBackdrop');

  // Category Presets for instant suggestions
  const CATEGORY_PRESETS = {
    'All': [
      'What courses does the college offer?',
      'How can I apply for admission?',
      'What are the college fees for BCA/BBA?',
      'When are the semester examinations?',
      'What companies visit for placements?',
      'What scholarships are available for students?'
    ],
    'Admissions': [
      'What are the eligibility criteria for undergraduate courses?',
      'How can I apply for admission to the college?',
      'What documents are required during the admission process?',
      'When is the last date to apply for new admissions?'
    ],
    'Courses': [
      'What courses and programs does the college offer?',
      'What is the curriculum and syllabus for SYBBA (CA) Semester III?',
      'Does the college offer internship and campus placement support?'
    ],
    'Fees': [
      'What are the college fees for undergraduate courses?',
      'Can college fees be paid in installments?',
      'What payment methods are accepted for fee payments?'
    ],
    'Examinations': [
      'When are semester examinations conducted?',
      'How do I get my semester examination hall ticket?',
      'What is the passing criteria and attendance requirement for exams?'
    ],
    'Placements': [
      'What companies visit the college for campus recruitment and placements?',
      'What is the average placement salary package for BBA and BCA students?',
      'Does the college offer practical placement interview preparation?'
    ],
    'Scholarships': [
      'What scholarships and financial assistance are available for students?',
      'Can economically weaker students get fee concessions?',
      'What is the application deadline for government scholarships?'
    ],
    'Hostels': [
      'What are the hostel accommodation rules and annual charges?',
      'Is there hostel accommodation available for outstation students?',
      'What amenities are provided in the college hostels?'
    ],
    'Helpdesk': [
      'How do I report a student grievance or contact the anti-ragging cell?',
      'How can I contact the college administration?',
      'Where can I find the official college holiday list and academic calendar?'
    ]
  };

  // Session ID Management
  let sessionId = localStorage.getItem('campusai_session_id');
  if (!sessionId) {
    sessionId = 'session_' + Math.random().toString(36).substring(2, 15) + Date.now().toString(36);
    localStorage.setItem('campusai_session_id', sessionId);
  }

  // Toast Notification Helper
  function showToast(message, type = 'info') {
    const container = document.getElementById('toastContainer');
    if (!container) return;
    const toast = document.createElement('div');
    toast.className = `toast-pill toast-${type}`;
    toast.innerHTML = `<span>${message}</span>`;
    container.appendChild(toast);
    setTimeout(() => {
      toast.classList.add('fade-out');
      setTimeout(() => toast.remove(), 300);
    }, 2800);
  }

  // Auto-scroll helper
  function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Format timestamp (e.g. "5:24 PM")
  function getCurrentTime() {
    return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  }

  // Safe HTML Escaping
  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // Safe Markdown Formatter
  function formatMarkdown(text) {
    if (!text) return '';
    let escaped = escapeHtml(text);
    escaped = escaped.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    escaped = escaped.replace(/\*(.*?)\*/g, '<em>$1</em>');
    escaped = escaped.replace(/\[(.*?)\]\((.*?)\)/g, (match, title, url) => {
      if (/^(https?:|mailto:|tel:)/i.test(url.trim())) {
        return `<a href="${url.trim()}" target="_blank" rel="noopener noreferrer">${title}</a>`;
      }
      return title;
    });

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
    if (inList) html += '</ul>';
    return html;
  }

  // Copy to Clipboard
  function copyToClipboard(text, btn) {
    const cleanText = text.replace(/\[DEMO RECORD\]/g, '').trim();
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(cleanText).then(() => {
        showToast('Answer copied to clipboard!', 'success');
        if (btn) {
          const originalText = btn.innerHTML;
          btn.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg><span>Copied!</span>`;
          setTimeout(() => { btn.innerHTML = originalText; }, 1800);
        }
      }).catch(() => fallbackCopy(cleanText));
    } else {
      fallbackCopy(cleanText);
    }
  }

  function fallbackCopy(text) {
    const ta = document.createElement('textarea');
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Answer copied!', 'success');
  }

  // Audio Speech Synthesis (Read Aloud)
  function speakAnswer(text, btn) {
    if (!('speechSynthesis' in window)) {
      showToast('Speech audio is not supported in this browser.', 'warning');
      return;
    }
    if (window.speechSynthesis.speaking) {
      window.speechSynthesis.cancel();
      if (btn) btn.classList.remove('speaking');
      return;
    }

    const clean = text
      .replace(/\[DEMO RECORD\]/g, '')
      .replace(/\[(.*?)\]\(.*?\)/g, '$1')
      .replace(/[*_#`]/g, '')
      .trim();

    const utterance = new SpeechSynthesisUtterance(clean);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;

    if (btn) {
      btn.classList.add('speaking');
      utterance.onend = () => btn.classList.remove('speaking');
      utterance.onerror = () => btn.classList.remove('speaking');
    }
    window.speechSynthesis.speak(utterance);
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

    let badgeHtml = '<span class="message-badge verified-badge">Verified DB Record</span>';
    if (data.source === 'ai') {
      badgeHtml = '<span class="message-badge ai-badge">Gemini 2.5 Flash</span>';
    } else if (data.source === 'fallback') {
      badgeHtml = '<span class="message-badge fallback-badge">Administration Notice</span>';
    } else if (data.source === 'greeting') {
      badgeHtml = '<span class="message-badge verified-badge">CampusAI</span>';
    }

    const formattedContent = formatMarkdown(data.response);
    const copyId = 'copy_' + Math.random().toString(36).substring(2, 9);
    const speakId = 'speak_' + Math.random().toString(36).substring(2, 9);
    const fbUpId = 'fbup_' + Math.random().toString(36).substring(2, 9);
    const fbDownId = 'fbdown_' + Math.random().toString(36).substring(2, 9);

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
          <button class="copy-btn" id="${copyId}" title="Copy Answer">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span>Copy</span>
          </button>
          <button class="speak-btn" id="${speakId}" title="Listen to Answer (Text-to-Speech)">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            <span>Listen</span>
          </button>
          <div class="feedback-group">
            <button class="feedback-btn" id="${fbUpId}" title="Helpful answer">👍</button>
            <button class="feedback-btn" id="${fbDownId}" title="Needs improvement">👎</button>
          </div>
        </div>
      </div>
    `;

    chatMessages.appendChild(wrapper);

    // Wire Copy Action
    const copyBtn = document.getElementById(copyId);
    if (copyBtn) {
      copyBtn.addEventListener('click', () => copyToClipboard(data.response, copyBtn));
    }

    // Wire Audio Speak Action
    const speakBtn = document.getElementById(speakId);
    if (speakBtn) {
      speakBtn.addEventListener('click', () => speakAnswer(data.response, speakBtn));
    }

    // Wire Feedback Actions
    const fbUp = document.getElementById(fbUpId);
    const fbDown = document.getElementById(fbDownId);
    if (fbUp) {
      fbUp.addEventListener('click', () => {
        fbUp.style.transform = 'scale(1.3)';
        fbUp.style.color = '#059669';
        showToast('Thank you! Feedback recorded.', 'success');
      });
    }
    if (fbDown) {
      fbDown.addEventListener('click', () => {
        fbDown.style.transform = 'scale(1.3)';
        fbDown.style.color = '#dc2626';
        showToast('Feedback noted. We will refine this answer.', 'info');
      });
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
          suggestions: ['What are the college fees for BCA/BBA?', 'What courses does the college offer?']
        });
      }
    } catch (err) {
      typingIndicator.style.display = 'none';
      sendBtn.disabled = false;
      appendAssistantMessage({
        response: 'Unable to reach CampusAI service right now. Please check your network connection or try again.',
        source: 'fallback',
        suggestions: ['How can I contact the college administration?']
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

  // Voice Input (Microphone Recognition)
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition && micBtn) {
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    micBtn.addEventListener('click', () => {
      if (micBtn.classList.contains('listening')) {
        recognition.stop();
        micBtn.classList.remove('listening');
      } else {
        try {
          recognition.start();
        } catch (e) {
          showToast('Voice recognition is already active.', 'info');
        }
      }
    });

    recognition.onstart = () => {
      micBtn.classList.add('listening');
      showToast('Listening... Speak your query clearly.', 'info');
    };

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      chatInput.value = transcript;
      charCounter.textContent = `${transcript.length}/600`;
      micBtn.classList.remove('listening');
      sendMessage(transcript);
    };

    recognition.onerror = () => {
      micBtn.classList.remove('listening');
      showToast('Microphone error or permission denied.', 'warning');
    };

    recognition.onend = () => {
      micBtn.classList.remove('listening');
    };
  } else if (micBtn) {
    micBtn.addEventListener('click', () => {
      showToast('Speech recognition is not supported in this browser.', 'warning');
    });
  }

  // Category Quick-Filter Bar Handler
  if (chatCategoryBar) {
    chatCategoryBar.addEventListener('click', (e) => {
      const pill = e.target.closest('.cat-pill');
      if (!pill) return;
      chatCategoryBar.querySelectorAll('.cat-pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      const cat = pill.getAttribute('data-category');
      const suggestions = CATEGORY_PRESETS[cat] || CATEGORY_PRESETS['All'];
      renderSuggestions(suggestions);
      showToast(`Browsing ${cat} questions`, 'info');
    });
  }

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
      const welcome = document.getElementById('welcomeMessage');
      chatMessages.innerHTML = '';
      if (welcome) {
        chatMessages.appendChild(welcome);
      }
      dynamicChipsContainer.innerHTML = '';
      sessionId = 'session_' + Math.random().toString(36).substring(2, 15) + Date.now().toString(36);
      localStorage.setItem('campusai_session_id', sessionId);
      showToast('Chat session cleared successfully', 'info');
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
