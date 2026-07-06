# Executive Summary

Our review found that the S005 agentic pipeline achieved better privacy safeguards but stalled on actual writing.  Recent rule fixes (e.g. **sealed-context** privacy boundaries) correctly treat every agentic hand-off as a potential leak.  However, the workflow remains fixated on internal architecture: agents keep producing planning cards instead of final posts.  In practice, this meant one LLM instance generated multiple variations of the *same* outline, yielding AI‐sounding symmetry and missing the human-authorship tone we wanted.  The solution is to shift from planning to **content generation**: spawn independent writer agents (each with fresh context) to break formulaic patterns, interpose adversarial reviewers before any draft is saved, and expose only a concise decision surface to the user.  We will delete the ephemeral S005 planning docs (they were never meant for publication) and focus on a multi-agent drafting pipeline that meets our non-technical goals of human ownership, transparency, and minimal human burden.

## Key Findings

- **Privacy (Sealed-Context):**  The team correctly identified and patched a privacy gap.  Agent contexts now treat *all* sensitive user content as sealed, never using it in prompts, tests, logs or intermediate tools.  This aligns with emerging best practices: an arXiv study on agentic privacy notes that “every boundary in an agentic pipeline is a site of potential privacy violation and must be assessed independently”.  With sealed-context rules in place (in `agents/rules/core/run-contract.md` and related files), we no longer expose private writing in agent transcripts.

- **Architecture vs. Writing Focus:**  The system’s design prioritized campaign planning over producing actual posts.  Internally, we generated concept maps, decision packages, thesis outlines, etc., but the user goal was to publish persuasive LinkedIn posts.  In other words, architecture became the objective instead of a means.  This mismatch led to “analysis paralysis”: agents spent too much effort on prep documents and not enough on writing.  We must reverse that balance.  The evidence from user answers is clear: the project was never supposed to be “architecture-heavy” – those plans were tools, not the deliverable.  Going forward, the pipeline should treat architecture as invisible scaffolding, and deliver concrete draft content as its primary output.

- **Multiagent Independence:**  Despite rules allowing multiple agents, the output showed very similar styles.  One agent’s “internal reviewer” failed to catch the formulaic structure before saving drafts, so all “options” shared the same AI-cadence.  To avoid this, we need *true* parallelism.  Slack’s multi-agent framework confirms this: each agent needs its own tailored view, because if they see the same information they fall into “confirmation bias” and loss of creativity.  The fix is to spawn fresh LLM instances with isolated memory for each writing task, so that one agent’s language patterns don’t infect the others.  This will naturally diversify phrasing and structure.

- **Review Gating (“Anti-Slop Firewall”):**  The current “writing-room” approach caught some high-level issues (overpromising, aphorisms), but didn’t prevent the final drafts from sounding like polished AI posts.  We lack a true gate that stops “sloppy” generative prose early.  Instead of only reviewing final drafts, we should validate *before* full-text generation.  For example, have agents produce short, concrete scene fragments or outlines first, use another agent to flag any AI-cadence or clichés, and then let a writer agent expand the cleaned fragment into a full draft.  This pre-draft review step would break the sequence of symmetrical paragraphs and formulaic patterns.

- **Human Decision Surface:**  The human interface remained cluttered with long artifact files.  The plan now clarifies that the human’s view should be compact: the orchestrator compresses details into simple summaries or option lists, not pages of agent chatter.  For example, instead of showing concept cards, we will show only the top recommended draft and a summary of why it was chosen.  This matches the AGENTS.md principle that agent instructions and human documentation have different audiences.  We must keep human-facing output concise and actionable.

## Gap Analysis

| Dimension                   | Current Behavior                                                 | Desired Behavior                                                       |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------------------|
| **Privacy**                 | Partial sealing. Agents still had capability to query private terms (now fixed).  Risk of leakage existed at multiple pipeline stages. | Fully sealed context. Treat each agent hand-off as an independent boundary. No private content used anywhere in prompts, logs, tests, or output.   |
| **Planning vs. Writing**    | Over-engineered planning. Agents generated extensive architecture and concept artifacts before any draft.  Writing was deferred. | Outcome-focused. Agents immediately generate draft content or fragments. Plans are internal only.  Architecture is a hidden tool, not a deliverable. |
| **Multiagent Independence** | Sequential/self-edit. One agent generated similar options with minor edits.  Limited diversity; style flaws repeated across outputs. | True parallel. Launch separate LLM instances (writer agents) with fresh memory for each draft. They will disagree and produce diverse phrasing, as multi-agent systems preserve “creativity” by not oversharing information.  |
| **Review Gating**           | Late-stage only. Quality checks occurred mainly after drafts were written, missing deep structural issues.  Weak anti-slop. | Pre-write and adversarial. Introduce explicit pre-draft review (e.g. fragment checks) and use critic agents before finalizing any draft. Catch “AI-speak” and clichés early. |
| **Human Burden**            | High. The user was shown lengthy plans, notes, and multiple drafts.  Reading was time-consuming. | Low and focused. Present only a concise decision surface: best draft summary, comparative notes, and a clear choice. Never expose raw agent reasoning or planning to the human. |

