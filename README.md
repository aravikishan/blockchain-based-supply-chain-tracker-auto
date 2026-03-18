# Blockchain-Based Supply Chain Tracker

## Overview
The Blockchain-Based Supply Chain Tracker is a decentralized application designed to enhance transparency and traceability within supply chain operations. By leveraging blockchain technology, this application ensures that every transaction and status update of products is securely recorded and easily accessible. This project addresses the common issues of data manipulation and lack of transparency in supply chains, providing a reliable solution for businesses, logistics companies, and consumers who need to track the provenance and status of products in real-time.

The application offers a user-friendly interface for managing products, tracking their journey, and ensuring that all data is immutable and verifiable. It is ideal for industries where supply chain integrity is critical, such as pharmaceuticals, food, and luxury goods.

## Features
- **Product Management**: Easily add, view, and manage products within the supply chain.
- **Real-time Tracking**: Track the current status and location of products with blockchain-backed data.
- **User Authentication**: Secure login system to protect sensitive supply chain data.
- **Dashboard Analytics**: Visual insights into supply chain operations and product statuses.
- **Responsive Design**: Accessible on various devices with a mobile-friendly interface.

## Tech Stack
| Technology    | Description                                   |
|---------------|-----------------------------------------------|
| FastAPI       | Web framework for building APIs               |
| Uvicorn       | ASGI server for running FastAPI applications  |
| SQLAlchemy    | ORM for database interactions                 |
| Jinja2        | Templating engine for rendering HTML          |
| SQLite        | Lightweight database for data storage         |
| Docker        | Containerization for deployment               |

## Architecture
The project is structured to separate concerns between the frontend and backend, with a clear data flow from the database to the user interface.

```plaintext
+-----------------+
|   Frontend      |
| (HTML/CSS/JS)   |
+-----------------+
        |
        v
+-----------------+
|   FastAPI       |
| (Backend API)   |
+-----------------+
        |
        v
+-----------------+
|   SQLite DB     |
+-----------------+
```

- **Frontend**: Static HTML templates rendered using Jinja2, styled with CSS, and interactive with JavaScript.
- **Backend**: FastAPI serves as the backend, handling API requests and serving HTML pages.
- **Database**: SQLite is used for storing product, user, and transaction data.

## Getting Started

### Prerequisites
- Python 3.11+
- pip package manager
- Docker (optional for containerized deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/blockchain-based-supply-chain-tracker-auto.git
   cd blockchain-based-supply-chain-tracker-auto
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. Start the FastAPI application:
   ```bash
   uvicorn app:app --reload
   ```
2. Visit the application in your browser at `http://localhost:8000`

## API Endpoints
| Method | Path                  | Description                               |
|--------|-----------------------|-------------------------------------------|
| GET    | /                     | Home page                                 |
| GET    | /dashboard            | Dashboard with analytics                  |
| GET    | /products             | Products management page                  |
| GET    | /track                | Product tracking page                     |
| GET    | /login                | User login page                           |
| GET    | /api/products         | Retrieve all products                     |
| POST   | /api/products         | Create a new product                      |
| GET    | /api/products/{id}    | Retrieve a product by ID                  |
| GET    | /api/track/{id}       | Track a product by ID                     |
| POST   | /api/auth/login       | User login with username and password     |

## Project Structure
```
blockchain-based-supply-chain-tracker-auto/
├── app.py                # Main application file
├── Dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── start.sh              # Script to start the application
├── static/               # Static files (CSS, JS)
│   ├── css/
│   │   └── style.css     # Styling for the application
│   └── js/
│       └── main.js       # JavaScript for interactivity
└── templates/            # HTML templates
    ├── dashboard.html    # Dashboard page
    ├── index.html        # Home page
    ├── login.html        # Login page
    ├── products.html     # Products page
    └── track.html        # Track product page
```

## Screenshots
- Placeholder for screenshots showing the user interface and features.

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t supply-chain-tracker .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 supply-chain-tracker
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
Built with Python and FastAPI.
