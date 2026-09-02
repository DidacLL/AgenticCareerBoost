---
title: P3CTeX
description: Un toolkit documental LaTeX2e/expl3 creado para convertir las PEC de la UOC en documentos técnicos rápidos de producir, reproducibles y con acabado profesional.
subtitle: El proyecto que construí para que maquetar una PEC dejara de competir con el trabajo de ingeniería que había dentro.
label: 01A / PROYECTO
summary: "Una clase documental extensible y una suite de paquetes para trabajo UOC: estructura de estilo oficial, listados de código, capturas resilientes, tablas basadas en datos, modelos de clases UML, metadatos reutilizables y builds deterministas."
order: 1
tags: [LaTeX2e, expl3, Programación TeX, UML, Herramientas documentales]
image: img/P3CTeXLogo.png
imageAlt: Logotipo de P3CTeX
repository: https://github.com/DidacLL/P3CTeX
status: Activo / proyecto principal
---
P3CTeX nació de un problema muy práctico: no quería pasar la última hora antes de una entrega de la UOC corrigiendo márgenes, portadas, tamaños de capturas, tablas, bloques de código o los mismos metadatos de siempre. Quería escribir el contenido, compilarlo y obtener un documento que me gustara entregar.

Empezó como una plantilla LaTeX orientada a la UOC y acabó convirtiéndose en el proyecto del que más orgulloso estoy aquí: una clase documental, un paquete core, librerías de funcionalidad independientes, código interno en `expl3`, manuales, ejemplos, tests de regresión y una TeX Directory Structure que puede registrarse como un árbol local de paquetes de verdad.

El resultado práctico es sencillo: puedo producir PECs e informes técnicos muy rápido manteniendo tipografía consistente, estructura reutilizable, referencias, figuras, código fuente, diagramas y un resultado pulido. La ingeniería interesante es todo lo que hay debajo de esa comodidad.

## Un pequeño ecosistema de software TeX

`P3CTeX.cls` controla el comportamiento a nivel de documento y los metadatos UOC. `pxCORE` actúa como capa de agregación, mientras que varias librerías enfocadas aportan funcionalidad de forma independiente:

- **pxGDX** — el sistema de diseño: colores, tipografía y convenciones visuales compartidas.
- **pxSRC** — inclusión robusta de figuras y capturas, pares de imágenes y secuencias numeradas. Los assets que todavía faltan pueden mostrarse como placeholders en vez de romper un documento en curso.
- **pxTAB** — tablas generadas desde datos en forma de listas, con presets reutilizables para cabeceras, grids, stripes, anchos, captions y layout.
- **pxPRP** — mapas de propiedades con nombre y registros que permiten manejar estado estructurado desde comandos LaTeX normales.
- **pxUML** — modelado UML de clases y objetos sobre TikZ/pgf-umlcd, con un registro que separa el modelo de dónde y cómo se dibuja.

Las APIs públicas siguen siendo utilizables desde documentos LaTeX2e normales; los internals pueden usar `expl3`, token lists, familias de keys y estructuras de datos cuando eso hace la implementación más limpia.

## UML que se comporta como un modelo

`pxUML` es una de mis partes favoritas del proyecto. Una clase se registra con atributos, operaciones, herencia, tipo de objeto (`class`, `interface`, `enumclass`, etc.) e información opcional de implementación. Después, la misma definición almacenada puede dibujarse en posiciones o estilos distintos sin volver a escribir el modelo.

Eso hace que el trabajo de orientación a objetos sea mucho menos mecánico. Clases, interfaces, herencia y relaciones como asociaciones, composición o agregación se describen una vez y se renderizan como un diagrama UML propiamente dicho. Se parece mucho más a trabajar con un modelo de objetos que a dibujar cajas manualmente en un editor de diagramas.

## Pensado para cómo se escriben de verdad las PECs

Gran parte del trabajo académico es iterativo: las capturas llegan tarde, los diagramas cambian, las tablas crecen y el informe tiene que seguir compilando mientras aún faltan piezas. P3CTeX tiene funciones diseñadas específicamente para ese workflow en lugar de tratar el documento como una página final e inmutable.

Por eso `pxSRC` puede conservar el espacio de una figura cuando la imagen todavía no está lista, las listas de imágenes pueden consumir capturas secuenciales, la configuración de metadatos y portada vive en keys reutilizables, y las tablas y estructuras UML se expresan como datos en lugar de repetir markup visual.

Programar en TeX también es muy distinto de programar aplicaciones convencionales. La expansión de macros, los streams de tokens y la frontera entre LaTeX2e y `expl3` obligan a pensar APIs y estado de otra manera. Construir algo mantenible en ese entorno es una parte importante de por qué todavía disfruto trabajando en P3CTeX.

## Verlo funcionando

- [Descargar el PDF showcase compilado de P3CTeX](https://raw.githubusercontent.com/DidacLL/P3CTeX/main/examples/P3CTeX-example.pdf)
- [Leer el source del showcase](https://github.com/DidacLL/P3CTeX/blob/main/examples/P3CTeX-example.tex)
- [Descargar el PDF de la plantilla UOC mínima](https://raw.githubusercontent.com/DidacLL/P3CTeX/main/examples/UOCTemplates/MinimalTemplate/PAC1/MinimalTemplatePAC.pdf)
- [Descargar el PDF de la plantilla UOC extendida](https://raw.githubusercontent.com/DidacLL/P3CTeX/main/examples/UOCTemplates/ExtendedTemplate/PAC1/ExtendedTemplatePAC.pdf)
- [Leer la API/manual de pxUML](https://github.com/DidacLL/P3CTeX/blob/main/tex/doc/pxUML.tex)

El repositorio contiene los sources de los paquetes, manuales, ejemplos y suites de tests. Los ejemplos compilados son la forma más rápida de entender por qué existe el proyecto; los archivos `.sty`, `.cls` y `.code.tex` muestran la profundidad que hay detrás del resultado.
