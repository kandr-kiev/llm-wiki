---
source_url: file:///workspace/Projects/AI-Education-Pro/client/src/assets/js/app.js
ingested: 2026-07-20
sha256: 67af6b17043ffac9571d0169a68bf7e3fd21d381fc5d3b08e6d74ceac2f9187c
blog_source: local:unknown
---
/**
 * AI Education Pro - Main Application Logic
 */

let currentUser = JSON.parse(localStorage.getItem('user_auth')) || null;
let userProgress = []; // Loaded from DB
let currentQuizLesson = null;
let quizAnswers = {};

// --- Helper Functions ---
function escapeHTML(str) {
    if (!str) return "";
    return str.replace(/[&<>"']/g, function (m) {
        return {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#39;'
        }[m];
    });
}

// --- Auth Logic ---
async function checkAuth() {
    const overlay = document.getElementById('authOverlay');
    if (!currentUser) {
        if (overlay) overlay.classList.remove('hidden');
        document.body.style.overflow = "hidden";
    } else {
        if (overlay) overlay.classList.add('hidden');
        document.body.style.overflow = "auto";
        await fetchProgress();
        renderSyllabus();
    }
}

async function fetchProgress() {
    if (!currentUser || !currentUser.id) return;
    try {
        const response = await fetch(config.apiEndpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ action: 'get_progress', user_id: currentUser.id })
        });
        const data = await response.json();
        if (data.success) {
            userProgress = data.progress;
            updateGreetingContent(); // Update greeting after progress is loaded
        }
    } catch (e) {
        console.error("Fetch progress error:", e);
    }
}

function updateGreetingContent() {
    const container = document.getElementById('ai-greeting-container');
    if (!currentUser || !container) {
        if (container) container.classList.add('hidden');
        return;
    }

    const completedCount = lessons.filter(l => isLessonPassed(l.id)).length;
    const totalCount = lessons.length;
    const remainingCount = totalCount - completedCount;

    // Find first unfinished lesson
    const nextLesson = lessons.find(l => !isLessonPassed(l.id)) || lessons[lessons.length - 1];

    container.innerHTML = `
        <div class="greeting-content flex items-center space-x-4">
            <div class="gemini-gradient p-2 rounded-xl text-white shrink-0">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M12 2L14.8 9.2L22 12L14.8 14.8L12 22L9.2 14.8L2 12L9.2 9.2L12 2Z" fill="currentColor" />
                </svg>
            </div>
            <div>
                <p class="text-stone-800 font-medium">Ласкаво просимо, <span class="text-indigo-600 font-bold">${escapeHTML(currentUser.nickname)}</span>, бажаю успіху в навчанні!</p>
                <a href="#lessons-list" onclick="renderSyllabus(${nextLesson.id}); setTimeout(() => document.getElementById('content-${nextLesson.id}')?.scrollIntoView({behavior:'smooth'}), 100)" class="next-lesson-link text-sm">
                    Продовжити: Урок ${nextLesson.id}. ${nextLesson.title}
                    <svg class="ml-1" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                </a>
            </div>
        </div>
        <div class="greeting-stats">
            <p class="text-[10px] uppercase font-bold text-stone-400 tracking-wider">Ваш прогрес</p>
            <p class="text-stone-800 font-black text-lg">
                ${completedCount} <span class="text-stone-300 font-normal">/ ${totalCount}</span>
            </p>
            <p class="text-[10px] text-indigo-500 font-bold">${remainingCount > 0 ? `Залишилось: ${remainingCount}` : 'Курс завершено! 🎓'}</p>
        </div>
    `;
    container.classList.remove('hidden');
}

// Activation is now implicit upon registration in this version
function activateAccount() {
    // Keep as placeholder if needed later
}

