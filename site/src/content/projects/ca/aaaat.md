---
title: AAAAT
description: Programari d'escriptori local-first per gestionar candidatures, material font, converses, documents i assistència opcional d'IA deliberadament acotada.
subtitle: Un workspace natiu en Python que manté el registre de candidatures en local i continua sent completament útil sense cap IA connectada.
label: 01B / PROJECTE
summary: "Una aplicació wxPython/SQLite centrada en la candidatura: font de l'oferta, estat, notes, properes accions, context reutilitzable, documents generats, artefactes locals i assistència opcional neutral respecte al proveïdor."
order: 2
tags: [Python, wxPython, SQLite, Local-first, PyInstaller]
image: img/AAAATlogo.png
imageAlt: Logotip d'AAAAT
repository: https://github.com/DidacLL/AAAAT
status: 1.0 / actiu
---
AAAAT és una aplicació d'escriptori que vaig construir perquè una cerca de feina real es converteix ràpidament en una barreja de fulls de càlcul, notes, pestanyes del navegador, historials de xat, PDFs i esborranys a mitges. La informació útil pertany al mateix context, però no volia que la solució es convertís en un altre compte cloud o en un wrapper d'IA.

La candidatura és el registre central. Connecta l'oportunitat original, etapa actual, propera acció, notes, recerca, preparació de converses, context professional reutilitzable, text generat i els fitxers que realment es van utilitzar en aquella candidatura.

## Local-first vol dir ownership local

El workspace autoritatiu és un directori local escollit per l'usuari, recolzat per SQLite i artefactes locals. El tracking, edició, cerca, preparació, renderitzat, backup i restore normals funcionen sense un LLM, connexió de xarxa, Git o un checkout del source.

La UI d'escriptori està construïda amb wxPython i empaquetada amb PyInstaller com a aplicacions natives per a Windows, macOS i Linux. L'aplicació està pensada per obrir-se i fer-se servir com a programari, no per executar-se des d'una terminal com una demo de desenvolupament.

## La IA és opcional i està deliberadament acotada

AAAAT pot treballar amb un host extern d'IA, però l'aplicació conserva l'autoritat sobre les seves pròpies dades. Un host connectat rep context limitat al propòsit de l'operació i un conjunt petit d'operacions, en comptes d'accés general a la base de dades, IDs interns, paths del workspace o navegació arbitrària per registres.

La integració és neutral respecte al proveïdor: AAAAT no necessita API keys, noms de models ni un SDK de proveïdor. La mateixa aplicació continua sent completa quan no hi ha res connectat. Aquesta separació entre programari útil i assistència opcional d'un model és una de les decisions arquitectòniques que més m'importen del projecte.

## Vistes operatives en comptes d'un dashboard genèric

Smart View està dissenyada per a la informació necessària durant una trucada amb un recruiter o una preparació urgent. Detailed View exposa el registre complet de la candidatura. User View conté context professional reutilitzable. L'aplicació també manté els fitxers generats i la seva provenance al costat del registre que els va produir.

- [Veure el workspace d'escriptori amb dades fictícies](https://github.com/DidacLL/AAAAT/blob/main/docs/assets/aaaat-desktop.svg)
- [Llegir l'arquitectura implementada](https://github.com/DidacLL/AAAAT/blob/main/docs/architecture.md)
- [Llegir el contracte d'integració opcional amb IA](https://github.com/DidacLL/AAAAT/blob/main/docs/ai-integration.md)

AAAAT va néixer d'un experiment anterior de tracking dins d'AgenticCareerBoost, però es va convertir en un projecte propi quan els límits del producte van quedar prou clars per merèixer un repositori i un procés de release independents.
