# 🔄 API + UI Consistency Checks Demo

This project demonstrates **hybrid testing** where:

- The **API** is the source of truth for data.
- The **UI** displays that data.
- Automated tests verify that the UI values match the API values.

Project name suggestion: `api-ui-consistency-checks-demo`

---

## 🧠 Idea

1. Fetch user data from the JSONPlaceholder API:
   - `GET https://jsonplaceholder.typicode.com/users/1`
2. Display similar data on a simple local HTML page.
3. Use Selenium + Requests + PyTest to compare:
   - UI name vs API name
   - UI email vs API email

This reflects real-world thinking:

> “I trust the backend API as source of truth and verify that the UI is consistent with it.”

---

## 📂 Folder Structure

```text
api-ui-consistency-checks-demo/
│
├── ui_mock/
│     └── user.html
│
├── utils/
│     ├── __init__.py
│     └── api_client.py
│
├── tests/
│     ├── __init__.py
│     └── test_api_ui.py
│
├── conftest.py
├── requirements.txt
└── README.md