const regForm = document.getElementById('regForm');
if (regForm) {
    regForm.onsubmit = async (e) => {
        e.preventDefault();
        const submitBtn = document.getElementById('regSubmit');
        submitBtn.disabled = true;
        submitBtn.innerText = "Обробка...";

        const formData = new FormData(regForm);
        const email = formData.get('email');
        const nickname = formData.get('nickname') || email.split('@')[0];

        if (!email || !email.includes('@')) {
            alert("Будь ласка, введіть коректний email.");
            submitBtn.disabled = false;
            submitBtn.innerText = "Зареєструватися";
            return;
        }

        try {
            const response = await fetch(config.apiEndpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'register', email: escapeHTML(email), nickname: escapeHTML(nickname) })
            });
            const data = await response.json();

            if (data.success) {
                alert(data.message);
                if (data.user) {
                    localStorage.setItem('user_auth', JSON.stringify(data.user));
                    currentUser = data.user;
                    await checkAuth(); // Update UI
                } else {
                    regForm.reset();
                }
            } else {
                alert("Помилка: " + data.error);
            }
        } catch (error) {
            alert("Помилка зв'язку з сервером. Спробуйте пізніше.");
        } finally {
            submitBtn.disabled = false;
            submitBtn.innerText = "Зареєструватися";
        }
    };
}

// --- Activation Handling ---
async function handleUrlActions() {
    const urlParams = new URLSearchParams(window.location.search);
    const action = urlParams.get('action');
    const token = urlParams.get('token');

    if (action === 'activate' && token) {
        try {
            const response = await fetch(config.apiEndpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ action: 'activate', token: token })
            });
            const data = await response.json();

            if (data.success) {
                alert(data.message);
                if (data.user) {
                    localStorage.setItem('user_auth', JSON.stringify(data.user));
                    currentUser = data.user;
                    await checkAuth(); // Update status and load progress
                }
                // Clear URL parameters
                window.history.replaceState({}, document.title, window.location.pathname);
            } else {
                alert("Помилка активації: " + data.error);
            }
        } catch (e) {
            console.error("Activation error:", e);
        }
    }
}

function renderSyllabus(expandedId = null) {
    const list = document.getElementById('lessons-list');
    if (!list) return;
    list.innerHTML = "";
    lessons.forEach(l => {
        const isPassed = isLessonPassed(l.id);
        const isLocked = !isLessonUnlocked(l.id);
        const isExpanded = (expandedId === l.id);
        const card = document.createElement('div');

        card.className = `lesson-card rounded-[2rem] overflow-hidden ${isLocked ? 'locked-lesson' : ''}`;
        card.innerHTML = `
            <button onclick="${isLocked ? '' : `toggleLesson(${l.id})`}" class="w-full text-left p-6 md:p-10 flex justify-between items-start hover:bg-stone-50 transition-colors">
                <div class="flex items-start space-x-4 md:space-x-6">
                    <span class="gemini-gradient text-white font-bold h-10 w-10 md:h-12 md:w-12 flex items-center justify-center rounded-2xl text-base md:text-lg shrink-0 shadow-lg">${l.id}</span>
                    <div>
                        <div class="flex items-center space-x-3">
                            <h3 class="font-bold text-xl md:text-2xl text-stone-900 tracking-tight">${l.title}</h3>
                            ${isPassed ? '<span class="passed-badge">Пройдено</span>' : ''}
                            ${isLocked ? '<span class="text-stone-300">🔒</span>' : ''}
                        </div>
                        <p class="text-xs md:text-sm text-stone-500 mt-2 leading-relaxed italic max-w-2xl">${l.shortTheory}</p>
                    </div>
                </div>
                <span id="arrow-${l.id}" class="text-stone-300 transition-transform duration-500 mt-2 text-lg ${isLocked ? 'hidden' : ''}">▼</span>
            </button>
            ${isLocked ? '' : `
            <div id="content-${l.id}" class="${isExpanded ? '' : 'hidden'} p-6 md:p-10 border-t border-stone-100 space-y-10 bg-white">
                <div class="base-theory-box">
                    <h4 class="font-bold text-blue-900 text-[10px] uppercase tracking-[0.3em] mb-3">📘 Базова теорія</h4>
                    <p class="text-stone-700 text-sm md:text-base leading-relaxed">${l.baseTheory}</p>
                </div>
                <div class="media-box">
                    <h4 class="font-bold text-stone-800 text-[10px] uppercase mb-4 tracking-[0.3em]">🎥 Медіа-матеріали</h4>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-center">
                        <div class="md:col-span-2 flex flex-row gap-3">
                            <button onclick="openModal('${l.presUrl}', '${l.title}')" class="gemini-gradient text-white px-4 py-3 rounded-xl font-bold hover:brightness-110 transition-all text-sm md:text-base shadow-md flex-1 text-center whitespace-nowrap">📊 Презентація</button>
                            ${l.videoUrl ? `<button onclick="openVideoModal('${l.videoUrl}', '${l.title}')" class="gemini-gradient text-white px-4 py-3 rounded-xl font-bold hover:brightness-110 transition-all text-sm md:text-base shadow-md flex-1 text-center whitespace-nowrap">📽️ Відеоогляд</button>` : ''}
                        </div>
                        <div class="md:col-span-1 bg-white p-2 rounded-xl border flex items-center shadow-sm"><audio controls class="w-full"><source src="${l.audioUrl}" type="audio/mpeg"></audio></div>
                    </div>
                </div>
                <div class="deep-theory-box">
                    <h4 class="font-bold text-indigo-900 text-[10px] uppercase tracking-[0.3em] mb-3">🧠 Глибока теорія</h4>
                    <p class="text-stone-700 text-sm md:text-base leading-relaxed">${l.deepTheory}</p>
                </div>
                <div class="task-box">
                    <h4 class="font-bold text-purple-900 text-[10px] uppercase mb-4 tracking-[0.3em]">🛠️ Практичні завдання</h4>
                    <ul class="space-y-2 mb-6">
                        ${l.tasks.map(t => `<li class="text-stone-700 text-sm md:text-base flex items-start"><span class="text-indigo-500 mr-2 text-lg leading-none">✦</span> <span>${t}</span></li>`).join('')}
                    </ul>
                    <div id="quiz-status-${l.id}" class="mt-6 pt-6 border-t border-stone-100">
                        <button onclick="startQuiz(${l.id})" class="inline-flex items-center px-8 py-3 bg-indigo-600 text-white font-bold rounded-xl hover:bg-indigo-700 transition-all shadow-lg hover:shadow-indigo-200">
                            🚀 Запустити тестування
                        </button>
                    </div>
                </div>
            </div>
            `}
        `;
        list.appendChild(card);
        if (isExpanded) {
            const arrow = document.getElementById(`arrow-${l.id}`);
            if (arrow) arrow.style.transform = "rotate(180deg)";
        }
        updateLessonStatusUI(l.id);
    });
    checkCourseCompletion();
}

