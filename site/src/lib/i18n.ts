export const locales = ["en", "es", "ca"] as const;
export type Locale = (typeof locales)[number];

export const defaultLocale: Locale = "en";
export const translatedLocales = ["es", "ca"] as const;

export const localeLabels: Record<Locale, string> = {
  en: "ENG",
  es: "CAST",
  ca: "CAT"
};

export const localeNames: Record<Locale, string> = {
  en: "English",
  es: "Castellano",
  ca: "Català"
};

export const dateLocales: Record<Locale, string> = {
  en: "en-GB",
  es: "es-ES",
  ca: "ca-ES"
};

export function isLocale(value: string): value is Locale {
  return locales.includes(value as Locale);
}

export function contentId(id: string, locale: Locale = defaultLocale) {
  return locale === defaultLocale ? id : `${locale}/${id}`;
}

export function entryLocale(id: string): Locale {
  const [prefix] = id.split("/");
  return isLocale(prefix) && prefix !== defaultLocale ? prefix : defaultLocale;
}

export function localContentId(id: string) {
  const parts = id.split("/");
  return isLocale(parts[0]) && parts[0] !== defaultLocale ? parts.slice(1).join("/") : id;
}

export function localizedEntries<T extends { id: string }>(entries: T[], locale: Locale) {
  return entries.filter((entry) => entryLocale(entry.id) === locale);
}
