from fastapi.testclient import TestClient
from db.mongo import MongoSessionRegular

import random
import json
from api.main import app

client = TestClient(app)

# test registering a new user, loggin them in, and then loggiing out the account PERMANENTLY
def test_logout_user():
    rando = random.randint(1, 50000000)
    email = "usertest" + str(rando) + "@example.com"
    password = "string"

    # add user in case not existing
    response = client.post("/register", json={
        "email": email,
        "password": password
    })

    # validate user email input
    assert response.json() != {
        "detail": [
            {
                "loc": [
                    "body",
                    "email"
                ],
                "msg": "value is not a valid email address",
                "type": "value_error.email"
            }
        ]
    }
    # verify if existing user
    assert response.json() != {
        "detail": "REGISTER_USER_ALREADY_EXISTS"
    }

    assert response.json()["is_active"] == True
    login_response = client.post("/login", data={"username": email, "password": password})
    jwt_token = json.loads(login_response.content)
    jwt_token = jwt_token["access_token"]
    headers = {"Authorization": "Bearer " + jwt_token}

    logout_response = client.post("/logout", headers=headers)
    assert logout_response.json() == {"user_email": email, "logout_success": "true"}


    # logout_response
    print('\n\n')
    print(response.json())
    print('\n\n')
    print(login_response.json())
    print(logout_response.json())
    print(response.json()["id"])
    print(response.json()["is_active"])
    # print(user["is_active"])
    # print(login_response.json())
    # print(login_response.json())
    print('done')



# def test_logout_non-existing_user():