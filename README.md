````markdown
# MVC Rocket Pets

Backend project developed in Python following the **MVC architectural pattern**, with clear separation of responsibilities between controllers, views, validators, models, and error handling.

The application was designed to practice backend development concepts such as request flow organization, validation layer, business rules, and API structure in a clean and maintainable way.

---

## Overview

MVC Rocket Pets is a backend application focused on managing pets and people, applying good software design practices through a layered architecture.

This project demonstrates:

- MVC-based project structure
- Separation between request handling and business logic
- Input validation
- Error handling
- Repository-oriented organization
- Cleaner and more maintainable backend code structure

---

## Project Structure

```bash
src/
├── controllers/
├── errors/
├── main/
├── models/
├── validators/
└── views/
````

The source code is organized into dedicated modules, reinforcing separation of concerns and improving readability and scalability.

---

## Architecture

The project follows a layered flow:

1. **View**
   Receives the request and coordinates the execution flow.

2. **Validator**
   Validates incoming data before it reaches the business layer.

3. **Controller**
   Applies business rules and orchestrates the application behavior.

4. **Model / Repository**
   Represents and persists application data.

5. **Error layer**
   Standardizes exception and failure handling.

This structure helps reduce coupling and makes the code easier to test, understand, and evolve.

---

## Technologies Used

* **Python**
* **Flask**
* **SQLite**
* **Pylint**
* **Pre-commit**

The repository also includes configuration files such as `.pylintrc`, `.pre-commit-config.yaml`, `requirements.txt`, and local database files, showing concern for code quality and project setup.

---

## Features

* Register people
* Register pets
* Validate request data
* Handle application errors
* Organize request and response flow using structured layers

---

## Learning Goals

This project was created to strengthen practical knowledge in:

* Backend architecture
* MVC pattern
* Code organization
* Business rule separation
* Validation strategies
* Error standardization
* Maintainable Python backend design

---

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/junior-bortolanza/mvc_rocket_pets.git
```

### 2. Access the project folder

```bash
cd mvc_rocket_pets
```

### 3. Create and activate a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python run.py
```

---

## Code Quality

This repository includes tools and configurations for maintaining code quality, such as:

* **Pylint** for static analysis
* **Pre-commit hooks** for development workflow consistency

These practices help keep the project cleaner and closer to professional development standards.

---

## Why This Project Matters

This project is a practical demonstration of how to build a backend application with a more professional structure instead of concentrating all logic in a single file.

It reflects important software engineering concerns such as:

* maintainability
* readability
* separation of concerns
* validation before processing
* scalable organization

---

## Future Improvements

Some possible next steps for this project:

* Add automated tests
* Improve API documentation
* Add environment variable management
* Implement Docker support
* Improve input validation for more real-world scenarios
* Add authentication and authorization
* Standardize API response format even further

---

## Author

**Junior Bortolanza**

* GitHub: [junior-bortolanza](https://github.com/junior-bortolanza)

---

## Repository

Project available at:
[https://github.com/junior-bortolanza/mvc_rocket_pets](https://github.com/junior-bortolanza/mvc_rocket_pets)

````

```markdown
# Alternative Shorter Opening

A Python backend project built with an MVC-based architecture to practice clean code organization, validation flow, business logic separation, and maintainable API design.
````

```markdown
# Recruiter-Friendly Summary

This project showcases backend development skills in Python through a structured MVC application, emphasizing clean architecture principles, validation layers, error handling, and separation of concerns.
```

```markdown
# Suggested Next Upgrade

I can also turn this into a more premium README version with:

- badges
- clickable table of contents
- endpoints section
- skills demonstrated section
- portfolio-style presentation
```
