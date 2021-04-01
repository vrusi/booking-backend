from Orders.models.models import UserProfile
from Orders.parsers.user_parser import UserParser


class UserLogic:
    parser = UserParser()

    def get_user_info(self, user_id):

        try:
            user = UserProfile.objects.filter(id=user_id)[0]
        except Exception as e:
            raise e

        api_user = self.parser.parser_user_info(user)
        return api_user
