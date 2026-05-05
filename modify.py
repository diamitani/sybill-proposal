import re

def update_proposal():
    with open('sybill-gencyai-proposal.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update logo path
    html = html.replace('src="assets/gencyai-logo.png"', 'src="GencyAI Products/gency-wordmark.png"')

    # 2. Add Sybill logo to hero
    sybill_logo = '<img src="https://media.licdn.com/dms/image/v2/C560BAQFfi5hDhomRWg/company-logo_200_200/company-logo_200_200/0/1630672218972/sybill_logo?e=1779321600&v=beta&t=_t60btjtjSs8Nepyq04WktOQ7WKm7P3Yxw8HpMTGyZM" alt="Sybill Logo" style="width: 60px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1);" />'
    html = html.replace('<span class="hero-brand-kicker">Revenue systems proposal</span>',
                        f'<span class="hero-brand-kicker">Revenue systems proposal for</span> {sybill_logo}')

    # 3. Update the package list in Overview
    old_package_list = """<ul>
              <li><strong>Inbound automation</strong> that turns contact intent into structured routing, cleaner lifecycle data, and usable sales follow-up.</li>
              <li><strong>Outbound prospecting workflow</strong> that finds the right accounts, ranks the right people, and drafts the right first touch.</li>
              <li><strong>System setup</strong> covering tools, accounts, properties, configurations, domains, reporting, and governance.</li>
              <li><strong>Sales playbook</strong> with ICP, messaging, ownership, KPIs, and operating rhythm.</li>
            </ul>"""
    new_package_list = """<ul>
              <li><strong>Inbound automation</strong> that turns contact intent into structured routing, cleaner lifecycle data, and usable sales follow-up.</li>
              <li><strong>Outbound prospecting workflow</strong> that finds the right accounts, ranks the right people, and drafts the right first touch.</li>
              <li><strong>Post-sales call automation</strong> that leverages Sybill's meeting outputs to auto-draft consultative follow-ups, extract competitor intel, and write CRM notes.</li>
              <li><strong>System setup & Playbook</strong> covering tools, reporting, ICP, messaging, and ownership.</li>
            </ul>"""
    html = html.replace(old_package_list, new_package_list)

    # 4. Replace grid-4 packages with grid-3 + grid-2
    old_grid_4 = """<div class="grid-4">
          <div class="card package-card">
            <div class="package-number">A</div>
            <h3>Inbound automation</h3>
            <ul>
              <li>AI intent classification on Contact Us and high-intent form submissions.</li>
              <li>HubSpot property updates for cleaner reason-for-contact reporting.</li>
              <li>Lifecycle stage correction only when required.</li>
              <li>Sales-intent routing plus follow-up draft generation.</li>
            </ul>
          </div>

          <div class="card package-card">
            <div class="package-number">B</div>
            <h3>Outbound prospecting</h3>
            <ul>
              <li>Target account ingestion and ICP screening.</li>
              <li>Contact enrichment, normalization, and ranking.</li>
              <li>Company research summaries and pain hypotheses.</li>
              <li>Personalized outbound message generation and sequence sync.</li>
            </ul>
          </div>

          <div class="card package-card">
            <div class="package-number">C</div>
            <h3>System setup</h3>
            <ul>
              <li>Tools, workspaces, domains, and account configuration.</li>
              <li>HubSpot fields, workflows, ownership, and routing rules.</li>
              <li>AI model access, prompt storage, and workflow orchestration.</li>
              <li>Reporting views, dashboards, and QA checkpoints.</li>
            </ul>
          </div>

          <div class="card package-card">
            <div class="package-number">D</div>
            <h3>Sales playbook</h3>
            <ul>
              <li>ICP and persona definitions for the buying committee.</li>
              <li>USP and message pillars tied to what Sybill actually wins on.</li>
              <li>Ownership rules, SLAs, and operating cadence.</li>
              <li>Sample messaging, objections, and follow-up standards.</li>
            </ul>
          </div>
        </div>"""
    
    new_grid_layout = """<div class="grid-3">
          <div class="card package-card">
            <div class="package-number">A</div>
            <h3>Inbound automation</h3>
            <ul>
              <li>AI intent classification on Contact Us and high-intent form submissions.</li>
              <li>HubSpot property updates for cleaner reason-for-contact reporting.</li>
              <li>Lifecycle stage correction only when required.</li>
              <li>Sales-intent routing plus follow-up draft generation.</li>
            </ul>
          </div>

          <div class="card package-card">
            <div class="package-number">B</div>
            <h3>Outbound prospecting</h3>
            <ul>
              <li>Target account ingestion and ICP screening.</li>
              <li>Contact enrichment, normalization, and ranking.</li>
              <li>Company research summaries and pain hypotheses.</li>
              <li>Personalized outbound message generation and sequence sync.</li>
            </ul>
          </div>

          <div class="card package-card">
            <div class="package-number">C</div>
            <h3>Post-sales call intelligence</h3>
            <ul>
              <li>Parallel AI agents processing Sybill call transcripts.</li>
              <li>Automated, country/context-grounded consultative follow-up emails.</li>
              <li>Competitor intelligence extraction (vs Gong, Clari, etc.).</li>
              <li>LinkedIn post generation from call insights.</li>
            </ul>
          </div>
        </div>
        
        <div class="grid-2" style="margin-top: 18px;">
          <div class="card package-card" style="min-height: auto;">
            <div class="package-number">D</div>
            <h3>System setup</h3>
            <ul>
              <li>Tools, workspaces, domains, and account configuration.</li>
              <li>HubSpot fields, workflows, ownership, and routing rules.</li>
              <li>Reporting views, dashboards, and QA checkpoints.</li>
            </ul>
          </div>

          <div class="card package-card" style="min-height: auto;">
            <div class="package-number">E</div>
            <h3>Sales playbook</h3>
            <ul>
              <li>ICP and persona definitions for the buying committee.</li>
              <li>USP and message pillars tied to what Sybill actually wins on.</li>
              <li>Ownership rules, SLAs, and operating cadence.</li>
            </ul>
          </div>
        </div>"""
    html = html.replace(old_grid_4, new_grid_layout)

    # 5. Insert Post-Sales Call Intelligence Article before System setup
    post_sales_call_article = """
          <article class="detail-card card">
            <span class="subline">3. Post-sales call intelligence workflow</span>
            <h3>Turn Sybill's meeting outputs into immediate, consultative action.</h3>
            <p>
              Since Sybill <em>is</em> the meeting intelligence platform, we should feed Sybill's own insights into a parallel agent orchestration engine. This turns transcripts and summaries into immediate follow-ups, competitor intel, and CRM notes without the rep lifting a finger.
            </p>

            <div class="workflow-flow" aria-label="Post-sales workflow diagram">
              <div class="flow-node"><strong>Sybill Meeting Output</strong><span>Transcript and summary ready</span></div>
              <div class="flow-arrow">→</div>
              <div class="flow-node"><strong>Parallel Agents</strong><span>5 specialized Claude agents analyze simultaneously</span></div>
              <div class="flow-arrow">→</div>
              <div class="flow-node"><strong>Consultative Follow-up</strong><span>Drafted response with competitor counter-positioning</span></div>
              <div class="flow-arrow">→</div>
              <div class="flow-node"><strong>CRM & Content</strong><span>HubSpot notes updated, LinkedIn post generated</span></div>
            </div>

            <div class="grid-2" style="margin-top: 18px;">
              <div class="mini-card">
                <h4>Parallel AI Agents</h4>
                <ul class="proof-list">
                  <li><strong>Agent 1: Consultative Follow-Up</strong>. Drafts a buyer-facing email mapped to specific pain points.</li>
                  <li><strong>Agent 2: Missed Questions</strong>. Identifies deal risks and what the rep should have asked.</li>
                  <li><strong>Agent 3: Competitor Intel</strong>. Detects mentions of Gong/Clari and pulls RAG-grounded counter-positioning.</li>
                  <li><strong>Agent 4: Social Content</strong>. Generates a high-performing LinkedIn post from a call insight.</li>
                  <li><strong>Agent 5: Expansion Analysis</strong>. Flags upsell opportunities for RevOps/Sales Managers.</li>
                </ul>
              </div>
              <div class="mini-card">
                <h4>Why this works for Sybill</h4>
                <ul class="proof-list">
                  <li>Drinking your own champagne: Proves that Sybill's context is the ultimate trigger for GTM automation.</li>
                  <li>Cuts follow-up time from hours to under 10 minutes.</li>
                  <li>Ensures reps actually use competitor counter-points (they're automatically drafted).</li>
                  <li>Captures coaching moments systematically across all 5 closers.</li>
                </ul>
              </div>
            </div>
          </article>
    """
    html = html.replace('<span class="subline">3. System setup</span>', 
                        post_sales_call_article + '\n          <article class="detail-card card">\n            <span class="subline">4. System setup</span>')
    
    html = html.replace('<span class="subline">4. Sales playbook for Sybill</span>', '<span class="subline">5. Sales playbook for Sybill</span>')

    # 6. Update pricing section to include post-sales
    old_pricing_list = """<ul class="pricing-list">
              <li>Inbound workflow implementation</li>
              <li>Outbound prospecting workflow implementation</li>
              <li>HubSpot property, routing, and dashboard setup</li>
              <li>n8n or Make orchestration and tool connection setup</li>
              <li>Clay, Apollo, Amplemarket, or sender configuration</li>
              <li>Claude skills pack, prompt tuning, and QA</li>
              <li>Reporting, documentation, and handoff</li>
            </ul>"""
    new_pricing_list = """<ul class="pricing-list">
              <li>Inbound workflow implementation</li>
              <li>Outbound prospecting workflow implementation</li>
              <li><strong>Post-sales call intelligence workflow implementation</strong></li>
              <li>HubSpot property, routing, and dashboard setup</li>
              <li>n8n or Make orchestration and tool connection setup</li>
              <li>Clay, Apollo, Amplemarket, or sender configuration</li>
              <li>Claude skills pack, prompt tuning, and QA</li>
              <li>Reporting, documentation, and handoff</li>
            </ul>"""
    html = html.replace(old_pricing_list, new_pricing_list)

    # 7. Update timeline
    old_timeline_wk4 = """<div class="week">
                <strong>Week 4</strong>
                <span>Install research and messaging generation, connect sequence handoff, tune prompts, and validate outputs.</span>
              </div>"""
    new_timeline_wk4 = """<div class="week">
                <strong>Week 4</strong>
                <span>Install research/messaging generation, build Post-Sales Call Intelligence pipeline (parallel agents), validate outputs.</span>
              </div>"""
    html = html.replace(old_timeline_wk4, new_timeline_wk4)

    with open('sybill-gencyai-proposal.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    update_proposal()
    print("Proposal updated successfully.")
