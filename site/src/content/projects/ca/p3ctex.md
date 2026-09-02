---
title: P3CTeX
description: Un toolkit documental LaTeX2e/expl3 creat per convertir les PEC de la UOC en documents tècnics ràpids de produir, reproduïbles i amb acabat professional.
subtitle: El projecte que vaig construir perquè maquetar una PEC deixés de competir amb la feina d'enginyeria que hi havia dins.
label: 01A / PROJECTE
summary: "Una classe documental extensible i una suite de paquets per a feina UOC: estructura d'estil oficial, llistats de codi, captures resilients, taules basades en dades, models de classes UML, metadades reutilitzables i builds deterministes."
order: 1
tags: [LaTeX2e, expl3, Programació TeX, UML, Eines documentals]
image: img/P3CTeXLogo.png
imageAlt: Logotip de P3CTeX
repository: https://github.com/DidacLL/P3CTeX
status: Actiu / projecte principal
---
P3CTeX va néixer d'un problema molt pràctic: no volia passar l'última hora abans d'una entrega de la UOC corregint marges, portades, mides de captures, taules, blocs de codi o les mateixes metadades de sempre. Volia escriure el contingut, compilar-lo i obtenir un document que em fes il·lusió entregar.

Va començar com una plantilla LaTeX orientada a la UOC i va acabar convertint-se en el projecte del qual estic més orgullós aquí: una classe documental, un paquet core, llibreries de funcionalitat independents, codi intern en `expl3`, manuals, exemples, tests de regressió i una TeX Directory Structure que es pot registrar com un arbre local de paquets de debò.

El resultat pràctic és senzill: puc produir PECs i informes tècnics molt ràpid mantenint tipografia consistent, estructura reutilitzable, referències, figures, codi font, diagrames i un resultat polit. L'enginyeria interessant és tot el que hi ha sota aquesta comoditat.

## Un petit ecosistema de software TeX

`P3CTeX.cls` controla el comportament a nivell de document i les metadades UOC. `pxCORE` actua com a capa d'agregació, mentre que diverses llibreries enfocades aporten funcionalitat de manera independent:

- **pxGDX** — el sistema de disseny: colors, tipografia i convencions visuals compartides.
- **pxSRC** — inclusió robusta de figures i captures, parelles d'imatges i seqüències numerades. Els assets que encara falten es poden mostrar com placeholders en comptes de trencar un document en curs.
- **pxTAB** — taules generades des de dades en forma de llistes, amb presets reutilitzables per a capçaleres, grids, stripes, amplades, captions i layout.
- **pxPRP** — mapes de propietats amb nom i registres que permeten gestionar estat estructurat des de comandes LaTeX normals.
- **pxUML** — modelatge UML de classes i objectes sobre TikZ/pgf-umlcd, amb un registre que separa el model d'on i com es dibuixa.

Les APIs públiques continuen sent utilitzables des de documents LaTeX2e normals; els internals poden fer servir `expl3`, token lists, famílies de keys i estructures de dades quan això fa la implementació més neta.

## UML que es comporta com un model

`pxUML` és una de les meves parts preferides del projecte. Una classe es registra amb atributs, operacions, herència, tipus d'objecte (`class`, `interface`, `enumclass`, etc.) i informació opcional d'implementació. Després, la mateixa definició emmagatzemada es pot dibuixar en posicions o estils diferents sense tornar a escriure el model.

Això fa que la feina d'orientació a objectes sigui molt menys mecànica. Classes, interfícies, herència i relacions com associacions, composició o agregació es descriuen una vegada i es renderitzen com un diagrama UML pròpiament dit. S'assembla molt més a treballar amb un model d'objectes que a dibuixar caixes manualment en un editor de diagrames.

## Pensat per com s'escriuen de debò les PECs

Gran part de la feina acadèmica és iterativa: les captures arriben tard, els diagrames canvien, les taules creixen i l'informe ha de continuar compilant mentre encara falten peces. P3CTeX té funcions dissenyades específicament per a aquest workflow en comptes de tractar el document com una pàgina final i immutable.

Per això `pxSRC` pot conservar l'espai d'una figura quan la imatge encara no està preparada, les llistes d'imatges poden consumir captures seqüencials, la configuració de metadades i portada viu en keys reutilitzables, i les taules i estructures UML s'expressen com dades en comptes de repetir markup visual.

Programar en TeX també és molt diferent de programar aplicacions convencionals. L'expansió de macros, els streams de tokens i la frontera entre LaTeX2e i `expl3` obliguen a pensar APIs i estat d'una altra manera. Construir alguna cosa mantenible en aquest entorn és una part important de per què encara gaudeixo treballant en P3CTeX.

## Veure'l funcionant

- [Descarregar el PDF showcase compilat de P3CTeX](https://raw.githubusercontent.com/DidacLL/P3CTeX/main/examples/P3CTeX-example.pdf)
- [Llegir el source del showcase](https://github.com/DidacLL/P3CTeX/blob/main/examples/P3CTeX-example.tex)
- [Descarregar el PDF de la plantilla UOC mínima](https://raw.githubusercontent.com/DidacLL/P3CTeX/main/examples/UOCTemplates/MinimalTemplate/PAC1/MinimalTemplatePAC.pdf)
- [Descarregar el PDF de la plantilla UOC estesa](https://raw.githubusercontent.com/DidacLL/P3CTeX/main/examples/UOCTemplates/ExtendedTemplate/PAC1/ExtendedTemplatePAC.pdf)
- [Llegir l'API/manual de pxUML](https://github.com/DidacLL/P3CTeX/blob/main/tex/doc/pxUML.tex)

El repositori conté els sources dels paquets, manuals, exemples i suites de tests. Els exemples compilats són la manera més ràpida d'entendre per què existeix el projecte; els fitxers `.sty`, `.cls` i `.code.tex` mostren la profunditat que hi ha darrere del resultat.
