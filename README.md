# InkNest — A Minimal Django Blog

InkNest is a small Django-powered blog application with user accounts, post creation/editing/deletion, image uploads, and a responsive frontend.

Key features
- User registration, login and logout (Django auth)
- Create, edit and delete posts (author-only)
- Upload images for posts (served from `/media/` during development)
- "My Posts" dashboard to manage a user's posts
- Clean, responsive CSS in `blogapp/static/style.css`

Quickstart (development)

1. Clone the repo and open the project folder.

2. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Apply migrations and create a superuser (optional):

```powershell
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py createsuperuser
```

5. Run the development server:

```powershell
.\.venv\Scripts\python.exe manage.py runserver
```

6. Open http://127.0.0.1:8000/ in your browser.

Notes
- Media files are stored in the `media/` directory; ensure `MEDIA_URL` and `MEDIA_ROOT` are configured in `blogproject/settings.py`.
- The project runs with `DEBUG=True` for development — update security settings before deploying.

Suggested next steps
- Add tests for views and forms
- Add Docker support or a `Makefile` for developer convenience
- Improve accessibility and add pagination for long lists of posts

If you'd like, I can add any of the suggested next steps now.

