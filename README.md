# Django REST API Project

This project implements a Django REST API for managing paragraphs and user authentication.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
2. Navigate to the project directory:
   ```bash
   cd your-repository
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply migrations:
   ```bash
    python manage.py migrate
5. Run the development server:
   ```bash
   python manage.py runserver

## Usage

Once the server is running, you can interact with the API using tools like cURL, Postman, or Swagger UI.

## API Endpoints

### User Authentication

- **Endpoint:** `/api/login/` 
- **Method:** POST
- **Description:** Authenticate users
- **Request Body:**
  ```json
  {
      "email": "dell@gmail.com",
      "password": "Niraj@2001"
  }
- **Sample Response:**
  ```json
  {
    "message": "Login successful"
  }

### Paragraph Creation

- **Endpoint:** `/api/paragraph/` or `http://127.0.0.1:8000/swagger/`
- **Method:** POST
- **Description:** Create new paragraphs
- **Request Body:**
  ```json
  {
      "paragraphs": [
          {
              "text": "This is the first paragraph."
          },
          {
              "text": "This is the second paragraph."
          }
      ]
  }
- **Sample Response:**
  ```json
  {
    "message": "Paragraphs saved successfully"
  }

### Search Word

- **Endpoint:** `/api/search/` or `http://127.0.0.1:8000/swagger/`
- **Method:** POST
- **Description:** Search for paragraphs containing a specific word
- **Request Body:**
  ```json
  {
      "word": "example"
  }
- **Sample Response:**
  ```json
  {
    "output": "Input - 'example' | Output: Paragraph 1 and Paragraph 2 are returned",
    "paragraphs": [
        {
            "id": 1,
            "text": "This is the first paragraph."
        },
        {
            "id": 2,
            "text": "This is the second paragraph."
        }
    ]
  }

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature-name`.
5. Submit a pull request.

Please ensure your code follows the project's coding conventions and includes appropriate tests.

## License

This project is licensed under the [MIT License](LICENSE).
