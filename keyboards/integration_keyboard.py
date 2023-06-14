from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def integration_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    # кнопки
    kb.button(text="Брно", callback_data="IC_K0")
    kb.button(text="Злин", callback_data="IC_K1")
    kb.button(text="Прага", callback_data="IC_K2")
    kb.button(text="Кадан", callback_data="IC_K3")
    kb.button(text="Плзень", callback_data="IC_K4")
    kb.button(text="Кладно", callback_data="IC_K5")
    kb.button(text="Теплице", callback_data="IC_K6")
    kb.button(text="Бенешов", callback_data="IC_K7")
    kb.button(text="Оломоуц", callback_data="IC_K8")
    kb.button(text="Йиглава", callback_data="IC_K9")
    kb.button(text="Либерец", callback_data="IC_K10")
    kb.button(text="Острава", callback_data="IC_K11")
    kb.button(text="Пршибрам", callback_data="IC_K12")
    kb.button(text="Пардубице", callback_data="IC_K13")
    kb.button(text="Кутна Гора", callback_data="IC_K14")
    kb.button(text="Карловы Вары", callback_data="IC_K15")
    kb.button(text="Млада болеслав", callback_data="IC_K16")
    kb.button(text="Усти над Лабем", callback_data="IC_K17")
    kb.button(text="Градец Кралове", callback_data="IC_K18")
    kb.button(text="Ческе Будеёвице", callback_data="IC_K19")

    kb.button(text="🔙", callback_data="integration_exit_call")
    # колчиество кнопок в ряд
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# брно
def brno_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="brno_dk0")
    kb.button(text="На карте 🗺", callback_data="brno_dk1")
    kb.button(text="📞 Телефон", callback_data="brno_dk2")
    kb.button(text="Как работает?", callback_data="brno_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# злин
def zlin_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="zlin_dk0")
    kb.button(text="На карте 🗺", callback_data="zlin_dk1")
    kb.button(text="📞 Телефон", callback_data="zlin_dk2")
    kb.button(text="Как работает?", callback_data="zlin_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# прага
def praha_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="praha_dk0")
    kb.button(text="На карте 🗺", callback_data="praha_dk1")
    kb.button(text="📞 Телефон", callback_data="praha_dk2")
    kb.button(text="Как работает?", callback_data="praha_dk3")
    kb.button(text="🔘 Сайт", url="https://www.cicops.cz/")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# злин
def kadan_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="kadan_dk0")
    kb.button(text="На карте 🗺", callback_data="kadan_dk1")
    kb.button(text="🔘 Сайт", callback_data="https://p-p-i.cz/")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# плзень
def plzen_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="plzen_dk0")
    kb.button(text="На карте 🗺", callback_data="plzen_dk1")
    kb.button(text="📞 Телефон", callback_data="plzen_dk2")
    kb.button(text="Как работает?", callback_data="plzen_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# кладно
def kladno_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="kladno_dk0")
    kb.button(text="На карте 🗺", callback_data="kladno_dk1")
    kb.button(text="📞 Телефон", callback_data="kladno_dk2")
    kb.button(text="Как работает?", callback_data="kladno_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# теплице
def teplice_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="teplice_dk0")
    kb.button(text="На карте 🗺", callback_data="teplice_dk1")
    kb.button(text="📞 Телефон", callback_data="teplice_dk2")
    kb.button(text="Как работает?", callback_data="teplice_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# теплице
def benesov_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="benesov_dk0")
    kb.button(text="На карте 🗺", callback_data="benesov_dk1")
    kb.button(text="📞 Телефон", callback_data="benesov_dk2")
    kb.button(text="Как работает?", callback_data="benesov_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# оломоуц
def olomouc_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="olomouc_dk0")
    kb.button(text="На карте 🗺", callback_data="olomouc_dk1")
    kb.button(text="📞 Телефон", callback_data="olomouc_dk2")
    kb.button(text="Как работает?", callback_data="olomouc_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Йиглава
def jihlava_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="jihlava_dk0")
    kb.button(text="На карте 🗺", callback_data="jihlava_dk1")
    kb.button(text="📞 Телефон", callback_data="jihlava_dk2")
    kb.button(text="Как работает?", callback_data="jihlava_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Либерец
def liberec_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="liberec_dk0")
    kb.button(text="На карте 🗺", callback_data="liberec_dk1")
    kb.button(text="📞 Телефон", callback_data="liberec_dk2")
    kb.button(text="Как работает?", callback_data="liberec_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Острава
def ostrava_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="ostrava_dk0")
    kb.button(text="На карте 🗺", callback_data="ostrava_dk1")
    kb.button(text="📞 Телефон", callback_data="ostrava_dk2")
    kb.button(text="Как работает?", callback_data="ostrava_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Пршибрам
def pribram_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pribram_dk0")
    kb.button(text="На карте 🗺", callback_data="pribram_dk1")
    kb.button(text="📞 Телефон", callback_data="pribram_dk2")
    kb.button(text="Как работает?", callback_data="pribram_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Пардубице
def pardubice_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pardubice_dk0")
    kb.button(text="На карте 🗺", callback_data="pardubice_dk1")
    kb.button(text="📞 Телефон", callback_data="pardubice_dk2")
    kb.button(text="Как работает?", callback_data="pardubice_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Кутна Гора
def kutnah_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="kutnah_dk0")
    kb.button(text="На карте 🗺", callback_data="kutnah_dk1")
    kb.button(text="📞 Телефон", callback_data="kutnah_dk2")
    kb.button(text="Как работает?", callback_data="kutnah_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Карловы Вары
def karlovyv_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="karlovyv_dk0")
    kb.button(text="На карте 🗺", callback_data="karlovyv_dk1")
    kb.button(text="📞 Телефон", callback_data="karlovyv_dk2")
    kb.button(text="Как работает?", callback_data="karlovyv_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Млада болеслав
def mladab_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="mladab_dk0")
    kb.button(text="На карте 🗺", callback_data="mladab_dk1")
    kb.button(text="📞 Телефон", callback_data="mladab_dk2")
    kb.button(text="Как работает?", callback_data="mladab_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Усти над Лабем
def ustinl_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="ustinl_dk0")
    kb.button(text="На карте 🗺", callback_data="ustinl_dk1")
    kb.button(text="📞 Телефон", callback_data="ustinl_dk2")
    kb.button(text="Как работает?", callback_data="ustinl_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Градец Кралове
def hradeck_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="hradeck_dk0")
    kb.button(text="На карте 🗺", callback_data="hradeck_dk1")
    kb.button(text="📞 Телефон", callback_data="hradeck_dk2")
    kb.button(text="Как работает?", callback_data="hradeck_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Ческе Будеёвице
def ceskeb_details_keyboard_integration() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="ceskeb_dk0")
    kb.button(text="На карте 🗺", callback_data="ceskeb_dk1")
    kb.button(text="📞 Телефон", callback_data="ceskeb_dk2")
    kb.button(text="Как работает?", callback_data="ceskeb_dk3")

    kb.button(text="🔙", callback_data="INTEG_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)

