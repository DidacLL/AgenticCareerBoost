import { defaultLocale, type Locale } from "../lib/i18n";

export type NavId = "home" | "projects" | "blog" | "cv" | "contact";

const profileBase = {
  github: {
    id: "github",
    label: "GitHub",
    href: "https://github.com/DidacLL",
    image: "img/logos/GitHub_Invertocat_White.png",
    imageAlt: "GitHub logo"
  },
  linkedin: {
    id: "linkedin",
    label: "LinkedIn",
    href: "https://www.linkedin.com/in/didacllorens/",
    image: "img/logos/InBug-White.png",
    imageAlt: "LinkedIn logo"
  },
  source: {
    id: "source",
    href: "https://github.com/DidacLL/AgenticCareerBoost",
    image: "img/routing-map.png",
    imageAlt: "AgenticCareerBoost routing map"
  }
} as const;

const navigationBase = [
  { id: "home" as NavId, number: "00" },
  { id: "projects" as NavId, number: "01" },
  { id: "blog" as NavId, number: "02" },
  { id: "cv" as NavId, number: "03" },
  { id: "contact" as NavId, number: "04" }
] as const;

const copy = {
  en: {
    defaultTitle: "Dídac Llorens — Software Engineer",
    description: "Personal developer portfolio by Dídac Llorens: P3CTeX, AAAAT, backend systems, AI-assisted engineering, and technical notes.",
    identityLines: ["Software engineer · Barcelona", "Tools · systems · data · backend"],
    navigation: {
      home: { label: "Home", kicker: "profile", description: "Profile, current work, and what I like building." },
      projects: { label: "Projects", kicker: "work", description: "P3CTeX, AAAAT, AgenticCareerBoost, and IronBank." },
      blog: { label: "Blog", kicker: "notes", description: "Notes on software, tooling, systems, and experiments." },
      cv: { label: "CV", kicker: "cv", description: "Web curriculum views and the downloadable public PDF." },
      contact: { label: "Contact", kicker: "signal", description: "Public profiles and ways to reach me." }
    },
    profiles: {
      github: "Repositories, source code, and technical work.",
      linkedin: "Professional profile and direct messages.",
      sourceLabel: "Site source",
      source: "Source, build tooling, and history for this portfolio."
    },
    cv: {
      pdfLabel: "Public PDF",
      sourceLabel: "LaTeX source",
      contactDescription: "Role-focused web views and the public PDF."
    },
    theme: { dark: "dark mode", light: "light mode", toggle: "Toggle colour theme" },
    monitor: {
      previous: "Previous signal", next: "Next signal", expand: "maximize", collapse: "minimize", label: "Visual signal monitor",
      profileLabel: "PROFILE / 418", profileLines: ["software engineering · Barcelona", "tools · systems · documents · experiments"],
      projects: "Projects", contact: "Contact", caption: "portrait / default signal"
    },
    banner: { alt: "418 banner artwork from Dídac Llorens visual identity", caption: "visual channel / 418" },
    ui: {
      primaryNavigation: "Primary navigation", document: "DOCUMENT", system: "SYSTEM", mode: "MODE", theme: "THEME", language: "LANGUAGE", links: "LINKS",
      profile: "PROFILE", lanes: "TARGET LANES", selectedWork: "SELECTED WORK", technicalBase: "TECHNICAL BASE", source: "SOURCE", context: "CONTEXT",
      note: "NOTE", index: "INDEX", project: "PROJECT", projectSignal: "PROJECT SIGNAL", publicRecord: "public record", status: "STATUS", repository: "Repository",
      openRepository: "Open repository ↗", openProject: "Open project", selectedProjectCaption: "project / selected work", channel: "CHANNEL", article: "ARTICLE",
      image: "IMAGE", return: "RETURN", returnHome: "Return to the home document →", view: "VIEW", pdf: "PDF", date: "DATE", tags: "TAGS", records: "RECORDS",
      count: "COUNT", cvViews: "CV views"
    }
  },
  es: {
    defaultTitle: "Dídac Llorens — Ingeniero de software",
    description: "Portfolio personal de desarrollo de Dídac Llorens: P3CTeX, AAAAT, sistemas backend, ingeniería asistida por IA y notas técnicas.",
    identityLines: ["Ingeniero de software · Barcelona", "herramientas · sistemas · datos · backend"],
    navigation: {
      home: { label: "Inicio", kicker: "perfil", description: "Perfil, trabajo actual y lo que me gusta construir." },
      projects: { label: "Proyectos", kicker: "trabajo", description: "P3CTeX, AAAAT, AgenticCareerBoost e IronBank." },
      blog: { label: "Blog", kicker: "notas", description: "Notas sobre software, herramientas, sistemas y experimentos." },
      cv: { label: "CV", kicker: "cv", description: "Vistas web del currículum y PDF público en inglés." },
      contact: { label: "Contacto", kicker: "señal", description: "Perfiles públicos y formas de contactar conmigo." }
    },
    profiles: {
      github: "Repositorios, código fuente y trabajo técnico.",
      linkedin: "Perfil profesional y mensajes directos.",
      sourceLabel: "Código del sitio",
      source: "Código, herramientas de build e historial de este portfolio."
    },
    cv: {
      pdfLabel: "PDF público (EN)",
      sourceLabel: "Fuente LaTeX",
      contactDescription: "Vistas web orientadas por rol y PDF público en inglés."
    },
    theme: { dark: "modo oscuro", light: "modo claro", toggle: "Cambiar tema de color" },
    monitor: {
      previous: "Señal anterior", next: "Señal siguiente", expand: "maximizar", collapse: "minimizar", label: "Monitor de señal visual",
      profileLabel: "PERFIL / 418", profileLines: ["ingeniería de software · Barcelona", "herramientas · sistemas · documentos · experimentos"],
      projects: "Proyectos", contact: "Contacto", caption: "retrato / señal por defecto"
    },
    banner: { alt: "Arte del banner 418 de la identidad visual de Dídac Llorens", caption: "canal visual / 418" },
    ui: {
      primaryNavigation: "Navegación principal", document: "DOCUMENTO", system: "SISTEMA", mode: "MODO", theme: "TEMA", language: "IDIOMA", links: "ENLACES",
      profile: "PERFIL", lanes: "ÁREAS OBJETIVO", selectedWork: "TRABAJO DESTACADO", technicalBase: "BASE TÉCNICA", source: "FUENTE", context: "CONTEXTO",
      note: "NOTA", index: "ÍNDICE", project: "PROYECTO", projectSignal: "SEÑAL DEL PROYECTO", publicRecord: "registro público", status: "ESTADO", repository: "Repositorio",
      openRepository: "Abrir repositorio ↗", openProject: "Abrir proyecto", selectedProjectCaption: "proyecto / trabajo seleccionado", channel: "CANAL", article: "ARTÍCULO",
      image: "IMAGEN", return: "VOLVER", returnHome: "Volver al documento de inicio →", view: "VISTA", pdf: "PDF", date: "FECHA", tags: "ETIQUETAS", records: "REGISTROS",
      count: "TOTAL", cvViews: "Vistas del CV"
    }
  },
  ca: {
    defaultTitle: "Dídac Llorens — Enginyer de programari",
    description: "Portfolio personal de desenvolupament de Dídac Llorens: P3CTeX, AAAAT, sistemes backend, enginyeria assistida per IA i notes tècniques.",
    identityLines: ["Enginyer de programari · Barcelona", "eines · sistemes · dades · backend"],
    navigation: {
      home: { label: "Inici", kicker: "perfil", description: "Perfil, feina actual i el que m'agrada construir." },
      projects: { label: "Projectes", kicker: "feina", description: "P3CTeX, AAAAT, AgenticCareerBoost i IronBank." },
      blog: { label: "Blog", kicker: "notes", description: "Notes sobre programari, eines, sistemes i experiments." },
      cv: { label: "CV", kicker: "cv", description: "Vistes web del currículum i PDF públic en anglès." },
      contact: { label: "Contacte", kicker: "senyal", description: "Perfils públics i maneres de contactar amb mi." }
    },
    profiles: {
      github: "Repositoris, codi font i feina tècnica.",
      linkedin: "Perfil professional i missatges directes.",
      sourceLabel: "Codi del lloc",
      source: "Codi, eines de build i historial d'aquest portfolio."
    },
    cv: {
      pdfLabel: "PDF públic (EN)",
      sourceLabel: "Font LaTeX",
      contactDescription: "Vistes web orientades per rol i PDF públic en anglès."
    },
    theme: { dark: "mode fosc", light: "mode clar", toggle: "Canviar el tema de color" },
    monitor: {
      previous: "Senyal anterior", next: "Senyal següent", expand: "maximitzar", collapse: "minimitzar", label: "Monitor de senyal visual",
      profileLabel: "PERFIL / 418", profileLines: ["enginyeria de programari · Barcelona", "eines · sistemes · documents · experiments"],
      projects: "Projectes", contact: "Contacte", caption: "retrat / senyal per defecte"
    },
    banner: { alt: "Art del bàner 418 de la identitat visual de Dídac Llorens", caption: "canal visual / 418" },
    ui: {
      primaryNavigation: "Navegació principal", document: "DOCUMENT", system: "SISTEMA", mode: "MODE", theme: "TEMA", language: "IDIOMA", links: "ENLLAÇOS",
      profile: "PERFIL", lanes: "ÀREES OBJECTIU", selectedWork: "FEINA DESTACADA", technicalBase: "BASE TÈCNICA", source: "FONT", context: "CONTEXT",
      note: "NOTA", index: "ÍNDEX", project: "PROJECTE", projectSignal: "SENYAL DEL PROJECTE", publicRecord: "registre públic", status: "ESTAT", repository: "Repositori",
      openRepository: "Obrir repositori ↗", openProject: "Obrir projecte", selectedProjectCaption: "projecte / feina seleccionada", channel: "CANAL", article: "ARTICLE",
      image: "IMATGE", return: "TORNAR", returnHome: "Tornar al document d'inici →", view: "VISTA", pdf: "PDF", date: "DATA", tags: "ETIQUETES", records: "REGISTRES",
      count: "TOTAL", cvViews: "Vistes del CV"
    }
  }
} as const;

