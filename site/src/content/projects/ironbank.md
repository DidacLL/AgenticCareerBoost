---
title: IronBank
description: Java/Spring Boot banking backend built as a small microservice system with gateway, discovery, security, data, transaction, and anti-fraud services.
subtitle: My 2022 Ironhack backend final project, built beyond a single CRUD service into a banking-oriented microservice system.
label: 01D / PROJECT
summary: Java 18 and Spring Boot services for banking data and transactions, with service discovery, an API gateway, Keycloak security, anti-fraud logic, OpenAPI documentation, Maven, and JUnit.
order: 4
tags: [Java 18, Spring Boot, Microservices, Keycloak, REST]
image: img/routing-architecture.png
imageAlt: Architecture diagram
repository: https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys
status: 2022 / historical
---
IronBank — `vBNK.sys` in the original repository — was my final project for the Ironhack Java Backend bootcamp. It is older code, but it still marks an important point in my development: the first time I tried to model a banking system as several cooperating backend services instead of one application with a large controller layer.

The repository separates discovery, gateway, security, data, transaction and anti-fraud concerns into individual Spring Boot services. Keycloak provides the authentication/security context, Springdoc exposes API documentation, Maven manages the modules, and JUnit is part of the test stack.

## Why a banking system

I came to software engineering after years of working inside banking and insurance operations, so the domain was familiar enough that I could think beyond endpoint shapes. Accounts, users, transactions, permissions and fraud controls are connected concerns, and splitting the system forced me to think about service boundaries and communication as well as the underlying entities.

The project also includes the architecture work around the code: service-call diagrams, system diagrams, use cases and requirement modelling.

- [Open the main system diagram](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/blob/master/diagrams/vBNK_MainSystemDiagram.png)
- [Open the service-call diagram](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/blob/master/diagrams/vBNK_servicesCalls_diagram.drawio%281%29.png)
- [Browse the original diagrams](https://github.com/DidacLL/Ironhack-IronBank_FinalProject_vBNKsys/tree/master/diagrams)

I keep IronBank in the portfolio as a historical backend project, not as a claim that I would build the same architecture unchanged today. Its value is the system it attempted, the domain it models, and the Java/Spring foundation it records.
