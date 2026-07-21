---
title: "app.js"
type: comparison
tags:
  - llm-wiki
  - knowledge-base
    - ai
  - application
  - async
  - container
  - data
  - gemini
  - search
---

# app.js

> **Source:** local-ai-education-proassetsjsappjs-2026-07-20.md
> **Type:** comparison
> **Created:** 2026-07-21
> **Updated:** 2026-07-21
> **Confidence:** high
> **Description:** --- source_url: file:///workspace/Projects/AI-Education-Pro/assets/js/app.js ingested: 2026-07-20 sha256: 67af6b17043ffac9571d0169a68bf7e3fd21d381fc5d3b08e6d74ceac2f9187c blog_source: local:unknown --...
> **Sources:**
>   - local-ai-education-proassetsjsappjs-2026-07-20.md
> **Links:**
- [[deploy]]
- [[add lesson]]
- [[daniel eks body scanning startup neko health raises another 700m]]
- [[apple intelligence approved for launch in china with alibabas qwen ai]]
- [[article]]

## Key Findings

---
source_url: file:///workspace/Projects/AI-Education-Pro/assets/js/app.js
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
'&': '&',
'': '>',
'"': '"',
"'": '''
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
Ласкаво просимо, ${escapeHTML(currentUser.nickname)}, бажаю успіху в навчанні!
[ document.getElementById('content-${nextLesson.id}')?.scrollIntoView({behavior:'smooth'}), 100)">
Продовжити: Урок ${nextLesson.id}. ${nextLesson.title}
- 
](#lessons-list)
Ваш прогрес
${completedCount} / ${totalCount}
${remainingCount > 0 ? `Залишилось: ${remainingCount}` : 'Курс завершено! 🎓'}
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
submitBtn.disabled = 

## Summary

false;
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
${l.id}
### ${l.title}
${isPassed ? 'Пройдено' : ''}
${isLocked ? '🔒' : ''}
${l.shortTheory}
▼
${isLocked ? '' : `
#### 📘 Базова теорія
${l.baseTheory}
#### 🎥 Медіа-матеріали
📊 Презентація
${l.videoUrl ? `📽️ Відеоогляд` : ''}
#### 🧠 Глибока теорія
${l.deepTheory}
#### 🛠️ Практичні завдання
${l.tasks.map(t => `- ✦ ${t}
`).join('')}
🚀 Запустити тестування
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
function checkCour

## Related Articles

- [[deploy]]
- [[add lesson]]
- [[daniel eks body scanning startup neko health raises another 700m]]
- [[apple intelligence approved for launch in china with alibabas qwen ai]]
- [[article]]
