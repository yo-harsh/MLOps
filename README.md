
# ZenML MLOps Project

This project demonstrates the usage of ZenML for MLOps (Machine Learning Operations). It includes a ZenML pipeline for training a model and a Streamlit web application for making predictions using the trained model.

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)

### Clone the Repository

To get started, clone this Git repository to your local machine:

```bash
git clone https://github.com/yo-harsh/MLOps.git
cd MLOps
```

## Build and Run with Docker

Build and run the Docker containers using Docker Compose:

```bash
docker-compose up --build
```

This command will build the necessary Docker images and start the services.


### Access ZenML Dashboard

Visit [localhost:8080]() to access the ZenML Dashboard. Here, you can view and manage your machine learning pipelines.

### Access Streamlit App

The Streamlit web application is available at [localhost:8501](). Use this app to interact with the trained model and make predictions.

don't run docker compose up --build again just first time after that run "docker compose up"


## Important Notice

Please note that Docker is required to run this project. Make sure to install Docker before attempting to build and run the project.


## Feedback and Suggestions

Feel free to provide feedback and suggestions.
