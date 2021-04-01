from Orders.models.models import UserProfile


class RegisterLogic:

    def register(self, data):
        user = UserProfile.objects.create(
            username=data['username'],
            first_name=data['firstName'],
            last_name=data['lastName'],
        )

        user.set_password(data['password'])
        user.save()