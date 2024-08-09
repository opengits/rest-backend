
# Backend for Shared ORM Library

## Overview

The **Backend** project is a Django application that utilizes the shared ORM library to provide an API endpoint for managing users and settings. This backend serves as the API provider for an Angular frontend and other clients.

## Project Structure

- **`backend/`**: Contains the Django project with the API endpoint and configurations.
- **`shared_orm_library/`**: The shared library with ORM models and database configurations.

## Setup and Installation

### Prerequisites

- Python 3.x
- PostgreSQL (or any other supported database)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/opengits/rest-backend.git
   cd backend_project
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install the Shared ORM Library**

   Clone it and generate distribution as directed from
   
    ```bash
   git clone https://github.com/opengits/shared_orm_library.git
   ```
    
   Navigate to the `dist/` directory where the shared ORM library package is located and install it:

   
   ```bash
   pip install dist/shared_orm_library-<version>.tar.gz
   ```

   Make sure to replace `<version>` with the actual version number of the built package.

6. **Configure the Django Project**

   Ensure the `shared_orm_library` is added to `INSTALLED_APPS` in `backend/settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'sharedorm',  # Add this line
       ...
   ]
   ```

7. **Apply Migrations**

   Create and apply migrations for the models defined in the shared library:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

8. **Create Superuser**

   Create a superuser account to access the Django admin interface:

   ```bash
   python manage.py createsuperuser
   ```

9. **Run the Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The backend server will be available at `http://127.0.0.1:8000`.

## API Endpoints

- **GET `/api/users/`**: Returns a list of all users in JSON format.

## Contributing

1. **Fork the Repository**
2. **Create a New Branch**
3. **Make Your Changes**
4. **Submit a Pull Request**

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please contact [Kamal Sharma](mailto:kamalsharma.git@gmail.com).
```

### Summary

- **Project Overview**: Brief description and structure.
- **Setup and Installation**: Steps to clone, install dependencies, configure the project, and run the server.
- **API Endpoints**: Information on available API endpoints.
- **Testing**: Instructions to run tests.
- **Contributing**: Guidelines for contributing.
- **License and Contact**: Licensing information and contact details.

This `README.md` provides clear instructions on how to set up and use the backend project, including integrating the shared ORM library and running the development server.
