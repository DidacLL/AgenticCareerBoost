---
title: Los sitios estáticos como banco de trabajo
description: Por qué la publicación estática funciona bien para un sitio técnico personal cuando contenido, presentación y output generado tienen owners claros.
date: 2026-06-27
tags: [Sitio estático, Modelo de contenido, Mantenimiento]
image: img/routing-map.png
imageAlt: Mapa de contenido y rutas del portfolio
---
Un sitio estático no tiene por qué significar HTML mantenido a mano, y un sitio mantenible tampoco necesita convertirse automáticamente en una aplicación server-side.

Para un portfolio técnico personal, la mayoría de páginas son documentos. Proyectos, notas, texto de perfil e información de contacto cambian cuando los edito; no necesitan una consulta a base de datos cada vez que alguien abre una página. Compilar esas fuentes a HTML encaja muy bien.

La frontera útil está entre contenido escrito y presentación. Un post del blog debería ser un documento fuente. Un layout debería saber cómo se ven los posts. La navegación debería vivir en un único owner compartido. El árbol generado `dist/` debería ser desechable. Si añadir un artículo exige copiar una plantilla de página o registrar el mismo slug en tres sitios, el modelo de source ya está filtrando detalles de implementación al authoring.

Por eso acabé moviendo este portfolio a Astro. Astro no es valioso aquí porque quisiera un framework; es útil porque puede actuar como compilador. Markdown sigue siendo lo que escribo, los componentes son propietarios de la estructura repetida y el output sigue siendo HTML estático normal.

Todavía hay espacio para comportamiento client-side. La persistencia del tema, el CRT/galería y la navegación interna fluida hacen que el sitio sea más agradable de usar. Lo importante es que ninguno de ellos es propietario del contenido y ninguno es necesario para leer la página. Con JavaScript desactivado, el documento debería seguir siendo un documento.

La publicación estática también hace comprobable la portabilidad del deployment. El mismo source puede construirse para `/` o para un subpath de proyecto, y las suposiciones rotas sobre URLs canónicas, assets o redirects aparecen durante el build en lugar de convertirse en estado de runtime.

El resultado que busco es deliberadamente aburrido de operar: escribir un archivo Markdown, commit, build y publicar archivos estáticos. La ingeniería interesante pertenece al modelo de source y a los checks, no a hacer que publicar resulte complicado.
