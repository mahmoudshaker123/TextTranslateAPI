# TextTranslateAPI

A text translation service built using Django REST Framework (DRF) and Google Translate API. This project allows users to translate text from one language to another by interacting with a RESTful API.

---

## Features
- Translate text from one language to another.
- Support for multiple languages via Google Translate API.
- Simple and efficient API endpoints.

---

## Prerequisites
Before you begin, ensure you have the following installed:

- Python 3.8+
- Django 4.0+
- Django REST Framework
- Google Translate API key
- pip (Python package installer)

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mahmoudshaker123/TextTranslateAPI.git
   cd TextTranslateAPI
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Google Translate API Key:**
   - Obtain an API key from [Google Cloud Console](https://console.cloud.google.com/).
   - Add the API key to your environment variables or directly to your project settings.

5. **Run Database Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server:**
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Base URL:
`http://127.0.0.1:8000/`

### **Translate Text**
- **Endpoint:** `/translate/`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
      "text": "hello",
      "language": "ar"
  }
  ```
- **Response:**
  ```json
  {
      "original_text": "hello",
      "translated_text": "\u0645\u0631\u062d\u0628\u0627",
      "target_language": "ar"
  }
  ```

---

## Project Structure
```
TextTranslateAPI/
|
|-- core/
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|
|-- translation/
|   |-- migrations/
|   |-- models.py
|   |-- serializers.py
|   |-- views.py
|   |-- urls.py
|
|-- manage.py
|-- requirements.txt
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any inquiries or feedback, please contact:
- **Name:** Mahmoud Shaker
- **GitHub:** [mahmoudshaker123](https://github.com/mahmoudshaker123)
- **Email:** mahmoud.shaker123123@gmail.com

