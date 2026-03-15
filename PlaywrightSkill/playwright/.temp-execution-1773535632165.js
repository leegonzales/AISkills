const { chromium } = require('playwright');

const TARGET_URL = 'http://localhost:3001';
const PASS = '✅';
const FAIL = '❌';
const INFO = 'ℹ️';

let passed = 0;
let failed = 0;
const failures = [];

function assert(condition, testName) {
    if (condition) {
        console.log(`${PASS} ${testName}`);
        passed++;
    } else {
        console.log(`${FAIL} ${testName}`);
        failed++;
        failures.push(testName);
    }
}

(async () => {
    const browser = await chromium.launch({ headless: false, slowMo: 50 });
    const page = await browser.newPage();
    page.setDefaultTimeout(10000);

    try {
        // ============================================
        // TEST 1: Landing Page
        // ============================================
        console.log('\n--- TEST 1: Landing Page ---');

        const response = await page.goto(TARGET_URL, { waitUntil: 'networkidle' });
        assert(response.ok(), 'Landing page loads with 200');

        const title = await page.title();
        assert(title.includes('RANGE') || title.includes('Fluency'), `Page title contains RANGE or Fluency: "${title}"`);

        // Check hero section
        const heroHeading = await page.textContent('h1');
        assert(heroHeading && heroHeading.includes('RANGE'), `Hero heading contains RANGE: "${heroHeading}"`);

        // Check RANGE dimension cards
        const dimensionCards = await page.locator('[class*="border"][class*="bg-surface"]').count();
        assert(dimensionCards >= 5, `At least 5 dimension cards rendered: found ${dimensionCards}`);

        // Check for R, A, N, G, E letters
        const pageText = await page.textContent('body');
        for (const dim of ['Reach', 'Autonomy', 'Navigation', 'Generalization', 'Execution Fidelity']) {
            assert(pageText.includes(dim), `Dimension "${dim}" visible on landing page`);
        }

        // Check CTA button exists
        const ctaButton = page.locator('a[href="/assess"]');
        const ctaCount = await ctaButton.count();
        assert(ctaCount >= 1, `CTA button to /assess exists: found ${ctaCount}`);

        // Check assessment info text
        assert(pageText.includes('25 questions'), 'Assessment info shows "25 questions"');
        assert(pageText.includes('5 minutes'), 'Assessment info shows "5 minutes"');

        // Screenshot landing page
        await page.screenshot({ path: '/tmp/range-01-landing.png', fullPage: true });
        console.log(`${INFO} Screenshot: /tmp/range-01-landing.png`);

        // ============================================
        // TEST 2: API - Session Creation
        // ============================================
        console.log('\n--- TEST 2: API - Session Creation ---');

        const sessionRes = await page.request.post(`${TARGET_URL}/api/session`);
        assert(sessionRes.ok(), 'POST /api/session returns 200');

        const sessionData = await sessionRes.json();
        assert(typeof sessionData.sessionId === 'string' && sessionData.sessionId.length > 0, `Session ID returned: ${sessionData.sessionId.substring(0, 8)}...`);
        assert(sessionData.totalQuestions === 25, `Total questions is 25: got ${sessionData.totalQuestions}`);

        const sessionId = sessionData.sessionId;

        // ============================================
        // TEST 3: API - Question Fetching
        // ============================================
        console.log('\n--- TEST 3: API - Question Fetching ---');

        const q1Res = await page.request.get(`${TARGET_URL}/api/questions?sessionId=${sessionId}`);
        assert(q1Res.ok(), 'GET /api/questions returns 200');

        const q1Data = await q1Res.json();
        assert(q1Data.question && typeof q1Data.question.id === 'number', `Question object returned with id: ${q1Data.question?.id}`);
        assert(q1Data.question && typeof q1Data.question.text === 'string', 'Question has text field');
        assert(q1Data.question && q1Data.question.correctAnswer === undefined, 'correctAnswer is NOT exposed to client');
        assert(q1Data.question && ['reach', 'autonomy', 'navigation', 'generalization', 'execution_fidelity'].includes(q1Data.question.rangeDimension), `Valid RANGE dimension: ${q1Data.question?.rangeDimension}`);
        assert(q1Data.progress && q1Data.progress.current === 1, `Progress current is 1: got ${q1Data.progress?.current}`);
        assert(q1Data.progress && q1Data.progress.total === 25, `Progress total is 25: got ${q1Data.progress?.total}`);

        // ============================================
        // TEST 4: API - Answer Submission
        // ============================================
        console.log('\n--- TEST 4: API - Answer Submission ---');

        const answerRes = await page.request.post(`${TARGET_URL}/api/questions`, {
            data: { sessionId, questionId: q1Data.question.id, answer: true }
        });
        assert(answerRes.ok(), 'POST /api/questions (submit answer) returns 200');

        const answerData = await answerRes.json();
        assert(answerData.accepted === true, 'Answer accepted');
        assert(answerData.progress && answerData.progress.current === 2, `Progress advanced to 2: got ${answerData.progress?.current}`);

        // ============================================
        // TEST 5: API - Complete Full Assessment
        // ============================================
        console.log('\n--- TEST 5: API - Complete Full Assessment ---');

        // Answer remaining 24 questions
        let shareId = null;
        for (let i = 2; i <= 25; i++) {
            // Small delay to avoid rate limiting
            await new Promise(r => setTimeout(r, 120));

            // Get next question
            const qRes = await page.request.get(`${TARGET_URL}/api/questions?sessionId=${sessionId}`);
            const qData = await qRes.json();

            if (qData.complete) {
                shareId = qData.shareId;
                break;
            }

            // Small delay before POST
            await new Promise(r => setTimeout(r, 120));

            // Submit answer (alternate true/false for variety)
            let aRes = await page.request.post(`${TARGET_URL}/api/questions`, {
                data: { sessionId, questionId: qData.question.id, answer: i % 2 === 0 }
            });

            // Retry once if rate limited
            if (aRes.status() === 429) {
                await new Promise(r => setTimeout(r, 200));
                aRes = await page.request.post(`${TARGET_URL}/api/questions`, {
                    data: { sessionId, questionId: qData.question.id, answer: i % 2 === 0 }
                });
            }

            const aData = await aRes.json();

            if (aData.complete) {
                shareId = aData.shareId;
                break;
            }
        }

        assert(shareId !== null && typeof shareId === 'string', `Assessment completed with shareId: ${shareId?.substring(0, 8)}...`);

        // ============================================
        // TEST 6: API - Results Retrieval
        // ============================================
        console.log('\n--- TEST 6: API - Results Retrieval ---');

        if (shareId) {
            const resultsRes = await page.request.get(`${TARGET_URL}/api/results?id=${shareId}`);
            assert(resultsRes.ok(), 'GET /api/results?id=xxx returns 200');

            const results = await resultsRes.json();
            assert(typeof results.totalScore === 'number', `Total score is number: ${results.totalScore}`);
            assert(results.totalQuestions === 25, `Total questions is 25: ${results.totalQuestions}`);
            assert(typeof results.percentage === 'number', `Percentage is number: ${results.percentage}`);
            assert(['novice', 'advanced-beginner', 'competent', 'proficient', 'expert'].includes(results.fluencyTier), `Valid fluency tier: ${results.fluencyTier}`);

            // Check RANGE scores
            assert(results.rangeScores && typeof results.rangeScores.reach === 'object', 'Reach score exists');
            assert(results.rangeScores && typeof results.rangeScores.autonomy === 'object', 'Autonomy score exists');
            assert(results.rangeScores && typeof results.rangeScores.navigation === 'object', 'Navigation score exists');
            assert(results.rangeScores && typeof results.rangeScores.generalization === 'object', 'Generalization score exists');
            assert(results.rangeScores && typeof results.rangeScores.execution_fidelity === 'object', 'Execution Fidelity score exists');

            // Check category scores
            assert(results.categoryScores && Object.keys(results.categoryScores).length > 0, `Category scores present: ${Object.keys(results.categoryScores).join(', ')}`);

            // Check dynamic route also works
            const dynamicRes = await page.request.get(`${TARGET_URL}/api/results/${shareId}`);
            assert(dynamicRes.ok(), 'GET /api/results/[id] dynamic route returns 200');

            // Test 404 for invalid share ID
            const badRes = await page.request.get(`${TARGET_URL}/api/results?id=nonexistent`);
            assert(badRes.status() === 404, 'Invalid shareId returns 404');
        }

        // ============================================
        // TEST 7: UI - Assessment Flow
        // ============================================
        console.log('\n--- TEST 7: UI - Assessment Flow ---');

        await page.goto(`${TARGET_URL}/assess`, { waitUntil: 'networkidle' });

        // Wait for loading to finish and first question to appear
        await page.waitForSelector('button:has-text("True")', { timeout: 10000 });
        await page.screenshot({ path: '/tmp/range-02-first-question.png', fullPage: true });
        console.log(`${INFO} Screenshot: /tmp/range-02-first-question.png`);

        // Check question card elements
        const questionText = await page.locator('p.text-xl, p.text-lg').first().textContent();
        assert(questionText && questionText.length > 10, `Question text visible: "${questionText?.substring(0, 50)}..."`);

        // Check True/False buttons exist
        const trueBtn = page.locator('button:has-text("True")');
        const falseBtn = page.locator('button:has-text("False")');
        assert(await trueBtn.count() > 0, 'True button exists');
        assert(await falseBtn.count() > 0, 'False button exists');

        // Check progress indicator
        const progressText = await page.textContent('body');
        assert(progressText.includes('1') && progressText.includes('25'), 'Progress shows question count');

        // Answer first question
        await trueBtn.click();
        await page.waitForTimeout(500);

        // Check progress advanced
        const updatedText = await page.textContent('body');
        assert(updatedText.includes('2') || updatedText.includes('of 25'), 'Progress advanced after answering');

        await page.screenshot({ path: '/tmp/range-03-second-question.png', fullPage: true });
        console.log(`${INFO} Screenshot: /tmp/range-03-second-question.png`);

        // Answer remaining questions quickly
        for (let i = 2; i <= 25; i++) {
            try {
                const btn = i % 2 === 0
                    ? page.locator('button:has-text("True")')
                    : page.locator('button:has-text("False")');
                await btn.waitFor({ timeout: 5000 });
                await btn.click();
                await page.waitForTimeout(300);
            } catch {
                // Might have already redirected to results
                break;
            }
        }

        // Should redirect to results page
        await page.waitForURL('**/results/**', { timeout: 15000 });
        const resultsUrl = page.url();
        assert(resultsUrl.includes('/results/'), `Redirected to results page: ${resultsUrl}`);

        // ============================================
        // TEST 8: UI - Results Page
        // ============================================
        console.log('\n--- TEST 8: UI - Results Page ---');

        await page.waitForSelector('h1', { timeout: 10000 });
        await page.waitForTimeout(1500); // Wait for animations

        await page.screenshot({ path: '/tmp/range-04-results.png', fullPage: true });
        console.log(`${INFO} Screenshot: /tmp/range-04-results.png`);

        const resultsPageText = await page.textContent('body');

        // Check tier card
        const hasTier = ['NOVICE', 'ADVANCED BEGINNER', 'COMPETENT', 'PROFICIENT', 'EXPERT'].some(t => resultsPageText.includes(t));
        assert(hasTier, 'Fluency tier displayed on results page');

        // Check radar chart (SVG)
        const svgCount = await page.locator('svg').count();
        assert(svgCount >= 1, `Radar chart SVG rendered: ${svgCount} SVG elements found`);

        // Check polygon in radar chart
        const polygonCount = await page.locator('svg polygon').count();
        assert(polygonCount >= 2, `Radar chart has polygons (outer + inner): found ${polygonCount}`);

        // Check RANGE dimension labels in chart
        const svgText = await page.locator('svg').first().textContent();
        for (const letter of ['R', 'A', 'N', 'G', 'E']) {
            assert(svgText.includes(letter), `Radar chart shows dimension "${letter}"`);
        }

        // Check dimension breakdown
        assert(resultsPageText.includes('RANGE Dimensions'), 'Dimension breakdown section visible');
        assert(resultsPageText.includes('Reach'), 'Reach dimension in breakdown');
        assert(resultsPageText.includes('Autonomy'), 'Autonomy dimension in breakdown');

        // Check category breakdown
        assert(resultsPageText.includes('Knowledge Categories'), 'Category breakdown section visible');

        // Check share section
        assert(resultsPageText.includes('Share'), 'Share section visible');

        // Check CTA
        assert(resultsPageText.includes('improve') || resultsPageText.includes('RANGE'), 'CTA section visible');

        // Check copy button
        const copyBtn = page.locator('button:has-text("Copy")');
        assert(await copyBtn.count() > 0, 'Copy URL button exists');

        // ============================================
        // TEST 9: API Security
        // ============================================
        console.log('\n--- TEST 9: API Security ---');

        // Test missing sessionId
        const noSessionRes = await page.request.get(`${TARGET_URL}/api/questions`);
        assert(noSessionRes.status() === 400, 'Missing sessionId returns 400');

        // Test invalid sessionId
        const badSessionRes = await page.request.get(`${TARGET_URL}/api/questions?sessionId=invalid`);
        assert(badSessionRes.status() === 404, 'Invalid sessionId returns 404');

        // Test missing answer fields
        const badAnswerRes = await page.request.post(`${TARGET_URL}/api/questions`, {
            data: { sessionId: 'invalid' }
        });
        assert(badAnswerRes.status() === 400 || badAnswerRes.status() === 404, 'Incomplete answer returns 400 or 404');

        // ============================================
        // TEST 10: Responsive Design
        // ============================================
        console.log('\n--- TEST 10: Responsive Design ---');

        // Mobile viewport
        await page.setViewportSize({ width: 375, height: 667 });
        await page.goto(TARGET_URL, { waitUntil: 'networkidle' });
        await page.waitForTimeout(500);
        await page.screenshot({ path: '/tmp/range-05-mobile-landing.png', fullPage: true });
        console.log(`${INFO} Screenshot: /tmp/range-05-mobile-landing.png`);

        // Check CTA is still visible on mobile
        const mobileCta = page.locator('a[href="/assess"]');
        assert(await mobileCta.count() >= 1, 'CTA button visible on mobile');

        // Tablet viewport
        await page.setViewportSize({ width: 768, height: 1024 });
        await page.goto(TARGET_URL, { waitUntil: 'networkidle' });
        await page.waitForTimeout(500);
        await page.screenshot({ path: '/tmp/range-06-tablet-landing.png', fullPage: true });
        console.log(`${INFO} Screenshot: /tmp/range-06-tablet-landing.png`);

        // Reset to desktop
        await page.setViewportSize({ width: 1280, height: 800 });

    } catch (error) {
        console.log(`\n${FAIL} UNEXPECTED ERROR: ${error.message}`);
        console.log(error.stack);
        failed++;
        failures.push(`Unexpected error: ${error.message}`);
        await page.screenshot({ path: '/tmp/range-error.png', fullPage: true });
        console.log(`${INFO} Error screenshot: /tmp/range-error.png`);
    } finally {
        // ============================================
        // SUMMARY
        // ============================================
        console.log('\n========================================');
        console.log(`RESULTS: ${passed} passed, ${failed} failed`);
        console.log('========================================');
        if (failures.length > 0) {
            console.log('\nFailures:');
            failures.forEach(f => console.log(`  ${FAIL} ${f}`));
        }

        await browser.close();
    }
})();
