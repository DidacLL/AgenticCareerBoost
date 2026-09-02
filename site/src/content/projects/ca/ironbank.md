---
title: IronBank
description: Backend bancari Java/Spring Boot construït com un petit sistema de microserveis amb gateway, discovery, seguretat, dades, transaccions i antifrau.
subtitle: El meu projecte final de backend a Ironhack de 2022, portat més enllà d'un únic servei CRUD cap a un sistema bancari orientat a microserveis.
label: 01D / PROJECTE
summary: Serveis Java 18 i Spring Boot per a dades i transaccions bancàries, amb service discovery, API gateway, seguretat Keycloak, lògica antifrau, documentació OpenAPI, Maven i JUnit.
order: 4
tags: [Java 18, Spring Boot, Microserveis, Keycloak, REST]
image: img/routing-architecture.png
imageAlt: Diagrama d'arquitectura
repository: https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys
status: 2022 / històric
---
IronBank — `vBNK.sys` al repositori original — va ser el meu projecte final del bootcamp Java Backend d'Ironhack. És codi antic, però continua marcant un punt important en el meu desenvolupament: la primera vegada que vaig intentar modelar un sistema bancari com diversos serveis backend cooperant entre si en comptes d'una aplicació amb una gran capa de controllers.

El repositori separa les responsabilitats de discovery, gateway, seguretat, dades, transaccions i antifrau en serveis Spring Boot individuals. Keycloak proporciona el context d'autenticació i seguretat, Springdoc exposa documentació d'API, Maven gestiona els mòduls i JUnit forma part del stack de tests.

## Per què un sistema bancari

Vaig arribar a l'enginyeria de programari després d'anys treballant dins d'operacions de banca i assegurances, així que coneixia prou el domini per pensar més enllà de la forma dels endpoints. Comptes, usuaris, transaccions, permisos i controls de frau són preocupacions connectades, i separar el sistema em va obligar a pensar tant en límits i comunicació entre serveis com en les entitats subjacents.

El projecte també inclou la feina d'arquitectura al voltant del codi: diagrames de crides entre serveis, diagrames de sistema, casos d'ús i modelatge de requisits.

- [Obrir el diagrama principal del sistema](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/blob/master/diagrams/vBNK_MainSystemDiagram.png)
- [Obrir el diagrama de crides entre serveis](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/blob/master/diagrams/vBNK_servicesCalls_diagram.drawio%281%29.png)
- [Explorar els diagrames originals](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/tree/master/diagrams)

Mantinc IronBank al portfolio com a projecte històric de backend, no com una afirmació que avui construiria exactament la mateixa arquitectura. El seu valor és el sistema que va intentar construir, el domini que modela i la base Java/Spring que documenta.
