# Next.js + Flask + PostgreSQL Application

This is a full-stack application using **Next.js** for the frontend, **Flask** for the backend, and **PostgreSQL** as the database. Below are the instructions to get the development environment set up and running.

## Prerequisites

Make sure you have the following installed:

- **Python** (for Flask backend)
- **Node.js** and **npm** (for Next.js frontend)
- **PostgreSQL** (for the database)

## Setup Instructions

### 1. **Change Database Credentials in `config.py`**

Before running the app, make sure to update your database credentials in `config.py`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost/mydatabase"
```

Replace `postgres`, `root`, and `localhost` with your actual PostgreSQL username, password, and host. Also, make sure to replace `mydatabase` with the name of your PostgreSQL database.

### 2. **Seed Data Already Included in `main.py`**

The seed data for the `BlogPost` model is already included in `main.py`. When the Flask backend is run, the seed data will be automatically inserted into your PostgreSQL database.

### 3. **Start the Backend Server**

- Open **Terminal** (Command Prompt or your terminal of choice).
- Change to the **backend** directory where `main.py` is located:

  ```bash
  cd backend
  ```

- Install the required Python packages:

  ```bash
  pip install -r requirements.txt
  ```

  **If `pip install -r requirements.txt` doesn't work**, you can install each package individually using the following commands:

  ```bash
  pip install Flask==2.0.1
  pip install Flask-SQLAlchemy==2.5.1
  pip install psycopg2-binary==2.9.1
  pip install Flask-Cors==5.0.0
  ```

- Run the Flask backend server:

  ```bash
  python main.py
  ```

The backend server will start running at **http://127.0.0.1:5000**.

### 4. **Start the Frontend Server**

- Open another **Terminal** window.
- Change to the **frontend** directory where the Next.js application is located:

  ```bash
  cd frontend
  ```

- Install the required Node.js packages:

  ```bash
  npm install
  ```

- Run the Next.js frontend server:

  ```bash
  npm run dev
  ```

The frontend server will start running at **http://localhost:3000**.

---

## Accessing the Application

- The **backend API** will be available at `http://127.0.0.1:5000`.
- The **frontend application** will be available at `http://localhost:3000`.

## Notes

- Make sure your **PostgreSQL** server is running and accessible.
- The backend will automatically seed the database with sample blog posts on startup.
- If you need to update the seed data, you can modify the `seed_data()` function in `main.py`.

---

## Troubleshooting

- If you encounter issues with `npm run dev`, try running `npm install` again in the frontend directory.
- If the backend server doesn’t start, ensure that **Flask** is installed correctly and that your PostgreSQL connection details in `config.py` are correct.
- If `pip install -r requirements.txt` fails, you can manually install the dependencies one by one as mentioned above in Step 3.

- PostgreSQL Server: Make sure your PostgreSQL server is running and that the database `mydatabase` is created. If you need help with starting PostgreSQL, refer to the PostgreSQL documentation or use pgAdmin to ensure the server is running and accessible.

