from telegram import InlineKeyboardButton


def map_inline_keyboard_buttons(config):
    def mapper(item):
        return [
            InlineKeyboardButton(
                text=config[item]['text'],
                callback_data=item,
            )
        ]

    return list(map(mapper, config))
