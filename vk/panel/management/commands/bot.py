import vk_api
from vk_api.bot_longpoll import VkBotEventType
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.keyboard import VkKeyboard
from vk_api.keyboard import VkKeyboardColor
from django.core.management.base import BaseCommand
from panel.models import User


def main():
    vk_session = vk_api.VkApi(
        token='b2530899fa53fa467a66deb22374abd1544366c83ba647ec3022915fbd7879139e8784cec48c1858fd83f',
        api_version='5.95',
    )

    button_work = 'Работа'
    button_store = 'Магазин'
    button_business = 'Бизнес'
    button_commands = 'Команды'

    menu = VkKeyboard(
        one_time=True,
    )
    menu.add_button(
        label=button_work,
        color=VkKeyboardColor.POSITIVE,
    )
    menu.add_button(
        label=button_store,
        color=VkKeyboardColor.PRIMARY,
    )
    menu.add_button(
        label=button_business,
        color=VkKeyboardColor.NEGATIVE,
    )
    menu.add_line()
    menu.add_button(
        label=button_commands,
        color=VkKeyboardColor.DEFAULT,
    )
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(
        vk=vk_session,
        group_id=180452399,
    )

    while True:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                user_id = event.object.peer_id
                profile, _ = User.objects.get_or_create(
                    external_id=user_id,
                    defaults={
                        'external_id': user_id,
                    }
                )
                message = event.object.text
                if event.from_user and not event.object.from_me:
                    if message.lower() == 'меню':
                        profile, _ = User.objects.get_or_create(
                            external_id=user_id,
                            defaults={
                                'external_id': user_id,
                            }
                        )
                        vk.messages.send(
                            peer_id=user_id,
                            keyboard=menu.get_keyboard(),
                            random_id=0,
                            message='Вот наше меню:',
                        )
                    elif message.lower() == 'деньги':
                        profile, _ = User.objects.get_or_create(
                            external_id=user_id,
                        )
                        profile.money += 10
                        profile.save()
                        vk.messages.send(
                            peer_id=user_id,
                            random_id=0,
                            message=f'Ваш баланс: {profile.money}',
                        )
                    else:
                        vk.messages.send(
                            peer_id=user_id,
                            random_id=0,
                            message='Привет'
                        )


class Command(BaseCommand):
    help = 'Бот для ВК'

    def handle(self, *args, **options):
        main()
