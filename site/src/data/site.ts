export type NavId = "home" | "projects" | "blog" | "cv" | "contact";

const profiles = {
  github: {
    id: "github",
    label: "GitHub",
    href: "https://github.com/DidacLL",
    description: "Repositories, source code, and technical work.",
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
    description: "Source, build tooling, and history for this portfolio.",
    image: "img/routing-map.png",
    imageAlt: "AgenticCareerBoost routing map"
  }
} as const;

export const site = {
  defaultTitle: "Dídac Llorens — Software Engineer",
  description: "Personal developer portfolio by Dídac Llorens: P3CTeX, AAAAT, backend systems, AI-assisted engineering, and technical notes.",
  identity: {
    name: "Dídac Llorens",
    avatar: "img/avatar.jpg",
    avatarAlt: "Dídac Llorens avatar",
    lines: ["Software engineer · Barcelona", "Tools · systems · data · backend"]
  },
  navigation: [
    { id: "home" as NavId, number: "00", label: "Home", kicker: "profile", description: "Profile, current work, and what I like building." },
    { id: "projects" as NavId, number: "01", label: "Projects", kicker: "work", description: "P3CTeX, AAAAT, AgenticCareerBoost, and IronBank." },
    { id: "blog" as NavId, number: "02", label: "Blog", kicker: "notes", description: "Notes on software, tooling, systems, and experiments." },
    { id: "cv" as NavId, number: "03", label: "CV", kicker: "cv", description: "Web curriculum views and the downloadable public PDF." },
    { id: "contact" as NavId, number: "04", label: "Contact", kicker: "signal", description: "Public profiles and ways to reach me." }
  ],
  external: [profiles.github, profiles.linkedin, profiles.source],
  contact: {
    channels: [profiles.linkedin, profiles.github, profiles.source]
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
      lines: ["software engineering · Barcelona", "tools · systems · documents · experiments"],
      links: [
        { label: "Projects", navId: "projects" as NavId },
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
    document: "DOCUMENT",
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
    project: "PROJECT",
    projectSignal: "PROJECT SIGNAL",
    publicRecord: "public record",
    status: "STATUS",
    repository: "Repository",
    openRepository: "Open repository ↗",
    openProject: "Open project",
    selectedProjectCaption: "project / selected work",
    channel: "CHANNEL",
    article: "ARTICLE",
    image: "IMAGE",
    return: "RETURN",
    returnHome: "Return to the home document →",
    view: "VIEW",
    pdf: "PDF",
    date: "DATE",
    tags: "TAGS",
    records: "RECORDS",
    count: "COUNT",
    cvViews: "CV views"
  }
} as const;
