# My Capstone Django Application

This is a Django application that showcases the power of Django framework in building web applications.

## Installation

1. Clone the repository:

git clone https://github.com/myratam/level-3.git


2. Create a virtual environment and activate it:

python -m venv myenv
source myenv/bin/activate # For Linux/Mac
myenv\Scripts\activate # For Windows


3. Install the project dependencies:

pip install -r requirements.txt

4. Run database migrations:

python manage.py migrate

5. Start the local development server:

python manage.py runserver

6. Access the application in your web browser at http://localhost:8000.

## Docker Deployment

1. Build the Docker image:

docker build -t my-blog ./

2. Run the Docker container:

docker run -p 8000:8000 my-blog

3. Access the application in your web browser at http://localhost:8000.


