import json
from starlette.testclient import TestClient
from main import app
client = TestClient(app)


def test_get():
    response = client.get("/listings/1")
    assert response.status_code == 200
    assert response.json()["data"]["listing_id"] == 1
    print(response.json())


def test_add():
    req = {"address": "test address 123", "price": 124000}
    response = client.post("/listings/add", data=json.dumps(req))
    assert response.status_code == 200
    assert response.json()["message"] == "Listing added successfully."
    print(response.json())


def test_update():
    req = {"listing_id": 1,  "address": "test address 124", "price": 124001}
    response = client.put("/listings/update", data=json.dumps(req))
    assert response.status_code == 200
    assert response.json()["message"] == "Listing updated successfully"
    print(response.json())
    get_response = client.get("/listings/1")
    assert response.status_code == 200
    assert response.json()["data"]["price"] == 124001


def test_delete():
    response = client.delete("/listings/8/delete")
    assert response.status_code == 200
    assert response.json()["message"] == "Listing deleted successfully"
    print(response.json())


test_get()
test_add()
test_update()
test_delete()
