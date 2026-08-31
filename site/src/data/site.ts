export const site = {
  title: "Dídac Llorens",
  description: "Software engineer in Barcelona working on LaTeX tooling, local-first career tooling, static publishing, technical documentation, AI workflows, and backend/data systems.",
  identity: {
    mark: "DL",
    name: "Dídac Llorens",
    location: "Barcelona",
    role: "Software engineer"
  },
  navigation: [
    { number: "00", label: "Home", path: "/" },
    { number: "01", label: "Projects", path: "/projects/" },
    { number: "02", label: "Blog", path: "/blog/" },
    { number: "03", label: "CV", path: "/cv/ml/" },
    { number: "04", label: "Contact", path: "/contact/" }
  ],
  external: [
    { label: "GitHub", href: "https://github.com/DidacLL" },
    { label: "LinkedIn", href: "https://www.linkedin.com/in/didacllorens/" },
    { label: "Source repo", href: "https://github.com/DidacLL/AgenticCareerBoost" }
  ],
  theme: { toggle: "Toggle colour theme", dark: "dark mode", light: "light mode" },
  gallery: {
    previous: "Previous portrait slide",
    next: "Next portrait slide",
    expand: "maximize",
    collapse: "minimize",
    image: "/img/me.png",
    alt: "Dídac Llorens portrait rendered as a retro monitor feed",
    caption: "portrait / default signal"
  },
  banner: { image: "/img/418_informal_banner.jpg", alt: "418 banner artwork with Dídac Llorens visual identity" },
  footer: "© Dídac Llorens · public technical work and source-led evidence."
} as const;
