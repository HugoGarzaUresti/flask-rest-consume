# Flask Consuming REST Service

This is a simple Flask application that consumes a RESTful web service, inspired by the Spring Boot guide.

## Getting Started

These instructions will help you set up and run the Flask consuming REST service on your local machine.

### Prerequisites

Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

### Installing

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/flask-consuming-rest.git
    cd flask-consuming-rest
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask application:**

    ```sh
    python run.py
    ```

2. **Access the service:**

    Open your web browser and go to:
    - [http://localhost:8080/consume](http://localhost:8080/consume) to fetch data from the GitHub API.
    - [http://localhost:8080/quote](http://localhost:8080/quote) to fetch a random quote.

### API Endpoints

- **GET /consume**

  Fetches data from a remote RESTful web service (GitHub API) and returns it as JSON.

- **GET /quote**

  Fetches a random quote from the Quotable API and returns it as JSON.

### Running Tests

1. **Run the tests:**

    ```sh
    python -m unittest discover
    ```

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [Requests](https://docs.python-requests.org/en/latest/) - HTTP library for Python

## Acknowledgments

- Inspired by the [Spring Boot Consuming REST guide](https://spring.io/guides/gs/consuming-rest)

