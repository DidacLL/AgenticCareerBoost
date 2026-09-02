---
title: Refactoritzar un portfolio sense convertir-lo en una app
description: Lliçons de substituir un runtime de contingut renderitzat al navegador per Astro estàtic mantenint la identitat visual i les petites peces interactives del lloc.
date: 2026-06-28
tags: [Astro, Refactorització, Publicació estàtica]
image: img/routing-architecture.png
imageAlt: Arquitectura de routing del refactor del portfolio
---
La primera versió d'aquest portfolio tenia un runtime propi al navegador: contingut JSON, un registre de rutes, un renderer, components reutilitzables i prou JavaScript perquè el lloc es comportés com una petita aplicació.

Funcionava. També era el model de manteniment equivocat per a un lloc la feina principal del qual és publicar documents.

El refactor va tenir menys a veure amb escollir Astro que amb decidir què havia de posseir cada tipus de source. La prosa de projectes i posts va passar a Markdown. La identitat i navegació compartides van obtenir un únic owner de dades. Layouts i components van conservar la presentació. L'origin i base path del deployment van passar a ser inputs de build. L'HTML generat va deixar de ser una cosa en què pensar durant l'authoring.

La part difícil va ser conservar allò que realment donava caràcter al lloc antic. El monitor CRT, el tractament de paper/grid, el bàner, el rail d'identitat i la navegació compacta mereixien quedar-se. El runtime de contingut personalitzat no. Tractar aquestes dues coses com decisions separades va fer que la migració fos molt més fàcil de raonar.

Tampoc no volia que una navegació fluida exigís convertir el lloc una altra vegada en una SPA. El client router d'Astro és suficient per evitar les recàrregues visibles d'imatges i capçaleres que feien que els canvis de pàgina semblessin barats, mentre cada ruta continua tenint un document HTML estàtic complet i es pot llegir sense JavaScript.

L'altra lliçó va ser que els llocs estàtics continuen necessitant verificació seriosa quan tenen més d'unes poques pàgines. Aquest build comprova deployments tant a l'arrel com en subpath, rutes generades, metadata, imatges, URLs retirades i comportament al navegador. Chromium executa navegació, tema i interaccions CRT i comprova overflow responsive en diversos viewports.

La prova final d'authoring és molt més senzilla que qualsevol d'aquests checks: publicar un article nou hauria de significar crear un fitxer Markdown. Si l'arquitectura és sofisticada però aquesta operació es torna molesta, l'arquitectura ha fallat al seu usuari —en aquest cas, jo.
