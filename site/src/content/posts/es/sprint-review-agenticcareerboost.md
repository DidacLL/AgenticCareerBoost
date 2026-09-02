---
title: Refactorizar un portfolio sin convertirlo en una app
description: Lecciones de sustituir un runtime de contenido renderizado en navegador por Astro estático manteniendo la identidad visual y las pequeñas piezas interactivas del sitio.
date: 2026-06-28
tags: [Astro, Refactorización, Publicación estática]
image: img/routing-architecture.png
imageAlt: Arquitectura de routing del refactor del portfolio
---
La primera versión de este portfolio tenía un runtime propio en el navegador: contenido JSON, un registro de rutas, un renderer, componentes reutilizables y suficiente JavaScript como para que el sitio se comportara como una pequeña aplicación.

Funcionaba. También era el modelo de mantenimiento equivocado para un sitio cuyo trabajo principal es publicar documentos.

El refactor tuvo menos que ver con elegir Astro que con decidir qué debía poseer cada tipo de source. La prosa de proyectos y posts pasó a Markdown. La identidad y navegación compartidas obtuvieron un único owner de datos. Layouts y componentes conservaron la presentación. El origin y base path del deployment pasaron a ser inputs de build. El HTML generado dejó de ser algo en lo que pensar durante el authoring.

La parte difícil fue conservar lo que realmente daba carácter al sitio antiguo. El monitor CRT, el tratamiento de papel/grid, el banner, el rail de identidad y la navegación compacta merecían quedarse. El runtime de contenido personalizado no. Tratar esas dos cosas como decisiones separadas hizo que la migración fuera mucho más fácil de razonar.

Tampoco quería que una navegación suave exigiera convertir el sitio otra vez en una SPA. El client router de Astro basta para evitar las recargas visibles de imágenes y cabeceras que hacían que los cambios de página se sintieran baratos, mientras cada ruta sigue teniendo un documento HTML estático completo y se puede leer sin JavaScript.

La otra lección fue que los sitios estáticos siguen necesitando verificación seria cuando tienen más de unas pocas páginas. Este build comprueba deployments tanto en raíz como en subpath, rutas generadas, metadata, imágenes, URLs retiradas y comportamiento en navegador. Chromium ejecuta navegación, tema e interacciones CRT y comprueba overflow responsive en varios viewports.

La prueba final de authoring es mucho más sencilla que cualquiera de esos checks: publicar un artículo nuevo debería significar crear un archivo Markdown. Si la arquitectura es sofisticada pero esa operación se vuelve molesta, la arquitectura ha fallado a su usuario —en este caso, yo.
