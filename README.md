# CashApp Managment - Dashboard de control financiero

Este proyecto tiene como finalidad ayudar a los usuarios con el manejo del dinero que tienen ahorrado, ya sea basado en cuentas bancarias o dinero físico. 
Debido a esto, existe este proyecto, el cual busca **combinar AI, machine learning y demas tecnologías para mostrar y administrar el dinero del cliente.** CashApp será una API la cual podrá manejar procesos CRUD basados en el saldo que disponga el cliente

Este monto debe ser ingresado a la plataforma, al cual se le puede insertar y restar cantidades que hayan sido movidas por el cliente. Este mini proyecto es una pequeña implementación de un futuro proyecto bancario, el cual consumirá este proyecto como su dashboard.

## Arquitectura

- Backend FastAPI
- Cliente Tkinter
- Base de datos SQLite
  
El proyecto está dividido en dos componentes independientes que se comunican vía HTTP:

┌─────────────────────┐        HTTP/REST        ┌──────────────────────┐
│   Cliente Tkinter    │  ───────────────────▶   │     API FastAPI       │
│  (desktop/)           │  ◀───────────────────   │     (api/)             │
└─────────────────────┘                          └──────────┬───────────┘
                                                              │
                                                              ▼
                                                    ┌──────────────────┐
                                                    │  SQLite (SQLAlchemy) │
                                                    └──────────────────┘

## Estructura
CashApp-Managment/
├── api/                          # Backend FastAPI
│   ├── main.py                   # Punto de entrada de la API
│   ├── database.py               # Configuración de SQLAlchemy / SQLite
│   ├── models/                   # Modelos ORM
│   ├── schemas/                  # Esquemas de validación (Pydantic)
│   ├── routers/                  # Endpoints (movements, prediction)
│   ├── services/                 # Lógica de negocio
│   └── ai/                       # Clasificador de Machine Learning
│       ├── train_model.py        # Script de entrenamiento
│       ├── classifier.py         # Carga del modelo y predicción
│       └── movement_model.pkl    # Modelo entrenado
├── desktop/                      # Cliente de escritorio (Tkinter)
│   ├── app.py                    # Punto de entrada de la app
│   ├── controllers/               # Consumo de la API (requests)
│   └── views/                    # Interfaz gráfica (Dashboard)
├── requirements.txt
└── README.md

## Funcionalidades
Las funcionalidades de CashApp son:
- Registrar ingresos.
- Registrar gastos.
- Consultar movimientos financieros.
- Actualizar movimientos.
- Eliminar movimientos.
- Visualizar el saldo actual.
- Mostrar un dashboard con información financiera.
- Clasificar automáticamente un gasto mediante Machine Learning (opcional).
---

## Requerimientos funcionales
- RF-01: El sistema deberá permitir registrar un nuevo movimiento financiero.
- RF-02: El sistema deberá permitir consultar los movimientos registrados.
- RF-03: El sistema deberá permitir actualizar un movimiento existente.
- RF-04: El sistema deberá permitir eliminar un movimiento.
- RF-05: El sistema deberá calcular automáticamente el saldo disponible.
- RF-06: El sistema deberá mostrar un dashboard con el resumen financiero.
- RF-07: El sistema deberá comunicarse con una API REST para gestionar la información.
- RF-08: El sistema podrá clasificar automáticamente un gasto mediante un modelo básico de Machine Learning.

---

## Requerimientos no funcionales
- RNF-01: La aplicación deberá desarrollarse utilizando Python.
- RNF-02: La interfaz gráfica deberá desarrollarse con Tkinter.
- RNF-03: La API deberá desarrollarse utilizando FastAPI.
- RNF-04: La información deberá almacenarse en SQLite.
- RNF-05: El proyecto deberá utilizar Git y GitHub aplicando Git Flow.
- RNF-06: El código deberá organizarse siguiendo una arquitectura por capas.
- RNF-07: La API deberá documentarse automáticamente mediante OpenAPI (Swagger).

---



## Tecnologías utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/sqlalchemy-%23D71F00.svg?style=for-the-badge&logo=sqlalchemy&logoColor=white) 
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) 
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) 
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) 
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green) 
![SQLITE](https://img.shields.io/badge/FastAPI-005571.svg?style=for-the-badge&logo=fastapi) 
![Scikit-learn-discovery-badge](https://images.credly.com/size/340x340/images/e3f72503-68fe-47d7-9766-c85a24932e89/blob) 
---

CashApp[^bignote]
---
[^bignote]: Created by Angel Duarte Montero Lebrón - BackEnd Developer
