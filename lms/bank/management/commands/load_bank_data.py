from django.core.management.base import BaseCommand
from bank.models import *
from django.contrib.auth.models import User


class Command(BaseCommand):
    list_of_users_names = ["Goha", "Ivan", "Kolya", "Grisha", "Vova", "Dorothy", "Oleg", "Danya", "Masha"]
    list_of_groups_names = ["Develop", "Test", "Product", "Chill"]
    list_of_profiles = [
        {"name": "Олег Игнатич",
         "city": "Москва",
         "rank": "Капитан",
         "description": "Играю Пои Шучу",
         "avatar": "bank/profile/1.jpg",
         "status": "user",
         },
        {"name": "Иван Сергеевич",
         "city": "Питер",
         "rank": "Майор",
         "description": "Что то о себе невнятное",
         "avatar": "bank/profile/2.jpg",
         "status": "user",
         },
        {"name": "Кольян Коляныч",
         "city": "Омск",
         "rank": "Ефрейтор",
         "description": "Служу России",
         "avatar": "bank/profile/3.jpg",
         "status": "user",
         },
        {"name": "Гриша Смольскас",
         "city": "Калуга",
         "rank": "Лейтенант",
         "description": "Не служил",
         "avatar": "bank/profile/4.jpg",
         "status": "boss",
         },
        {"name": "Просто Вова",
         "city": "Томск",
         "rank": "Нет",
         "description": "Имею машину",
         "avatar": "bank/profile/5.jpg",
         "status": "user",
         },
        {"name": "Ирина Николаевна",
         "city": "Москва",
         "rank": "Нет",
         "description": "Работаю в офисе",
         "avatar": "bank/profile/6.jpg",
         "status": "user",
         },
        {"name": "Олег Иваныч",
         "city": "Обнинск",
         "rank": "Сам по себе",
         "description": "Курю кальян",
         "avatar": "bank/profile/7.jpg",
         "status": "user",
         },
        {"name": "Даниил Игоревич",
         "city": "Калуга",
         "rank": "Рядовой",
         "description": "Тусю, Курю, Отдыхаю",
         "avatar": "bank/profile/8.jpg",
         "status": "user",
         },
        {"name": "Марии Константиновна",
         "city": "Ржев",
         "rank": "Рядовая",
         "description": "Работаю в бизнесе",
         "avatar": "bank/profile/9.jpg",
         "status": "editor",
         },
    ]

    def __fill_user_name(self, name):
        """Сгенерим данные пользователя"""

        data = {"username": name,
                "email": f'{name}@mail.ru', }
        return data

    def _create_users(self):
        """Создадим пользователей и назначим пароль"""

        list_of_users_data = [self.__fill_user_name(x) for x in self.list_of_users_names]

        self.users_instances = []
        for user_data in list_of_users_data:
            user, status = User.objects.get_or_create(**user_data)
            user.set_password("1")
            user.save()
            self.users_instances.append(user)


    def __create_profile(self, username=None, profile_data=None):
        """Создадим один профиль"""

        # username = "Goha"
        # profile_data = self.list_of_profiles[0]

        user = User.objects.get(username=username)
        profile, status = Profile.objects.get_or_create(user=user)
        Profile.objects.filter(user=user).update(**profile_data)
        return profile

    def _create_profiles(self):
        """Создадим профили для всех пользователей"""

        self.profiles_instances = []
        for index in range(9):
            username = self.list_of_users_names[index]
            profile_data = self.list_of_profiles[index]
            profile = self.__create_profile(username, profile_data)
            self.profiles_instances.append(profile)


    def __create_group(self, username, groupname):
        """Создадим одну группу"""

        # username = "Goha"
        # group_name = "Winners"

        user = User.objects.get(username=username)
        group, status = VtbGroup.objects.get_or_create(name=groupname, owner=user)
        group.users.add(user)
        return group

    def __add_to_exist_group(self, username, group):
        """Добавить к уже существующей группе"""

        user = User.objects.get(username=username)
        group.users.add(user)


    def _create_groups(self):
        """Создадим добавим пользователей в группы"""

        self.groups_instances = []
        for index in range(4):
            group_name = self.list_of_groups_names[index]
            user_name = self.list_of_users_names[index]
            group = self.__create_group(username=user_name, groupname=group_name)
            self.groups_instances.append(group)

            # остальных пользователей добавим тоже (а не только первых 4)
            user_name = self.list_of_users_names[index + 5]
            self.__add_to_exist_group(username=user_name, group=group)
            self.groups_instances.append(group)


    def _create_accounts(self):
        """Создадим аккаунты для всех пользователей"""

        self.accounts_instances = []
        for index in range(9):
            username = self.list_of_users_names[index]
            user = User.objects.get(username=username)
            account, status = Account.objects.get_or_create(user=user)
            account.create_wallet()
            self.accounts_instances.append(account)

    def handle(self, *args, **options):
        """В каком порядку выполняем"""

        self._create_users()
        self._create_groups()
        self._create_profiles()
        self._create_accounts()