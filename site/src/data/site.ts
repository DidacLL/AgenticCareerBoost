export type NavId = "home" | "projects" | "blog" | "cv" | "contact";

const profiles = {
  github: {
    id: "github",
    label: "GitHub",
    href: "https://github.com/DidacLL",
    description: "Repositories, technical work, and source history.",
    image: "img/logos/GitHub_Invertocat_White.png",
    imageAlt: "GitHub logo"
  },
  linkedin: {
    id: "linkedin",
    label: "LinkedIn",
    href: "https://www.linkedin.com/in/didacllorens/",
    description: "Professional profile and direct messages.",
    image: "img/logos/InBug-White.png",
    imageAlt: "LinkedIn logo"
  },
  source: {
    id: "source",
    label: "Site source",
    href: "https://github.com/DidacLL/AgenticCareerBoost",
    description: "Source repository for this portfolio.",
    image: "img/routing-map.png",
    imageAlt: "AgenticCareerBoost routing map"
  }
} as const;

export const site = {
  defaultTitle: "Dídac Llorens — Software Engineer",
  description: "Public engineering portfolio: software systems, AI workflows, data, backend work, LaTeX tooling, and technical documentation.",
  identity: {
    name: "Dídac Llorens",
    avatar: "img/me.png",
    avatarAlt: "Portrait of Dídac Llorens",
    lines: ["Software engineer · Barcelona", "Systems · AI workflows · data · backend"]
  },
  navigation: [
    { id: "home" as NavId, number: "00", label: "Home", kicker: "profile", description: "Technical profile, current direction, and selected routes." },
    { id: "projects" as NavId, number: "01", label: "Projects", kicker: "work", description: "AgenticCareerBoost, P3CTeX, AAAAT, and IronBank." },
    { id: "blog" as NavId, number: "02", label: "Blog", kicker: "notes", description: "Dated technical notes and historical project records." },
    { id: "cv" as NavId, number: "03", label: "CV", kicker: "cv", description: "Role-focused web CV views and the public PDF." },
    { id: "contact" as NavId, number: "04", label: "Contact", kicker: "signal", description: "Public profile and contact channels." }
  ],
  external: [profiles.github, profiles.linkedin, profiles.source],
  contact: {
    channels: [profiles.linkedin, profiles.github]
  },
  cv: {
    sourceUrl: "https://github.com/DidacLL/AgenticCareerBoost/blob/main/agents/cv/tex/didac-llorens-cv.tex",
    pdfLabel: "Public PDF",
    sourceLabel: "LaTeX source",
    logo: "img/logos/250px-PDF_file_icon.png",
    logoAlt: "PDF document icon",
    contactDescription: "Role-focused web views and the public PDF."
  },
  theme: {
    storageKey: "didac-site-theme",
    dark: "dark mode",
    light: "light mode",
    toggle: "Toggle colour theme"
  },
  monitor: {
    previous: "Previous signal",
    next: "Next signal",
    expand: "maximize",
    collapse: "minimize",
    label: "Visual signal monitor",
    profile: {
      label: "PROFILE / 418",
      title: "Dídac Llorens",
      image: "img/me.png",
      alt: "Dídac Llorens portrait rendered as a retro monitor feed",
      lines: ["software engineering · Barcelona", "implementation · systems · documentation"],
      links: [
        { label: "Open CV", navId: "cv" as NavId },
        { label: "Contact", navId: "contact" as NavId }
      ],
      caption: "portrait / default signal"
    }
  },
  banner: {
    image: "img/418_informal_banner.jpg",
    alt: "418 banner artwork from Dídac Llorens visual identity",
    caption: "visual channel / 418"
  },
  ui: {
    primaryNavigation: "Primary navigation",
    system: "SYSTEM",
    mode: "MODE",
    theme: "THEME",
    links: "LINKS",
    profile: "PROFILE",
    lanes: "TARGET LANES",
    selectedWork: "SELECTED WORK",
    technicalBase: "TECHNICAL BASE",
    source: "SOURCE",
    context: "CONTEXT",
    note: "NOTE",
    index: "INDEX",
    projectSignal: "PROJECT SIGNAL",
    channel: "CHANNEL"
  }
} as const;
