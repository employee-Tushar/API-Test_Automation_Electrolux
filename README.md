# API Automation Tests - JSONPlaceholder

## Overview
This project contains automated API tests for:
https://jsonplaceholder.typicode.com/posts

Framework: Pytest  
Language: Python  

---

## Setup Instructions

### 1️⃣ Clone the repository

git clone <repo-url>
cd api-tests

### 2️⃣ Create virtual environment (Recommended)

python -m venv venv
source venv/bin/activate   (Linux/Mac)
venv\Scripts\activate      (Windows)

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ Run tests

pytest

---

## Test Coverage

✔ Get all posts  
✔ Get post by ID  
✔ Create post  
✔ Negative test for invalid post ID  

---

## Design Approach

- API client abstraction for maintainability
- Configuration separated
- Clear folder structure
- Easy to scale with more endpoints