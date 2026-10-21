import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import { chromium } from 'playwright';

const root = new URL('../', import.meta.url).pathname;
const browser = await chromium.launch({
  headless: true,
  executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
});

const page = await browser.newPage({ viewport: { width: 1440, height: 960 } });
const errors = [];
page.on('pageerror', e => errors.push(e.message));
page.on('requestfailed', req => errors.push(req.url()));

console.log('Navigating to course/index.html...');
await page.goto('file://' + root + 'course/index.html');
await page.waitForFunction(() => window.COURSE_APP);
await page.evaluate(() => document.fonts.ready);

// 1. Verify Core Counts
const counts = await page.evaluate(() => ({
  core: COURSE.core.length,
  quizzes: COURSE.quizzes.length,
  skills: COURSE.skills.length,
  mock: COURSE.mock.length,
  recalls: COURSE.recalls.length
}));
console.log('Course Data Counts:', counts);
assert.equal(counts.skills, 98, 'All 98 skills must be mapped');
assert.equal(counts.mock, 75, 'Mock must have 75 questions');
assert.equal(counts.quizzes, 250, 'Quizzes must have 250 questions');

// 2. Test Slide Deck Mode
console.log('Testing Slide Deck Mode & Russian Doll Layers...');
await page.evaluate(() => COURSE_APP.selectItem('core-005')); // Tokens, context, and inference
assert.equal(await page.textContent('.slide-main-title'), 'Tokens, context, and inference');
assert.ok(await page.locator('.diagram-figure-wrapper img').count() > 0, 'Diagram image must exist');

// Test Russian doll tabs
await page.click('#btn-layer-architecture');
let layerText = await page.textContent('.rd-layer-body');
assert.ok(layerText.length > 20, 'Architecture layer must have content');

await page.click('#btn-layer-api');
layerText = await page.textContent('.rd-layer-body');
assert.ok(layerText.includes('converse') || layerText.includes('maxTokens') || layerText.includes('inferenceConfig') || layerText.length > 20);

await page.click('#btn-layer-traps');
layerText = await page.textContent('.rd-layer-body');
assert.ok(layerText.length > 20);

await page.click('#btn-layer-rule');
layerText = await page.textContent('.rd-layer-body');
assert.ok(layerText.length > 20);

// Capture Slide Deck Screenshot
await page.screenshot({ path: root + '.build/aip-slide-deck.png' });
console.log('Saved Slide Deck screenshot: .build/aip-slide-deck.png');

// 3. Test Linked Quiz Drawer
console.log('Testing Linked Quiz Drawer...');
await page.click('#btn-open-linked-quiz');
assert.equal(await page.locator('#quiz-drawer').isVisible(), true, 'Quiz drawer must open');
await page.screenshot({ path: root + '.build/aip-quiz-drawer.png' });
await page.click('#quiz-drawer-close');
assert.equal(await page.locator('#quiz-drawer').isVisible(), false, 'Quiz drawer must close');

// 4. Test Lightbox
console.log('Testing Diagram Lightbox...');
await page.click('#btn-zoom-main');
assert.equal(await page.locator('#diagram-lightbox').isVisible(), true, 'Lightbox must open');
await page.screenshot({ path: root + '.build/aip-lightbox.png' });
await page.click('#lightbox-close');
assert.equal(await page.locator('#diagram-lightbox').isVisible(), false, 'Lightbox must close');

// 5. Test Visual Treatise Mode
console.log('Testing Visual Treatise Mode...');
await page.click('.mode-tab[data-mode="treatise"]');
assert.ok(await page.locator('.treatise-container').count() > 0, 'Treatise container must render');
assert.ok(await page.locator('.treatise-section-card').count() >= 90, 'All treatise sections must render');
await page.screenshot({ path: root + '.build/aip-visual-treatise.png' });
console.log('Saved Visual Treatise screenshot: .build/aip-visual-treatise.png');

// 6. Test Practice Quiz Bank
console.log('Testing Practice Question Bank Mode...');
await page.click('.mode-tab[data-mode="quizzes"]');
assert.ok(await page.locator('.quiz-card').count() > 0, 'Quiz card must render');
// Pick an option and check
await page.locator('.quiz-option-label').first().click();
await page.click('#btn-check-quiz');
assert.ok(await page.locator('.quiz-feedback-box').isVisible(), 'Feedback box must appear');
await page.screenshot({ path: root + '.build/aip-question-bank.png' });

// 7. Test Timed Mock Exam Mode
console.log('Testing Mock Exam Mode...');
await page.click('.mode-tab[data-mode="mock"]');
await page.click('#btn-start-mock');
const timerText = await page.textContent('#timer-display');
console.log('Mock Timer Active:', timerText);
assert.ok(timerText.includes(':'), 'Timer must show formatted countdown');

// 8. Test Recall Cards
console.log('Testing Recall Cards Mode...');
await page.click('.mode-tab[data-mode="recalls"]');
assert.ok(await page.locator('.recall-accordion').count() > 0);

// 9. Test Skills Map
console.log('Testing 98-Skill Map Mode...');
await page.click('.mode-tab[data-mode="skills"]');
assert.ok(await page.locator('.teaching-points-box').count() > 0);

// Final assertion: Zero errors throughout all mode transitions!
console.log('Recorded Errors:', errors);
assert.deepEqual(errors, []);

await browser.close();
console.log('ALL AUDITS & VISUAL CHECKS PASSED WITH 100% SUCCESS!');
