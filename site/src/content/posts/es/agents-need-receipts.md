---
title: Los agentes necesitan «recibos»
description: Por qué la ingeniería asistida por agentes necesita artefactos duraderos, estado exacto y cambios revisables en vez de depender del historial de chat.
date: 2026-06-27
tags: [Agentes, Revisión, Workflow]
image: img/sprint-paircheck-loop.png
imageAlt: Diagrama del workflow de pair-check
---
El trabajo asistido por agentes se vuelve realmente útil cuando el resultado sobrevive a la conversación que lo produjo.

Una transcripción es un mal artefacto de ingeniería. Es larga, difícil de diffear, fácil de perder y está llena de afirmaciones intermedias que quizá nunca llegaron a ser ciertas. El output útil es más pequeño: el source commiteado, el resultado exacto de un test, la decisión que cambió una interfaz, la fuente utilizada para una afirmación factual o el issue que todavía sigue abierto.

Pienso en esas cosas como recibos. Permiten que otra persona —o yo mismo seis meses después— responda preguntas básicas sin reconstruir una sesión de chat: ¿Qué cambió? ¿Por qué? ¿Contra qué estado? ¿Qué se verificó realmente? ¿Qué sigue siendo incierto?

Esto importa todavía más con trabajo asistido por LLMs porque los resúmenes fluidos pueden esconder una cantidad sorprendente de ambigüedad. Un modelo puede decir que un build pasó, que un archivo se actualizó o que dos implementaciones son equivalentes. El repositorio debería hacer esas afirmaciones comprobables de manera independiente.

Las reglas prácticas a las que vuelvo una y otra vez son sencillas:

- hacer cambios suficientemente pequeños para poder revisarlos;
- registrar las decisiones en el sistema que es propietario de ellas, no sólo en una conversación;
- asociar la verificación a la revisión exacta que verificó;
- mantener reproducible el output generado en vez de tratarlo como source;
- conservar la incertidumbre cuando algo no se ha comprobado realmente.

Eso no requiere un gran framework de agentes. En muchos casos una branch, un diff, un run de tests y una nota corta son mejor memoria institucional que otra capa de orquestación.

El objetivo de usar un agente es hacer trabajo útil más rápido. El objetivo de los recibos es asegurarse de que esa velocidad no se consigue a costa de dejar de saber qué contiene realmente el sistema.
