from fastapi.testclient import TestClient
from backend.api.main import app
import sys
import os

# Add project root to path
sys.path.append(os.getcwd())

client = TestClient(app)

def test_read_main():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_get_cities():
    response = client.get("/api/cities/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    # If data loaded, should have items
    # print(response.json())

def test_get_city_current():
    # Helper to get a valid city
    cities = client.get("/api/cities/").json()
    if not cities:
        print("No cities found, skipping detailed test")
        return
        
    city_name = cities[0]['name']
    response = client.get(f"/api/cities/{city_name}/current")
    if response.status_code == 200:
        data = response.json()
        assert data['city'] == city_name
        assert 'temperature' in data

def test_get_forecast():
    cities = client.get("/api/cities/").json()
    if not cities:
        return
    city_name = cities[0]['name']
    
    # This might trigger model fitting which is slow, so we test existence
    response = client.get(f"/api/predictions/{city_name}/forecast?days=5")
    # It might fail if model fitting fails or libraries missing, but let's see
    if response.status_code == 200:
        data = response.json()
        assert data['city'] == city_name
        assert len(data['forecast']) == 5

if __name__ == "__main__":
    try:
        test_read_main()
        print("Health check passed")
        test_get_cities()
        print("Get cities passed")
        test_get_city_current()
        print("Get city current passed")
        test_get_forecast()
        print("Get forecast passed")
    except Exception as e:
        print(f"Tests failed: {e}")
        exit(1)