## High-Level Requirements

Based on the above findings and our non-technical goals, the pipeline must satisfy:

- **Absolute Privacy at Boundaries:**  Apply the sealed-context principle end-to-end.  Never allow private or user-authored text to flow into agent queries, tools, logs, or prompts.  As one recent study emphasizes, “every boundary” in an agentic workflow is a potential privacy leak.  We must treat *each call* as a strict firewall: any usage of private voice must be purely passive (for style only, never for content or filtering) and local to that agent.

- **Compact Human Decision Surface:**  The human should see only what they need to decide.  This means final outputs (draft text) and a tiny summary of options/risks—not the agent reasoning.  Think of the human interface like a streamlined dashboard.  (AGENTS.md, for example, separates agent instructions from human docs; similarly, our agent artifacts are for machines, while humans get only the digest.)  The orchestrator’s job includes compressing any necessary context into bullets or a summary for decision-making, not dumping full data.

- **True Multi-Agent Pipeline:**  Each creative task (e.g. writing the post) should be handled by multiple *independent* agents running in parallel.  No memory should carry over between them.  This ensures stylistic variety and avoids one agent “contaminating” another.  Agents should be specialized: e.g., one writer agent per draft, one or more critic/reviewer agents analyzing a draft fragment.  A system like Slack’s agent framework shows that giving each agent a separate context helps them stay creative yet coherent.

- **Adversarial Review (Draft-Quality Firewall):**  Before any draft reaches the human, apply automated checks.  For example, have critic agents look at outlines or bullet-point drafts to flag any cliché phrasing, hidden agenda language, or overly neat structure.  If an outline fails (uses “not X but Y” formulas, hackneyed hooks, etc.), revise it or reject it.  Only post-review fragments should be expanded into full drafts.  This gate-keeping step is essential to break the AI’s symmetric writing patterns and align the tone with our honest, technical voice.

- **Output-Driven Process:**  The pipeline must be triggered by specific content goals, not by building more plans.  Once the topic and direction are set (as in the A+C spine we chose), the next step is **writing**, not another plan.  The orchestrator should recognize when the next creative output is obvious and execute it.  In practice, this means after deciding “Forensic first, origin second,” we immediately produce drafts, rather than another concept map.

- **Remove Stale Artifacts:**  All transient S005 planning files (the “2026-07-04…” and “2026-07-05…” markdowns we created) should be deleted or archived outside the main repo.  They contain private analysis and draft fragments that are not part of the published campaign.  They are explicitly marked as **not** for use in future posts (per the run boundary file), so keeping them only risks confusion and leakage.

## Behavioral Norms for the Pipeline

- **Seal and Ignore:** Treat any private voice or planning detail as sealed: it may guide *agent thinking* but must never appear in prompts or outputs.  In practice, do not use private content as search patterns or prompt fragments.  Never feed it into validators or fixture data.

- **Focus on Drafts:** After campaign direction is set, the next tasks are writing tasks.  Do not default to more planning.  If a writer agent can start drafting right away, do it.  Additional concept artifacts are allowed only if the next step is not clear; otherwise, push all efforts into producing draft text.

- **Spawn Fresh Instances:** For each new draft or review task, spin up a new LLM instance.  Do not reuse context or memory from previous runs.  This enforces diversity: each agent sees only what the orchestrator gives it and can come up with its own phrasing and examples.

- **Adversarial Checkpoint:** Before finalizing, have a dedicated review agent (or set of agents) scrutinize the draft fragment.  If it smells like AI output or misaligned with our narrative (e.g. sounding too much like generic marketing copy), flag it.  Only approved fragments proceed.

- **Lean Human Interface:** Always compress agent work for the human.  The user should get “Action Required: [best draft] vs [second best], reasons, and decision.”  No stray bullet lists or internal notes.

