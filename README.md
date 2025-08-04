<h1 align="center">Movie Ticket Booking System</h1>

---

## Tech Stack
- **Frontend**
    - Vue.js
    - Axios

- **Backend**
    - Python 3.13
    - FastAPI
    - SQLAlchemy
    - Alembic
    - Jwt (`pyjwt`)

- **Database**
    - PostgreSQL

---

## Setup
1. Clone the repository:
```bash
git clone https://github.com/Bhabishworgrg/movie-booking-system.git
cd movie-booking-system
```

2. Create a virtual environment and activate it:
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

4. Set up the database:
- Create a database in PostgreSQL.

5. Configure `.env` file:
- Create a `.env` file in the `backend` directory:
```env
DATABASE_URL=postgresql://username:password@localhost/database_name
SECRET_KEY=your_secret_key
```
> Replace `username`, `password` and `database_name` with your PostgreSQL credentials.
> Replace `your_secret_key` with a secure key for JWT.

6. Back in the `backend` directory, run database migrations:
```bash
alembic upgrade head
```

7. Navigate to the `frontend` directory and install Node.js dependencies:
```bash
cd ../frontend
npm install
```

---

## Usage
1. In the `backend` directory, start the FastAPI server:
```bash
fastapi dev app/main.py
```

2. In the `frontend` directory, start the Vue.js application:
```bash
npm run dev
```

---
