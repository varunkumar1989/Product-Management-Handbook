# Functional test report

Automated run in Microsoft Edge (headless, Playwright) against the local `file://` site.

**28 of 28 checks passed.**

| Check | Result | Detail |
|---|---|---|
| All site pages load without JavaScript errors | PASS |  |
| Dashboard lists 12 module cards | PASS | 12 cards |
| Dashboard shows current focus | PASS |  |
| Search returns results for 'contribution margin' | PASS | 12 hits |
| Clicking a search result navigates to the target page | PASS | m07.html#m07-unit-economics-contribution-margin-cac-ltv-payback |
| '/' focuses the search box | PASS |  |
| Theme toggle changes the page background | PASS | rgb(255, 255, 255) → rgb(11, 18, 32) |
| Theme choice persists after reload | PASS |  |
| Quiz marks a correct answer | PASS |  |
| Quiz reveals the explanation | PASS |  |
| Quiz shows a running score | PASS | Score: 1 / 7 (1 answered) |
| Marking a module complete updates the sidebar indicator | PASS |  |
| Overall progress counter updates | PASS |  |
| 'Expand all' opens every collapsible answer | PASS | 0 still closed |
| Framework library category filter works | PASS | 7 visible after 'Prioritization' |
| Interview page text filter narrows the list | PASS | 8 sets match 'RAG' |
| Interview handbook contains ≥ 100 questions | PASS | 106 questions |
| Model answers expand on click | PASS |  |
| Glossary search filters terms | PASS | 1 of 175 shown for 'idempot' |
| Templates page offers downloadable files | PASS | 22 download links |
| All template/dataset download links resolve to files | PASS |  |
| Module page links to its PDF and the file exists | PASS | pdf/Module-07-Analytics.pdf |
| Back-to-top button appears after scrolling | PASS |  |
| Back-to-top returns to the top | PASS | scrollY=48 |
| Quiz options are keyboard-focusable | PASS |  |
| No horizontal page scroll at 375 px width | PASS |  |
| Sidebar hidden on mobile until the menu is opened | PASS |  |
| Menu button opens the sidebar on mobile | PASS |  |