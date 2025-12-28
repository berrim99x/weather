# Query Weather Forecast — Clean Architecture & TDD

## 📌 Project Overview
This project is an educational implementation of a **Weather Forecast Query** use case.
The main goal is **not** to build a real weather application, but to demonstrate how to design
**maintainable software** using:

- Test Driven Development (TDD)
- Clean Architecture
- SOLID principles
- Test Doubles (Dummy, Stub, Spy)
- Clean Code practices

The project follows the same pedagogical approach introduced during lectures.

---

## 🎯 Main Objective
The system answers the following question:

> *Given a city and a date/time, how should the system behave when querying weather forecast data?*

The focus is on **business decisions**, not on external systems such as APIs or databases.

---

## 🧠 Business Rules Covered
The use case handles the following scenarios:

1. ❌ Input is `None` → request is unsuccessful  
2. ❌ City does not exist → unsuccessful (`city_exist = False`)  
3. ❌ City exists but no weather data available → unsuccessful (`city_exist = True`)  
4. ✅ City exists and weather data is available → successful result  

Each scenario is validated through unit tests.

---

## 🧪 Test Driven Development (TDD)
The project strictly follows the **RED → GREEN → BLUE** cycle:

- **RED**: Write a failing test describing a new behavior
- **GREEN**: Write the minimal code to pass the test
- **BLUE**: Refactor and improve code structure without changing behavior

Every commit clearly indicates its TDD stage.

---

## 🧱 Architecture Overview
The project follows **Clean Architecture**, separating concerns into layers:

- **Use Case (Business Logic)**  
  - Contains all business rules and decision-making
  - Independent from frameworks and infrastructure

- **DTOs (Input / Output)**  
  - Define clear data contracts

- **Interfaces (Boundaries)**  
  - Repository interface
  - Presenter interface

- **External Layers (later stages)**  
  - Controller
  - Presenter implementation
  - Repository implementation (fake/in-memory)

Dependencies always point **inward**, toward the business logic.

---

## 🧩 Project Structure
