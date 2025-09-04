# Application Tracker — v1 Project Plan

## 🎯 Goal
A simple application tracker where users can:
- Sign up / login (basic JWT auth).
- Add a job application entry (company, role, status, applied date, notes).
- View, update, delete applications.
- Dashboard: list all applications.

---

## 🛠️ Tech Stack
- **Backend**: FastAPI + MySQL (SQLAlchemy ORM)
- **Frontend**: React (Vite + Tailwind CSS)
- **Auth**: JWT (access token only)
- **Version Control**: GitHub repo with collaborator access

---

## 📂 Backend High-Level Design
Very simple layering:

### Data Model (v1)
- **User**: `id, email, password_hash, created_at`
- **Application**: `id, user_id, company, role, status, applied_on, notes, created_at`

---

## 🔑 API Endpoints (v1)
- **Auth**
  - `POST /auth/register`
  - `POST /auth/login`
- **Applications**
  - `POST /applications`
  - `GET /applications`
  - `GET /applications/{id}`
  - `PUT /applications/{id}`
  - `DELETE /applications/{id}`

---

## 📆 Timeline (1 Month Plan)

### Week 1 → Backend Foundations
- [ ] Setup GitHub repo + collaborator
- [ ] Setup FastAPI project structure
- [ ] Configure MySQL + SQLAlchemy
- [ ] Implement User model + register/login with JWT
- [ ] Test with Swagger UI

### Week 2 → Application CRUD
- [ ] Create Application model + schemas
- [ ] Build CRUD routes (create/list/update/delete)
- [ ] Protect routes with auth
- [ ] Write a few pytest tests (optional but good practice)

### Week 3 → Frontend Basics
- [ ] Setup React project (Vite + Tailwind)
- [ ] Auth pages (login/register)
- [ ] Applications dashboard (list applications)
- [ ] Form to add new application

### Week 4 → Polish & Demo
- [ ] Edit & delete from frontend
- [ ] Display status badges
- [ ] Simple filters (by status)
- [ ] Deploy backend (Render/Heroku/Fly.io with MySQL) and frontend (Vercel/Netlify)

---

## 👥 Git + Collaboration Setup
1. You create a GitHub repo (private or public).
2. Go to **Settings → Collaborators → Add your friend (GitHub username)**.
3. Both clone the repo:
   ```bash
   git clone https://github.com/<username>/<repo>.git