- **Valuate Real Evidence:** When writing, base claims on actual project history.  For example, concrete events (URL migration, test commit, etc.) should be used as evidence in the narrative.  But use them as details to illustrate our point, not as the point itself.  The posts should make readers *infer* the lesson from the story, rather than stating it directly.

- **Declare Done:** Once a set of full draft candidates is prepared, present them to the user as the next actionable step.  Do not leave tasks open-ended.  The human then decides which draft to develop or publish, which closes this planning cycle.

## Comparison Table: Current vs. Desired Pipeline

| **Aspect**              | **Current (Pre-Fix)**                                                                                  | **Desired (Post-Fix)**                                                                                                               |
|-------------------------|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Privacy                 | Partial. Agents could still reference user samples in prompts/logs (though final output was scrubbed). | Complete. All private content is *for context only* and never appears in any agent message or tool call.             |
| Planning vs. Writing    | Bias toward planning. Agents generate many intermediate artifacts before any draft.                    | Outcome-driven. Immediate drafting after setting direction; architecture artifacts do not go to the user.                           |
| Multiagent Execution    | Effectively single-agent with self-edit. One chain of LLM calls produced similar variants.            | Independent agents. Each writer/reviewer is a fresh agent instance. Parallel drafting breaks symmetry.              |
| Review Process          | Late stage, human-review intensive. Lacked automated anti-slop checks in early draft stage.           | Layered. Introduce early reviewer agents to catch style/content issues before full draft.  Human sees only polished candidate drafts. |
| Human Burden            | High. User read lengthy notes, cards, and multiple nearly-identical drafts.                           | Low. User gets a concise summary and 1–3 high-quality drafts.  Human feedback triggers final edits or publication.                  |

```mermaid
flowchart TD
  subgraph Orchestration
    O[Orchestrator Agent] 
  end
  subgraph Writing
    O --> W1[Writer Agent 1<br>(draft fragment)]
    O --> W2[Writer Agent 2<br>(draft fragment)]
    O --> W3[Writer Agent 3<br>(draft fragment)]
  end
  subgraph Review
    W1 --> R[Review Agent(s)<br>(anti-slop checks)]
    W2 --> R
    W3 --> R
    R --> D[Draft Candidates]
  end
  subgraph Decision
    D --> H[Human Decision Surface<br>(concise summary)]
    H --> P[Publication Gate]
  end
```

In this intended pipeline, the Orchestrator spawns multiple independent writer agents (W1, W2, W3). Each produces a fragment or short draft. Reviewer agents (R) then analyze these fragments and filter or refine them. The surviving **Draft Candidates** are presented (via the orchestrator) to the human as a compact decision surface (H), showing only the best options and key differences. Finally, the human chooses to publish (P) or request revisions. 

## Checklist for the Team

- ✅ **Enforce Sealed Context:** Verify all pipeline rules reflect that user content is non-operational (e.g. as in `run-contract.md`).  Test the system to ensure no prompts or logs ever contain private data.  
- ✅ **Remove S005 Artifacts:** Delete or archive all `agents/work/social/2026-07-*` files created during the S005 run.  They served only as draft-workspace, and retaining them risks leakage and confusion.  
- ✅ **Adopt Multi-Agent Spawning:** Update orchestrator logic so each writer/reviewer task runs in a fresh agent instance (no shared memory).  Confirm that agents receive only the approved campaign direction and necessary evidence links.  
- ✅ **Implement Review Gate:** Create a “critic” role to examine draft fragments before full drafting.  Drafts should not proceed without passing basic quality checks (no AI-clichés, unsupported claims, etc.).  
- ✅ **Streamline Outputs:** Adjust output formatting so humans see only the final draft candidates and an executive summary.  Trim all extra agent notes. Ensure outputs follow the public voice guidelines (no jargon, no private-sample phrasing).  
- ✅ **Communicate Transparently:** Inform all stakeholders about these changes and train any overseers on the new norms.  Emphasize that future posts will look and feel more like authentic technical narratives, not generic marketing copy.

## Message for the Organization

We have recalibrated our agentic workflow to reflect our core values.  Privacy is now airtight: no private material leaks into any agent step, in line with cutting-edge standards.  More importantly, we are shifting our focus back to *writing*.  Going forward, our agents will independently draft and self-review content, producing multiple distinct post candidates for each topic.  The human team will only see concise summaries and polished options.  This means we can confidently tell the project’s story (its engineering challenges and lessons learned) in a natural voice, without over-relying on rote AI patterns.  In short, the architecture remains our secret tool – the end product will be high-quality content ready for publication, with minimal extra overhead for our team.  

