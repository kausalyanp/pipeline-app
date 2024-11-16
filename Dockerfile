# Step 1: Start with a base Python image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . .

# Step 6: Expose the port the app will run on (default Flask port is 5000)
EXPOSE 8081
EXPOSE 8082
EXPOSE 9090

# Step 7: Set the environment variable to run the Flask app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 8: Command to run the Flask app
CMD ["flask", "run"]