export function siteFor(locale: Locale = defaultLocale) {
  const text = copy[locale];
  const profiles = {
    github: { ...profileBase.github, description: text.profiles.github },
    linkedin: { ...profileBase.linkedin, description: text.profiles.linkedin },
    source: { ...profileBase.source, label: text.profiles.sourceLabel, description: text.profiles.source }
  };

  return {
    defaultTitle: text.defaultTitle,
    description: text.description,
    identity: {
      name: "Dídac Llorens",
      avatar: "img/avatar.jpg",
      avatarAlt: "Dídac Llorens avatar",
      lines: text.identityLines
    },
    navigation: navigationBase.map((item) => ({ ...item, ...text.navigation[item.id] })),
    external: [profiles.github, profiles.linkedin, profiles.source],
    contact: { channels: [profiles.linkedin, profiles.github, profiles.source] },
    cv: {
      sourceUrl: "https://github.com/DidacLL/AgenticCareerBoost/blob/main/agents/cv/tex/didac-llorens-cv.tex",
      pdfLabel: text.cv.pdfLabel,
      sourceLabel: text.cv.sourceLabel,
      logo: "img/logos/250px-PDF_file_icon.png",
      logoAlt: "PDF document icon",
      contactDescription: text.cv.contactDescription
    },
    theme: { storageKey: "didac-site-theme", ...text.theme },
    monitor: {
      previous: text.monitor.previous,
      next: text.monitor.next,
      expand: text.monitor.expand,
      collapse: text.monitor.collapse,
      label: text.monitor.label,
      profile: {
        label: text.monitor.profileLabel,
        title: "Dídac Llorens",
        image: "img/me.png",
        alt: "Dídac Llorens portrait rendered as a retro monitor feed",
        lines: text.monitor.profileLines,
        links: [
          { label: text.monitor.projects, navId: "projects" as NavId },
          { label: text.monitor.contact, navId: "contact" as NavId }
        ],
        caption: text.monitor.caption
      }
    },
    banner: { image: "img/418_informal_banner.jpg", ...text.banner },
    ui: text.ui
  } as const;
}

export const site = siteFor(defaultLocale);
