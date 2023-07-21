# Pricing-Module

This is a web application that supports differential pricing for products/services. It provides a configurable pricing module with the ability to manage and calculate prices based on distance, time, and waiting time.

## Installation

1. Clone the repository:
```
git clone <repository_url>
```
2. Install the required packages:
```
pip install -r requirements.txt
```
3. Apply the database migrations:
```
python manage.py migrate
```
4. Create a superuser to access the Django Admin:
```
python manage.py createsuperuser
```
5. Start the development server:
```
python manage.py runserver
```
6. Access the application at `http://127.0.0.1:8000/`.

## Usage

### Django Admin

- Access the Django Admin interface at `http://127.0.0.1:8000/admin/`.
- Log in with the superuser credentials created earlier.
- Use the custom form to add, modify, and remove pricing configurations.

### API Endpoints

#### Manage Pricing Configurations

- **GET /api/pricing_configurations/**: Retrieve a list of all pricing configurations.

- **POST /api/pricing_configurations/**: Create a new pricing configuration.
- Payload:
 ```
 {
     "distance_base_price": 80,
     "distance_additional_price": 30,
     "time_multiplier_factor": 1.25,
     "waiting_charges": 5,
     "day_of_week": "Mon",
     "is_active": true
 }
 ```
- **GET /api/pricing_configurations/{id}/**: Retrieve details of a specific pricing configuration.

- **PUT /api/pricing_configurations/{id}/**: Update a specific pricing configuration.

 ```
 {
     "distance_base_price": 90,
     "distance_additional_price": 35,
     "time_multiplier_factor": 1.5,
     "waiting_charges": 6,
     "day_of_week": "Tue",
     "is_active": true
 }
 ```
- **DELETE /api/pricing_configurations/{id}/**: Delete a specific pricing configuration.

#### Calculate Price

- **POST /api/calculate_price/**: Calculate the price based on the given parameters.
- Payload:
 ```
 {
     "distance": 2.5,
     "time_duration": 0.75,
     "waiting_time": 5,
     "day_of_week": "Mon"
 }
 ```
