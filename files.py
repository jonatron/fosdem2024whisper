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
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3274-opendesk-the-open-source-collaborative-suite.av1.webm",
    "title": "openDesk - The Open Source collaborative suite\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-1858-using-generative-ai-and-content-service-platforms-together.av1.webm",
    "title": "Using Generative AI and Content Service Platforms together\n"
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
    "href": "https://video.fosdem.org/2024/ub2252a/fosdem-2024-3187-vscode-container-wasm-an-extension-of-vscode-on-browser-for-running-containers-within-your-browser.av1.webm",
    "title": "vscode-container-wasm: An Extension of VSCode on Browser for Running Containers Within Your Browser\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2784-debug-your-stage-1-systemd-with-gdb-and-the-nixos-test-framework.av1.webm",
    "title": "Debug your stage-1 systemd with GDB and the NixOS test framework\n"
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
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2509-using-flexmeasures-to-build-a-climate-tech-startup-in-15-minutes.av1.webm",
    "title": "Using FlexMeasures to build a climate tech startup, in 15 minutes\n"
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
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-3303-the-linux-phone-app-ecosystem.av1.webm",
    "title": "The Linux Phone App Ecosystem\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1309/fosdem-2024-2386-flutter-about-the-nightmare-of-cross-platform-development-targetting-linux-mobile.av1.webm",
    "title": "Flutter - about the nightmare of cross platform development targetting Linux mobile\n"
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
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-2110-the-challenges-of-running-the-fuzion-language-natively-on-the-openjdk.av1.webm",
    "title": "The Challenges of Running the Fuzion Language Natively on the OpenJDK\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5132/fosdem-2024-3085-java-to-unlock-gpu-acceleration-for-polyglot-language-runtimes.av1.webm",
    "title": "Java… to unlock GPU acceleration for Polyglot Language Runtimes\n"
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
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1970-automating-spark-and-pipeline-upgrades-while-testing-in-production.av1.webm",
    "title": "Automating Spark (and Pipeline) Upgrades While \"Testing\" in Production\n"
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
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-2170-improving-infrastructure-security-through-access-auditing.av1.webm",
    "title": "Improving Infrastructure Security Through Access Auditing\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h1301/fosdem-2024-2540-codebase-conquest-how-nx-turbocharged-our-react-workflow.av1.webm",
    "title": "Codebase Conquest: How Nx Turbocharged Our React Workflow\n"
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
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-3215-iputils-project-introduction.av1.webm",
    "title": "iputils project introduction\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-2388-zeekjs-javascript-support-in-zeek.av1.webm",
    "title": "ZeekJS: JavaScript support in Zeek\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub5230/fosdem-2024-1659-declarative-networking-in-declarative-world.av1.webm",
    "title": "Declarative Networking in Declarative World\n"
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
    "href": "https://video.fosdem.org/2024/aw1120/fosdem-2024-2167-moodle-empowering-educators-to-improve-our-world.av1.webm",
    "title": "Moodle: Empowering educators to improve our world\n"
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
    "href": "https://video.fosdem.org/2024/h1302/fosdem-2024-3123-build-your-enum-lcr-server-using-cgrates.av1.webm",
    "title": "Build your ENUM LCR Server using CGRateS\n"
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
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-1733-perl-at-payprop.av1.webm",
    "title": "Perl at PayProp\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k3401/fosdem-2024-3743-open-food-facts-learning-and-using-perl-in-2024-to-transform-the-food-system-.av1.webm",
    "title": "Open Food Facts: Learning and using Perl in 2024 to transform the food system !\n"
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
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1828-bare-metal-networking-for-everyone.av1.webm",
    "title": "Bare-Metal Networking For Everyone\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-3256-instant-ramen-quick-and-easy-multi-cluster-kubernetes-development-on-your-laptop.av1.webm",
    "title": "Instant Ramen: Quick and easy multi-cluster Kubernetes development on your laptop\n"
  }
]
