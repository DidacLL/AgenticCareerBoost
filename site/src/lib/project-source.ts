import type { Loader } from "astro/loaders";

type ProjectSource = {
  id: string;
  repository: string;
  branch: "main";
  documentPath: ".acb/site.md";
  coverPath: string;
};

export const projectSources: ProjectSource[] = [
  {
    id: "p3ctex",
    repository: "DidacLL/P3CTeX",
    branch: "main",
    documentPath: ".acb/site.md",
    coverPath: ".acb/cover.png"
  },
  {
    id: "aaaat",
    repository: "DidacLL/AAAAT",
    branch: "main",
    documentPath: ".acb/site.md",
    coverPath: ".acb/cover.svg"
  },
  {
    id: "ironbank",
    repository: "DidacLL/Ironhack-IronBank_FinalProject_vBNKsys",
    branch: "main",
    documentPath: ".acb/site.md",
    coverPath: ".acb/cover.png"
  }
];

function rawSourceUrl(source: ProjectSource, path: string) {
  return `https://raw.githubusercontent.com/${source.repository}/${source.branch}/${path}`;
}

export function getProjectSource(id: string) {
  const source = projectSources.find((item) => item.id === id);

  if (!source) {
    return undefined;
  }

  return {
    ...source,
    documentUrl: rawSourceUrl(source, source.documentPath),
    coverUrl: rawSourceUrl(source, source.coverPath)
  };
}

export function projectSourceLoader(): Loader {
  return {
    name: "project-source",
    async load({ renderMarkdown, store }) {
      store.clear();

      for (const source of projectSources) {
        const documentUrl = rawSourceUrl(source, source.documentPath);
        const response = await fetch(documentUrl);

        if (!response.ok) {
          throw new Error(
            `Project source ${source.id} is unavailable at ${documentUrl} (${response.status}).`
          );
        }

        const markdown = await response.text();

        store.set({
          id: source.id,
          data: {
            repository: source.repository,
            documentUrl,
            coverUrl: rawSourceUrl(source, source.coverPath)
          },
          rendered: await renderMarkdown(markdown, {
            fileURL: new URL(documentUrl)
          })
        });
      }
    }
  };
}
