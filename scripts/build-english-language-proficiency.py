#!/usr/bin/env python3
"""Build the English Language Proficiency interior page.

Source copy: https://admissions.umd.edu/apply/english-language-proficiency
Component rationale: briefs/english-language-proficiency.md

Run after editing this file, shared chrome, or the reusable rich-text table:
    python3 scripts/build-english-language-proficiency.py
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _chrome


REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(REPO, "page-builder", "TEMPLATE.html")
OUT = os.path.join(
    REPO, "pages", "how-to-apply", "english-language-proficiency.html"
)
TITLE = (
    "English Language Proficiency — Undergraduate Admissions | "
    "University of Maryland"
)


template = open(TEMPLATE, encoding="utf-8").read()
template_lines = template.split("\n")
critical_end = next(
    index for index, line in enumerate(template_lines) if line.strip() == "</style>"
)
head = _chrome.with_robots("\n".join(template_lines[:critical_end]))
head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head, count=1)

pin = re.search(r"web-components-library@([\d.]+)/dist/cdn\.js", template)
assert pin, "TEMPLATE.html has no web-components-library cdn.js pin"

body = r'''  </style>
  <script src="https://unpkg.com/@universityofmaryland/web-components-library@@@PIN@@/dist/cdn.js"></script>
@@CHROME:chrome-css@@
@@CHROME:gate@@
</head>
<body>
@@CHROME:header@@

  <main id="main-content">
    <section>
      <umd-element-hero-minimal data-theme="dark">
        <p slot="eyebrow">International Applicants</p>
        <img slot="image" src="../../images/shared/interior-hero-pattern.png" alt="" />
        <h1 slot="headline">English Language Proficiency</h1>
      </umd-element-hero-minimal>
    </section>

    <div class="umd-layout-space-horizontal-normal umd-layout-space-vertical-interior">
      <umd-element-breadcrumb>
        <div slot="paths">
          <a href="../../pages/" aria-label="Return Home"><span aria-hidden="true">Home</span></a>
          <a href="../../pages/how-to-apply/"><span>How To Apply</span></a>
          <a href="../../pages/how-to-apply/international-applicants.html"><span>International Applicants</span></a>
          <p aria-label="Current Page"><span>English Language Proficiency</span></p>
        </div>
      </umd-element-breadcrumb>
    </div>

    <div class="umd-layout-space-horizontal-normal">
      <div id="umd-shell-content">
        <section class="umd-layout-space-vertical-interior">
          <div class="umd-text-rich-advanced">
            <p class="umd-sans-large text-black">If you are a Domestic student and English is not your native language or you are an International student, you must provide the university with verification of your proficiency in English. We may consider waiving the English proficiency test requirement if a student has met certain requirements. Please read below to learn more about approved English proficiency exams and potential waivers.</p>
            <p>The Office of Undergraduate Admissions employs a holistic review process when considering all applicants and will consider all materials submitted in the application package to determine the level of English language proficiency.</p>
            <p>Please have an official report of your scores sent directly to the Office of Undergraduate Admissions by the <a href="https://admissions.umd.edu/apply/application-deadlines">appropriate deadline</a>. Submitted scores must be less than two years old.</p>
            <p>For the University of Maryland (UMD) to receive your scores, <strong>please use the reporting code 5814</strong>.</p>
          </div>
        </section>

        <section class="umd-layout-space-vertical-interior">
          <h2 class="umd-layout-space-vertical-interior-child text-black umd-sans-larger-bold">Accepted English Proficiency Tests:</h2>
          <div class="umd-layout-grid-gap-three umd-layout-grid-child-fill-height">
            <umd-element-card-overlay data-theme="light">
              <h3 slot="headline"><a href="https://englishtest.duolingo.com/applicants" target="_blank" rel="noopener">Duolingo English Test (DET)</a></h3>
              <div slot="text">
                <p>UMD accepts official scores from the <a href="https://englishtest.duolingo.com/applicants" target="_blank" rel="noopener">Duolingo English Test</a>, which can be taken online and on-demand. </p>
                <p>UMD passing score: 120</p>
                <p>Maryland English Institute score: 115 or lower</p>
              </div>
            </umd-element-card-overlay>
            <umd-element-card-overlay data-theme="light">
              <h3 slot="headline"><a href="http://www.ielts.org/" target="_blank" rel="noopener">International English Language Testing System (IELTS)</a></h3>
              <div slot="text">
                <p>UMD accepts official <a href="http://www.ielts.org/" target="_blank" rel="noopener">IELTS</a> and <a href="https://www.ielts.org/about-ielts/ielts-indicator" target="_blank" rel="noopener">IELTS Indicator</a> scores.</p>
                <p>UMD passing score: 7</p>
                <p>Maryland English Institute score: 6.5 or lower</p>
              </div>
            </umd-element-card-overlay>
            <umd-element-card-overlay data-theme="light">
              <h3 slot="headline"><a href="http://www.ets.org/toefl" target="_blank" rel="noopener">Test of English as a Foreign Language (TOEFL)</a></h3>
              <div slot="text">
                <p>UMD accepts official <a href="http://www.ets.org/toefl" target="_blank" rel="noopener">TOEFL</a> and <a href="https://www.ets.org/s/cv/toefl/at-home/" target="_blank" rel="noopener">TOEFL iBT</a>&nbsp;(Home Edition) scores. At this time, we are not accepting TOEFL superscores known as MyBest Scores. <br></p>
                <p>UMD passing score: 5 (1-6 point scale),  95 (0-120 point scale)<br><br>Maryland English Institute score: 4.5 or lower (1-6 point scale), 94 or lower (0-120 point scale)<br></p>
              </div>
            </umd-element-card-overlay>
          </div>
        </section>

        <section class="umd-layout-space-vertical-interior">
          <h2 class="umd-layout-space-vertical-interior-child text-black umd-sans-larger-bold">Potential Waivers for English Proficiency Requirement</h2>
          <div class="umd-text-rich-advanced">
            <p>While a passing English proficiency test score is the only absolute way a student can meet the English language proficiency requirement, we may consider waiving the English proficiency test requirement if a student has completed all elements of one of the following waivers by the application deadline:</p>
            <ul>
              <li>Four years at a U.S. high school or U.S. accredited high school without enrolling in any English as a Second Language coursework (ESL, ESOL, ELL, ELD, or other English Language Support coursework)</li>
              <li>Posted associate’s, bachelor’s or master’s degree earned from a regionally accredited U.S. institution</li>
              <li>Completed 55+ semester credits or 82.5 quarter credits from a regionally accredited U.S. institution with coursework equivalent to English Compositions 1 and 2</li>
              <li>English is your first language, you hold a citizenship and/or&nbsp;you have a completed high school or university degree earned from one of the following countries or territories:</li>
            </ul>
          </div>
        </section>

        <section class="umd-layout-space-vertical-interior">
          <h2 class="umd-layout-space-vertical-interior-child text-black umd-sans-larger-bold">English-speaking countries</h2>
          <div class="umd-layout-grid-gap-two umd-layout-space-vertical-interior-child">
              <div class="umd-text-rich-advanced">
                <hr>
                <ul>
                  <li>Antigua</li>
                  <li>Australia</li>
                  <li>Bahamas</li>
                  <li>Barbados</li>
                  <li>Belize</li>
                  <li>Bermuda</li>
                  <li>British Virgin Islands</li>
                  <li>Canada<sup>1</sup></li>
                  <li>Cayman Islands</li>
                  <li>Dominica</li>
                  <li>The Gambia</li>
                  <li>Ghana</li>
                  <li>Grenada</li>
                  <li>Guyana</li>
                  <li>Ireland</li>
                  <li>Jamaica</li>
                  <li>Kenya</li>
                </ul>
              </div>
              <div class="umd-text-rich-advanced">
                <hr>
                <ul>
                  <li>Montserrat</li>
                  <li>Namibia</li>
                  <li>New Zealand</li>
                  <li>Nigeria</li>
                  <li>Singapore</li>
                  <li>South Africa</li>
                  <li>St. Lucia</li>
                  <li>St. Vincent</li>
                  <li>Swaziland</li>
                  <li>Tanzania</li>
                  <li>Trinidad and Tobago</li>
                  <li>Turks and Caicos Islands</li>
                  <li>Uganda</li>
                  <li>United Kingdom</li>
                  <li>Zambia</li>
                  <li>Zimbabwe</li>
                </ul>
              </div>
          </div>
          <p class="umd-sans-smaller">1. English proficiency test is required for the French system only.</p>
        </section>

        <section class="umd-layout-space-vertical-interior">
          <h2 class="umd-layout-space-vertical-interior-child text-black umd-sans-larger-bold">Resources</h2>
          <div class="umd-layout-grid-gap-two">
            <umd-element-card-icon>
              <img slot="image" src="../../page-builder/images/icons/icon-link.svg" alt="" />
              <h3 slot="headline">
                <a href="https://marylandenglishinstitute.com/" target="_blank" rel="noopener">Maryland English Institute</a>
              </h3>
              <div slot="text">
                <p>The Maryland English Institute (MEI) provides English language instruction and assessment at the postsecondary level for speakers of other languages. MEI offers rigorous courses of study while providing a positive and supportive learning community and promoting cross-cultural understanding.</p>
                <p>In some cases, UMD applicants must complete coursework through MEI before beginning their degree program. Students are notified within their admission decision letter if this is required of them.</p>
              </div>
            </umd-element-card-icon>
          </div>
        </section>

        <section class="umd-layout-space-vertical-interior">
          <umd-element-banner-promo>
            <h2 slot="headline">There is a lot more to learn about UMD</h2>
            <p slot="text">Let's stay in touch! <a href="https://apply.umd.edu/register/request-info" target="_blank" rel="noopener">Join the Mailing List</a> or <a href="https://admissions.umd.edu/connect">Connect</a>!</p>
            <div slot="actions" class="banner-promo-actions">
              <umd-element-call-to-action data-display="primary">
                <a href="https://apply.umd.edu/register/request-info" target="_blank" rel="noopener">Join the List</a>
              </umd-element-call-to-action>
            </div>
          </umd-element-banner-promo>
        </section>

      </div>
    </div>
  </main>

@@CHROME:footer@@

  <script>
    customElements.whenDefined('umd-element-banner-promo').then(() => {
      document.querySelectorAll('umd-element-banner-promo').forEach(el => {
        const style = document.createElement('style');
        style.textContent = '.banner-promo-actions{display:flex!important;flex-direction:column!important;align-items:flex-end!important;gap:8px!important}';
        el.shadowRoot && el.shadowRoot.appendChild(style);
      });
    });
  </script>

@@CHROME:chrome-scripts@@
</body>
</html>
'''

body = body.replace("@@PIN@@", pin.group(1))
for key in ("chrome-css", "gate", "header", "footer", "chrome-scripts"):
    body = body.replace(f"@@CHROME:{key}@@", _chrome.block(key, OUT))

output = head + "\n" + body
assert "@@" not in output, "unreplaced build token"
assert output.count("<umd-element-hero-minimal") == 1
assert "<umd-element-hero " not in output
assert 'src="../../images/shared/interior-hero-pattern.png" alt=""' in output
assert output.count("<umd-element-card-overlay") == 3
assert "<umd-element-accordion-item" not in output
assert 'data-visual-open="true"' not in output
assert "<umd-element-pathway" not in output
assert output.count("umd-element-banner-promo") >= 1
assert "Let's stay in touch! <a href=\"https://apply.umd.edu/register/request-info\"" in output
assert output.count('href="https://apply.umd.edu/register/request-info"') == 2
assert '>Join the List</a>' in output
assert '>Join the Mailing List</a> or <a href="https://admissions.umd.edu/connect">Connect</a>!' in output
banner_start = output.index("<umd-element-banner-promo>")
shell_start = output.index('<div id="umd-shell-content"')
shell_end = output.index("</div>\n    </div>\n  </main>", shell_start)
assert shell_start < banner_start < shell_end
countries_heading = '<h2 class="umd-layout-space-vertical-interior-child text-black umd-sans-larger-bold">English-speaking countries</h2>'
assert output.count(countries_heading) == 1
countries_start = output.index(countries_heading)
countries_end = output.index("</section>", countries_start)
countries_markup = output[countries_start:countries_end]
assert '<div class="umd-layout-grid-gap-two umd-layout-space-vertical-interior-child">' in countries_markup
assert countries_markup.count('<div class="umd-text-rich-advanced">') == 2
assert countries_markup.count("<hr>") == 2
assert countries_markup.count("<li>") == 33
assert '<p class="umd-sans-smaller">1. English proficiency test is required for the French system only.</p>' in countries_markup
waivers_start = output.index("Potential Waivers for English Proficiency Requirement")
assert "</section>" in output[waivers_start:countries_start]
resources_heading = '<h2 class="umd-layout-space-vertical-interior-child text-black umd-sans-larger-bold">Resources</h2>'
assert output.count(resources_heading) == 1
resources_start = output.index(resources_heading)
resources_end = output.index("</section>", resources_start)
resources_markup = output[resources_start:resources_end]
assert '<div class="umd-layout-grid-gap-two">' in resources_markup
assert resources_markup.count("<umd-element-card-icon>") == 1
assert 'src="../../page-builder/images/icons/icon-link.svg" alt=""' in resources_markup
assert '<h3 slot="headline">' in resources_markup
assert 'href="https://marylandenglishinstitute.com/" target="_blank" rel="noopener">Maryland English Institute</a>' in resources_markup
assert "Students are notified within their admission decision letter" in resources_markup
assert "mei-resource-" not in output
assert "<table" not in output
assert "rich-text-table.css" not in output
# The page lede is a PARAGRAPH, not a heading. umd-sans-large gives it 18px/700
# in place; wrapping a multi-sentence lede in <h2> puts a paragraph in the
# document outline and makes screen-reader heading navigation announce the whole
# thing. Matches tuition/frederick-douglass-scholarship.html.
assert '<p class="umd-sans-large text-black">' in output
assert '<h2 class="umd-sans-large' not in output
assert '<html lang="en">' in output
assert (
    f"web-components-library@{pin.group(1)}/dist/cdn.js" in output
), "generated component CDN URL is missing its version separator"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as handle:
    handle.write(output)

print(os.path.relpath(OUT, REPO))
