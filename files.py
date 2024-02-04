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
    "href": "https://video.fosdem.org/2024/janson/fosdem-2024-3683-the-regulators-are-coming-one-year-on.av1.webm",
    "title": "The Regulators Are Coming: One Year On\n"
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
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-3443-public-calendars-aggregation-using-linkal.av1.webm",
    "title": "Public calendars aggregation using Linkal\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2213/fosdem-2024-2396-opentalk-video-conferencing-secure-and-gdpr-compliant.av1.webm",
    "title": "OpenTalk - Video conferencing secure and GDPR compliant\n"
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
    "href": "https://video.fosdem.org/2024/k4401/fosdem-2024-2784-debug-your-stage-1-systemd-with-gdb-and-the-nixos-test-framework.av1.webm",
    "title": "Debug your stage-1 systemd with GDB and the NixOS test framework\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-3056-dns-for-i2p-distributed-network-without-central-authority.av1.webm",
    "title": "DNS for I2P: Distributed Network without Central Authority\n"
  },
  {
    "href": "https://video.fosdem.org/2024/k4201/fosdem-2024-2198-the-first-13-years-of-blockchain-name-systems.av1.webm",
    "title": "The first 13 years of blockchain name systems\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ud2120/fosdem-2024-3264-an-open-source-open-hardware-offline-finding-system.av1.webm",
    "title": "An open-source, open-hardware offline finding system\n"
  },
  {
    "href": "https://video.fosdem.org/2024/h2214/fosdem-2024-2509-using-flexmeasures-to-build-a-climate-tech-startup-in-15-minutes.av1.webm",
    "title": "Using FlexMeasures to build a climate tech startup, in 15 minutes\n"
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
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1970-automating-spark-and-pipeline-upgrades-while-testing-in-production.av1.webm",
    "title": "Automating Spark (and Pipeline) Upgrades While \"Testing\" in Production\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ua2118/fosdem-2024-1761-how-the-kubernetes-community-is-improving-kubernetes-for-hpc-ai-ml-workloads.av1.webm",
    "title": "How the Kubernetes Community is Improving Kubernetes for HPC/AI/ML Workloads\n"
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
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1910-making-virtio-sing-implementing-virtio-sound-in-rust-vmm-project.av1.webm",
    "title": "Making VirtIO sing - implementing virtio-sound in rust-vmm project\n"
  },
  {
    "href": "https://video.fosdem.org/2024/ub2147/fosdem-2024-1828-bare-metal-networking-for-everyone.av1.webm",
    "title": "Bare-Metal Networking For Everyone\n"
  }
]