function isLessonUnlocked(lessonId) {
    if (lessonId === 1) return true;
    const prevLessonId = lessonId - 1;
    const prev = userProgress.find(p => p.lesson_id == prevLessonId);
    return prev && prev.score >= 6;
}

function isLessonPassed(lessonId) {
    const current = userProgress.find(p => p.lesson_id == lessonId);
    return current && current.score >= 6;
}

function checkCourseCompletion() {
    const allPassed = lessons.every(l => isLessonPassed(l.id));
    if (allPassed) {
        showGraduation();
    }
}

function showGraduation() {
    const screen = document.getElementById('courseFinished');
    if (!screen) return;
    document.getElementById('reportUserName').innerText = `Студент: ${currentUser ? escapeHTML(currentUser.nickname) : 'Гість'}`;

    const rows = document.getElementById('reportRows');
    rows.innerHTML = "";

    lessons.forEach(l => {
        const prog = userProgress.find(p => p.lesson_id == l.id);
        const score = prog ? parseInt(prog.score) : 0;
        let comment = "";
        if (score === 8) comment = "Чудова робота! Ви справжній експерт.";
        else if (score >= 6) comment = "Гарний результат. Ви впевнено володієте матеріалом.";
        else comment = "Матеріал засвоєно частково. Рекомендуємо переглянути ще раз.";

        rows.innerHTML += `
            <tr>
                <td class="px-6 py-4 font-bold text-stone-800">${l.title}</td>
                <td class="px-6 py-4 text-center font-black text-indigo-600">${score} / 8</td>
                <td class="px-6 py-4 text-stone-500 text-xs italic">${comment}</td>
            </tr>
        `;
    });

    screen.classList.remove('hidden');
    document.body.style.overflow = "hidden";

    // Confetti effect
    const duration = 5 * 1000;
    const animationEnd = Date.now() + duration;
    const defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 4000 };

    function randomInRange(min, max) {
        return Math.random() * (max - min) + min;
    }

    const interval = setInterval(function () {
        const timeLeft = animationEnd - Date.now();
        if (timeLeft <= 0) return clearInterval(interval);
        const particleCount = 50 * (timeLeft / duration);
        confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 } }));
        confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 } }));
    }, 250);
}

