---
title: AAAAT
description: Software de escritorio local-first para gestionar candidaturas, material fuente, conversaciones, documentos y asistencia opcional de IA deliberadamente acotada.
subtitle: Un workspace nativo en Python que mantiene el registro de candidaturas en local y sigue siendo completamente útil sin ninguna IA conectada.
label: 01B / PROYECTO
summary: "Una aplicación wxPython/SQLite centrada en la candidatura: fuente de la oferta, estado, notas, próximas acciones, contexto reutilizable, documentos generados, artefactos locales y asistencia opcional neutral respecto al proveedor."
order: 2
tags: [Python, wxPython, SQLite, Local-first, PyInstaller]
image: img/AAAATlogo.png
imageAlt: Logotipo de AAAAT
repository: https://github.com/DidacLL/AAAAT
status: 1.0 / activo
---
AAAAT es una aplicación de escritorio que construí porque una búsqueda de empleo real se convierte rápidamente en una mezcla de hojas de cálculo, notas, pestañas del navegador, historiales de chat, PDFs y borradores a medias. La información útil pertenece al mismo contexto, pero no quería que la solución se convirtiera en otra cuenta cloud o en un wrapper de IA.

La candidatura es el registro central. Conecta la oportunidad original, etapa actual, próxima acción, notas, investigación, preparación de conversaciones, contexto profesional reutilizable, texto generado y los archivos que realmente se utilizaron en esa candidatura.

## Local-first significa ownership local

El workspace autoritativo es un directorio local elegido por el usuario, respaldado por SQLite y artefactos locales. El tracking, edición, búsqueda, preparación, renderizado, backup y restore normales funcionan sin un LLM, conexión de red, Git o un checkout del source.

La UI de escritorio está construida con wxPython y empaquetada con PyInstaller como aplicaciones nativas para Windows, macOS y Linux. La aplicación está pensada para abrirse y usarse como software, no para ejecutarse desde una terminal como una demo de desarrollo.

## La IA es opcional y está deliberadamente acotada

AAAAT puede trabajar con un host externo de IA, pero la aplicación conserva la autoridad sobre sus propios datos. Un host conectado recibe contexto limitado al propósito de la operación y un conjunto pequeño de operaciones, en lugar de acceso general a la base de datos, IDs internos, paths del workspace o navegación arbitraria por registros.

La integración es neutral respecto al proveedor: AAAAT no necesita API keys, nombres de modelos ni un SDK de proveedor. La misma aplicación sigue siendo completa cuando no hay nada conectado. Esa separación entre software útil y asistencia opcional de un modelo es una de las decisiones arquitectónicas que más me importan en el proyecto.

## Vistas operativas en vez de un dashboard genérico

Smart View está diseñada para la información necesaria durante una llamada con un recruiter o una preparación urgente. Detailed View expone el registro completo de la candidatura. User View contiene contexto profesional reutilizable. La aplicación también mantiene los archivos generados y su provenance junto al registro que los produjo.

- [Ver el workspace de escritorio con datos ficticios](https://github.com/DidacLL/AAAAT/blob/main/docs/assets/aaaat-desktop.svg)
- [Leer la arquitectura implementada](https://github.com/DidacLL/AAAAT/blob/main/docs/architecture.md)
- [Leer el contrato de integración opcional con IA](https://github.com/DidacLL/AAAAT/blob/main/docs/ai-integration.md)

AAAAT nació de un experimento anterior de tracking dentro de AgenticCareerBoost, pero se convirtió en un proyecto propio cuando los límites del producto quedaron suficientemente claros como para merecer un repositorio y un proceso de release independientes.
