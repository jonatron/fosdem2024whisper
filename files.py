'''
https://fosdem.org/2024/schedule/events/

let links = document.querySelectorAll('#main td a')
let linklist = [];
for(let link of links) {
    if(link.href.includes(".webm")) {
        let title = link.closest('tr').querySelector('td').innerText;
        linklist.push({'href': link.href, 'title': title})
    }
}
'''


files = \
[
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3023-welcome-to-fosdem-2024.av1.webm",
    "title": "Welcome to FOSDEM 2024\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2850-where-have-the-women-of-tech-history-gone-.av1.webm",
    "title": "Where have the women of tech history gone?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2522-outreachy-1000-interns.av1.webm",
    "title": "Outreachy: 1000 interns\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3024-closing-fosdem-2024.av1.webm",
    "title": "Closing FOSDEM 2024\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-1808-how-to-chart-your-own-career-path-in-open-source-panel-discussion.av1.webm",
    "title": "How to Chart your own Career Path in Open Source - Panel Discussion\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3683-the-regulators-are-coming-one-year-on.av1.webm",
    "title": "The Regulators Are Coming: One Year On\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3209-how-open-source-projects-approach-functional-safety.av1.webm",
    "title": "How open source projects approach Functional Safety\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3648-privacy-respecting-usage-metrics-for-free-software-projects.av1.webm",
    "title": "Privacy-respecting usage metrics for free software projects\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2871-ingesting-and-analyzing-millions-of-events-per-second-in-real-time-using-open-source-tools.av1.webm",
    "title": "Ingesting and analyzing millions of events per second in real-time using open source tools\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3553-learning-from-disaster-response-teams-to-save-the-internet.av1.webm",
    "title": "Learning from disaster response teams to save the internet\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2332-magic-and-software.av1.webm",
    "title": "Magic and Software\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3345-opening-up-communication-silos-with-matrix-2-0-and-the-eu-digital-markets-act.av1.webm",
    "title": "Opening up communication silos with Matrix 2.0 and the EU Digital Markets Act\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2151-alexandria3k-researching-the-world-s-knowledge-on-your-laptop.av1.webm",
    "title": "Alexandria3k: Researching the world's knowledge on your laptop\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2716-firefox-power-profiling-a-powerful-visualization-of-web-sustainability.av1.webm",
    "title": "Firefox power profiling: a powerful visualization of web sustainability\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3362-open-source-for-sustainable-and-long-lasting-phones.av1.webm",
    "title": "Open Source for Sustainable and Long lasting Phones\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2674-unveiling-the-open-renewable-energy-systems-ores-initiative-panel-discussion.av1.webm",
    "title": "Unveiling the Open Renewable Energy Systems (ORES) Initiative - Panel Discussion\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-2741-take-your-foss-project-from-surviving-to-thriving.av1.webm",
    "title": "Take Your FOSS Project From Surviving To Thriving\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-3508-netbsd-10-thirty-years-still-going-strong-.av1.webm",
    "title": "NetBSD 10: Thirty years, still going strong!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-3353-reproducible-builds-the-first-ten-years.av1.webm",
    "title": "Reproducible Builds: The First Ten Years\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-3370-an-engineer-s-guide-to-linux-kernel-upgrades.av1.webm",
    "title": "An engineer's guide to Linux Kernel upgrades\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-2092-the-d-programming-language-for-modern-open-source-development.av1.webm",
    "title": "The D Programming Language for Modern Open Source Development\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-1902-first-aid-kit-for-c-c-server-performance.av1.webm",
    "title": "First Aid Kit for C/C++ Server Performance\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-1830-20-years-of-open-source-building-xwiki-and-cryptpad.av1.webm",
    "title": "20 Years of Open Source building XWiki and CryptPad\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-1931-you-too-could-have-made-curl-.av1.webm",
    "title": "You too could have made curl!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-1930-openprinting-we-make-printing-just-work-.av1.webm",
    "title": "OpenPrinting - We make printing just work!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-3238-scion-hitting-the-future-internet-road-next-generation-internet-ecosystem-and-burgeoning-opportunities.av1.webm",
    "title": "SCION, hitting the future Internet road: Next-generation Internet ecosystem and burgeoning opportunities\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-3297-sequoia-pgp-rethinking-openpgp-tooling.av1.webm",
    "title": "Sequoia PGP: Rethinking OpenPGP Tooling\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3595-open-food-facts-acting-on-the-health-and-environnemental-impacts-of-the-food-system.av1.webm",
    "title": "Open Food Facts : Acting on the health and environnemental impacts of the food system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3740-observations-on-a-dnssec-incident-the-russian-tld.av1.webm",
    "title": "Observations on a DNSSEC incident: the russian TLD\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-2671-a-simple-caching-service-for-your-ci.av1.webm",
    "title": "A simple caching service for your CI\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3669-reinventing-database-exploration-with-azimutt.av1.webm",
    "title": "Reinventing database exploration with Azimutt\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-1962-kzu-a-graph-database-management-system-for-python-graph-data-science.av1.webm",
    "title": "Kùzu: A Graph Database Management System for Python Graph Data Science\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3747-testing-containers-with-python-and-pytest.av1.webm",
    "title": "Testing Containers with Python and pytest\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-2848-documenting-and-fixing-non-reproducible-builds-due-to-configuration-options.av1.webm",
    "title": "Documenting and Fixing Non-Reproducible Builds due to Configuration Options\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3543-platform-engineering-for-dummies.av1.webm",
    "title": "Platform engineering for dummies\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3245-taming-the-beast-managing-high-growth-postgres-databases-at-circleci.av1.webm",
    "title": "Taming the Beast: Managing High-Growth Postgres Databases at CircleCI\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3662--serde-memdbg-sux-dsi-bitstream-webgraph-a-rust-ecosystem-for-large-graph-processing.av1.webm",
    "title": "ε-serde / mem_dbg / sux / dsi-bitstream / webgraph: a Rust ecosystem for large graph processing\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3705-using-elliptic-curve-cryptography-for-the-purposes-of-identity.av1.webm",
    "title": "Using elliptic curve cryptography for the purposes of identity\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3661-timestamping-with-opentimestamps.av1.webm",
    "title": "Timestamping with opentimestamps\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3468-compiler-options-hardening-for-c-and-c-.av1.webm",
    "title": "Compiler Options Hardening for C and C++\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-2231-a-lazy-developer-s-approach-to-building-real-time-web-applications.av1.webm",
    "title": "A Lazy Developer’s Approach to Building Real-Time Web Applications\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3615-0-a-d-game-vulkan-api.av1.webm",
    "title": "0 A.D. game: Vulkan API\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-2177-system-for-television-off-air-recording-and-archiving-bfi-national-television-archive.av1.webm",
    "title": "System for Television Off-air Recording and Archiving, BFI National Television Archive\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-2046-do-you-know-yaml-.av1.webm",
    "title": "Do you know YAML?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-2957-introduction-to-blisslabs-and-bliss-os.av1.webm",
    "title": "Introduction to BlissLabs and Bliss OS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3390-introducing-the-open-podcast-api.av1.webm",
    "title": "Introducing the Open Podcast API\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-2043-foss-for-docs.av1.webm",
    "title": "FOSS for DOCS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-1776-journey-to-an-open-source-contribution.av1.webm",
    "title": "Journey to an open source contribution\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3296-aerodynamic-data-models-flying-fast-at-scale-with-duckdb.av1.webm",
    "title": "Aerodynamic Data Models: Flying Fast at Scale with DuckDB\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3175-trusted-postgres-architect-deploying-postgres-with-infrastructure-as-code.av1.webm",
    "title": "Trusted Postgres Architect - Deploying Postgres with Infrastructure as Code\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3342-the-wonderful-life-of-a-sql-query-in-a-streaming-database.av1.webm",
    "title": "The wonderful life of a SQL query in a streaming database\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3472-switching-the-fosdem-conference-management-system-to-pretalx.av1.webm",
    "title": "Switching the FOSDEM conference management system to pretalx\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3025-fosdem-infrastructure-review.av1.webm",
    "title": "FOSDEM infrastructure review\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-2629-from-openllm-france-to-openllm-europe-paving-the-way-to-sovereign-and-open-source-ai.av1.webm",
    "title": "From OpenLLM-France to OpenLLM-Europe: Paving the way to sovereign and open source AI\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-2623-linto-studio-as-your-ultimate-open-source-ai-driven-media-management-solution.av1.webm",
    "title": "LinTO Studio as Your Ultimate Open Source AI-driven Media Management Solution\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-2384-langchain-from-0-to-1-unveiling-the-power-of-llm-programming.av1.webm",
    "title": "LangChain From 0 To 1: Unveiling the Power of LLM Programming\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-1958-ml-guided-optimizations-in-llvm.av1.webm",
    "title": "ML Guided Optimizations in LLVM\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3754-dynamic-explainability-through-dynamic-causal-modeling.av1.webm",
    "title": "Dynamic Explainability through Dynamic Causal Modeling\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-2424-using-haystack-to-build-custom-functionality-for-llm-applications.av1.webm",
    "title": "Using Haystack to Build Custom Functionality for LLM Applications\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-1953-using-code-generated-by-ai-issues-misconceptions-and-solutions.av1.webm",
    "title": "Using code generated by AI: issues, misconceptions and solutions\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3507-reducing-the-risks-of-open-source-ai-models-and-optimizing-upsides.av1.webm",
    "title": "Reducing the risks of open source AI models and optimizing upsides\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-2863-open-source-ai-at-techworks-the-uk-trade-body-for-electronic-systems-engineering.av1.webm",
    "title": "Open Source AI at TechWorks, the UK trade body for Electronic Systems Engineering\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-2531-introduction-to-openapi.av1.webm",
    "title": "Introduction to OpenAPI\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-1710-deploy-fast-without-breaking-things-level-up-apiops-with-opentelemetry.av1.webm",
    "title": "Deploy Fast, Without Breaking Things: Level Up APIOps With OpenTelemetry\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3443-public-calendars-aggregation-using-linkal.av1.webm",
    "title": "Public calendars aggregation using Linkal\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2923-indico-an-event-management-system.av1.webm",
    "title": "Indico: an event management system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2396-opentalk-video-conferencing-secure-and-gdpr-compliant.av1.webm",
    "title": "OpenTalk - Video conferencing secure and GDPR compliant\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3126-securely-collaborate-with-cryptpad.av1.webm",
    "title": "Securely collaborate with CryptPad\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2828-collabora-online-wasm.av1.webm",
    "title": "Collabora Online: WASM\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3396-collabora-online-usability-optimization.av1.webm",
    "title": "Collabora Online usability optimization\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-1994-document-collaboration-made-simpler-revealing-the-concept-of-rooms-in-onlyoffice-docspace.av1.webm",
    "title": "Document collaboration made simpler: Revealing the concept of rooms in ONLYOFFICE DocSpace\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3274-opendesk-the-open-source-collaborative-suite.av1.webm",
    "title": "openDesk - The Open Source collaborative suite\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3134-another-approach-to-ai.av1.webm",
    "title": "Another approach to AI\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-1858-using-generative-ai-and-content-service-platforms-together.av1.webm",
    "title": "Using Generative AI and Content Service Platforms together\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3317-web-accessibility-and-environmental-sustainability-and-with-popular-cms.av1.webm",
    "title": "Web Accessibility and Environmental Sustainability and with Popular CMS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-1831-cristal-a-new-wiki-ui-to-rule-them-all.av1.webm",
    "title": "Cristal: a new Wiki UI to rule them all\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3484-pushing-tiki-to-its-limits.av1.webm",
    "title": "Pushing Tiki to its limits\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2781-how-to-get-rid-of-confluence-comparing-open-source-knowledgemanagent-systems.av1.webm",
    "title": "How to get rid of Confluence: Comparing Open Source Knowledgemanagent Systems\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-1945-the-challenges-of-creating-a-foss-fact-checking-platform-for-the-brazilian-community.av1.webm",
    "title": "The Challenges of Creating a FOSS Fact-Checking Platform for the Brazilian Community\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-1780-how-do-you-change-the-governance-model-of-an-established-open-source-project-.av1.webm",
    "title": "How do you change the governance model of an established open source project?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-1693-please-make-it-make-sense-product-management-methods-to-make-your-project-s-purpose-clear.av1.webm",
    "title": "Please Make It Make Sense: Product Management Methods to Make Your Project's Purpose Clear\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-2190-single-vendor-is-the-new-proprietary.av1.webm",
    "title": "Single-vendor is the new proprietary\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-2029-open-source-in-2024-boundaries-burnout-business.av1.webm",
    "title": "Open Source in 2024: boundaries, burnout, business\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-2751-the-state-of-funding-free-open-source-software.av1.webm",
    "title": "The State of Funding Free & Open Source Software\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-2581-the-many-hats-of-a-maintainer-organizational-design-that-helps-reduce-them.av1.webm",
    "title": "The Many Hats of a Maintainer: Organizational Design That Helps Reduce Them\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-1653-open-practices-for-open-projects.av1.webm",
    "title": "Open practices for open projects\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-2105-kickstarting-an-open-source-culture-a-guide-for-mentors.av1.webm",
    "title": "Kickstarting an Open Source Culture: A Guide for Mentors\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-1938-strategies-for-building-healthy-open-source-communities.av1.webm",
    "title": "Strategies for Building Healthy Open Source Communities\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-2599-building-communities-with-science-.av1.webm",
    "title": "Building Communities with Science!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2608-intel-tdx-deep-dive.av1.webm",
    "title": "Intel TDX Deep Dive\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2372-sev-step-a-single-stepping-framework-for-amd-sev.av1.webm",
    "title": "SEV-Step: A Single-Stepping Framework for AMD-SEV\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-1775-shielding-data-embracing-openness-optimizing-performance-a-journey-through-trustworthy-environments-for-database-systems.av1.webm",
    "title": "Shielding Data, Embracing Openness, Optimizing Performance: A Journey Through Trustworthy Environments for Database Systems\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2317-the-ups-and-downs-of-running-enclaves-in-production.av1.webm",
    "title": "The ups and downs of running enclaves in production\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-3097-securing-embedded-systems-with-ftpm-implemented-as-trusted-application-in-tee.av1.webm",
    "title": "Securing Embedded Systems with fTPM implemented as Trusted Application in TEE\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2461-integrity-protect-workloads-with-mushroom.av1.webm",
    "title": "Integrity Protect Workloads with Mushroom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-1769-reproducible-builds-for-confidential-computing-why-remote-attestation-is-worthless-without-it.av1.webm",
    "title": "Reproducible builds for confidential computing: Why remote attestation is worthless without it\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2265-increasing-trust-and-preserving-privacy-advancing-remote-attestation.av1.webm",
    "title": "Increasing Trust and Preserving Privacy: Advancing Remote Attestation\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-1855-forensic-container-checkpointing-and-analysis.av1.webm",
    "title": "Forensic container checkpointing and analysis\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-2988-introducing-incus.av1.webm",
    "title": "Introducing Incus\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3063-using-chroots-in-a-single-linux-container-as-an-alternative-to-docker-compose.av1.webm",
    "title": "Using chroots in a single Linux Container as an alternative to docker-compose\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3282-soft-reboot-keep-your-containers-running-while-your-image-based-linux-host-gets-updated.av1.webm",
    "title": "Soft Reboot: keep your containers running while your image-based Linux host gets updated\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3412-juggling-with-uids-and-gids-rootless-container-deployment-with-ansible.av1.webm",
    "title": "Juggling with UIDs and GIDs: rootless container deployment with Ansible\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3060-what-s-new-in-containerd-2-0-.av1.webm",
    "title": "What's new in Containerd 2.0!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3008-lift-and-shift-modernising-a-legacy-lamp-application-with-systemd-nspawn.av1.webm",
    "title": "Lift and shift: Modernising a legacy LAMP application with systemd-nspawn\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3187-vscode-container-wasm-an-extension-of-vscode-on-browser-for-running-containers-within-your-browser.av1.webm",
    "title": "vscode-container-wasm: An Extension of VSCode on Browser for Running Containers Within Your Browser\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3220-zero-touch-infrastructure-for-container-applications.av1.webm",
    "title": "Zero-touch Infrastructure for Container Applications\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2784-debug-your-stage-1-systemd-with-gdb-and-the-nixos-test-framework.av1.webm",
    "title": "Debug your stage-1 systemd with GDB and the NixOS test framework\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-1857-help-us-improve-time-manipulation-with-gdb.av1.webm",
    "title": "Help us improve time manipulation with GDB\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2392-rocgdb-gdb-and-amdgpu-debugging.av1.webm",
    "title": "ROCgdb, GDB and AMDGPU debugging\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2796-gdb-on-windows-status-plans.av1.webm",
    "title": "GDB on Windows: status & plans\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2668-online-debugging-and-abi-data-services.av1.webm",
    "title": "Online Debugging and ABI Data Services\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2556-poke-all-the-microcontrollers-.av1.webm",
    "title": "Poke all the microcontrollers!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2255-yet-another-event-sourcing-library.av1.webm",
    "title": "Yet another event sourcing library\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-1872-how-to-create-the-universal-operating-system.av1.webm",
    "title": "How to create the universal operating system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-1990-how-much-math-can-you-fit-in-700k-.av1.webm",
    "title": "How much math can you fit in 700K?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-1755-risc-v-bootstrapping-in-guix-and-live-bootstrap.av1.webm",
    "title": "RISC-V Bootstrapping in Guix and Live-Bootstrap\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2560-self-hosting-and-autonomy-using-guix-forge.av1.webm",
    "title": "Self-hosting and autonomy using guix-forge\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2305-open-source-leadership-at-scale-how-1300-people-improved-drupal-s-multilingual-features.av1.webm",
    "title": "Open source leadership at scale, how 1300+ people improved Drupal’s multilingual features\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2315-making-foss-cms-easier-to-teach-with-shared-competency-standards.av1.webm",
    "title": "Making FOSS CMS easier to teach with shared competency standards\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2638-breaking-barriers-content-management-systems-and-accessibility.av1.webm",
    "title": "Breaking Barriers: Content Management Systems and Accessibility\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-3559-wrestling-giants-how-can-free-open-source-cmses-remain-competitive-with-enterprise-clients-.av1.webm",
    "title": "Wrestling giants: How can free open source CMSes remain competitive with enterprise clients?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-3634-shaping-the-future-investing-wisely-in-long-term-open-source-development-with-five-for-the-future-.av1.webm",
    "title": "Shaping the Future: Investing Wisely in Long-Term Open Source Development with \"Five for the Future\"\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1985-ukis-tpms-immutable-initrds-and-full-disk-encryption-what-distributions-should-keep-in-mind-when-hopping-onto-the-system-integrity-train.av1.webm",
    "title": "UKIs, TPMs, immutable initrds and full disk encryption – What Distributions Should Keep in Mind when Hopping onto the System Integrity Train\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2888-mkosi-initrd-building-initrds-out-of-distribution-packages.av1.webm",
    "title": "mkosi-initrd: Building initrds out of distribution packages\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2945-the-monolith-versus-the-swarm-a-comparison-of-opensuse-s-and-fedora-s-build-infrastructures.av1.webm",
    "title": "The Monolith versus the Swarm - A Comparison of openSUSE’s and Fedora’s Build Infrastructures\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1860-desktop-linux-as-easy-as-a-smartphone-just-in-a-snap-.av1.webm",
    "title": "Desktop Linux, as easy as a smartphone! Just in a Snap!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2881-upstream-and-downstream-best-friends-forever-.av1.webm",
    "title": "Upstream and downstream, best friends forever?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2927-supporting-architecture-psabis-with-gnu-guix.av1.webm",
    "title": "Supporting architecture psABIs with GNU Guix\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2951-releasing-a-linux-based-os-an-overview-of-flatcar-release-cycle.av1.webm",
    "title": "Releasing a Linux based OS: an overview of Flatcar release cycle\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2678-an-introduction-to-image-builder-building-up-to-date-customised-operating-system-images-the-easy-way.av1.webm",
    "title": "An introduction to Image Builder: building up-to-date, customised operating system images the easy way\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2028-homebrew-s-evolution.av1.webm",
    "title": "Homebrew's Evolution\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-3056-dns-for-i2p-distributed-network-without-central-authority.av1.webm",
    "title": "DNS for I2P: Distributed Network without Central Authority\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2835-algo-rollover-for-nl.av1.webm",
    "title": "Algo-rollover for .nl\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-1856-bootstrapping-time-on-openbsd.av1.webm",
    "title": "Bootstrapping time on OpenBSD\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2316-let-s-make-people-love-domain-names-again.av1.webm",
    "title": "Let's make people love domain names again\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2906-dnsconfd-system-integrated-dns-cache.av1.webm",
    "title": "dnsconfd: system integrated DNS cache\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2853-domain-a-modular-rust-dns-toolkit.av1.webm",
    "title": "Domain: A modular Rust DNS toolkit\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2198-the-first-13-years-of-blockchain-name-systems.av1.webm",
    "title": "The first 13 years of blockchain name systems\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-2572--vanilla-debian-on-an-industrial-embedded-device.av1.webm",
    "title": "\"Vanilla\" Debian On An Industrial Embedded Device\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3012-using-linux-yocto-as-a-yocto-bsp-kernel.av1.webm",
    "title": "Using linux-yocto as a Yocto BSP kernel\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3136-embedded-security-2023.av1.webm",
    "title": "Embedded Security 2023\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-2103-enioka-scan-say-no-to-vendor-lock-in-for-your-barcode-scanners.av1.webm",
    "title": "enioka Scan: say No! to vendor lock-in for your barcode scanners\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-2479-the-small-device-c-compiler-sdcc-.av1.webm",
    "title": "The Small Device C Compiler (SDCC)\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3225-dora-rs-simplifying-robotics-stack-for-next-gen-robots.av1.webm",
    "title": "Dora-rs: simplifying robotics stack for next gen robots\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-2842-vehicle-abstraction-in-automotive-grade-linux-with-eclipse-kuksa.av1.webm",
    "title": "Vehicle Abstraction in Automotive Grade Linux with Eclipse Kuksa\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3264-an-open-source-open-hardware-offline-finding-system.av1.webm",
    "title": "An open-source, open-hardware offline finding system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3194-from-an-artificial-nose-weekend-hack-to-a-future-proof-iot-device.av1.webm",
    "title": "From an artificial nose weekend hack to a future-proof IoT device\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-2132-google-home-but-better-building-our-own-smart-home-display-with-flutter.av1.webm",
    "title": "Google Home, But Better: Building our own Smart Home Display with Flutter\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2146-how-do-you-write-an-emulator-anyway-.av1.webm",
    "title": "How do you write an emulator anyway ?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1726-panda3ds-climbing-the-tree-of-3ds-emulation.av1.webm",
    "title": "Panda3DS: Climbing the tree of 3DS emulation\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2826-breathing-life-into-legacy-an-open-source-emulator-of-legacy-apple-devices.av1.webm",
    "title": "Breathing Life into Legacy: An Open-Source Emulator of Legacy Apple Devices\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1762-arm64ec-microsoft-s-emulation-frankenstein.av1.webm",
    "title": "Arm64EC: Microsoft's emulation Frankenstein\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-3746-opening-energy-reimagining-this-ecosystem-through-open-source-devroom.av1.webm",
    "title": "Opening Energy: Reimagining this Ecosystem through Open Source devroom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2546-everest-one-stack-to-charge-them-all-.av1.webm",
    "title": "EVerest: One stack to charge them all?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2509-using-flexmeasures-to-build-a-climate-tech-startup-in-15-minutes.av1.webm",
    "title": "Using FlexMeasures to build a climate tech startup, in 15 minutes\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2304-owntech-project-an-open-source-generic-reprogrammable-technology-suite-for-reimagining-the-energy-ecosystem.av1.webm",
    "title": "OwnTech Project: An open-source generic reprogrammable technology suite for reimagining the energy ecosystem\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2155-enhancing-ocpp-with-e2e-security-and-binary-data-streams-for-a-more-secure-energy-ecosystem.av1.webm",
    "title": "Enhancing OCPP with E2E-Security and Binary Data Streams for a more Secure Energy Ecosystem\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2483-citrineos.av1.webm",
    "title": "CitrineOS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2101-power-grid-model-open-source-high-performance-power-systems-analysis.av1.webm",
    "title": "Power Grid Model: Open source high performance power systems analysis\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-1918-gridsuite-and-powsybl-an-open-source-approach-to-develop-advanced-tools-for-grid-analysis-and-simulation-of-power-systems-.av1.webm",
    "title": "GridSuite and PowSyBl: an Open Source approach to develop advanced tools for grid analysis and simulation of power systems.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2662-lfenergy-seapath-easier-operations-in-electrical-substations-through-digital-twin-empowerment.av1.webm",
    "title": "LFEnergy SEAPATH - Easier Operations in Electrical Substations through Digital Twin Empowerment\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2211-openstef-opensource-short-term-energy-forecasting.av1.webm",
    "title": "OpenSTEF: Opensource Short Term Energy Forecasting\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2208-unleash-the-power-of-flexibility-with-shapeshifter-a-universal-flex-trading-protocol.av1.webm",
    "title": "Unleash the Power of Flexibility with Shapeshifter: A Universal Flex Trading Protocol\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-1956-openscd-everything-everywhere-all-at-once.av1.webm",
    "title": "OpenSCD: Everything Everywhere All at Once\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2645-power-to-the-people-technology-for-access-to-energy.av1.webm",
    "title": "Power to the People - Technology for Access to Energy\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2640-sharing-the-operational-cost-of-europe-s-electricity-grid-optimization-and-transparency-through-open-source.av1.webm",
    "title": "Sharing the operational cost of Europe's electricity grid: optimization and transparency through open source\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2960-quartz-solar-os-building-an-open-source-ai-solar-forecast-for-everyone.av1.webm",
    "title": "Quartz Solar OS: Building an open source AI solar forecast for everyone\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2614-can-open-source-development-drive-energy-transition-pypsa-earth-experience.av1.webm",
    "title": "Can open source development drive energy transition? PyPSA-Earth experience\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-1885-carbon-measurement-and-energy-attribution-for-processes-and-hardware-devices-in-the-linux-kernel.av1.webm",
    "title": "Carbon measurement and energy attribution for processes and hardware devices in the Linux kernel\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2061-advanced-linux-power-management-evaluation-using-perf.av1.webm",
    "title": "Advanced Linux Power Management Evaluation using Perf\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2367-how-can-open-source-help-the-wind-power-industry-.av1.webm",
    "title": "How can Open-Source help the Wind Power industry?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-1940-energy-optimisation-smart-home-meets-smart-district.av1.webm",
    "title": "Energy optimisation: smart home meets smart district\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-3234-a-journey-accross-the-environmental-materiality-of-digital-services.av1.webm",
    "title": "A journey accross the environmental materiality of digital services\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2723-power-profiling-my-entire-house-with-the-firefox-profiler.av1.webm",
    "title": "Power profiling my entire house with the Firefox Profiler\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-3744-closing-energy-reimagining-this-ecosystem-through-open-source-devroom.av1.webm",
    "title": "Closing Energy: Reimagining this Ecosystem through Open Source devroom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-3612-beam-me-up-scotty.av1.webm",
    "title": "BEAM me up, Scotty\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2039-gleam-past-present-future-.av1.webm",
    "title": "Gleam: Past, present, future!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-3473-property-based-testing-in-elixir.av1.webm",
    "title": "Property based testing in Elixir\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2130-genstatem-unveiled-a-theoretical-exploration-of-state-machines.av1.webm",
    "title": "gen_statem Unveiled: A Theoretical Exploration of State Machines\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-3278-guess-less-with-erlang-doctor.av1.webm",
    "title": "Guess Less with Erlang Doctor\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2256-implementing-udp-protocols-in-elixir.av1.webm",
    "title": "Implementing UDP protocols in Elixir\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-3258-evolve-your-web-app-while-it-is-running.av1.webm",
    "title": "Evolve your (web)app while it is running\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-1635-mit-app-inventor.av1.webm",
    "title": "MIT App Inventor\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-1863-coderdojo.av1.webm",
    "title": "CoderDojo\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-1867-snap-.av1.webm",
    "title": "Snap!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-3736-youth-hacking-4-freedom.av1.webm",
    "title": "Youth Hacking 4 Freedom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-3104-live-coding-music-with-microblocks-and-microcontrollers-.av1.webm",
    "title": "Live coding music with MicroBlocks and microcontrollers.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-3550-hedy.av1.webm",
    "title": "Hedy\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-1935-google-blockly.av1.webm",
    "title": "Google Blockly\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-1865-zimjs-2d-pwa-apps-into-3d-vr-with-threejs.av1.webm",
    "title": "ZIMjs 2D PWA apps into 3D+VR with ThreeJS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2234-from-phone-hardware-to-mobile-linux.av1.webm",
    "title": "From phone hardware to mobile Linux\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-1716-u-boot-for-modern-qualcomm-phones.av1.webm",
    "title": "U-Boot for modern Qualcomm phones\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-1707-mainline-linux-on-qualcomm-socs-are-we-here-now-.av1.webm",
    "title": "Mainline Linux on Qualcomm SoCs, are we here now ?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3378-volte-for-foss.av1.webm",
    "title": "VoLTE for FOSS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3200-universal-serial-bug-a-tale-of-spontaneous-modem-resets.av1.webm",
    "title": "Universal Serial Bug - a tale of spontaneous modem resets\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3303-the-linux-phone-app-ecosystem.av1.webm",
    "title": "The Linux Phone App Ecosystem\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2386-flutter-about-the-nightmare-of-cross-platform-development-targetting-linux-mobile.av1.webm",
    "title": "Flutter - about the nightmare of cross platform development targetting Linux mobile\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2035-5g-in-modemmanager.av1.webm",
    "title": "5G in ModemManager\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3165-droidian-bridging-the-gap-between-various-platforms-with-convergence.av1.webm",
    "title": "Droidian - Bridging the gap between various platforms with convergence\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3017-genode-on-the-pinephone-on-track-to-real-world-usability.av1.webm",
    "title": "Genode on the PinePhone on track to real-world usability\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2972-wayland-s-input-method-is-broken-and-it-s-my-fault.av1.webm",
    "title": "Wayland's input-method is broken and it's my fault\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3364-why-not-run-opencl-accelerated-llm-on-your-phone-.av1.webm",
    "title": "Why not run OpenCL-accelerated LLM on your phone?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2851-the-journey-to-ubuntu-touch-20-04-on-pine64.av1.webm",
    "title": "The Journey to Ubuntu Touch 20.04 on PINE64\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3290-towards-a-bright-future-with-mobian-.av1.webm",
    "title": "Towards a bright future with Mobian?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3254-the-state-of-openjdk.av1.webm",
    "title": "The State of OpenJDK\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2427-a-decade-of-jdk-updates-in-openjdk.av1.webm",
    "title": "A decade of JDK Updates in OpenJDK\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-1876-exploring-quarkus-native-choices-and-implementation.av1.webm",
    "title": "Exploring Quarkus Native: Choices and Implementation\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3015-project-lilliput-compact-object-headers.av1.webm",
    "title": "Project Lilliput - Compact Object Headers\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2491-an-in-depth-look-at-jfr-in-graalvm-and-how-it-compares-to-jfr-in-openjdk.av1.webm",
    "title": "An in-depth look at JFR in GraalVM and how it compares to JFR in OpenJDK\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-1714-foreign-function-memory-api.av1.webm",
    "title": "Foreign Function & Memory API\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-1969-ruby-on-the-modern-jvm-fibers-ffi-and-more.av1.webm",
    "title": "Ruby on the Modern JVM: Fibers, FFI, and More\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2110-the-challenges-of-running-the-fuzion-language-natively-on-the-openjdk.av1.webm",
    "title": "The Challenges of Running the Fuzion Language Natively on the OpenJDK\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2154-openjdk-project-wakefield-the-wayland-desktop-for-jdk-on-linux.av1.webm",
    "title": "OpenJDK Project Wakefield : The Wayland Desktop for JDK on Linux\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3454-zeroing-and-the-semantic-gap-between-host-and-guest.av1.webm",
    "title": "Zeroing and the semantic gap between host and guest\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2336-cryostat-jfr-in-the-cloud.av1.webm",
    "title": "Cryostat: JFR in the cloud\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-1675-inner-workings-of-safepoints.av1.webm",
    "title": "Inner Workings of Safepoints\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3085-java-to-unlock-gpu-acceleration-for-polyglot-language-runtimes.av1.webm",
    "title": "Java… to unlock GPU acceleration for Polyglot Language Runtimes\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2713-how-to-bring-up-gcc-for-your-new-chip.av1.webm",
    "title": "How to bring up GCC for your new chip\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2759-what-can-compiler-explorer-do-for-gcc.av1.webm",
    "title": "What can Compiler-Explorer do for GCC\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2350-yacking-about-bison.av1.webm",
    "title": "Yacking about Bison\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2606-can-the-mold-linker-be-usr-bin-ld-.av1.webm",
    "title": "Can the mold linker be /usr/bin/ld?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2690-build-distribution-for-maintaining-the-famous-gcc-4-7.av1.webm",
    "title": "Build Distribution for Maintaining the Famous GCC 4.7\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2634-sega-dreamcast-homebrew-with-gcc.av1.webm",
    "title": "Sega Dreamcast Homebrew with GCC\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1704-the-secret-life-of-a-goroutine.av1.webm",
    "title": "The secret life of a goroutine\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1813-you-re-already-running-my-code-in-production-my-simple-journey-to-becoming-a-go-contributor-.av1.webm",
    "title": "You're already running my code in production: My simple journey to becoming a Go contributor.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2055-efficient-integration-testing-in-go-a-case-study-on-dapr.av1.webm",
    "title": "Efficient Integration Testing in Go: A Case Study on Dapr\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1927-effortless-bug-hunting-with-differential-fuzzing.av1.webm",
    "title": "Effortless Bug Hunting with Differential Fuzzing\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2000-maintaining-go-as-a-day-job-a-year-later.av1.webm",
    "title": "Maintaining Go as a day job - a year later\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1884-how-we-almost-secured-our-projects-by-writing-more-tests.av1.webm",
    "title": "How we almost secured our projects by writing more tests\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1868-dependency-injection-a-different-way-to-structure-a-project.av1.webm",
    "title": "Dependency injection: a different way to structure a project\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1853-putting-an-end-to-makefiles-in-go-projects-with-goreleaser.av1.webm",
    "title": "Putting an end to Makefiles in go projects with GoReleaser\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2568-rest-in-peace-using-generics-to-remove-rest-boilerplate.av1.webm",
    "title": "REST in Peace: using generics to remove REST boilerplate\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2621-low-code-graphical-apps-with-go-top-to-bottom-.av1.webm",
    "title": "Low code graphical apps with Go top to bottom!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1886-creating-a-multiplayer-game-in-go-from-zero.av1.webm",
    "title": "Creating a multiplayer game in Go, from zero\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2492--replacement-talk-having-fun-with-midi-and-go.av1.webm",
    "title": "[Replacement Talk] Having fun with MIDI and Go\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2562-smartwatch-firmware-in-go-on-tinygo-small-displays-and-building-a-delightful-developer-experience.av1.webm",
    "title": "Smartwatch firmware... in Go? On TinyGo, small displays, and building a delightful developer experience\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2270-go-without-wires-strikes-back.av1.webm",
    "title": "Go Without Wires Strikes Back\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2033-turnip-update-on-open-source-vulkan-driver-for-adreno-gpus.av1.webm",
    "title": "turnip: Update on Open Source Vulkan Driver for Adreno GPUs\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2841-graphics-stack-updates-for-raspberry-pi-devices.av1.webm",
    "title": "Graphics stack updates for Raspberry Pi devices\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-3177-delegated-compositing-utilizing-wayland-protocols-for-chromium-on-chromeos.av1.webm",
    "title": "Delegated compositing utilizing Wayland protocols for Chromium on ChromeOS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-3219-greenfield-wayland-in-the-browser-an-update.av1.webm",
    "title": "Greenfield: Wayland in the browser, an update\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2303--scratching-an-itch-by-patching-kmscon-or-how-opengl-can-lead-to-systems-programming-.av1.webm",
    "title": "\"Scratching an itch... by patching kmscon\" or \"How OpenGL can lead to systems-programming\"\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2667-flutter-in-embedded.av1.webm",
    "title": "Flutter in Embedded\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2631-building-cross-platform-gui-apps-with-ease-and-go-desktop-mobile-and-beyond-.av1.webm",
    "title": "Building Cross-platform GUI apps with ease (and Go) - desktop, mobile and beyond!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2570-the-fim-fbi-improved-universal-image-viewer-in-a-nutshell.av1.webm",
    "title": "The FIM (Fbi IMproved) Universal Image Viewer, in a Nutshell\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1740-productionizing-jupyter-notebooks.av1.webm",
    "title": "Productionizing Jupyter Notebooks\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1916-overcoming-mpi-abi-incompatibility.av1.webm",
    "title": "Overcoming MPI ABI incompatibility\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2338-pypartmc-engineering-python-to-fortran-bindings-in-c-for-use-in-julia-and-matlab.av1.webm",
    "title": "PyPartMC: engineering Python-to-Fortran bindings in C++, for use in Julia and Matlab\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2272-feeding-ml-models-with-the-data-from-the-databases-in-real-time.av1.webm",
    "title": "Feeding ML models with the data from the databases in real-time\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2275-hpc-container-conformance.av1.webm",
    "title": "HPC Container Conformance\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1970-automating-spark-and-pipeline-upgrades-while-testing-in-production.av1.webm",
    "title": "Automating Spark (and Pipeline) Upgrades While \"Testing\" in Production\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1784-semantically-driven-data-management-solution-for-i-o-intensive-hpc-workflows.av1.webm",
    "title": "Semantically-driven data management solution for I/O intensive HPC workflows\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2376-rctab-cloud-subscription-management-system.av1.webm",
    "title": "RCTab Cloud Subscription Management System\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2031-vector-search-in-modern-databases.av1.webm",
    "title": "Vector Search in Modern Databases\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1761-how-the-kubernetes-community-is-improving-kubernetes-for-hpc-ai-ml-workloads.av1.webm",
    "title": "How the Kubernetes Community is Improving Kubernetes for HPC/AI/ML Workloads\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2590-kubernetes-and-hpc-bare-metal-bros.av1.webm",
    "title": "Kubernetes and HPC: Bare-metal bros\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-3487-welcome-to-the-identity-and-access-management-devroom-.av1.webm",
    "title": "Welcome to the Identity and Access Management devroom!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2341-spicedb-mature-open-source-rebac.av1.webm",
    "title": "SpiceDB: mature, open source ReBAC\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2170-improving-infrastructure-security-through-access-auditing.av1.webm",
    "title": "Improving Infrastructure Security Through Access Auditing\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2425-role-of-iga-in-access-management-with-multilateral-identities.av1.webm",
    "title": "Role of IGA in Access Management with Multilateral Identities\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-1939-fusioniam-a-full-open-source-identity-access-management-solution.av1.webm",
    "title": "FusionIAM - a full Open Source Identity & Access Management solution\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2065-add-user-self-management-brokerage-and-federation-to-your-infrastructure-with-keycloak.av1.webm",
    "title": "Add user self-management, brokerage and federation to your infrastructure with Keycloak\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2618-ipa-tuura-freeipa-connector-for-keycloak.av1.webm",
    "title": "Ipa-tuura: FreeIPA connector for Keycloak\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-3753-passkey-authentication-the-result.av1.webm",
    "title": "Passkey authentication - the result\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2413-post-quantum-cryptography-transition-where-we-are-now.av1.webm",
    "title": "Post-Quantum Cryptography transition: where we are now\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-1669-beyond-passwords-secure-authentication-with-passkeys.av1.webm",
    "title": "Beyond passwords: secure authentication with passkeys\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-1665-making-ansible-playbooks-to-configure-single-sign-on-for-popular-open-source-applications.av1.webm",
    "title": "Making Ansible playbooks to configure Single Sign On for popular open source applications\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2681-fixing-a-kerberos-vulnerability-with-the-bare-necessities.av1.webm",
    "title": "Fixing a Kerberos vulnerability with the bare necessities\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2169-passwordless-authentication-in-the-gui.av1.webm",
    "title": "Passwordless authentication in the GUI\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2453-automated-integration-of-freeipa-with-ad-and-external-idp.av1.webm",
    "title": "Automated Integration of FreeIPA with AD and External IdP\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2102-connecting-ibm-aix-to-red-hat-identity-manager-freeipa-.av1.webm",
    "title": "Connecting IBM AIX to Red Hat Identity Manager (FreeIPA)\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2456-empowering-freeipa-a-dive-into-the-modern-webui.av1.webm",
    "title": "Empowering FreeIPA: a dive into the modern WebUI\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2587-posix-identities-out-of-oauth2-identity-providers-how-to-redesign-sssd-and-samba-.av1.webm",
    "title": "POSIX identities out of OAuth2 identity providers: how to redesign SSSD and Samba?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-2722-your-web-app-is-taking-up-too-much-ram-let-s-fix-it-.av1.webm",
    "title": "Your web app is taking up too much RAM. Let's fix it!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-2890-unraveling-javascript-s-heart-mastering-the-event-loop-for-peak-performance.av1.webm",
    "title": "Unraveling JavaScript's Heart: Mastering the Event Loop for Peak Performance\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-2540-codebase-conquest-how-nx-turbocharged-our-react-workflow.av1.webm",
    "title": "Codebase Conquest: How Nx Turbocharged Our React Workflow\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-2319-can-we-simplify-charting-libraries-.av1.webm",
    "title": "Can we simplify charting libraries?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-3665-building-your-own-javascript-runtime-with-rust.av1.webm",
    "title": "Building your own JavaScript runtime with Rust\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-2832-messageformat-the-future-of-i18n-on-the-web.av1.webm",
    "title": "MessageFormat: The future of i18n on the web\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-2649-all-things-astro.av1.webm",
    "title": "All Things Astro\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3214-how-to-win-1st-place-in-the-kernel-patch-statistics-tools-and-workflows.av1.webm",
    "title": "How to Win 1st Place in the Kernel Patch Statistics - Tools and Workflows\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2209-streamlining-kernel-hacking-with-mkosi-kernel.av1.webm",
    "title": "Streamlining kernel hacking with mkosi-kernel\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3102-libvpoll-create-synthetic-events-for-poll-select-and-friends.av1.webm",
    "title": "libvpoll: create synthetic events for poll, select and friends\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2987-more-flexible-user-namespaces.av1.webm",
    "title": "More flexible user namespaces\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3222-linux-matchmaking-helping-devices-and-drivers-find-each-other.av1.webm",
    "title": "Linux Matchmaking: Helping devices and drivers find each other\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2123-from-kernel-api-to-desktop-integration-how-do-we-integrate-battery-charge-limiting-in-the-desktop.av1.webm",
    "title": "From Kernel API to Desktop Integration, how do we integrate battery charge limiting in the desktop\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3217-converting-filesystems-to-support-idmapped-mounts.av1.webm",
    "title": "Converting filesystems to support idmapped mounts\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3371-what-is-linux-kernel-keystore-and-why-you-should-use-it-in-your-next-application.av1.webm",
    "title": "What is Linux kernel keystore and why you should use it in your next application\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2149-a-few-limitations-in-the-available-fs-related-system-calls.av1.webm",
    "title": "A few limitations in the available fs-related system calls\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3425-packet-where-are-you-track-in-the-stack-with-pwru.av1.webm",
    "title": "Packet, where are you?: Track in the stack with pwru\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-2595-figuring-out-trademark-policy-on-the-fly.av1.webm",
    "title": "Figuring out trademark policy on the fly\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3401-the-new-swiss-open-source-law-public-money-public-code-by-default.av1.webm",
    "title": "The new Swiss Open Source Law: \"Public Money Public Code\" by default\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-3582-welcome-to-the-llvm-dev-room.av1.webm",
    "title": "Welcome to the LLVM dev room\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2340-linker-scripts-in-lld-and-how-they-compare-with-gnu-ld.av1.webm",
    "title": "Linker Scripts in LLD and how they compare with GNU ld\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2371-patch-based-test-coverage-for-quick-test-feedback.av1.webm",
    "title": "Patch based test coverage for quick test feedback\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2254-elfconv-aot-compiler-that-translates-linux-aarch64-elf-binary-to-llvm-bitcode-targeting-webassembly.av1.webm",
    "title": "elfconv: AOT compiler that translates Linux/AArch64 ELF binary to LLVM bitcode targeting WebAssembly\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-1682-map-llvm-values-to-corresponding-source-level-expressions.av1.webm",
    "title": "Map LLVM values to corresponding source-level expressions\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3285-the-matrix-state-of-the-union.av1.webm",
    "title": "The Matrix State of the Union\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3157-interoperability-matrix.av1.webm",
    "title": "Interoperability & Matrix\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2817-let-s-talk-matrix-between-governments-and-citizens.av1.webm",
    "title": "Let's talk Matrix between Governments and Citizens\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2824-embracing-matrix-for-enhanced-communication-migrating-the-wordpress-community-from-slack-to-matrix.av1.webm",
    "title": "Embracing Matrix for Enhanced Communication: Migrating the WordPress Community from Slack to Matrix\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2464-neodatefix-a-solution-to-organising-meetings-in-matrix.av1.webm",
    "title": "NeoDateFix - A solution to organising meetings in Matrix\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2876-matrixrtc-the-future-of-matrix-calls.av1.webm",
    "title": "MatrixRTC: The Future of Matrix Calls\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3283-the-state-of-the-matrix-rust-sdk-in-2023.av1.webm",
    "title": "The state of the Matrix Rust SDK in 2023\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3011-a-microkernel-based-orchestrator-for-distributed-internet-services-.av1.webm",
    "title": "A microkernel-based orchestrator for distributed Internet services?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3269-run-node-js-in-a-unikernel-reliably.av1.webm",
    "title": "Run Node.js in a unikernel reliably\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3227-using-the-nova-microhypervisor-for-trusted-computing-at-scale.av1.webm",
    "title": "Using the NOVA Microhypervisor for Trusted Computing at Scale\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-1960-is-toro-unikernel-faster-for-mpi-.av1.webm",
    "title": "Is Toro unikernel faster for MPI?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3375-news-from-the-hermit-crab-from-soundness-foundations-to-gpu-virtualization.av1.webm",
    "title": "News from the Hermit Crab — From Soundness Foundations to GPU Virtualization\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3483-support-dynamically-linked-executables-via-linux-ld-so-and-implement-ena-driver-to-expand-application-of-osv.av1.webm",
    "title": "Support Dynamically Linked Executables via Linux ld.so and Implement ENA Driver to Expand Application of OSv\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3089-streamlining-application-development-for-genode-with-goa.av1.webm",
    "title": "Streamlining application development for Genode with Goa\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2179--protocols-security-of-starttls-in-the-e-mail-context.av1.webm",
    "title": "[Protocols] Security of STARTTLS in the E-Mail Context\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2647--protocols-things-we-wish-we-knew-before-starting-an-imap-library.av1.webm",
    "title": "[Protocols] Things we wish we knew before starting an IMAP library\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2534--protocols-unicode-in-email-rcpt-to-gr-gr-org-.av1.webm",
    "title": "[Protocols] Unicode in email: RCPT TO:<grå@grå.org>\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2135--jmap-jmap-getting-started.av1.webm",
    "title": "[JMAP] JMAP: Getting Started\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2477--jmap-openxport-jmap-a-php-library-for-data-portability.av1.webm",
    "title": "[JMAP] OpenXPort JMAP: a PHP library for Data Portability\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2538--jmap-intro-to-ltt-rs-a-jmap-client-for-android.av1.webm",
    "title": "[JMAP] Intro to Ltt.rs a JMAP client for Android\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2642--servers-aerogramme-a-multi-region-imap-server.av1.webm",
    "title": "[Servers] Aerogramme, a multi-region IMAP server\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-1870--servers-apache-james-modular-email-server.av1.webm",
    "title": "[Servers] Apache James: Modular email server\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2261--servers-mox-a-modern-full-featured-mail-server.av1.webm",
    "title": "[Servers] Mox: a modern full-featured mail server\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2497--clients-introduction-to-thunderbird-for-android.av1.webm",
    "title": "[Clients] Introduction to Thunderbird for Android\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2673--clients-taking-care-of-roundcube-webmail-current-status-and-future-prospects.av1.webm",
    "title": "[Clients] Taking care of Roundcube Webmail - current status and future prospects\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2849--security-thunderbird-email-security-plans-and-challenges-.av1.webm",
    "title": "[Security] Thunderbird Email Security, plans and challenges.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3026--security-email-autoconfiguration-and-2fa-for-email.av1.webm",
    "title": "[Security] Email Autoconfiguration, and 2FA for email\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2478--structuredemail-structured-vacation-notices-and-structured-email-for-roundcube.av1.webm",
    "title": "[StructuredEmail] Structured Vacation Notices and Structured Email for Roundcube\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2053--structuredemail-when-is-my-flight-semantic-data-extraction-in-kmail-and-nextcloud-mail.av1.webm",
    "title": "[StructuredEmail] When is my flight? - Semantic data extraction in KMail and Nextcloud Mail\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3624-welcome-to-the-monitoring-observability-devroom.av1.webm",
    "title": "Welcome to the Monitoring & Observability devroom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-1947-when-prometheus-met-opentelemetry.av1.webm",
    "title": "When Prometheus Met OpenTelemetry\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3445-strategic-sampling-architectural-approaches-to-efficient-telemetry.av1.webm",
    "title": "Strategic Sampling: Architectural Approaches to Efficient Telemetry\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-1734-unifying-observability-the-power-of-a-common-schema.av1.webm",
    "title": "Unifying Observability: The Power of a Common Schema\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-1921-linux-load-average-and-other-silly-metrics.av1.webm",
    "title": "Linux load average and other silly metrics\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3299-fast-cheap-diy-monitoring-with-open-source-analytics-and-visualization.av1.webm",
    "title": "Fast, Cheap, DIY Monitoring with Open Source Analytics and Visualization\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3499-implementing-distributed-traces-with-ebpf.av1.webm",
    "title": "Implementing distributed traces with eBPF\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3513-what-s-possible-in-observability-when-we-have-frame-pointers.av1.webm",
    "title": "What’s possible in observability when we have frame pointers\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3514-modern-application-observability-with-grafana-and-quickwit.av1.webm",
    "title": "Modern application observability with Grafana and Quickwit\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3262-what-is-ci-cd-observability-and-how-to-bring-observability-to-ci-cd-pipelines-.av1.webm",
    "title": "What is CI/CD observability, and how to bring observability to CI/CD pipelines?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-2128-introducing-observability-to-an-airline.av1.webm",
    "title": "Introducing Observability to an airline\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-1981-netdata-open-source-distributed-observability-pipeline-journey-and-challenges-.av1.webm",
    "title": "Netdata: Open Source, Distributed Observability Pipeline - Journey and Challenges.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1873-debugging-http-3-upload-speed-in-firefox.av1.webm",
    "title": "Debugging HTTP/3 upload speed in Firefox\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1822-the-mdn-curriculum-better-web-developers-for-a-better-web.av1.webm",
    "title": "The MDN Curriculum: Better web developers for a better web\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-2489-firefox-good-things-come-in-deb-packages.av1.webm",
    "title": "Firefox: Good things come in .deb packages\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1748-network-topology-discovery-how-it-really-works.av1.webm",
    "title": "Network Topology Discovery: how it really works\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-3328-iptgeofence-protecting-networks-using-geofencing-blocklists-and-service-analysis.av1.webm",
    "title": "ipt_geofence: Protecting Networks using GeoFencing, Blocklists and Service Analysis\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2812-testing-iptables-firewall-rules-with-scapy.av1.webm",
    "title": "Testing iptables firewall rules with scapy\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-3215-iputils-project-introduction.av1.webm",
    "title": "iputils project introduction\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2388-zeekjs-javascript-support-in-zeek.av1.webm",
    "title": "ZeekJS: JavaScript support in Zeek\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1818-bringing-routes-to-kubernetes-nodes-via-bgp-introducing-frr-k8s.av1.webm",
    "title": "Bringing routes to Kubernetes nodes via BGP: introducing frr-k8s\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1944-mutli-network-in-kubernetes-no-batteries-included.av1.webm",
    "title": "Multi-network in Kubernetes: No batteries included\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1659-declarative-networking-in-declarative-world.av1.webm",
    "title": "Declarative Networking in Declarative World\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-3062-i-want-my-own-cellular-network-having-fun-with-lte-networks-and-open5gs-.av1.webm",
    "title": "I want my own cellular network! Having fun with LTE networks and Open5Gs.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1983-remediating-thousands-of-untracked-security-vulnerabilities-in-nixpkgs.av1.webm",
    "title": "Remediating thousands of untracked security vulnerabilities in nixpkgs\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3058-nix-for-genetics-powering-a-bioinformatics-pipeline.av1.webm",
    "title": "Nix for genetics : powering a bioinformatics pipeline\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3045-automatic-boot-assessment-with-boot-counting.av1.webm",
    "title": "Automatic boot assessment with boot counting\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-2847-typhon-nix-based-continuous-integration.av1.webm",
    "title": "Typhon: Nix-based continuous integration\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1767-rix-an-r-package-for-reproducible-dev-environments-with-nix.av1.webm",
    "title": "rix: an R package for reproducible dev environments with Nix\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3125-preparing-a-30-year-long-project-with-nix-and-nixos.av1.webm",
    "title": "Preparing a 30 year-long project with Nix and NixOS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1692-running-nlnet-on-nixos.av1.webm",
    "title": "Running NLnet on NixOS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2763-dune-3d-the-making-of-a-maker-s-tool.av1.webm",
    "title": "Dune 3D - the making of a maker's tool\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2913-comprehensible-open-hardware-building-the-open-book.av1.webm",
    "title": "Comprehensible Open Hardware: Building the Open Book\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-3086-freecad-state-of-the-union.av1.webm",
    "title": "FreeCAD - state of the union\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-1709-kicad-status-update.av1.webm",
    "title": "KiCad Status Update\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-3087-librepcb-status-update.av1.webm",
    "title": "LibrePCB Status Update\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2834-ngspice-circuit-simulator-stand-alone-and-embedded-into-kicad.av1.webm",
    "title": "ngspice circuit simulator - stand-alone and embedded into KiCad\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-3052-modos-building-an-ecosystem-of-open-hardware-e-ink-devices.av1.webm",
    "title": "Modos: Building an Ecosystem of Open-Hardware E Ink Devices\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2019-qubik-a-1p-pocketqube-satellite-platform.av1.webm",
    "title": "QUBIK a 1p PocketQube satellite platform\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-3070-jumpstarter-open-hardware-in-the-loop-for-everybody.av1.webm",
    "title": "Jumpstarter: Open Hardware In The Loop for everybody\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-3497-from-hackathon-idea-to-hackaday-prize-how-we-make-a-braille-embosser-.av1.webm",
    "title": "From hackathon idea to hackaday prize - How we make a Braille embosser.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-3226-automated-documentation-for-open-source-hardware.av1.webm",
    "title": "Automated Documentation for Open Source Hardware\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-3022-sharing-parametric-models-as-web-apps-with-replicad.av1.webm",
    "title": "Sharing parametric models as web apps with replicad\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3079-webassembly-webcomponents-and-media-filters-all-at-once-a-proposal-to-open-the-web-to-variety-of-formats.av1.webm",
    "title": "WebAssembly, WebComponents and media filters all at once: a proposal to open the Web to variety of formats\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3590-gstreamer-state-of-the-union-2024.av1.webm",
    "title": "GStreamer: State of the Union 2024\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3567-streaming-live-using-rist-on-demand-to-thousands-how-you-can-have-your-cake-and-eat-it-too.av1.webm",
    "title": "Streaming live using RIST On Demand to thousands, how you can have your cake and eat it too\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3557-the-state-of-video-offloading-on-the-linux-desktop.av1.webm",
    "title": "The state of video offloading on the Linux Desktop\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3573-livepeer-catalyst-and-the-conspiracy-to-solve-video-for-everybody-forever.av1.webm",
    "title": "Livepeer Catalyst and The Conspiracy to Solve Video for Everybody Forever\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2423-multithreading-and-other-developments-in-the-ffmpeg-transcoder.av1.webm",
    "title": "Multithreading and other developments in the ffmpeg transcoder\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3549-streamcrafter-in-browser-broadcasting.av1.webm",
    "title": "StreamCrafter - In browser broadcasting\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-1988-pipewire-state-of-the-union.av1.webm",
    "title": "PipeWire State of the Union\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2083-generating-music-with-open-tools-apis-and-no-ai-.av1.webm",
    "title": "Generating music with Open tools, APIs, and NO AI!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3537-open-source-community-updates.av1.webm",
    "title": "Open Source Community Updates\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3538-ffmpeg-vvc-decoder.av1.webm",
    "title": "FFmpeg VVC Decoder\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2804-edit-video-audio-with-or-without-vim.av1.webm",
    "title": "Edit video/audio with or without Vim\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2802-s2s-peertube-instance-dedicated-to-sign-language.av1.webm",
    "title": "S2S: PeerTube instance dedicated to Sign Language\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3199-5g-mag-reference-tools-bringing-5g-media-to-life.av1.webm",
    "title": "5G-MAG Reference Tools: Bringing 5G Media to Life\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2959-dublang-a-multi-language-live-coding-system.av1.webm",
    "title": "dublang, a multi-language live coding system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2400-vvdec-arm-optimizing-an-open-source-vvc-decoder-for-arm-architectures.av1.webm",
    "title": "VVdeC<>Arm: Optimizing an open source VVC decoder for Arm architectures\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3253-bridging-research-and-open-source-the-genesis-of-gephi-lite.av1.webm",
    "title": "Bridging Research and Open Source: the genesis of Gephi Lite\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3394-cosma-a-visualization-tool-for-network-synthesis.av1.webm",
    "title": "Cosma, a visualization tool for network synthesis\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3190-from-the-lab-to-jupyter-a-brief-history-of-computational-notebooks-from-a-sts-perspective.av1.webm",
    "title": "From the lab to Jupyter : a brief history of computational notebooks from a STS perspective\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3406-prompt-compass-a-methodological-approach-to-evaluating-the-use-of-large-language-models-in-ssh-research.av1.webm",
    "title": "Prompt Compass: A Methodological Approach to Evaluating the Use of Large Language Models in SSH research\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3434-beyond-ratings-empowering-communities-through-wikirate-for-transparent-corporate-impact-research-and-analysis-.av1.webm",
    "title": "Beyond Ratings: Empowering Communities through Wikirate for Transparent Corporate Impact Research and Analysis.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3479-from-grassroots-to-standard-practice-how-an-open-science-society-shaped-university-initiatives.av1.webm",
    "title": "From Grassroots to Standard Practice: how an Open Science society shaped university initiatives\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2928-bridging-contributor-s-knowledge-and-the-technology-of-the-turing-way-an-open-guide-for-data-science.av1.webm",
    "title": "Bridging contributor's knowledge and the technology of The Turing Way, an open guide for data science\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3205-the-carpentriesoffline-teaching-foundational-data-science-and-coding-skills-with-little-or-no-internet-access.av1.webm",
    "title": "The CarpentriesOffline: Teaching Foundational Data Science and Coding Skills with Little or no Internet Access\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3185-the-french-open-science-monitor-steering-the-science-based-on-open-bibliographic-databases.av1.webm",
    "title": "The French Open Science Monitor: steering the science based on open bibliographic databases\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3436-infra-finder-increasing-visibility-of-open-technologies-for-open-science.av1.webm",
    "title": "Infra Finder: Increasing visibility of open technologies for open science\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2405-best-practices-for-research-in-open-source-ecosystems.av1.webm",
    "title": "Best practices for research in open source ecosystems\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3109-updating-open-data-standards.av1.webm",
    "title": "Updating open data standards\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2797-wikimedia-projects-and-openstreetmap-as-an-open-research-infrastructure.av1.webm",
    "title": "Wikimedia projects and OpenStreetMap as an Open Research Infrastructure\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3204-detecting-propaganda-on-facebook-and-instagram-ads-using-meta-api.av1.webm",
    "title": "Detecting Propaganda on Facebook and Instagram Ads using Meta API\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3452-unlocking-research-data-management-with-inveniordm.av1.webm",
    "title": "Unlocking Research Data Management with InvenioRDM\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3010-making-openrefine-more-reproducible.av1.webm",
    "title": "Making OpenRefine more reproducible\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3179-qadence-a-library-for-digital-analog-quantum-computing.av1.webm",
    "title": "Qadence - A library for Digital Analog Quantum Computing\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3316-science-without-secrets-how-galaxy-democratizes-data-analysis.av1.webm",
    "title": "Science without secrets – how Galaxy democratizes data analysis\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3415-workflow-managers-in-high-energy-physics-enhancing-analyses-with-snakemake.av1.webm",
    "title": "Workflow managers in high-energy physics: enhancing analyses with Snakemake\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-2223-open-neuroscience-practical-suggestions-for-conducting-open-neuroscience-research.av1.webm",
    "title": "Open Neuroscience: practical suggestions for conducting open neuroscience research\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3323-minimill-a-miniature-field-mill-electrometer-for-airborne-platforms.av1.webm",
    "title": "MiniMill: a miniature Field Mill Electrometer for airborne platforms\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3694-welcome-to-the-eu-policy-workshop-devroom.av1.webm",
    "title": "Welcome to the EU Policy Workshop Devroom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-1838-cra-pld-begin-workshop-how-will-the-open-source-community-adapt-to-the-new-eu-cyber-resilience-act-and-product-liability-directive.av1.webm",
    "title": "CRA & PLD: [begin workshop] How will the open-source community adapt to the new EU Cyber Resilience Act and Product Liability Directive\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3395-cra-40-new-ways-the-cra-can-accidentally-harm-open-source.av1.webm",
    "title": "CRA: 40 new ways the CRA can accidentally harm open source\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3697-pld-when-software-causes-harm-who-pays-and-why-.av1.webm",
    "title": "PLD: When software causes harm – who pays and why?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3676-cra-pld-panel.av1.webm",
    "title": "CRA & PLD: panel\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3679-cra-pld-workshop.av1.webm",
    "title": "CRA & PLD: workshop\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3137-cra-pld-cra-conformance-for-open-source-projects.av1.webm",
    "title": "CRA & PLD: CRA conformance for Open Source Projects\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3677-cra-pld-rapporteur-playback.av1.webm",
    "title": "CRA & PLD: rapporteur playback\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2451-foss-policy-engagement-a-cra-retrospective-.av1.webm",
    "title": "FOSS policy engagement: a CRA retrospective.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3709-foss-policy-engagement-the-impact-of-the-ngi-open-source-projects-on-eu-policy-and-values.av1.webm",
    "title": "FOSS policy engagement: The impact of the NGI Open Source projects on EU policy and values\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3692-public-services-interoperability-begin-workshop-free-open-source-and-interoperable-european-public-services.av1.webm",
    "title": "Public services interoperability: [begin workshop] Free/open source and Interoperable European public services\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3710-public-services-interoperability-the-interoperable-europe-act-the-challenges-and-opportunities-for-the-free-and-open-source-communities-.av1.webm",
    "title": "Public services interoperability: The Interoperable Europe Act; the challenges and opportunities for the free and open source communities.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3711-public-services-interoperability-workshop-interoperable-europe-act.av1.webm",
    "title": "Public services interoperability: workshop Interoperable Europe Act\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3712-public-services-interoperability-open-source-efforts-in-and-around-the-european-commission-and-how-about-a-next-ec-open-source-strategy.av1.webm",
    "title": "Public services interoperability: Open Source efforts in and around the European Commission; and how about a next EC open source strategy\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3713-public-services-interoperability-workshop-open-source-strategy-at-the-european-commission.av1.webm",
    "title": "Public services interoperability: workshop Open Source strategy at the European Commission\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3714-public-services-interoperability-rapporteur-playback.av1.webm",
    "title": "Public services interoperability: rapporteur playback\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3315-digital-services-interoperability-intertwining-eu-telecom-law-the-dma-internet-devices-and-free-software.av1.webm",
    "title": "Digital Services Interoperability: Intertwining EU telecom law, the DMA, internet devices and Free Software\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3696-eu-policy-devroom-wrap-up.av1.webm",
    "title": "EU Policy Devroom Wrap-Up\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-3049-reimagining-personal-computing-with-e-ink-community-insights-and-design-challenges.av1.webm",
    "title": "Reimagining Personal Computing with E ink: Community Insights and Design Challenges\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-2897-liquid-prompt-yes-we-can-drastically-rethink-the-design-of-a-shell-prompt.av1.webm",
    "title": "Liquid Prompt: yes, we can drastically rethink the design of a shell prompt\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-3135-bad-ux-is-bad-security-adventures-in-qubes-os-ux-design.av1.webm",
    "title": "Bad UX is Bad Security: Adventures in Qubes OS UX Design\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-3509-penpot-2-0-is-here-.av1.webm",
    "title": "Penpot 2.0 is here!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-2936-open-source-firmware-status-on-amd-platforms-2024-5th-edition.av1.webm",
    "title": "Open Source Firmware status on AMD platforms 2024 - 5th edition\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-2854-immune-guard-streamlining-boot-and-kernel-security-in-the-cloud.av1.webm",
    "title": "immune Guard: Streamlining Boot and Kernel Security in the Cloud\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-1987-systemd-boot-systemd-stub-ukis.av1.webm",
    "title": "systemd-boot, systemd-stub, UKIs\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-3309-kernel-command-line-to-configure-userspace-considered-harmful.av1.webm",
    "title": "Kernel command line to configure userspace considered harmful\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3598-beyond-joins-and-indexes.av1.webm",
    "title": "Beyond Joins and Indexes\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3600-isolation-levels-and-mvcc-in-sql-databases-a-technical-comparative-study.av1.webm",
    "title": "Isolation Levels and MVCC in SQL Databases: A Technical Comparative Study\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3601-reducing-costs-and-improving-performance-with-data-modeling-in-postgres.av1.webm",
    "title": "Reducing Costs and Improving Performance With Data Modeling in Postgres\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3602-clustering-in-postgresql-because-one-database-server-is-never-enough-and-neither-is-two-.av1.webm",
    "title": "Clustering in PostgreSQL: Because one database server is never enough (and neither is two)\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3604-your-virtual-dba-postgresql-on-kubernetes-using-an-operator-.av1.webm",
    "title": "Your Virtual DBA (PostgreSQL on Kubernetes using an Operator)\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3486-introduction-to-the-public-code-and-digital-public-goods-devroom.av1.webm",
    "title": "Introduction to the Public Code and Digital Public Goods devroom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2818-some-updates-on-public-code-in-germany.av1.webm",
    "title": "Some updates on Public Code in Germany\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2666-gnu-health-incorporating-digital-public-goods-in-the-european-healthcare-system.av1.webm",
    "title": "GNU Health. Incorporating Digital Public Goods in the European healthcare system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2658-from-disconnected-elements-to-a-harmonious-ecosystem-the-epiverse-trace-project.av1.webm",
    "title": "From disconnected elements to a harmonious ecosystem : The Epiverse-TRACE project\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2954-legislation-editing-open-software-leos-an-innovative-open-source-solution-for-drafting-legislation-.av1.webm",
    "title": "Legislation Editing Open Software (LEOS) - an innovative open-source solution for drafting legislation​\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-1706-trubudget-a-dpg-to-support-the-project-workflow-in-international-multi-stakeholder-environments.av1.webm",
    "title": "TruBudget - a DPG to support the project workflow in international multi-stakeholder environments\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2167-moodle-empowering-educators-to-improve-our-world.av1.webm",
    "title": "Moodle: Empowering educators to improve our world\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3312-what-can-digital-open-source-projects-do-to-reduce-our-environmental-footprint.av1.webm",
    "title": "What can digital open source projects do to reduce our environmental footprint\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3755-open-terms-archive.av1.webm",
    "title": "Open Terms Archive\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2243-developing-in-public-open-source-tech-education.av1.webm",
    "title": "Developing in Public : Open Source Tech Education\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2112-how-to-use-private-data-in-generative-ai-end-to-end-solution-for-retrieval-augmented-generation-with-cratedb-and-langchain.av1.webm",
    "title": "How to Use Private Data in Generative AI: End-to-End Solution for Retrieval Augmented Generation with CrateDB and LangChain\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2072-a-murder-party-with-lea.av1.webm",
    "title": "A murder party with Lea\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2326-a-slow-migration-from-django-templates-to-vue-graphql.av1.webm",
    "title": "A slow migration from Django templates to Vue+GraphQL\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1894-django-migrations-friend-or-foe-optimize-them-for-testing.av1.webm",
    "title": "Django migrations, friend or foe? Optimize them for testing\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2443-how-can-we-trust-3rd-party-code-using-python-to-understand-the-trust-relationships-within-the-python-ecosystem.av1.webm",
    "title": "How can we trust 3rd party code? Using Python to understand the trust relationships within the python ecosystem\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1996-match-all-things-python-parsing-structured-content-with-python-s-new-match-statement.av1.webm",
    "title": "Match all things Python: Parsing structured content with Python's new match statement\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2592-annotated-a-type-hint-you-can-use-at-runtime.av1.webm",
    "title": "Annotated, a type hint you can use at runtime\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1678-python-3-12-s-new-monitoring-and-debugging-api.av1.webm",
    "title": "Python 3.12's new monitoring and debugging API\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2337-how-i-ve-built-a-web-frontend-for-a-federated-communication-tool-with-brython.av1.webm",
    "title": "How I've Built a Web Frontend for a Federated Communication Tool with Brython\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2601-opening-railways-and-open-transport-devroom.av1.webm",
    "title": "Opening Railways and Open Transport devroom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-1898-open-standards-open-data-open-source-tools-their-governance-and-future.av1.webm",
    "title": "Open standards, open data, open-source tools: their governance and future\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2202-rust-transit-libraries-to-manage-transit-data-in-rust.av1.webm",
    "title": "Rust-transit: libraries to manage transit data in rust\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2550-counting-on-openness-privacy-safe-passenger-counting.av1.webm",
    "title": "Counting on openness: Privacy-safe passenger counting\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2203-matsim-at-sbb-using-and-contributing-to-the-open-source-transport-simulation-for-advanced-passenger-demand-modeling-.av1.webm",
    "title": "MATSim at SBB: Using and contributing to the open-source transport simulation for advanced passenger demand modeling.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2594-bending-geographic-maps-for-enhanced-railway-space-time-diagrams.av1.webm",
    "title": "Bending geographic maps for enhanced railway space-time diagrams\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2650-mareco-algorithm-how-to-drive-a-train-using-the-least-amount-of-energy.av1.webm",
    "title": "MARECO algorithm: how to drive a train using the least amount of energy\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2665-railway-signaling-detecting-conflicts-in-a-complex-world.av1.webm",
    "title": "Railway signaling: detecting conflicts in a complex world\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2409-how-we-at-deutsche-bahn-develop-iot-use-cases-quickly-and-cost-effectively.av1.webm",
    "title": "How we at Deutsche Bahn develop IoT use cases quickly and cost-effectively\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2363-transportr-the-past-the-present-and-the-future.av1.webm",
    "title": "Transportr: the Past, the Present and the Future\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-1772-software-needs-of-a-volunteer-operated-heritage-railway.av1.webm",
    "title": "Software needs of a volunteer operated heritage railway\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3111-enhancing-the-video-call-experience-with-forward-error-correction.av1.webm",
    "title": "Enhancing the video call experience with Forward Error Correction\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1907-shig-distribute-and-clone-live-streams-among-fediverse-instances.av1.webm",
    "title": "Shig: distribute and clone live streams among Fediverse instances\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3000-getting-av1-svc-to-work-in-the-janus-webrtc-server.av1.webm",
    "title": "Getting AV1/SVC to work in the Janus WebRTC Server\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3646-using-gstreamer-to-build-real-time-applications-with-golang.av1.webm",
    "title": "Using GStreamer to build real-time applications with Golang\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3123-build-your-enum-lcr-server-using-cgrates.av1.webm",
    "title": "Build your ENUM LCR Server using CGRateS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-2930-secsipidx-library-cli-tool-and-restapi-server-for-stir-shaken.av1.webm",
    "title": "SecSIPIdX - Library, CLI tool and RESTApi server for STIR/SHAKEN\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2721-the-big-adventure-of-little-professor-and-its-4-bits-handheld-friends-running-tms-1000.av1.webm",
    "title": "The big adventure of little professor and its 4-bits handheld friends running TMS 1000\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1771-gameboy-advance-hacking-for-retrogamers.av1.webm",
    "title": "Gameboy Advance hacking for retrogamers\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2334-running-dos-unix-on-an-8-bit-commodore.av1.webm",
    "title": "Running DOS & Unix on an 8-bit Commodore\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1718-a-game-boy-and-his-cellphone.av1.webm",
    "title": "A Game Boy and his cellphone\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1742-pistorm-the-evolution-of-an-open-source-amiga-accelerator.av1.webm",
    "title": "PiStorm - The evolution of an open source Amiga accelerator\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2008-a-journey-documenting-the-sanco-8003-computer.av1.webm",
    "title": "A journey documenting the Sanco 8003 computer\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2898-controlling-a-6-degree-robot-arm-using-a-48k-zx-spectrum.av1.webm",
    "title": "Controlling a 6 degree Robot Arm using a 48K ZX Spectrum\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-2458-mambo-dynamic-binary-modification-tool-for-risc-v.av1.webm",
    "title": "MAMBO - Dynamic Binary Modification Tool for RISC-V\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-2327-unleashing-risc-v-in-managed-runtimes-navigating-extensions-memory-models-and-performance-challenges-in-openjdk.av1.webm",
    "title": "Unleashing RISC-V in Managed Runtimes: Navigating Extensions, Memory Models, and Performance Challenges in OpenJDK\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-3752-a-framework-for-risc-v-sbi-verification-and-isa-extension-validation.av1.webm",
    "title": "A framework for RISC-V SBI verification and ISA extension validation\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2293-the-best-case-scenario.av1.webm",
    "title": "The best `case` scenario\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2182-besides-web-a-worker-story-.av1.webm",
    "title": "Besides Web: a Worker story.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2473-backtracie-and-the-quest-for-prettier-ruby-backtraces.av1.webm",
    "title": "Backtracie and the quest for prettier Ruby backtraces\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2682-semver-in-the-rust-ecosystem-breakage-tooling-and-edge-cases.av1.webm",
    "title": "SemVer in the Rust ecosystem: breakage, tooling, and edge cases\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-1638-writing-your-own-rust-linter.av1.webm",
    "title": "Writing your own Rust linter\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2207-the-plan-for-gccrs.av1.webm",
    "title": "The plan for gccrs\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2322-hardware-pointer-checks-in-a-rust-application-near-you-.av1.webm",
    "title": "Hardware pointer checks in a Rust application near you?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2571-proving-performance.av1.webm",
    "title": "Proving Performance\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2632-friend-or-foe-inside-exploring-in-process-isolation-to-maintain-memory-safety-for-unsafe-rust.av1.webm",
    "title": "Friend or Foe Inside? Exploring In-Process Isolation to Maintain Memory Safety for Unsafe Rust\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2434-the-four-horsemen-of-bad-rust-code.av1.webm",
    "title": "The Four Horsemen of Bad Rust Code\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-1934-introducing-ratatui-a-rust-library-to-cook-up-terminal-user-interfaces.av1.webm",
    "title": "Introducing Ratatui: A Rust library to cook up terminal user interfaces\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-1691-wasm-101-porting-a-sega-game-gear-emulator-to-the-browser.av1.webm",
    "title": "WASM 101: porting a Sega Game Gear emulator to the browser\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2703-a-deep-dive-into-tower.av1.webm",
    "title": "A Deep Dive into Tower\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2321-embedding-servo-in-rust-projects.av1.webm",
    "title": "Embedding Servo in Rust projects\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2469-thunderbird-how-to-exchange-rot-for-rust.av1.webm",
    "title": "Thunderbird: How to Exchange Rot For Rust\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2420-the-journey-of-hacking-in-a-new-serde-dataformat.av1.webm",
    "title": "The journey of hacking in a new serde dataformat\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-3172-spdx-3-0-a-migration-journey.av1.webm",
    "title": "SPDX 3.0 - a migration journey\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2920-know-your-ingredients-security-starts-with-the-sbom.av1.webm",
    "title": "Know Your Ingredients: Security Starts With the SBOM\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-3073-make-your-software-products-trustable.av1.webm",
    "title": "Make your software products trustable\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-3358-can-sboms-become-first-class-citizens-in-open-source-ecosystems-.av1.webm",
    "title": "Can SBOMs become first-class citizens in Open Source ecosystems?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-3318-spdx-in-the-yocto-project.av1.webm",
    "title": "SPDX in the Yocto Project\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-1896-12-months-of-sboms-an-experience-report.av1.webm",
    "title": "12 months of SBOMs - an experience report\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-3146-phantom-dependencies-in-python-and-what-to-do-about-them-.av1.webm",
    "title": "Phantom dependencies in Python (and what to do about them)\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-1685-open-source-based-software-composition-analysis-at-scale.av1.webm",
    "title": "Open Source based Software Composition Analysis at scale\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-3623-panel-discussion-best-practices-managing-sboms-in-the-supply-chain.av1.webm",
    "title": "Panel discussion: Best practices managing SBOMs in the supply chain\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-3074-sharing-and-reusing-sboms-with-the-osselot-curation-database.av1.webm",
    "title": "Sharing and reusing SBOMs with the OSSelot curation database\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2530-welcome-to-the-devroom-and-announcements.av1.webm",
    "title": "Welcome to the Devroom and Announcements\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1643-using-gpu-for-real-time-sdr-signal-processing.av1.webm",
    "title": "Using GPU for real-time SDR Signal processing\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2050-covert-ground-based-synthetic-aperture-radar-using-a-wifi-emitter-and-sdr-receiver.av1.webm",
    "title": "Covert Ground Based Synthetic Aperture RADAR using a WiFi emitter and SDR receiver\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2084-design-of-a-follow-up-qo-100-payload-.av1.webm",
    "title": "Design of a follow-up QO-100 payload -\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1841-maia-sdr-an-open-source-fpga-based-project-for-ad936x-zynq-radios.av1.webm",
    "title": "Maia SDR: an open-source FPGA-based project for AD936x+Zynq radios\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1646-quickstream-a-new-sdr-framework.av1.webm",
    "title": "quickstream: a new SDR framework\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2348-an-open-source-digital-radio-protocol-for-amateur-radio.av1.webm",
    "title": "An open source digital radio protocol for amateur radio\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2537-openrtx-an-open-source-firmware-for-ham-radio-devices.av1.webm",
    "title": "OpenRTX: an open source firmware for ham radio devices\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1641-expanding-iqengine-into-a-hub-for-previewing-rf-signal-processing-software.av1.webm",
    "title": "Expanding IQEngine into a Hub for Previewing RF Signal Processing Software\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1721-dapnet-bringing-pagers-back-to-the-21st-century.av1.webm",
    "title": "DAPNET: Bringing pagers back to the 21st Century\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2709-srsran-project-update.av1.webm",
    "title": "srsRAN Project Update\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-1959-boosting-cephfs-security-in-kubernetes-rook-s-intelligent-network-fencing-for-uninterrupted-data-flow-and-workload-harmony-.av1.webm",
    "title": "Boosting CephFS Security in Kubernetes: Rook's Intelligent Network Fencing for Uninterrupted Data Flow and Workload Harmony!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2127-crash-consistent-group-snapshots-in-cephfs-for-k8s-csi-and-you-.av1.webm",
    "title": "Crash-consistent group snapshots in CephFS for k8s CSI and you!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2974-deploying-a-hyper-converged-infrastructure-with-ceph-across-the-cloud-edge-continuum.av1.webm",
    "title": "Deploying a hyper-converged infrastructure with Ceph across the Cloud-Edge Continuum\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-3281-chorus-effortless-ceph-s3-petabyte-migration.av1.webm",
    "title": "Chorus - Effortless Ceph S3 Petabyte Migration\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-1851-smb-for-linux-with-smb3-posix-extensions.av1.webm",
    "title": "SMB for Linux with SMB3 POSIX extensions\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-3009-advances-in-garage-the-low-tech-storage-platform-for-geo-distributed-clusters.av1.webm",
    "title": "Advances in Garage, the low-tech storage platform for geo-distributed clusters\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-3416-microceph-get-ceph-up-and-running-in-minutes.av1.webm",
    "title": "MicroCeph: Get Ceph Up and Running in Minutes\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-1671-welcome-to-testing-and-continuous-delivery-devroom.av1.webm",
    "title": "Welcome to Testing and Continuous Delivery devroom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2964-streamlining-developer-experience-the-power-of-ci-cd-standardization-and-interoperability.av1.webm",
    "title": "Streamlining Developer Experience: The Power of CI/CD Standardization and Interoperability\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2687-ghosting-the-hardware.av1.webm",
    "title": "Ghosting the hardware\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3475-pushing-test-lab-to-its-limits-performance-tracking-techniques.av1.webm",
    "title": "Pushing test lab to its limits: performance tracking techniques\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2968-performance-testing-and-why-even-the-imperfect-one-is-important.av1.webm",
    "title": "Performance testing and why even the imperfect one is important\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-1805-squash-the-flakes-how-to-minimize-the-impact-of-flaky-tests.av1.webm",
    "title": "squash the flakes! - how to minimize the impact of flaky tests\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2983-from-free-lunch-to-dog-fooding-a-culinary-journey-in-crafting-iac-for-kairos-testing-and-building.av1.webm",
    "title": "From \"Free-Lunch\" to Dog-Fooding: A Culinary Journey in Crafting IaC for Kairos Testing and Building\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3263-practical-ci-cd-observability-with-opentelemetry.av1.webm",
    "title": "Practical CI/CD Observability with OpenTelemetry\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2194-chaos-engineering-in-action-enhancing-resilience-in-strimzi.av1.webm",
    "title": "Chaos Engineering in Action: Enhancing Resilience in Strimzi\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2502-progressive-delivery-made-easy-with-argo-rollouts.av1.webm",
    "title": "Progressive Delivery Made Easy with Argo Rollouts\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2282-own-your-ci-with-nix.av1.webm",
    "title": "Own your CI with Nix\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-1802-testing-go-command-line-programs-with-go-internal-testscript-.av1.webm",
    "title": "Testing Go command line programs with `go-internal/testscript`\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2486-how-mutation-testing-got-practical.av1.webm",
    "title": "How mutation testing got practical\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3431-running-systemd-integration-tests-with-mkosi.av1.webm",
    "title": "Running systemd integration tests with mkosi\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-2877-making-it-easy-to-get-to-slsa-level-2.av1.webm",
    "title": "Making it easy to get to SLSA level 2\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2208/fosdem-2024-3029-are-project-tests-enough-for-automated-dependency-updates-a-case-study-of-262-java-projects-on-github.av1.webm",
    "title": "Are Project Tests Enough for Automated Dependency Updates? A Case Study of 262 Java Projects on Github\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-1733-perl-at-payprop.av1.webm",
    "title": "Perl at PayProp\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-3743-open-food-facts-learning-and-using-perl-in-2024-to-transform-the-food-system-.av1.webm",
    "title": "Open Food Facts: Learning and using Perl in 2024 to transform the food system !\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2346-synergy-a-chat-bot-framework.av1.webm",
    "title": "Synergy: a chat bot framework\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2395-the-cpan-security-working-group.av1.webm",
    "title": "The CPAN Security Working Group\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-3500-openqa-how-do-you-test-a-testing-software-.av1.webm",
    "title": "openQA - How do you test a testing software?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2390-corinna-perl-s-new-object-oriented-system.av1.webm",
    "title": "Corinna—Perl's new object-oriented system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2238-the-art-of-concurrent-scripting-with-raku.av1.webm",
    "title": "The Art of Concurrent Scripting with Raku\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-3570-updates-from-the-psc.av1.webm",
    "title": "Updates from the PSC\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2528-open-source-docops.av1.webm",
    "title": "Open Source DocOps\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-1815-easily-going-beyond-markdown-with-material-for-mkdocs.av1.webm",
    "title": "Easily Going Beyond MarkDown with Material for MkDocs\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2542-drop-the-docs-and-embrace-the-model-with-gaphor.av1.webm",
    "title": "Drop the docs and embrace the model with Gaphor\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2379-experimenting-with-ai-and-llm-to-make-docs-searchable-through-a-chat-application.av1.webm",
    "title": "Experimenting with AI and LLM to make docs searchable through a chat application\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2125-embeddable-code-playgrounds-for-fun-and-profit.av1.webm",
    "title": "Embeddable code playgrounds for fun and profit\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-3516-welcome-to-the-translations-devroom.av1.webm",
    "title": "Welcome to the Translations DevRoom\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-1759-a-universal-data-model-for-localizable-messages.av1.webm",
    "title": "A universal data model for localizable messages\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-1906-lessons-learnt-as-a-translation-contributor-the-past-4-years.av1.webm",
    "title": "Lessons learnt as a translation contributor the past 4 years\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2071-long-term-effort-to-keep-translations-up-to-date.av1.webm",
    "title": "Long Term Effort to Keep Translations Up-To-Date\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-3348-using-open-source-ais-for-accessibility-and-localization.av1.webm",
    "title": "Using Open Source AIs for Accessibility and Localization\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2411-the-importance-of-web-performance-to-information-equity.av1.webm",
    "title": "The importance of Web Performance to Information Equity\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2088-let-s-build-a-rum-system-with-open-source-tools.av1.webm",
    "title": "Let's build a RUM system with open source tools\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2003-better-than-loading-fast-is-loading-instantly-.av1.webm",
    "title": "Better than loading fast… is loading instantly!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2410-keyboard-interactions.av1.webm",
    "title": "Keyboard Interactions\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2162-web-performance-at-mozilla-and-wikimedia.av1.webm",
    "title": "Web Performance at Mozilla and Wikimedia\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2777-understanding-how-the-web-browser-works-or-tracing-your-way-out-of-performance-problems.av1.webm",
    "title": "Understanding how the web browser works, or tracing your way out of (performance) problems\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2773-fast-javascript-with-data-oriented-design.av1.webm",
    "title": "Fast JavaScript with Data-Oriented Design\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2266-from-google-adsense-to-foss-lightning-fast-privacy-friendly-banners.av1.webm",
    "title": "From Google AdSense to FOSS: Lightning-fast privacy-friendly banners\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-1975-insights-from-the-rum-archive.av1.webm",
    "title": "Insights from the RUM Archive\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2394-linux-on-a-confidential-vm-in-a-cloud-where-s-the-challenge-.av1.webm",
    "title": "Linux on a Confidential VM in a cloud: where's the challenge?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1663-how-much-do-you-know-about-snapshot.av1.webm",
    "title": "How Much Do You Know about Snapshot\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2024-uki-addons-and-extensions-safely-extending-ukis-kernel-command-line-and-initrd.av1.webm",
    "title": "UKI addons and extensions: safely extending UKIs kernel command line and initrd\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-3003-from-virtualization-platform-to-hybrid-cloud-solution-a-hands-on-account.av1.webm",
    "title": "From Virtualization Platform to Hybrid Cloud Solution: A Hands-On Account\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1910-making-virtio-sing-implementing-virtio-sound-in-rust-vmm-project.av1.webm",
    "title": "Making VirtIO sing - implementing virtio-sound in rust-vmm project\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2262-exercising-qemu-generated-acpi-smbios-tables-using-biosbits-from-within-a-guest-vm-.av1.webm",
    "title": "Exercising QEMU generated ACPI/SMBIOS tables using Biosbits from within a guest VM.\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1708-one-sdn-to-connect-them-all.av1.webm",
    "title": "One SDN to connect them all\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2943-deploy-kubernetes-from-kubernetes-an-overview-of-cluster-api.av1.webm",
    "title": "Deploy Kubernetes... From Kubernetes: an overview of Cluster API\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2129-operating-kubernetes-across-hypervisors-with-cluster-api-gitops.av1.webm",
    "title": "Operating Kubernetes Across Hypervisors with Cluster API & GitOps\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-3021--snapsafety-de-duplicating-state-across-virtual-machine-clones.av1.webm",
    "title": "#snapsafety: de-duplicating state across Virtual Machine clones\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1686-pipewire-audio-backend-in-qemu.av1.webm",
    "title": "Pipewire audio backend in QEMU\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2794-ai-driven-observability-and-operations-in-cloud-edge-systems.av1.webm",
    "title": "AI-Driven Observability and Operations in Cloud-Edge Systems\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1828-bare-metal-networking-for-everyone.av1.webm",
    "title": "Bare-Metal Networking For Everyone\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-3256-instant-ramen-quick-and-easy-multi-cluster-kubernetes-development-on-your-laptop.av1.webm",
    "title": "Instant Ramen: Quick and easy multi-cluster Kubernetes development on your laptop\n"
  }
]
