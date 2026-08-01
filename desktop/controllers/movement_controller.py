import requests


class MovementController:

    BASE_URL = "http://127.0.0.1:8000/movements"

    

    def get_movements(self):
        response = requests.get(self.BASE_URL)

        response.raise_for_status()

        return response.json()

    def create_movement(
        self,
        description,
        amount,
        category,
        movement_type
    ):
        data = {
            "description": description,
            "amount": amount,
            "category": category,
            "movement_type": movement_type
        }

        response = requests.post(
            self.BASE_URL,
            json=data
        )

        response.raise_for_status()

        return response.json()

    def update_movement(
        self,
        movement_id,
        description,
        amount,
        category,
        movement_type
    ):
        data = {
            "description": description,
            "amount": amount,
            "category": category,
            "movement_type": movement_type
        }

        response = requests.put(
            f"{self.BASE_URL}/{movement_id}",
            json=data
        )

        response.raise_for_status()

        return response.json()

    def delete_movement(self, movement_id):
        response = requests.delete(
            f"{self.BASE_URL}/{movement_id}"
        )

        response.raise_for_status()

        return response.json()

    def predict_category(self, description):

            response = requests.post(
                "http://127.0.0.1:8000/prediction/predict-category",
                json={
                    "description": description
                }
            )

            response.raise_for_status()

            return response.json()["category"]
      