// --- Quiz Logic ---

function updateLessonStatusUI(lessonId) {
    const statusDiv = document.getElementById(`quiz-status-${lessonId}`);
    if (!statusDiv) return;

    const prog = userProgress.find(p => p.lesson_id == lessonId);
    if (prog && prog.score >= 6) {
        statusDiv.innerHTML = `
            <div class="bg-green-50 border border-green-200 rounded-2xl p-4 flex items-center justify-between">
                <div class="flex items-center space-x-3">
                    <span class="text-2xl">✅</span>
                    <div>
                        <p class="font-bold text-green-800">Тест пройдено!</p>
                        <p class="text-xs text-green-600">Ваш результат: ${prog.score} з 8</p>
                    </div>
                </div>
                <button onclick="startQuiz(${lessonId})" class="text-sm font-bold text-green-700 hover:underline">Переглянути</button>
            </div>
        `;
    }
}

function startQuiz(lessonId) {
    currentQuizLesson = lessons.find(l => l.id === lessonId);
    const saved = localStorage.getItem(`quiz_lesson_${lessonId}`);
    const questionCount = currentQuizLesson.quiz.length;
    const state = saved ? JSON.parse(saved) : { answers: Array(questionCount).fill(null), score: null };

    document.getElementById('testModalTitle').innerText = `Тест: ${currentQuizLesson.title}`;
    renderQuizContent(state);
    document.getElementById('testModal').style.display = "block";
    document.body.style.overflow = "hidden";
}

function renderQuizContent(state) {
    const container = document.getElementById('test-container');
    if (!container) return;
    const isFinished = state.score !== null;

    let html = `<div class="space-y-8">`;

    currentQuizLesson.quiz.forEach((q, idx) => {
        const selectedIdx = state.answers[idx];
        html += `
            <div id="q-block-${idx}" class="space-y-4 transition-all duration-300">
                <p class="font-bold text-stone-800 text-lg">${idx + 1}. ${q.q}</p>
                <div class="grid gap-3 ${currentQuizLesson.id === 11 ? 'grid-cols-1 md:grid-cols-1' : ''}">
                    ${q.a.map((opt, optIdx) => {
            let classes = "test-option p-4 rounded-xl text-sm font-medium ";
            if (selectedIdx === optIdx) classes += "selected ";
            if (isFinished) {
                if (optIdx === q.correct) classes += "!border-green-500 !bg-green-50 !text-green-800 shadow-sm ";
                else if (selectedIdx === optIdx) classes += "!border-red-400 !bg-red-50 !text-red-800 ";
                classes += "pointer-events-none ";
            }
            return `<div class="${classes}" onclick="selectOption(${idx}, ${optIdx}, this)">${opt}</div>`;
        }).join('')}
                </div>
            </div>
        `;
    });

    if (!isFinished) {
        html += `
            <button onclick="finishQuiz()" class="w-full gemini-gradient text-white font-bold py-4 rounded-xl shadow-lg mt-8">
                Завершити та перевірити
            </button>
        `;
    } else {
        const total = currentQuizLesson.quiz.length;
        const pct = (state.score / total) * 100;

        if (pct === 100) { resultMsg = "Чудова робота! Ви справжній експерт. 🎉"; scoreColor = "text-green-600"; }
        else if (pct >= 85) { resultMsg = "Гарно! Майже ідеально. 👍"; scoreColor = "text-blue-600"; }
        else if (pct >= 75) { resultMsg = "Непогано. Ви впевнено володієте матеріалом. 🙂"; scoreColor = "text-indigo-600"; }
        else { resultMsg = "Матеріал засвоєно частково. Рекомендуємо повторити. 📚"; scoreColor = "text-red-500"; }

        html += `
            <div class="bg-stone-50 p-8 rounded-3xl text-center space-y-4 mt-8 border-2 border-dashed border-stone-200">
                <p class="text-4xl font-black ${scoreColor}">${state.score} / ${total}</p>
                <p class="text-xl font-bold text-stone-700">${resultMsg}</p>
                ${pct >= 75 ? `
                    <div class="pt-4">
                        <p class="text-stone-500 mb-4">Вітаємо з пройденим тестом!</p>
                        <button onclick="goToNextLesson(${currentQuizLesson.id})" class="bg-stone-900 text-white px-8 py-3 rounded-xl font-bold">Перейти до наступного уроку</button>
                    </div>
                ` : `
                    <button onclick="resetQuiz(${currentQuizLesson.id})" class="text-indigo-600 font-bold">Спробувати ще раз</button>
                `}
            </div>
        `;
    }

    html += `</div>`;
    container.innerHTML = html;
}

