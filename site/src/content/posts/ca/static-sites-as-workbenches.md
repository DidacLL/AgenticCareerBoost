---
title: Els llocs estàtics com a banc de treball
description: Per què la publicació estàtica funciona bé per a un lloc tècnic personal quan contingut, presentació i output generat tenen owners clars.
date: 2026-06-27
tags: [Lloc estàtic, Model de contingut, Manteniment]
image: img/routing-map.png
imageAlt: Mapa de contingut i rutes del portfolio
---
Un lloc estàtic no ha de voler dir HTML mantingut a mà, i un lloc mantenible tampoc no necessita convertir-se automàticament en una aplicació server-side.

Per a un portfolio tècnic personal, la majoria de pàgines són documents. Projectes, notes, text de perfil i informació de contacte canvien quan els edito; no necessiten una consulta a base de dades cada vegada que algú obre una pàgina. Compilar aquestes fonts a HTML encaixa molt bé.

La frontera útil és entre contingut escrit i presentació. Un post del blog hauria de ser un document font. Un layout hauria de saber com es veuen els posts. La navegació hauria de viure en un únic owner compartit. L'arbre generat `dist/` hauria de ser descartable. Si afegir un article exigeix copiar una plantilla de pàgina o registrar el mateix slug en tres llocs, el model de source ja està filtrant detalls d'implementació a l'authoring.

Per això vaig acabar movent aquest portfolio a Astro. Astro no és valuós aquí perquè volgués un framework; és útil perquè pot actuar com a compilador. Markdown continua sent el que escric, els components són propietaris de l'estructura repetida i l'output continua sent HTML estàtic normal.

Encara hi ha espai per a comportament client-side. La persistència del tema, el CRT/galeria i la navegació interna fluida fan que el lloc sigui més agradable d'utilitzar. L'important és que cap d'ells és propietari del contingut i cap és necessari per llegir la pàgina. Amb JavaScript desactivat, el document hauria de continuar sent un document.

La publicació estàtica també fa comprovable la portabilitat del deployment. El mateix source es pot construir per a `/` o per a un subpath de projecte, i les suposicions trencades sobre URLs canòniques, assets o redirects apareixen durant el build en comptes de convertir-se en estat de runtime.

El resultat que busco és deliberadament avorrit d'operar: escriure un fitxer Markdown, commit, build i publicar fitxers estàtics. L'enginyeria interessant pertany al model de source i als checks, no a fer que publicar resulti complicat.
