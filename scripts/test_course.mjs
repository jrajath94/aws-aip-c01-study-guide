import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {chromium} from 'playwright';
const root=new URL('../',import.meta.url).pathname;
const browser=await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
const page=await browser.newPage({viewport:{width:1440,height:1100}});const errors=[];page.on('pageerror',e=>errors.push(e.message));
await page.goto('file://'+root+'course/reader.html');await page.waitForFunction(()=>window.COURSE_APP);await page.evaluate(()=>document.fonts.ready);
const counts=await page.evaluate(()=>({core:COURSE.core.length,refs:COURSE.references.length,quiz:COURSE.quizzes.length,skills:COURSE.skills.length}));assert.equal(counts.skills,98);assert.equal(counts.quiz,250);
const results=[];
for(const [mode,list] of [['core','core'],['references','references'],['services','services'],['quizzes','quizzes'],['recalls','recalls'],['skills','skills']]){
 const ids=await page.evaluate(key=>COURSE[key].map(x=>x.id),list);
 for(const id of ids){
  const result=await page.evaluate(({id,mode})=>{COURSE_APP.go(id,mode);const main=document.querySelector('main');return {id,mode,title:!!document.querySelector('#slide h1'),horizontal:document.documentElement.scrollWidth>innerWidth,body:document.querySelector('#slide').textContent.length};},{id,mode});
  assert(result.title,result.id+' title');assert(!result.horizontal,result.id+' horizontal overflow');assert(result.body>20,result.id+' empty');results.push(result);
 }
}
await page.evaluate(()=>COURSE_APP.go('core-006','core'));assert.equal(await page.locator('.flow li.pending').count(),3);await page.click('#flow-next');assert.equal(await page.locator('.flow li.pending').count(),2);await page.click('#flow-all');assert.equal(await page.locator('.flow li.pending').count(),0);
await page.screenshot({path:root+'.build/course-rag.png',fullPage:true});
await page.evaluate(()=>COURSE_APP.go(COURSE.quizzes[0].id,'quizzes'));const correct=await page.evaluate(()=>COURSE.quizzes[0].options.findIndex(o=>o.correct));await page.locator('.options input').nth(correct).check();await page.click('#check-answer');assert((await page.locator('#feedback').innerText()).includes('Correct against the source key.'));
await page.screenshot({path:root+'.build/course-quiz.png',fullPage:true});
await page.fill('#search','1.5.4');assert((await page.locator('#list button').count())>0);await page.fill('#search','');
await page.evaluate(()=>COURSE_APP.go(COURSE.mock[0],'mock'));await page.click('#start-mock');assert((await page.locator('#timer').innerText()).startsWith('3:')||(await page.locator('#timer').innerText()).startsWith('2:'));await page.click('#finish-mock');assert((await page.locator('#slide').innerText()).includes('Mock results'));
await page.evaluate(()=>COURSE_APP.go('core-001','core'));await page.click('#weak');assert.equal(await page.locator('#weak').getAttribute('aria-pressed'),'true');await page.reload();assert.equal(await page.locator('#weak').getAttribute('aria-pressed'),'true');
await page.setViewportSize({width:390,height:844});await page.screenshot({path:root+'.build/course-mobile.png',fullPage:true});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
await page.click('#menu');assert.equal(await page.locator('#menu').getAttribute('aria-expanded'),'true');
assert.deepEqual(errors,[]);await fs.writeFile(root+'audits/browser-tests.json',JSON.stringify({counts,viewsChecked:results.length,errors,checks:['Every core, reference, service, quiz, recall, and skill view rendered.','No horizontal document overflow at desktop size.','Progress persisted across reload.','Diagram stage controls worked.','Correct source answer scored correctly.','Mock timer and result mode worked.','Search by skill ID returned results.','Mobile menu and page width worked.'],limits:['Automated layout checks and sampled visual review do not validate every inherited fact.','PowerPoint desktop was not used in this test.']},null,2));await browser.close();console.log('PASS',results.length,'view states');