function selectOption(qIdx, optIdx, el) {
    const saved = localStorage.getItem(`quiz_lesson_${currentQuizLesson.id}`);
    const qCount = currentQuizLesson.quiz.length;
    let state = saved ? JSON.parse(saved) : { answers: Array(qCount).fill(null), score: null };

    if (state.score !== null) return; // Lock if finished

    state.answers[qIdx] = optIdx;
    localStorage.setItem(`quiz_lesson_${currentQuizLesson.id}`, JSON.stringify(state));

    // Minor UI feedback: fast selection
    const parent = el.parentNode;
    parent.querySelectorAll('.test-option').forEach(opt => opt.classList.remove('selected'));
    el.classList.add('selected');
}

async function finishQuiz() {
    const saved = JSON.parse(localStorage.getItem(`quiz_lesson_${currentQuizLesson.id}`));
    if (!saved || saved.answers.includes(null)) {
        alert("Будь ласка, дайте відповіді на всі запитання!");
        return;
    }

    let score = 0;
    currentQuizLesson.quiz.forEach((q, idx) => {
        if (saved.answers[idx] === q.correct) score++;
    });

    saved.score = score;
    localStorage.setItem(`quiz_lesson_${currentQuizLesson.id}`, JSON.stringify(saved));

    // --- Save to Server ---
    try {
        const total = currentQuizLesson.quiz.length;
        const pct = (score / total) * 100;
        let comment = pct === 100 ? "Експерт" : (pct >= 75 ? "Добре" : "Спробуйте ще");
        const resp = await fetch(config.apiEndpoint, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                action: 'save_score',
                user_id: currentUser.id,
                lesson_id: currentQuizLesson.id,
                score: score,
                total: total, // Passing total questions
                comment: comment
            })
        });
        const data = await resp.json();
        if (!data.success) {
            alert("Помилка збереження результату на сервері: " + (data.error || "Невідома помилка"));
        } else {
            // Sync local progress cache only on success
            const existing = userProgress.find(p => p.lesson_id == currentQuizLesson.id);
            if (existing) {
                existing.score = score;
                existing.comment = comment;
            } else {
                userProgress.push({ lesson_id: currentQuizLesson.id, score, comment });
            }
        }
    } catch (e) {
        console.error("Save score error:", e);
        alert("Помилка зв'язку з сервером при збереженні результату.");
    }

    updateGreetingContent(); // Refresh progress in greeting banner
    renderQuizContent(saved);

    const total = currentQuizLesson.quiz.length;
    const pct = (score / total) * 100;
    if (pct >= 75) {
        renderSyllabus(currentQuizLesson.id);
    } else {
        updateLessonStatusUI(currentQuizLesson.id);
    }
}

function resetQuiz(lessonId) {
    localStorage.removeItem(`quiz_lesson_${lessonId}`);
    startQuiz(lessonId);
    updateLessonStatusUI(lessonId);
}

function goToNextLesson(currentId) {
    closeTestModal();
    const nextId = currentId + 1;
    if (nextId <= lessons.length) {
        renderSyllabus(nextId);
        const nextContent = document.getElementById(`content-${nextId}`);
        if (nextContent) {
            nextContent.scrollIntoView({ behavior: 'smooth' });
        }
    }
}

function closeTestModal() {
    const modal = document.getElementById('testModal');
    if (modal) modal.style.display = "none";
    document.body.style.overflow = "auto";
}

// --- Original AI & Modal Functions ---

