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

