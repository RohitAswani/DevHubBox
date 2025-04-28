# DevBoxHub

DevBoxHub simplifies the process of setting up development environments using Docker. With just a single command, developers can spin up pre-configured stacks like **MERN**, **LAMP**, and more. You can also customize which services (frontend, backend, database) you need for your project, all automated.

## Features

- **Single Command Setup**: Easily spin up stacks like **MERN**, **LAMP**, and others.
- **Customizable Services**: Select the services you want (frontend, backend, MongoDB, etc.).
- **Automatic Configuration**: Automatically generates a `docker-compose.yml` file based on your selected services.
- **Persistent Data**: MongoDB and other services store data persistently using Docker volumes.

## Getting Started

### Prerequisites

- Python 3.x
- Docker and Docker Compose

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/devboxhub.git
   cd devboxhub

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt


**Usage**
Run the DevBoxHub CLI to create your development environment:

   ```bash 
   python3 cli/devboxhub.py run mern
   ```

Follow the prompts to select the services you want in your stack (e.g., frontend, backend, MongoDB). The docker-compose.yml file will be automatically generated and services will be started.

To view available templates (like MERN, LAMP), use:

   ```bash
   python3 cli/devboxhub.py list
   ```
<br>


### Example
To set up a MERN stack (frontend, backend, MongoDB):

This will:
- Build and start the frontend (React app).
- Build and start the backend (Node.js/Express app).
- Set up MongoDB.

You can modify the stack and services as per your project requirements.

<br>


### Tech Stack
- Frontend: React
- Backend: Node.js, Express
- Database: MongoDB (or any other service selected)
- Docker: Containerization for the entire environment

<br>


### Contributing
- Feel free to contribute to the project. Here’s how you can help:
- Fork the repository.
- Create a new branch for your changes.
- Push your changes and create a pull request.

<br>

<br>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

