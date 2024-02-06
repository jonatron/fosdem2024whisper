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
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2850-where-have-the-women-of-tech-history-gone-.av1.webm",
    "title": "Where have the women of tech history gone?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-2522-outreachy-1000-interns.av1.webm",
    "title": "Outreachy: 1000 interns\n"
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
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3648-privacy-respecting-usage-metrics-for-free-software-projects.av1.webm",
    "title": "Privacy-respecting usage metrics for free software projects\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k1105/fosdem-2024-3370-an-engineer-s-guide-to-linux-kernel-upgrades.av1.webm",
    "title": "An engineer's guide to Linux Kernel upgrades\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-3595-open-food-facts-acting-on-the-health-and-environnemental-impacts-of-the-food-system.av1.webm",
    "title": "Open Food Facts : Acting on the health and environnemental impacts of the food system\n"
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
    "href": "https://video.fosdem.org/2024/h2215/fosdem-2024-2231-a-lazy-developer-s-approach-to-building-real-time-web-applications.av1.webm",
    "title": "A Lazy Developer’s Approach to Building Real-Time Web Applications\n"
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
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2396-opentalk-video-conferencing-secure-and-gdpr-compliant.av1.webm",
    "title": "OpenTalk - Video conferencing secure and GDPR compliant\n"
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
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-1858-using-generative-ai-and-content-service-platforms-together.av1.webm",
    "title": "Using Generative AI and Content Service Platforms together\n"
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
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-1780-how-do-you-change-the-governance-model-of-an-established-open-source-project-.av1.webm",
    "title": "How do you change the governance model of an established open source project?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2114/fosdem-2024-2105-kickstarting-an-open-source-culture-a-guide-for-mentors.av1.webm",
    "title": "Kickstarting an Open Source Culture: A Guide for Mentors\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2372-sev-step-a-single-stepping-framework-for-amd-sev.av1.webm",
    "title": "SEV-Step: A Single-Stepping Framework for AMD-SEV\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2317-the-ups-and-downs-of-running-enclaves-in-production.av1.webm",
    "title": "The ups and downs of running enclaves in production\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2461-integrity-protect-workloads-with-mushroom.av1.webm",
    "title": "Integrity Protect Workloads with Mushroom\n"
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
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3060-what-s-new-in-containerd-2-0-.av1.webm",
    "title": "What's new in Containerd 2.0!\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3187-vscode-container-wasm-an-extension-of-vscode-on-browser-for-running-containers-within-your-browser.av1.webm",
    "title": "vscode-container-wasm: An Extension of VSCode on Browser for Running Containers Within Your Browser\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2784-debug-your-stage-1-systemd-with-gdb-and-the-nixos-test-framework.av1.webm",
    "title": "Debug your stage-1 systemd with GDB and the NixOS test framework\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2305-open-source-leadership-at-scale-how-1300-people-improved-drupal-s-multilingual-features.av1.webm",
    "title": "Open source leadership at scale, how 1300+ people improved Drupal’s multilingual features\n"
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
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2198-the-first-13-years-of-blockchain-name-systems.av1.webm",
    "title": "The first 13 years of blockchain name systems\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3136-embedded-security-2023.av1.webm",
    "title": "Embedded Security 2023\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-2479-the-small-device-c-compiler-sdcc-.av1.webm",
    "title": "The Small Device C Compiler (SDCC)\n"
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
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2826-breathing-life-into-legacy-an-open-source-emulator-of-legacy-apple-devices.av1.webm",
    "title": "Breathing Life into Legacy: An Open-Source Emulator of Legacy Apple Devices\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2509-using-flexmeasures-to-build-a-climate-tech-startup-in-15-minutes.av1.webm",
    "title": "Using FlexMeasures to build a climate tech startup, in 15 minutes\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2155-enhancing-ocpp-with-e2e-security-and-binary-data-streams-for-a-more-secure-energy-ecosystem.av1.webm",
    "title": "Enhancing OCPP with E2E-Security and Binary Data Streams for a more Secure Energy Ecosystem\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2640-sharing-the-operational-cost-of-europe-s-electricity-grid-optimization-and-transparency-through-open-source.av1.webm",
    "title": "Sharing the operational cost of Europe's electricity grid: optimization and transparency through open source\n"
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
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2130-genstatem-unveiled-a-theoretical-exploration-of-state-machines.av1.webm",
    "title": "gen_statem Unveiled: A Theoretical Exploration of State Machines\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-3278-guess-less-with-erlang-doctor.av1.webm",
    "title": "Guess Less with Erlang Doctor\n"
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
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2851-the-journey-to-ubuntu-touch-20-04-on-pine64.av1.webm",
    "title": "The Journey to Ubuntu Touch 20.04 on PINE64\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3290-towards-a-bright-future-with-mobian-.av1.webm",
    "title": "Towards a bright future with Mobian?\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-1876-exploring-quarkus-native-choices-and-implementation.av1.webm",
    "title": "Exploring Quarkus Native: Choices and Implementation\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2491-an-in-depth-look-at-jfr-in-graalvm-and-how-it-compares-to-jfr-in-openjdk.av1.webm",
    "title": "An in-depth look at JFR in GraalVM and how it compares to JFR in OpenJDK\n"
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
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3085-java-to-unlock-gpu-acceleration-for-polyglot-language-runtimes.av1.webm",
    "title": "Java… to unlock GPU acceleration for Polyglot Language Runtimes\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2759-what-can-compiler-explorer-do-for-gcc.av1.webm",
    "title": "What can Compiler-Explorer do for GCC\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2606-can-the-mold-linker-be-usr-bin-ld-.av1.webm",
    "title": "Can the mold linker be /usr/bin/ld?\n"
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
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1884-how-we-almost-secured-our-projects-by-writing-more-tests.av1.webm",
    "title": "How we almost secured our projects by writing more tests\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-1868-dependency-injection-a-different-way-to-structure-a-project.av1.webm",
    "title": "Dependency injection: a different way to structure a project\n"
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
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2033-turnip-update-on-open-source-vulkan-driver-for-adreno-gpus.av1.webm",
    "title": "turnip: Update on Open Source Vulkan Driver for Adreno GPUs\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3201/fosdem-2024-2841-graphics-stack-updates-for-raspberry-pi-devices.av1.webm",
    "title": "Graphics stack updates for Raspberry Pi devices\n"
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
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1761-how-the-kubernetes-community-is-improving-kubernetes-for-hpc-ai-ml-workloads.av1.webm",
    "title": "How the Kubernetes Community is Improving Kubernetes for HPC/AI/ML Workloads\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-2590-kubernetes-and-hpc-bare-metal-bros.av1.webm",
    "title": "Kubernetes and HPC: Bare-metal bros\n"
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
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-2540-codebase-conquest-how-nx-turbocharged-our-react-workflow.av1.webm",
    "title": "Codebase Conquest: How Nx Turbocharged Our React Workflow\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3401-the-new-swiss-open-source-law-public-money-public-code-by-default.av1.webm",
    "title": "The new Swiss Open Source Law: \"Public Money Public Code\" by default\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-1682-map-llvm-values-to-corresponding-source-level-expressions.av1.webm",
    "title": "Map LLVM values to corresponding source-level expressions\n"
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
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2477--jmap-openxport-jmap-a-php-library-for-data-portability.av1.webm",
    "title": "[JMAP] OpenXPort JMAP: a PHP library for Data Portability\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2538--jmap-intro-to-ltt-rs-a-jmap-client-for-android.av1.webm",
    "title": "[JMAP] Intro to Ltt.rs a JMAP client for Android\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-1734-unifying-observability-the-power-of-a-common-schema.av1.webm",
    "title": "Unifying Observability: The Power of a Common Schema\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2220/fosdem-2024-3499-implementing-distributed-traces-with-ebpf.av1.webm",
    "title": "Implementing distributed traces with eBPF\n"
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
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1944-mutli-network-in-kubernetes-no-batteries-included.av1.webm",
    "title": "Mutli-network in Kubernetes: No batteries included\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1659-declarative-networking-in-declarative-world.av1.webm",
    "title": "Declarative Networking in Declarative World\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1983-remediating-thousands-of-untracked-security-vulnerabilities-in-nixpkgs.av1.webm",
    "title": "Remediating thousands of untracked security vulnerabilities in nixpkgs\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3045-automatic-boot-assessment-with-boot-counting.av1.webm",
    "title": "Automatic boot assessment with boot counting\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1767-rix-an-r-package-for-reproducible-dev-environments-with-nix.av1.webm",
    "title": "rix: an R package for reproducible dev environments with Nix\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-1692-running-nlnet-on-nixos.av1.webm",
    "title": "Running NLnet on NixOS\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2913-comprehensible-open-hardware-building-the-open-book.av1.webm",
    "title": "Comprehensible Open Hardware: Building the Open Book\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3567-streaming-live-using-rist-on-demand-to-thousands-how-you-can-have-your-cake-and-eat-it-too.av1.webm",
    "title": "Streaming live using RIST On Demand to thousands, how you can have your cake and eat it too\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub4132/fosdem-2024-3190-from-the-lab-to-jupyter-a-brief-history-of-computational-notebooks-from-a-sts-perspective.av1.webm",
    "title": "From the lab to Jupyter : a brief history of computational notebooks from a STS perspective\n"
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
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3676-cra-pld-panel.av1.webm",
    "title": "CRA & PLD: panel\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-3135-bad-ux-is-bad-security-adventures-in-qubes-os-ux-design.av1.webm",
    "title": "Bad UX is Bad Security: Adventures in Qubes OS UX Design\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-3486-introduction-to-the-public-code-and-digital-public-goods-devroom.av1.webm",
    "title": "Introduction to the Public Code and Digital Public Goods devroom\n"
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
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2167-moodle-empowering-educators-to-improve-our-world.av1.webm",
    "title": "Moodle: Empowering educators to improve our world\n"
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
    "href": "https://video.fosdem.org/2024/ud2218a/fosdem-2024-2443-how-can-we-trust-3rd-party-code-using-python-to-understand-the-trust-relationships-within-the-python-ecosystem.av1.webm",
    "title": "How can we trust 3rd party code? Using Python to understand the trust relationships within the python ecosystem\n"
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
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1742-pistorm-the-evolution-of-an-open-source-amiga-accelerator.av1.webm",
    "title": "PiStorm - The evolution of an open source Amiga accelerator\n"
  },
  {
    "href": "https://video.fosdem.org/2024/aw1126/fosdem-2024-2458-mambo-dynamic-binary-modification-tool-for-risc-v.av1.webm",
    "title": "MAMBO - Dynamic Binary Modification Tool for RISC-V\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-1691-wasm-101-porting-a-sega-game-gear-emulator-to-the-browser.av1.webm",
    "title": "WASM 101: porting a Sega Game Gear emulator to the browser\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1308/fosdem-2024-2469-thunderbird-how-to-exchange-rot-for-rust.av1.webm",
    "title": "Thunderbird: How to Exchange Rot For Rust\n"
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
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2050-covert-ground-based-synthetic-aperture-radar-using-a-wifi-emitter-and-sdr-receiver.av1.webm",
    "title": "Covert Ground Based Synthetic Aperture RADAR using a WiFi emitter and SDR receiver\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2348-an-open-source-digital-radio-protocol-for-amateur-radio.av1.webm",
    "title": "An open source digital radio protocol for amateur radio\n"
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
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2390-corinna-perl-s-new-object-oriented-system.av1.webm",
    "title": "Corinna—Perl's new object-oriented system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4601/fosdem-2024-2528-open-source-docops.av1.webm",
    "title": "Open Source DocOps\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2088-let-s-build-a-rum-system-with-open-source-tools.av1.webm",
    "title": "Let's build a RUM system with open source tools\n"
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
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1663-how-much-do-you-know-about-snapshot.av1.webm",
    "title": "How Much Do You Know about Snapshot\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2024-uki-addons-and-extensions-safely-extending-ukis-kernel-command-line-and-initrd.av1.webm",
    "title": "UKI addons and extensions: safely extending UKIs kernel command line and initrd\n"
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
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-2129-operating-kubernetes-across-hypervisors-with-cluster-api-gitops.av1.webm",
    "title": "Operating Kubernetes Across Hypervisors with Cluster API & GitOps\n"
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

