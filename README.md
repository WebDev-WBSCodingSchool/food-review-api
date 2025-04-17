# 🍽️ Food Review API – WBS CODING SCHOOL

A simple RESTful API built with Flask for educational purposes at **WBS CODING SCHOOL**.  
This project demonstrates basic user authentication flow and restaurant/review management using Flask and PostgreSQL.

⚠️ **Note**: For simplicity, authentication uses a base64-encoded user ID as the API key. In production environments, proper JWT or OAuth-based auth should be used.

---

## 🔧 Installation

1. **Clone the repository**

```bash
git clone git@github.com:WebDev-WBSCodingSchool/food-review-api.git
cd food-review-api
```

2. **Create and activate a virtual environment**

macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows

```bash
py -3 -m venv .venv
.venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set your environment variable**

```bash
export PG_URI=your_postgres_connection_string
```

5. **Run the application**

```bash
flask --app foodreview run --debug --port 8080
```

## 📚 API Endpoints

### 🔐 Auth Routes

`POST /auth/register`

Body:

```json
{
  "username": "your_name",
  "email": "user@example.com",
  "password": "your_password"
}
```

Response:

```json
{
  "id": 1,
  "username": "your_name",
  "email": "user@example.com"
}
```

`POST /auth/login`

Body:

```json
{
  "email": "user@example.com",
  "password": "your_password"
}
```

Response:

```json
{
  "X-API-Key": "base64_user_id"
}
```

### 🍴 Restaurant Routes

All routes below require `X-API-Key` in the headers (base64 user ID).

`GET /restaurants`

Response:

```json
[
  {
    "id": 1,
    "name": "Pizza Place",
    "description": "Authentic Italian Pizza",
    "owner_id": 2,
    "total_reviews": 5,
    "average_rating": 4.6,
    "reviews_url": "http://localhost:8080/restaurants/1/reviews"
  },
  ...
]
```

`POST /restaurants`

Body:

```json
{
  "name": "Sushi Spot",
  "description": "Fresh sushi rolls"
}
```

Response:

```json
{
  "id": 2,
  "name": "Sushi Spot",
  "description": "Fresh sushi rolls",
  "owner_id": 1
}
```

### 📝 Review Routes

`POST /restaurants/<id>/reviews`

Body:

```json
{
  "rating": 5,
  "comment": "Amazing food!"
}
```

Response:

```json
{
  "id": 10,
  "restaurant_id": 2,
  "user_id": 1,
  "rating": 5,
  "comment": "Amazing food!"
}
```

`GET /restaurants/<id>/reviews`

Response:

```json
{
  "restaurant_id": 2,
  "restaurant_name": "Sushi Spot",
  "total_reviews": 3,
  "average_rating": 4.7,
  "reviews": [
    {
      "id": 10,
      "user_id": 1,
      "rating": 5,
      "comment": "Amazing food!"
    },
    ...
  ]
}
```

### 📌 Notes

This project is not secure for production use — it's designed for learning purposes.

Make sure your PostgreSQL DB is set up and the `PG_URI` env variable is correctly configured. A `create-database.sql` file is provided to create the relations and seed some sample data.
