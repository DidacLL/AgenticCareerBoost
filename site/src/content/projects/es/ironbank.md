---
title: IronBank
description: Backend bancario Java/Spring Boot construido como un pequeño sistema de microservicios con gateway, discovery, seguridad, datos, transacciones y antifraude.
subtitle: Mi proyecto final de backend en Ironhack de 2022, llevado más allá de un único servicio CRUD hacia un sistema bancario orientado a microservicios.
label: 01D / PROYECTO
summary: Servicios Java 18 y Spring Boot para datos y transacciones bancarias, con service discovery, API gateway, seguridad Keycloak, lógica antifraude, documentación OpenAPI, Maven y JUnit.
order: 4
tags: [Java 18, Spring Boot, Microservicios, Keycloak, REST]
image: img/routing-architecture.png
imageAlt: Diagrama de arquitectura
repository: https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys
status: 2022 / histórico
---
IronBank — `vBNK.sys` en el repositorio original — fue mi proyecto final del bootcamp Java Backend de Ironhack. Es código antiguo, pero sigue marcando un punto importante en mi desarrollo: la primera vez que intenté modelar un sistema bancario como varios servicios backend cooperando entre sí en vez de una aplicación con una gran capa de controllers.

El repositorio separa las responsabilidades de discovery, gateway, seguridad, datos, transacciones y antifraude en servicios Spring Boot individuales. Keycloak proporciona el contexto de autenticación y seguridad, Springdoc expone documentación de API, Maven gestiona los módulos y JUnit forma parte del stack de tests.

## Por qué un sistema bancario

Llegué a la ingeniería de software después de años trabajando dentro de operaciones de banca y seguros, así que conocía el dominio lo suficiente como para pensar más allá de la forma de los endpoints. Cuentas, usuarios, transacciones, permisos y controles de fraude son preocupaciones conectadas, y separar el sistema me obligó a pensar tanto en límites y comunicación entre servicios como en las entidades subyacentes.

El proyecto también incluye el trabajo de arquitectura alrededor del código: diagramas de llamadas entre servicios, diagramas de sistema, casos de uso y modelado de requisitos.

- [Abrir el diagrama principal del sistema](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/blob/master/diagrams/vBNK_MainSystemDiagram.png)
- [Abrir el diagrama de llamadas entre servicios](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/blob/master/diagrams/vBNK_servicesCalls_diagram.drawio%281%29.png)
- [Explorar los diagramas originales](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/tree/master/diagrams)

Mantengo IronBank en el portfolio como proyecto histórico de backend, no como afirmación de que hoy construiría exactamente la misma arquitectura. Su valor está en el sistema que intentó construir, el dominio que modela y la base Java/Spring que documenta.
