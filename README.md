# LunchVoteService

This service helps employees make decisions about lunch places. It allows restaurants to upload menus daily via API and enables employees to vote for menus through a mobile app. The backend is implemented using Django and Django Rest Framework (DRF).

## API Functionality
- Authentication: Users can authenticate using JWT tokens.
- Restaurant Management: API endpoints for creating and managing restaurants.
- Menu Management: API endpoints for uploading menus for each restaurant daily.
- Employee Management: API endpoints for creating and managing employees.
- Get Current Day Menu: Endpoint to retrieve the menu for the current day.
- Get Results for the Current Day: Endpoint to get the voting results for the current day.

### Tech Stack
- Backend Framework: Django + Django Rest Framework
- Database: PostgreSQL
- Testing: TestCase
- Containerization: Docker (docker-compose)
- Linting: Flake8

### Quick Start
Docker and Python3 must be installed on your system to run this project.

1. Clone the repository to your local machine:
```bash
git clone <repository_url>
```

2. Set up environment variables:
- Create a `.env` file in the root directory.
- Add necessary environment variables like POSTGRES_PORT, SECRET_KEY, etc.

3. Build and run the project using Docker:
```bash
docker-compose up --build
```

4. Access the API at `http://localhost:8000/` and explore the available endpoints.

### API Endpoints
- `/api/restaurants/`: GET, POST
- `/api/restaurants/menus/`: GET, POST
- `/api/votes/`: GET, POST
- `/api/votes/results/`: GET

### User Endpoints
- `/api/employees/register/`: POST
- `/api/employees/token/`: POST
- `/api/employees/token/refresh/`: POST
- `/api/employees/token/verify/`: POST
- `/api/employees/me/`: GET, PUT


### Feel free to reach out for any further assistance or clarification!
