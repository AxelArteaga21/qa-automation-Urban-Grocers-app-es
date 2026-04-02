# 🛒 URBAN GROCERS

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [API](#-api)
  - [Create User](#-create-user---api)
  - [Create Kit for a Specific Card or User](#-create-kit-for-a-specific-card-or-user---api)
- [Stack Tecnológico](#-stack-tecnológico)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Automated Test Cases](#-automated-test-cases)
  - [Create User](#-create-user)
  - [Create Kit by User](#create-kit-by-user)
- [Report Bugs](#-report-bugs)
  - [firstName allows spaces when it should be rejected with 400 status](#api-firstname-allows-spaces-when-it-should-be-rejected-with-400-status)
  - [kit name accepts empty value when it should be rejected with 400 status](#api-kit-name-accepts-empty-value-when-it-should-be-rejected-with-400-status)
  - [kit name exceeds maximum length when it should be rejected with 400 status](#api-kit-name-exceeds-maximum-length-when-it-should-be-rejected-with-400-status)
  - [Create kit while skip the name parameter when it should be rejected with a 400 status](#api-create-kit-while-skip-the-name-parameter-when-it-should-be-rejected-with-a-400-status)
  - [kit name accepts numeric value but returns 201 instead of 400 Bad Request](#api-kit-name-accepts-numeric-value-but-returns-201-instead-of-400-bad-request)
- [Recruiter Highlights](#-recruiter-highlights)
- [Autor](#-autor)

## 📖 Project Overview
This project contains **automated API tests** for the **Urban Grocers** application, focusing on **user creation and user-specific kit creation**. It is developed in **Python** using **pytest** and **requests**, applying testing techniques such as **parameterization**, **boundary value analysis**, and **equivalence partitioning**. 

The goal is to ensure system quality through **robust**, **maintainable**, and **scalable tests**.

## 🚀 API

### 👨 Create User - API
#### Endpoint
#### POST /api/v1/users

#### Json
```
{
    "firstName": "Max",
    "phone": "+10005553535",
    "address": "8042 Lancaster Ave.Hamburg, NY"
}
```
#### Success Response
```
HTTP/1.1 201 Creado
{
    authToken: 'jknnFApafP4awfAIFfafam2fma'
}
```
#### Error Response
```
HTTP/1.1 400 Bad request.
{
    "code": 400,
    "message": "Required parameters missing: firstName, phone, address"
}

HTTP/1.1 400 Bad request.
{
    "code": 400,
    "message": "Invalid firstName. Only Latin letters allowed, length 2–15 characters."
}
```
[Back](#-table-of-contents)

### 🧺 Create Kit for a Specific Card or User - API

- Either the **Authorization** header or the **cardId** parameter is required to create a kit.
- If a request includes an **Authorization** header with a user's **authToken**, the kit will be created for that user.
- If the **cardId** parameter is provided, the kit will be created within the specified card.
- If neither parameter is provided, an error will be returned. When both parameters are provided, **Authorization** takes priority.

#### Endpoint
#### POST /api/v1/kits

#### Encabezados
```
{
    "Content-Type": "application/json",
    "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
}
```
#### Json
```
HTTP/1.1 201 Creado
{
    "name": "Mi conjunto"
}
```
#### Success Response
```
HTTP/1.1 201 Creado
{
    "name": "My Kit",
    "card": {
        "id": 1,
        "name": "For the Occasion"
    },
    "productsList": null,
    "id": 7,
    "productsCount": 0
}
```
#### Error Response

```
HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "Required parameters missing"
}

HTTP/1.1 400 Bad request.
{
       "code": 400,
       "message": "Name must contain only Latin letters, spaces, or hyphens, 2–15 characters"
   }
```

> ⚠️ The API may return varying error messages or, in some cases, no response body. Tests are designed to validate responses flexibly.

[Back](#-table-of-contents)

## 🛠️ Stack Tecnológico

| Tecnología      | Uso                       |
|:----------------|:--------------------------|
| Python 3.14.3   | Main programming language |
| Request 2.32.5  | HTTP requests             |
| Pytest 9.0.2    | Testing framework         |
| Git             | Version control           |

[Back](#-table-of-contents)

## 📁 Project Structure

```
qa-project-Urban-Grocers-app-es/
├──api/ → HTTP requests
├──config / → Configuration files
├──data/ → Reusable test data
└──test/ → Test cases
```

[Back](#-table-of-contents)

## ⚙️ Installation
### Clone the repository
```
git clone https://github.com/usuario/qa-project-Urban-Grocers-app-es.git
```
### Create a virtual environment (Optional but recommended)
```
1. python -m venv venv

2. .venv\Scripts\activate
```
### Install dependencies
```
pip install -r requirements.txt
```

[Back](#-table-of-contents)

## 🤖 Automated Test Cases
### ⚠️ Known Issues

During testing, several inconsistencies were identified in the API behavior:
- The `firstName` field allows spaces and returns a 201 status code, even though it should be rejected with a 400 error based on validation rules.
- The `name` field for kit creation accepts empty values (`""`) and still returns a 201 status code instead of a 400 error.
- The `name` field allows values exceeding the maximum length (more than 511 characters) and returns 201 instead of 400.
- When required parameters are missing in the request body (e.g., `{}`), the API returns a 500 Internal Server Error instead of a 400 Bad Request.
- The `name` field allows numbers and returns a 201 status code, even though it should be rejected with a 400 error based on validation rules.
- The `name` field allows differents types and returns a 201 status code, even though it should be rejected with a 400 error based on validation rules.
> ⚠️ These issues were identified through negative testing, boundary value analysis, and validation scenarios. Tests were designed based on expected business rules rather than current API behavior.

### ✅ Create User
#### Test Execution
```
pytest .\tests\test_create_user.py -v
```
1. Validate requests to create new users.

| ID | Escenario de Prueba           | Cuerpo de la Solicitud (Body) | Resultado Esperado                                                                                                                    |
|:--:|:------------------------------|:--- |:--------------------------------------------------------------------------------------------------------------------------------------|
| **1** | Minimum allowed length (2)    | `{"firstName": "Aa", "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **201 Created**. The `authToken` **parameter is generated**, and the data is stored in the `Users` table.                             |
| **2** | Maximum allowed length (15)   | `{"firstName": "Aaaaaaaaaaaaaaa", "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **201 Created**. The `authToken` **parameter is generated**, and the data is stored in the `Users` table.                                      |
| **3** | Below minimum length (1)      | `{"firstName": "A", "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **400 Bad Request**. **Message**: `The firstName can only contain Latin letters, and the length must be between 2 and 15 characters`. |
| **4** | Upper minimum length (16)     | `{"firstName": "Аааааааааааааааа", "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **400 Bad Request**. **Message**: `The firstName can only contain Latin letters, and the length must be between 2 and 15 characters`.            |
| **5** | Spaces not allowed            | `{"firstName": "A Aaa", "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **400 Bad Request**. **Message**: `The firstName can only contain Latin letters, and the length must be between 2 and 15 characters`.             |
| **6** | Special character not allowed | `{"firstName": "№%@", "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **400 Bad Request**. **Message**: `The firstName can only contain Latin letters, and the length must be between 2 and 15 characters`.             |
| **7** | Number not allowed            | `{"firstName": "123", "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **400 Bad Request**. **Message**: `The firstName can only contain Latin letters, and the length must be between 2 and 15 characters`.            |
| **8** | Missing parameter             | `{"phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **400 Bad Request**. **Message**: `Not all required parameters were provided`.                                                        |
| **9** | Empty values                  | `{"firstName": "", "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **400 Bad Request**. **Message**: `Not all required parameters were provided`.                                                       |
| **10** | invalid types (Número)        | `{"firstName": 12, "phone": "+1234567890", "address": "123 Elm Street, Hilltop"}` | **400 Bad Request**.                                                                                                                  |

#### ▶️ Test Execution Output

- tests/test_create_user.py::test_create_user... PASSED [ 10%]
- tests/test_create_user.py::test_create_user... PASSED [ 20%]
- tests/test_create_user.py::test_create_user... PASSED [ 30%]
- tests/test_create_user.py::test_create_user... PASSED [ 40%]
- tests/test_create_user.py::test_create_user... FAILED [ 50%]
- tests/test_create_user.py::test_create_user... PASSED [ 60%]
- tests/test_create_user.py::test_create_user... PASSED [ 70%]
- tests/test_create_user.py::test_create_user... PASSED [ 80%]
- tests/test_create_user.py::test_create_user... PASSED [ 90%]
- tests/test_create_user.py::test_create_user... PASSED [100%]

### ✅Create Kit by User
#### Test Execution
```
pytest .\tests\test_create_kit_by_user.py -v
```
2. Create a kit for a specific user (not a card) by following these steps:
   - Send a request to create a new user and save their authentication token (authToken).
   - Send a request to create a personal kit for this user, including the Authorization header.

| ID | Escenario de Prueba          | Cuerpo de la Solicitud (Body)                                        | Resultado Esperado                                                                                                              |
|:--:|:-----------------------------|:---------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| **1** | Minimum allowed length (1)   | `{ "name": "a"}`                                                     | **201 Created**. The `name` field in the response body matches the `name` field in the request body.                             |
| **2** | Maximum allowed length (511) | `"name":"The test value for this check will be 511 characters long"` | **201 Created**. The `name` field in the response body matches the `name` field in the request body. |
| **3** | Below minimum length (0)     | `{ "name": "" }`                                                     | **400 Bad Request**                                                                                                         |
| **4** | Upper minimum length (512)   | `"name":"The test value for this check will be 512 characters long"` | **400 Bad Request**                                                                                                        |
| **5** | Special character allowed    | `{ "name": ""№%@"," }`                                               | **201 Created**. The `name` field in the response body matches the `name` field in the request body.     |
| **6** | Spaces allowed               | `{ "name": " A Aaa " }`                                              | **201 Created**. The `name` field in the response body matches the `name` field in the request body.     |
| **7** | Numbers allowed              | `{ "name": "123" }`                                                  | **201 Created**. The `name` field in the response body matches the `name` field in the request body.     |
| **8** | Missing parameter            | `{ }`                                                                | **400 Bad Request**                                                                                                             |
| **9** | invalid types                | `{ "name": 123 }`                                                    | **400 Bad Request**                                                                                                             |

#### ▶️ Test Execution Output

- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... PASSED [ 11%]
- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... PASSED [ 22%]
- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... FAILED [ 33%]
- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... FAILED [ 44%]
- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... PASSED [ 55%]
- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... PASSED [ 66%]
- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... PASSED [ 77%]
- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... FAILED [ 88%]
- tests/test_create_kit_by_user.py::test_create_kit_by_user_success... FAILED [100%]

[Back](#-table-of-contents)

### 🐞 Report Bugs
####  [API] firstName allows spaces when it should be rejected with 400 status

**Environment:**
- Endpoint: POST /api/v1/users
- Method: POST
- Content-Type: application/json

**Steps to Reproduce:**
1. Send POST request to /api/v1/users
2. Use body:
   {
     "firstName": "A Aaa",
     "phone": "+1234567890",
     "address": "123 Elm Street, Hilltop"
   }
3. Observe the response

   **Expected Result:**
   - Status code: 400 Bad Request
   - Validation error indicating invalid format (spaces not allowed)

    **Actual Result:**
   - Status code: 201 Created
   - User is successfully created

    **Impact:**
   - Invalid data is accepted by the system
   - Breaks validation rules for user input
   - May cause inconsistencies in downstream systems

> ⚠️**Note**
> - According to validation rules, `firstName` should only contain Latin letters (no spaces)
> - This issue was identified during boundary and negative testing
#### [API] kit name accepts empty value when it should be rejected with 400 status

**Environment:**
- Endpoint: POST /api/v1/kits
- Method: POST
- Content-Type: application/json

**Steps to Reproduce:**
1. Send POST request to /api/v1/kits
2. Use body:
  {
      "name": ""
  }
3. Observe the response status code

    **Expected Result:**
   - Status code: 400 Bad Request
   - Validation error indicating that the "name" field cannot be empty
   
   **Actual Result:**
     - Status code: 201 Created
     - Kit is successfully created with an empty name
   
   **Impact:**
     - Invalid data is accepted by the system
     - Breaks validation rules for required fields
     - May cause inconsistencies in data and downstream processes
   
> ⚠️**Note**
> - The "name" field should be required and contain valid characters
> - This issue was identified during negative and boundary testing

#### [API] kit name exceeds maximum length when it should be rejected with 400 status

**Environment:**
- Endpoint: POST /api/v1/kits
- Method: POST
- Content-Type: application/json

**Steps to Reproduce:**
1. Send POST request to /api/v1/kits
2. Use body:
   {
     "name": "<string with 512 characters>"
   }
3. Observe the response status code

    **Expected Result:**
    - Status code: 400 Bad Request
    - Validation error indicating that the maximum length (511) was exceeded

    **Actual Result:**
    - Status code: 201 Created
    - Kit is successfully created despite exceeding the allowed length

    **Impact:**
    - Validation rules are not enforced correctly
    - Allows invalid data into the system
    - May lead to data inconsistencies and unexpected behavior

> ⚠️**Note**
> - Maximum allowed length for "name" is 511 characters
> - This issue was identified using boundary value analysis

#### [API] Create kit while skip the name parameter when it should be rejected with a 400 status

**Environment:**
- Endpoint: POST /api/v1/kits
- Method: POST
- Content-Type: application/json

**Steps to Reproduce:**
1. Send POST request to /api/v1/kits
2. Use body:
   { }
3. Observe the response status code

    **Expected Result:**
    - Status code: 400 Bad Request
    - Validation error indicating missing required field(s), such as "name"

    **Actual Result:**
    - Status code: 500 Internal Server Error
    - Server fails instead of handling validation properly

    **Impact:**
    - Critical: Invalid input causes server error
    - Indicates lack of proper validation handling
    - May affect system stability and reliability

> ⚠️**Notes**
> - Missing required fields should be handled as client errors (4xx), not server errors (5xx)
> - This issue was identified during negative testing

#### [API] kit name accepts numeric value but returns 201 instead of 400 Bad Request

**Environment:**
- Endpoint: POST /api/v1/kits
- Method: POST
- Content-Type: application/json

**Steps to Reproduce:**
1. Send POST request to /api/v1/kits
2. Use body:
   {
     "name": 123
   }
3. Observe the response status code

    **Expected Result:**
    - Status code: 400 Bad Request
    - Validation error indicating that the "name" field must be a string

    **Actual Result:**
    - Status code: 201 Created
    - Kit is successfully created with a numeric value

    **Impact:**
    - Invalid data types are accepted by the system
    - Breaks input validation rules
    - May cause inconsistencies or failures in downstream processing

> ⚠️**Note**
> - The "name" field should only accept string values
> - This issue was identified during negative testing

[Back](#-table-of-contents)

## 💼 Recruiter Highlights

This project showcases:

- Designed a modular API automation framework with clear separation of responsibilities (API, tests, data, configuration).
- Implemented data-driven tests with parameterization to efficiently cover multiple scenarios.
- Applied key testing techniques such as boundary value analysis and equivalence partitioning.
- Developed independent and reusable test cases to enhance maintainability and scalability.
- Built robust validation strategies to handle inconsistent API responses effectively.
- Identified and documented API defects in alignment with expected business rules.

[Back](#-table-of-contents)

## 👨‍💻 Autor

Axel Arteaga

QA Automation Engineer | Python, Pytest & Requests | Test Automation & Quality Focused

LinkedIn: www.linkedin.com/in/axel-arteaga

[Back](#-table-of-contents)
