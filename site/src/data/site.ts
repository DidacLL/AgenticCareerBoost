export const site = {
  title: "Dídac Llorens",
  description: "Software engineer in Barcelona working on technical systems, documentation, and practical AI workflows.",
  identity: { mark: "DL", name: "Dídac Llorens", location: "Barcelona", role: "Software engineer" },
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
    previous: "Previous signal", next: "Next signal", expand: "maximize", collapse: "minimize",
    slides: [
      { image: "/img/me.png", alt: "Dídac Llorens portrait in monitor signal treatment", caption: "portrait / default signal" },
      { image: "/img/avatar.jpg", alt: "Dídac Llorens portrait alternate signal", caption: "portrait / alternate signal" }
    ]
  },
  banner: { image: "/img/418_informal_banner.jpg", alt: "418 visual channel" },
  footer: "© Dídac Llorens · public technical work and source-led evidence."
} as const;
