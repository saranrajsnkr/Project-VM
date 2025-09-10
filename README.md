Project VM

```
# AI Learning Platform — Django Starter


This repository contains a starter Django project for an AI-powered personalized learning platform (MVP). It includes apps for users, learning styles, AI content generation, and analytics.


## Quickstart (local)


1. Create virtual environment and install requirements:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


2. Copy .env.example to .env and set values (especially SECRET_KEY and OPENAI_API_KEY if using OpenAI).


3. Run migrations and create superuser:
```bash
python manage.py migrate
python manage.py createsuperuser
```


4. Run the development server:
```bash
python manage.py runserver
```


5. Open http://127.0.0.1:8000/admin and http://127.0.0.1:8000/api/


## Notes and next steps (suggested)
- Add token-based authentication (djoser, simplejwt).
- Implement file parsing for PDFs and images (pdfminer, pytesseract).
- Replace placeholder AI calls with robust integrations (OpenAI, HuggingFace, or commercial text->video services).
- Add front-end (React) if you want an SPA; currently DRF provides API endpoints and browsable UI.
- Add tests, CI, and deployment scripts.


```


---


# Final notes


This starter code aims to give you a full end-to-end skeleton so you can iterate quickly: models, serializers, views, and placeholder AI utilities. Many parts (video generation, PDF parsing, advanced ML for learning-style detection) are intentionally left as pluggable placeholders so you can choose the service you prefer.


Save the files into the project structure above and run migrations to get started.


---
