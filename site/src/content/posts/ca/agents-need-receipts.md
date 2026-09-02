---
title: Els agents necessiten «rebuts»
description: Per què l'enginyeria assistida per agents necessita artefactes duradors, estat exacte i canvis revisables en comptes de dependre de l'historial de xat.
date: 2026-06-27
tags: [Agents, Revisió, Workflow]
image: img/sprint-paircheck-loop.png
imageAlt: Diagrama del workflow de pair-check
---
La feina assistida per agents es torna realment útil quan el resultat sobreviu a la conversa que el va produir.

Una transcripció és un mal artefacte d'enginyeria. És llarga, difícil de diffejar, fàcil de perdre i està plena d'afirmacions intermèdies que potser mai van arribar a ser certes. L'output útil és més petit: el source commitejat, el resultat exacte d'un test, la decisió que va canviar una interfície, la font utilitzada per a una afirmació factual o l'issue que encara continua obert.

Penso en aquestes coses com rebuts. Permeten que una altra persona —o jo mateix sis mesos després— respongui preguntes bàsiques sense reconstruir una sessió de xat: Què va canviar? Per què? Contra quin estat? Què es va verificar realment? Què continua sent incert?

Això importa encara més amb feina assistida per LLMs perquè els resums fluids poden amagar una quantitat sorprenent d'ambigüitat. Un model pot dir que un build ha passat, que un fitxer s'ha actualitzat o que dues implementacions són equivalents. El repositori hauria de fer aquestes afirmacions comprovables de manera independent.

Les regles pràctiques a les quals torno una vegada i una altra són senzilles:

- fer canvis prou petits per poder-los revisar;
- registrar les decisions al sistema que n'és propietari, no només en una conversa;
- associar la verificació a la revisió exacta que va verificar;
- mantenir reproduïble l'output generat en comptes de tractar-lo com a source;
- conservar la incertesa quan alguna cosa no s'ha comprovat realment.

Això no necessita un gran framework d'agents. En molts casos una branch, un diff, un run de tests i una nota curta són millor memòria institucional que una altra capa d'orquestració.

L'objectiu d'utilitzar un agent és fer feina útil més ràpid. L'objectiu dels rebuts és assegurar que aquesta velocitat no s'aconsegueixi a costa de deixar de saber què conté realment el sistema.
