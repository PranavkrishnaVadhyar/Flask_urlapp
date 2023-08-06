# URL Shortener Flask App

This is a simple URL shortener web application built using Flask. Users can create short URLs for long links and access them later.

## Description

This Flask web application allows users to shorten URLs and access them using the provided short codes. It stores the URLs and their corresponding short codes in a JSON file (`url.json`) and uses sessions to track the history of created URLs.

## Prerequisites

Before running the application, ensure you have the following:

- Python and Flask installed.
- `url.json` file in the project directory.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/YourUsername/YourRepository.git
   cd YourRepository
   ```

2. Install Flask:

   ```bash
   pip install Flask
   ```

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Access the application in your web browser at `http://127.0.0.1:5000`.

3. Use the web interface to create and manage short URLs.

## Routes

- `/`: Home page that displays existing short codes and allows users to create new short URLs.
- `/your_url`: Route to create a new short URL. Supports both URL and file uploads.
- `/<string:code>`: Redirects to the original URL associated with the given code.

## Error Handling

- 404 Not Found: Custom error page (`page_not_found.html`) is displayed when a short code does not exist.

## API

The application provides a simple API to retrieve a list of created short codes.

- `/api`: Returns a JSON list of short codes.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

This URL shortener Flask app was developed by [Your Name](https://github.com/PranavkrishnaVadhyar).


```