async function runAi() {
    const promptInput = document.getElementById('ai-prompt');
    const prompt = promptInput.value;
    const welcome = document.getElementById('gemini-welcome');
    const responseArea = document.getElementById('ai-response-area');
    const loader = document.getElementById('loader');
    const sendBtn = document.getElementById('send-btn');
    const coachMode = document.getElementById('coach-mode').checked;

    if (!prompt) return;

    if (welcome) welcome.classList.add('hidden');
    if (responseArea) {
        responseArea.classList.remove('hidden');
        responseArea.innerHTML = "<div class='animate-pulse py-8'><div class='h-4 bg-stone-100 rounded w-3/4 mb-4'></div><div class='h-4 bg-stone-100 rounded w-full'></div></div>";
    }
    if (loader) loader.classList.remove('hidden');
    if (sendBtn) sendBtn.classList.add('hidden');

    try {
        let finalPrompt = prompt;
        if (coachMode) {
            const systemPrompt = "Ти — Професійний коуч з курсу 'Мистецтво роботи з Штучним Інтелектом'. Відповідай експертно, надихаюче та структуровано. Допомагай студенту опанувати навички роботи з ШІ через практику.";
            finalPrompt = `${systemPrompt}\n\nЗапит студента: ${prompt}`;
        }

        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${config.aiModel}:generateContent?key=${config.apiKey}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: finalPrompt }] }]
            })
        });

        if (!response.ok) {
            const errorData = await response.json();
            let errorMessage = "Сталася помилка при зверненні до ШІ.";

            if (response.status === 429) {
                errorMessage = "Перевищено ліміт запитів. Будь ласка, зачекайте хвилину та спробуйте ще раз.";
            } else if (response.status === 401 || response.status === 403) {
                errorMessage = "Помилка авторизації (API Key). Будь ласка, зверніться до підтримки.";
            } else if (response.status >= 500) {
                errorMessage = "Сервер ШІ тимчасово недоступний. Спробуйте пізніше.";
            } else if (errorData.error?.message) {
                errorMessage = `Помилка: ${errorData.error.message}`;
            }

            throw new Error(errorMessage);
        }

        const data = await response.json();

        if (data.candidates?.[0]?.finishReason === "SAFETY") {
            if (responseArea) responseArea.innerHTML = "<div class='p-4 bg-orange-50 border border-orange-200 rounded-2xl text-orange-800 text-sm'>⚠️ Відповідь заблокована фільтрами безпеки. Спробуйте змінити запит.</div>";
            return;
        }

        const text = data.candidates?.[0]?.content?.parts?.[0]?.text || "Вибачте, сталася помилка при генерації відповіді.";
        if (responseArea) {
            responseArea.innerHTML = `<div class="py-4 text-stone-800">${marked.parse(text)}</div>`;
        }
        promptInput.value = "";
        const scrollArea = document.getElementById('gemini-scroll-area');
        if (scrollArea) scrollArea.scrollTop = 0;
    } catch (e) {
        console.error("Gemini Error:", e);
        let displayMsg = e.message;
        if (e.message === "Failed to fetch") {
            displayMsg = "Відсутній зв'язок з інтернетом або API Gemini недоступне.";
        }
        if (responseArea) {
            responseArea.innerHTML = `
                <div class='p-6 bg-red-50 border border-red-100 rounded-3xl space-y-3'>
                    <div class='flex items-center space-x-2 text-red-600 font-bold'>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
                        <span>Упс! Виникла проблема</span>
                    </div>
                    <p class='text-red-700 text-sm'>${displayMsg}</p>
                    <button onclick="runAi()" class='text-xs font-bold text-red-600 uppercase tracking-widest hover:underline'>Спробувати ще раз</button>
                </div>`;
        }
    } finally {
        if (loader) loader.classList.add('hidden');
        if (sendBtn) sendBtn.classList.remove('hidden');
    }
}

function toggleLesson(id) {
    const content = document.getElementById(`content-${id}`);
    const arrow = document.getElementById(`arrow-${id}`);
    if (!content || !arrow) return;
    const isHidden = content.classList.contains('hidden');

    if (isHidden) {
        content.classList.remove('hidden');
        arrow.style.transform = "rotate(180deg)";
    } else {
        content.classList.add('hidden');
        arrow.style.transform = "rotate(0deg)";
    }
}

function openModal(url, title) {
    const modal = document.getElementById('presModal');
    const modalTitle = document.getElementById('modalTitle');
    const iframe = document.getElementById('presIframe');
    if (modalTitle) modalTitle.innerText = title;
    if (iframe) iframe.src = url;
    if (modal) modal.style.display = "block";
    document.body.style.overflow = "hidden";
}

