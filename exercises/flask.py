from flask import Flask, request
from markupsafe import escape


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    users = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.post("/user")
        def create_user():
            req_dict = request.get_json()

            if "name" in req_dict:
                user = req_dict["name"]
                FlaskExercise.users[user] = req_dict
                response = ({"data": f"User {user} is created!"}, 201)
            else:
                response = ({"errors": {"name": "This field is required"}}, 422)
            return response

        @app.get("/user/<username>")
        def user_get(username):
            username = escape(username)
            if username in FlaskExercise.users:
                response = ({"data": f"My name is {username}"}, 200)
            else:
                response = ({"errors": {username: "This user not found"}}, 404)
            return response

        @app.patch("/user/<username>")
        def update_user(username):
            username = escape(username)
            req_dict = request.get_json()
            if username in FlaskExercise.users:
                if "name" in req_dict.keys():
                    user = req_dict["name"]
                    FlaskExercise.users.pop(username)
                    FlaskExercise.users[user] = req_dict
                    response = ({"data": f"My name is {user}"}, 200)
                else:
                    response = ({"errors": {"name": "This field is required"}}, 422)
            else:
                response = app.response_class(status=204)
            return response

        @app.delete("/user/<username>")
        def delete_user(username):
            if username in FlaskExercise.users:
                FlaskExercise.users.pop(username)
            return app.response_class(status=204)
