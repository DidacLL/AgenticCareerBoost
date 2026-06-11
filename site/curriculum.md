---
layout: default
title: "Curriculum - Dídac Llorens"
description: "Configurable curriculum for Dídac Llorens with ML/Data, agentic systems, backend, and print views."
extra_js:
  - /assets/js/cv.js
---

<div class="hero slim">
  <div>
    <div class="eyebrow">Configurable CV</div>
    <h1>Curriculum</h1>
    <p class="lead">Current view: <strong data-current-view>Agentic systems</strong>. Use URL parameters directly: <code>?view=ml</code>, <code>?view=agentic</code>, <code>?view=backend</code>, or <code>?view=print</code>.</p>
    <div class="actions">
      <a class="button primary" href="https://github.com/DidacLL/AgenticCareerBoost/raw/main/content/reports/build/didac-llorens-cv.pdf">Download PDF CV</a>
      <a class="button" href="https://github.com/DidacLL/AgenticCareerBoost">Inspect Repository</a>
    </div>
  </div>
</div>

<div class="cv-toolbar no-print" aria-label="CV view selector">
  <div class="segmented">
    <button type="button" data-cv-view="ml">ML/Data</button>
    <button type="button" data-cv-view="agentic">Agentic</button>
    <button type="button" data-cv-view="backend">Backend</button>
    <button type="button" data-cv-view="print">Print</button>
  </div>
  <p class="cv-note">Unknown view parameters fall back to the agentic systems view.</p>
</div>

<section>
  <h2>Profile</h2>
  <p data-views="ml print">Software Engineering student at UOC specializing in Machine Learning and Artificial Intelligence, expected February 2027. Current public evidence combines ML/data direction with agentic workflow systems, technical reporting, and regulated-domain operations experience.</p>
  <p data-views="agentic print">Software Engineering student at UOC building a public, inspectable agentic workflow system for career evidence, static site delivery, project traceability, and formal technical reports.</p>
  <p data-views="backend print">Software Engineering student with Java/Spring Boot backend evidence, LaTeX/tooling depth, and 15 years of banking and insurance operations before engineering.</p>
</section>

<section>
  <h2>Target Roles</h2>
  <div class="tag-list" data-views="ml print">
    <span class="tag">ML Engineering</span><span class="tag">Data Engineering</span><span class="tag">AI Tooling</span><span class="tag">Research Engineering</span><span class="tag">Regulated-domain data</span>
  </div>
  <div class="tag-list" data-views="agentic print">
    <span class="tag">Agentic AI</span><span class="tag">Workflow Systems</span><span class="tag">Platform / Tooling</span><span class="tag">Technical Documentation</span><span class="tag">Research Engineering</span>
  </div>
  <div class="tag-list" data-views="backend print">
    <span class="tag">Backend Engineering</span><span class="tag">Java</span><span class="tag">Spring Boot</span><span class="tag">Platform / Tooling</span><span class="tag">Regulated-domain systems</span>
  </div>
</section>

<section>
  <h2>Selected Evidence</h2>
  <div class="grid">
    <article class="card" data-views="agentic ml print">
      <h3>AgenticCareerBoost</h3>
      <p>Path-based, model-agnostic agentic system with role contracts, workflow routing, status surfaces, public reports, and this Jekyll site.</p>
      <p><a href="{{ '/projects/agentic-career-boost/' | relative_url }}">Project page</a> · <a href="https://github.com/DidacLL/AgenticCareerBoost">Repository</a></p>
    </article>
    <article class="card" data-views="agentic backend print">
      <h3>P3CTeX</h3>
      <p>Custom LaTeX document class and package ecosystem. Evidence of tooling depth, technical writing, package design, and buildable documentation.</p>
      <p><a href="{{ '/projects/p3ctex/' | relative_url }}">Project page</a> · <a href="https://github.com/DidacLL/P3CTeX">Repository</a></p>
    </article>
    <article class="card" data-views="backend print">
      <h3>IronBank</h3>
      <p>Older Java/Spring Boot banking simulation from IronHack. Useful backend evidence and a natural bridge from banking operations to software systems.</p>
      <p><a href="{{ '/projects/ironbank/' | relative_url }}">Project page</a> · <a href="https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys">Repository</a></p>
    </article>
  </div>
</section>

<section>
  <h2>Technical Stack</h2>
  <p data-views="ml print"><strong>ML/Data emphasis:</strong> Python learning path, SQL, data quality, ML/AI specialization, technical reporting, Git/GitHub, and regulated-domain process context.</p>
  <p data-views="agentic print"><strong>Agentic systems emphasis:</strong> Markdown contracts, Jekyll, LaTeX reports, GitHub Actions, workflow design, static status surfaces, JavaScript, and repo-first documentation.</p>
  <p data-views="backend print"><strong>Backend emphasis:</strong> Java, Spring Boot, REST APIs, Maven, SQL, Git, Linux, authentication context, and microservice-oriented capstone work.</p>
</section>

<section>
  <h2>Education</h2>
  <table>
    <thead><tr><th>Institution</th><th>Program</th></tr></thead>
    <tbody>
      <tr><td>Universitat Oberta de Catalunya</td><td>Software Engineering, ML/AI specialization, expected February 2027</td></tr>
      <tr><td>IronHack</td><td>Java Backend Development bootcamp</td></tr>
      <tr><td>Additional training</td><td>Android/Kotlin, FullStack React, Linux administration</td></tr>
    </tbody>
  </table>
</section>

<section>
  <h2>Operations Background</h2>
  <p>15 years in customer-facing banking and insurance operations: team leadership, case triage, regulated processes, stakeholder communication, and high-volume problem resolution. Engineering relevance: data quality, compliance awareness, failure-mode thinking, audit trails, and systems that survive operational pressure.</p>
</section>

<section>
  <h2>Contact</h2>
  <p>Barcelona. LinkedIn: <a href="https://www.linkedin.com/in/didacllorens/">linkedin.com/in/didacllorens</a>. GitHub: <a href="https://github.com/DidacLL">github.com/DidacLL</a>.</p>
</section>
