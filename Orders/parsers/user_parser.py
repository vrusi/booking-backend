import Orders.api_models.models as api


class UserParser:

    def parser_user_info(self, user):
        api_user = api.User(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
        )

        return api_user
