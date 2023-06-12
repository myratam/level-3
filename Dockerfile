#Set the base image to Python (lastest version)
FROM python:latest

#Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

#Install the project dependencies
RUN pip install -r requirements.txt

#Copy the entire project directory into the container
COPY . .

#Expose the port on which your Django app will run
EXPOSE 8000

#Set environment variables, if necessary
#ENV VARIABLE_NAME=value

#Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

