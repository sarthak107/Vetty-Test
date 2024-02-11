# File Content Viewer

Welcome to the File Content Viewer Flask application! This lightweight web tool provides a convenient way to inspect the contents of text files hosted on your server. Whether you're debugging, analyzing logs, or simply exploring data, this application streamlines the process of viewing file contents directly from your web browser.

With its intuitive interface and customizable options, you can easily specify the file name and optionally the start and end line numbers to narrow down your focus to specific sections of the file. Powered by Flask, a micro web framework for Python, this application offers simplicity and flexibility, making it a valuable addition to your development toolkit.

Get started now and streamline your file inspection workflow with the File Content Viewer Flask application!


## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3
- Flask

### Installation

1. Clone this repository to your local machine:


2. Navigate to the project directory:


3. Install the required dependencies:
  pip install -r requirements.txt


### Usage

1. Run the Flask application:
    python app.py

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. You can specify the file name, start, and end line numbers as query parameters to view specific parts of the file. For example:

- [http://127.0.0.1:5000/?filename=file1.txt](http://127.0.0.1:5000/?filename=file1.txt) (View the entire file)
- [http://127.0.0.1:5000/?filename=file1.txt&start=1&end=10](http://127.0.0.1:5000/?filename=file1.txt&start=1&end=10) (View lines 1 to 10)
- [http://127.0.0.1:5000/?filename=file1.txt&start=5](http://127.0.0.1:5000/?filename=file1.txt&start=5) (View from line 5 to the end)

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.

