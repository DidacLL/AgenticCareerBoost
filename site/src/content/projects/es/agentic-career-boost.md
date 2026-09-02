---
title: AgenticCareerBoost
description: Workspace de ingeniería detrás de este portfolio, combinando publicación estática, builds documentales, CI, automatización local e historial técnico preservado.
subtitle: El repositorio donde construyo y mantengo este sitio y la automatización que lo acompaña.
label: 01C / PROYECTO
summary: Publicación Astro escrita en Markdown, GitHub Actions, artefactos documentales generados, utilidades locales, validación y el historial de desarrollo detrás del portfolio.
order: 3
tags: [Astro, Markdown, GitHub Actions, Automatización]
image: img/routing-map.png
imageAlt: Mapa de routing del sitio y repositorio AgenticCareerBoost
repository: https://github.com/DidacLL/AgenticCareerBoost
status: Activo / fuente del portfolio
---
AgenticCareerBoost es el repositorio detrás de este sitio y la colección de pequeñas herramientas, workflows documentales y experimentos que crecieron alrededor del mantenimiento de mi trabajo técnico público.

La versión actual es deliberadamente sencilla en su frontera pública. El contenido del portfolio es Markdown. Astro lo convierte en HTML estático. Una pequeña cantidad de JavaScript en cliente mantiene la navegación fluida y ejecuta el tema y las interacciones CRT/galería. GitHub Actions construye el sitio tanto para raíz como para un subpath de proyecto, comprueba metadata y assets, compila artefactos documentales y prueba el resultado en Chromium.

## El repositorio es más grande que la web

Uso ACB como repositorio de trabajo de ingeniería, así que no todo archivo útil pertenece al sitio público. El árbol `site/` contiene sólo lo que el portfolio sirve realmente. Informes técnicos, decisiones históricas y material de workflows anteriores permanecen bajo `agents/`; los datos locales de aplicaciones quedan completamente fuera de Git.

Esa separación necesitó varias iteraciones. Las versiones anteriores intentaban hacer que demasiado estado del repositorio formara parte del runtime público. El diseño actual mantiene claro el ownership del source: el contenido es propietario de la prosa, los datos compartidos son propietarios de identidad y navegación, los componentes son propietarios de la presentación y el output generado se trata como material de build desechable.

## Trabajo asistido por agentes con estado inspeccionable

El proyecto también ha sido un lugar para experimentar con ingeniería asistida por agentes. La parte que he mantenido no es un framework permanente de orquestación; es la disciplina de dejar estado útil detrás: cambios pequeños, archivos fuente, resultados de validación, decisiones y suficiente historial para entender por qué algo cambió.

Las reglas antiguas, informes y documentos de workflow permanecen en el repositorio porque son evidencia útil de esa evolución, pero no son un harness activo que el trabajo nuevo deba obedecer.

## Dónde fueron los experimentos

Los primeros experimentos de tracking de candidaturas vivían aquí porque ACB era el lugar cómodo para probarlos. Cuando esa idea se convirtió en software sustancial, pasó a [AAAAT](https://github.com/DidacLL/AAAAT). Mantener esa frontera es más útil que dejar que este repositorio se convierta en un monolito sólo porque los experimentos empezaron aquí.

ACB se entiende mejor como el source y el historial de ingeniería del propio portfolio: publicación estática, automatización, validación, documentos técnicos y las correcciones que hicieron mantenibles esas piezas.
