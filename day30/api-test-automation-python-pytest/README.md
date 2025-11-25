# 📘 API Test Automation Suite (Python + PyTest + Requests)

A lightweight **API testing project** built using:

- Python
- PyTest
- Requests

The tests target the public JSONPlaceholder API:

https://jsonplaceholder.typicode.com

---

## 🚀 Project Overview

This suite validates:

- Status codes (200, 201, 404)
- Basic response structure (contract testing)
- Positive and negative flows
- Data-driven tests with `@pytest.mark.parametrize`
- Simple POST creation behavior

Covered endpoints:

- `/users`
- `/users/{id}`
- `/posts`
- `/posts/{id}` (implicitly, via list and POST tests)

---

## 📂 Folder Structure

```text
api-test-automation-python-pytest/
│
├── tests/
│     ├── test_users_api.py
│     ├── test_posts_api.py
│
├── utils/
│     ├── __init__.py
│     └── api_client.py
│
├── requirements.txt
└── README.md
