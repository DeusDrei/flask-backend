
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

- **PostgreSQL Server**: Make sure your PostgreSQL server is running and that the database `mydatabase` is created. If you need help with starting PostgreSQL, refer to the PostgreSQL documentation or use pgAdmin to ensure the server is running and accessible.

---

## Flask API Routes

Below are the API routes available in the Flask backend:

### **GET `/blogs`**
- **Description**: Fetches all blog posts.
- **Response**: A JSON array of blog posts.
  ```json
  {
    "blogs": [
      {
        "id": 1,
        "title": "First Blog Post",
        "author": "Alice",
        "content": "This is the content of the first blog post.",
        "created_at": "2023-03-15T00:00:00"
      },
      ...
    ]
  }
  ```

### **GET `/blogs/<int:blog_id>`**
- **Description**: Fetches a single blog post by its ID.
- **Response**: A JSON object with the blog post details.
  ```json
  {
    "id": 1,
    "title": "First Blog Post",
    "author": "Alice",
    "content": "This is the content of the first blog post.",
    "created_at": "2023-03-15T00:00:00"
  }
  ```

### **POST `/create_blog`**
- **Description**: Creates a new blog post.
- **Request Body**:
  ```json
  {
    "title": "New Blog Post",
    "author": "John",
    "content": "This is the content of the new blog post."
  }
  ```
- **Response**: A message indicating success and the created blog post.

### **PATCH `/update_blog/<int:blog_id>`**
- **Description**: Updates an existing blog post by ID.
- **Request Body**: You can update any of the fields.
  ```json
  {
    "title": "Updated Blog Title",
    "content": "Updated content here."
  }
  ```
- **Response**: A message indicating success and the updated blog post.

### **DELETE `/delete_blog/<int:blog_id>`**
- **Description**: Deletes a blog post by ID.
- **Response**: A message indicating the blog post has been deleted.

---

## File Structure in Next.js

Here’s an overview of the Next.js project file structure:

```
frontend/
├── .next/                     # Compiled Next.js files (ignore in Git)
├── node_modules/               # Node.js dependencies (ignore in Git)
├── public/                     # Static assets like images
│   └── images/
├── src/
│   ├── pages/                  # React components for pages
│   │   ├── index.js            # Homepage
│   │   ├── blogs/              # Blog-related pages
│   │   │   ├── [id].js         # Dynamic page for blog details
│   │   │   └── index.js        # Blog list page
│   └── services/               # API service files (e.g., blog API calls)
│       └── blog.js             # Blog API interaction logic
├── .gitignore                  # Files to be ignored by Git
├── next.config.js              # Next.js configuration
├── package.json                # Node.js dependencies and scripts
└── README.md                   # Project documentation
```

- **`pages/`**: Contains the page components for each route. The `index.js` file represents the homepage, and `[id].js` is a dynamic route to show individual blog posts.
- **`services/`**: Contains the logic for making API calls (like fetching blog posts from the backend).
- **`public/`**: Contains static assets such as images and favicon.
- **`.gitignore`**: Specifies which files should not be committed to Git, such as `node_modules/` and `.next/`.

---
