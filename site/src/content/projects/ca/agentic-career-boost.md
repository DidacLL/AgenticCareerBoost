---
title: AgenticCareerBoost
description: Workspace d'enginyeria darrere d'aquest portfolio, combinant publicació estàtica, builds documentals, CI, automatització local i historial tècnic preservat.
subtitle: El repositori on construeixo i mantinc aquest lloc i l'automatització que l'acompanya.
label: 01C / PROJECTE
summary: Publicació Astro escrita en Markdown, GitHub Actions, artefactes documentals generats, utilitats locals, validació i l'historial de desenvolupament darrere del portfolio.
order: 3
tags: [Astro, Markdown, GitHub Actions, Automatització]
image: img/routing-map.png
imageAlt: Mapa de routing del lloc i repositori AgenticCareerBoost
repository: https://github.com/DidacLL/AgenticCareerBoost
status: Actiu / font del portfolio
---
AgenticCareerBoost és el repositori darrere d'aquest lloc i la col·lecció de petites eines, workflows documentals i experiments que van créixer al voltant del manteniment de la meva feina tècnica pública.

La versió actual és deliberadament senzilla a la seva frontera pública. El contingut del portfolio és Markdown. Astro el converteix en HTML estàtic. Una petita quantitat de JavaScript al client manté la navegació fluida i executa el tema i les interaccions CRT/galeria. GitHub Actions construeix el lloc tant per a arrel com per a un subpath de projecte, comprova metadata i assets, compila artefactes documentals i prova el resultat en Chromium.

## El repositori és més gran que la web

Faig servir ACB com a repositori de feina d'enginyeria, així que no tot fitxer útil pertany al lloc públic. L'arbre `site/` conté només el que el portfolio serveix realment. Informes tècnics, decisions històriques i material de workflows anteriors romanen sota `agents/`; les dades locals d'aplicacions queden completament fora de Git.

Aquesta separació va necessitar diverses iteracions. Les versions anteriors intentaven fer que massa estat del repositori formés part del runtime públic. El disseny actual manté clar l'ownership del source: el contingut és propietari de la prosa, les dades compartides són propietàries d'identitat i navegació, els components són propietaris de la presentació i l'output generat es tracta com a material de build descartable.

## Feina assistida per agents amb estat inspeccionable

El projecte també ha estat un lloc per experimentar amb enginyeria assistida per agents. La part que he mantingut no és un framework permanent d'orquestració; és la disciplina de deixar estat útil al darrere: canvis petits, fitxers font, resultats de validació, decisions i prou historial per entendre per què alguna cosa va canviar.

Les regles antigues, informes i documents de workflow romanen al repositori perquè són evidència útil d'aquesta evolució, però no són un harness actiu que la feina nova hagi d'obeir.

## On van anar els experiments

Els primers experiments de tracking de candidatures vivien aquí perquè ACB era el lloc còmode per provar-los. Quan aquella idea es va convertir en programari substancial, va passar a [AAAAT](https://github.com/DidacLL/AAAAT). Mantenir aquesta frontera és més útil que deixar que aquest repositori es converteixi en un monòlit només perquè els experiments van començar aquí.

ACB s'entén millor com el source i l'historial d'enginyeria del mateix portfolio: publicació estàtica, automatització, validació, documents tècnics i les correccions que van fer mantenibles aquestes peces.
