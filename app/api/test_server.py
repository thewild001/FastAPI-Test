from fastapi.testclient import TestClient
from .server import app

client = TestClient(app)

def test_proccess_order():
    """
    Test the '/solution' endpoint.
    """

    request_data = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
            {"id": 3, "item": "Headphones", "quantity": 3, "price": 99.90, "status": "completed"},
            {"id": 4, "item": "Mouse", "quantity": 4, "price": 24.99, "status": "canceled"}
        ],
        "criterion": "completed"
    }

    response = client.post("/solution", json=request_data)
    assert response.status_code == 200

def test_process_order_completed():
    """
    Test the endpoint '/solution' with the criterion 'completed' to calculate the total revenue.
    """

    request_data = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "completed"},
        ],
        "criterion": "completed"
    }

    
    response = client.post("/solution", json=request_data)
    
    assert response.status_code == 200
    assert response.json() == {"total_revenue": 1499.94}

def test_process_order_pending():
    """
    Test the endpoint '/solution' with the criterion 'pending' to calculate the total revenue.
    """

    request_data = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
        ],
        "criterion": "pending"
    }

    response = client.post("/solution", json=request_data)

    assert response.status_code == 200
    assert response.json() == {"total_revenue": 1999.89}

def test_process_order_all():
    """
    Try the endpoint '/solution' with the criterion 'all' to calculate the total revenue of all orders.
    """

    request_data = {
        "orders": [
            {"id": 1, "item": "Laptop", "quantity": 1, "price": 999.99, "status": "completed"},
            {"id": 2, "item": "Smartphone", "quantity": 2, "price": 499.95, "status": "pending"},
        ],
        "criterion": "all"
    }


    response = client.post("/solution", json=request_data)

    assert response.status_code == 200
    assert response.json() == {"total_revenue": 1999.89}


    