function closeModal() {
    const modal = document.getElementById('presModal');
    const iframe = document.getElementById('presIframe');
    const modalContent = modal ? modal.querySelector('.modal-content') : null;

    if (modal) modal.style.display = "none";
    if (iframe) iframe.src = "";
    if (modalContent) {
        modalContent.classList.remove('maximized');
        document.getElementById('maxIcon')?.classList.remove('hidden');
        document.getElementById('restoreIcon')?.classList.add('hidden');
    }
    document.body.style.overflow = "auto";
}

function openVideoModal(url, title) {
    const modal = document.getElementById('videoModal');
    const modalTitle = document.getElementById('videoModalTitle');
    const video = document.getElementById('lessonVideo');
    const source = document.getElementById('videoSource');

    if (modalTitle) modalTitle.innerText = `📽️ Відеоогляд: ${title}`;
    if (source) source.src = url;
    if (video) {
        video.load();
        video.play().catch(e => console.log("Auto-play prevented:", e));
    }
    if (modal) modal.style.display = "block";
    document.body.style.overflow = "hidden";
}

function closeVideoModal() {
    const modal = document.getElementById('videoModal');
    const video = document.getElementById('lessonVideo');
    const source = document.getElementById('videoSource');

    if (video) {
        video.pause();
        video.currentTime = 0;
    }
    if (source) source.src = "";
    if (modal) modal.style.display = "none";
    document.body.style.overflow = "auto";
}

function toggleMaximize() {
    const modal = document.getElementById('presModal');
    if (!modal) return;
    const modalContent = modal.querySelector('.modal-content');
    const maxIcon = document.getElementById('maxIcon');
    const restoreIcon = document.getElementById('restoreIcon');

    if (modalContent.classList.contains('maximized')) {
        modalContent.classList.remove('maximized');
        maxIcon?.classList.remove('hidden');
        restoreIcon?.classList.add('hidden');
    } else {
        modalContent.classList.add('maximized');
        maxIcon?.classList.add('hidden');
        restoreIcon?.classList.remove('hidden');
    }
}

function openFeedbackModal() {
    const modal = document.getElementById('feedbackModal');
    if (modal) modal.style.display = "block";
    document.body.style.overflow = "hidden";
}

function closeFeedbackModal() {
    const modal = document.getElementById('feedbackModal');
    if (modal) modal.style.display = "none";
    document.body.style.overflow = "auto";
}

window.onclick = (e) => {
    if (e.target == document.getElementById('presModal')) closeModal();
    if (e.target == document.getElementById('videoModal')) closeVideoModal();
    if (e.target == document.getElementById('feedbackModal')) closeFeedbackModal();
    if (e.target == document.getElementById('testModal')) closeTestModal();
}

window.onload = () => {
    handleUrlActions();
    checkAuth();

    // Встановлюємо назву моделі з конфігу
    const modelNameDisplay = document.getElementById('model-name-display');
    if (modelNameDisplay && typeof config !== 'undefined' && config.aiModel) {
        modelNameDisplay.textContent = config.aiModel;
    }
};

const aiPrompt = document.getElementById('ai-prompt');
if (aiPrompt) {
    aiPrompt.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') runAi();
    });
}

const feedbackForm = document.getElementById('feedbackForm');
if (feedbackForm) {
    feedbackForm.onsubmit = async (e) => {
        e.preventDefault();
        const submitBtn = document.getElementById('feedbackSubmit');
        submitBtn.disabled = true;
        submitBtn.innerText = "Надсилаю...";

        const name = formData.get('name');
        const email = formData.get('email');
        const message = formData.get('message');

        if (!name || !email || !message) {
            alert("Будь ласка, заповніть всі поля.");
            submitBtn.disabled = false;
            submitBtn.innerText = "Надіслати";
            return;
        }

        const feedbackData = {
            action: 'save_feedback',
            user_id: currentUser ? currentUser.id : null,
            name: escapeHTML(name),
            email: escapeHTML(email),
            message: escapeHTML(message)
        };

        try {
            const response = await fetch(config.apiEndpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(feedbackData)
            });
            const data = await response.json();

            if (data.success) {
                feedbackForm.classList.add('hidden');
                document.getElementById('feedbackSuccess').classList.remove('hidden');
            } else {
                alert('Помилка збереження: ' + data.error);
            }
        } catch (error) {
            alert('Помилка мережі. Спробуйте пізніше.');
        } finally {
            submitBtn.disabled = false;
            submitBtn.innerText = "Надіслати";
        }
    };
}
