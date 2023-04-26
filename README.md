# Informetrika test

This project contains a Django web application that provides a RESTful API and a Vue.js front-end application that consumes the API to display data in a table.

## Django Setup

### Prerequisites

- Python 3
-   Django 3.x
-   Vue.js 3.x
-   Node.js and npm (for building the Vue.js client)

### Installation

1. Clone the repository.
2. Navigate to the `django_crud` directory.
3. Install the dependencies with `pip install -r requirements.txt`.
4. Run the migrations with `python manage.py makemigrations`. and  `python manage.py migrate`
5. Start the server with `python manage.py runserver`.

**The Django API should now be accessible at
 [http://localhost:8000/insurance/api/v1/](http://localhost:8000/insurance/api/v1/).**
 
 **The Django API documentation now be accessible at
 [http://localhost:8000/insurance/docs/](http://localhost:8000/insurance/docs/).**

## Vue Setup

### Prerequisites

- Node.js and npm (Node Package Manager)

### Installation

1. Navigate to the `client` directory inside the project.
2. Install the dependencies with `npm install`.
3. Start the development server with `npm run dev`.

**The Vue app should now be accessible at [http://localhost:5173/](http://localhost:5173/).**

## Project Structure

- `django_app`: Contains the Django RESTful API application using a variation of MVT architecture.
  - `insurance`: Contains the API views, serializers and models.  
  - `manage.py`: Django's command-line utility for administrative tasks.
  - `requirements.txt`: Contains the Python dependencies for the  
  - `docs/`: Contains the data strcuture diagram.
  - **`test/`: Contains the necesary tests for the current CRUD functionalities. you can tun the tests using: `python manage.py test`**.
  - 
- `client`: Contains the Vue.js front-end application.
  - `src`: Contains the Vue.js components, services, and views. 
  - `package.json`: Contains the Node.js dependencies for the application. 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```
