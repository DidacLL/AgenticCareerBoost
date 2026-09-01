export type NavId = "home" | "projects" | "blog" | "cv" | "focus" | "contact";

export const site = {
  defaultTitle: "Dídac Llorens — Software Engineer",
  description: "Public engineering portfolio: software systems, AI workflows, data, backend work, LaTeX tooling, and technical documentation.",
  identity: {
    mark: "DL_418",
    name: "Dídac Llorens",
    lines: ["Software engineer · Barcelona", "Systems · AI workflows · data · backend"]
  },
  navigation: [
    { id: "home" as NavId, number: "00", label: "Home", kicker: "profile", description: "Technical profile, current direction, and selected routes." },
    { id: "projects" as NavId, number: "01", label: "Projects", kicker: "work", description: "AgenticCareerBoost, P3CTeX, AAAAT, and IronBank." },
    { id: "blog" as NavId, number: "02", label: "Blog", kicker: "notes", description: "Dated technical notes and historical project records." },
    { id: "cv" as NavId, number: "03", label: "CV", kicker: "cv", description: "Role-focused web CV views and the public PDF." },
    { id: "focus" as NavId, number: "04", label: "Focus", kicker: "routes", description: "ML/data, AI workflow, and backend/tooling views." },
    { id: "contact" as NavId, number: "05", label: "Contact", kicker: "signal", description: "Public profile and contact channels." }
  ],
  external: [
    { label: "GitHub", href: "https://github.com/DidacLL" },
    { label: "LinkedIn", href: "https://www.linkedin.com/in/didacllorens/" },
    { label: "Site source", href: "https://github.com/DidacLL/AgenticCareerBoost" }
  ],
  cv: {
    sourceUrl: "https://github.com/DidacLL/AgenticCareerBoost/blob/main/agents/cv/tex/didac-llorens-cv.tex",
    pdfLabel: "Public PDF",
    sourceLabel: "LaTeX source"
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
      alt: "Portrait of Dídac Llorens",
      lines: ["software engineering · Barcelona", "implementation · systems · documentation"],
      links: [
        { label: "Open CV", navId: "cv" as NavId },
        { label: "Contact", navId: "contact" as NavId }
      ],
      caption: "identity / current profile"
    }
  },
  banner: {
    image: "img/418_informal_banner.jpg",
    alt: "418 banner artwork from Dídac Llorens visual identity",
    caption: "visual channel / 418"
  },
  ui: {
    primaryNavigation: "Primary navigation",
    externalLinks: "External links",
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
    relatedWork: "RELATED WORK",
    relatedNotes: "RELATED NOTES",
    channel: "CHANNEL"
  }
} as const;