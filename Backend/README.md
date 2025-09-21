# AI Story Generator Backend

This project is the backend service for the AI Story Generator application. It provides APIs for generating, storing, and managing AI-generated stories.

## Features

- Generate stories using AI models
- Save and retrieve generated stories
- User authentication and management
- RESTful API endpoints

## Technologies Used

- Python (FastAPI)
- PostgreSQL
- Docker

## Getting Started

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/ai-story-generator-backend.git
    cd ai-story-generator-backend
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure environment variables**
    - Copy `.env.example` to `.env` and update values as needed.

4. **Run the application**
    ```bash
    uvicorn main:app --reload
    ```

## API Documentation

- Access interactive docs at `/docs` when the server is running.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the MIT License.