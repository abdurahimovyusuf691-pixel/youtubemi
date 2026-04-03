# YouTubeMi - Video Sharing Platform

Uzbek video sharing sayti loyihasi. Foydalanuvchilar video yuklaydi, obuna bo'ladi, like/dislike qiladi.

## Setup

1. Virtualenv yarating:
   ```
   python -m venv venv
   venv\\Scripts\\activate  # Windows
   ```

2. Dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Superuser:
   ```
   python manage.py createsuperuser
   ```

5. Server:
   ```
   python manage.py runserver
   ```

Admin: /admin/

Media papkasiga video rasmlar yuklang.

## .env

SECRET_KEY ni .env ga qo'ying (generate: https://djecrety.ir/)

## GitHub

Media/ ni chiqarib tashlang (.gitignore).
"# youtubemi" 
"# youtubemi" 
"# youtubemi" 
