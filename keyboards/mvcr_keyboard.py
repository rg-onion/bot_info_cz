# from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    # кнопки
    kb.button(text="MVCR", callback_data="MVCR_start_call")
    kb.button(text="Integration center", callback_data="INTEG_start_call")
    # kb.button(text="Удалить ту ⬇️ клавиатуру ", callback_data="deleteKey0")
    # колчиество кнопок в ряд
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


def mvcr_keyboard() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='🕜 Бронирование online', url='https://frs.gov.cz/')
    kb.button(text='Контакты online 🔵',
              url='https://www.mvcr.cz/clanek/sluzby-pro-verejnost-informace-pro-cizince-kontakty.aspx')

    kb.button(text="Прага", callback_data="JC_K9")
    kb.button(text="Устецкий", callback_data="JC_K11")
    kb.button(text="Высочина", callback_data="JC_K12")
    kb.button(text="Злинский", callback_data="JC_K13")
    kb.button(text="Либерецкий", callback_data="JC_K04")
    kb.button(text="Оломоуцкий", callback_data="JC_K6")
    kb.button(text="Пльзенский", callback_data="JC_K8")
    kb.button(text="Южночешский", callback_data="JC_K0")
    kb.button(text="Пардубицкий", callback_data="JC_K7")
    kb.button(text="Карловарский", callback_data="JC_K2")
    kb.button(text="Среднечешский", callback_data="JC_K10")
    kb.button(text="Южно-Моравский", callback_data="JC_K1")
    kb.button(text="Краловеградецкий", callback_data="JC_K3")
    kb.button(text="Моравскосилезский", callback_data="JC_K5")

    kb.button(text="🔙", callback_data="MVCR_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Южночешский край mvcr
def jc_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Ческе-Будейовицe", callback_data="JC_sity_k0")
    kb.button(text="Писек", callback_data="JC_sity_k1")
    kb.button(text="Йиндрихув Градец", callback_data="JC_sity_k2")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


# ceske budejovice
def jc_cb_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="cb_dk0")
    kb.button(text="На карте 🗺", callback_data="cb_dk1")
    kb.button(text="📞 Телефон", callback_data="cb_dk2")
    kb.button(text="Как работает?", callback_data="cb_dk3")

    kb.button(text="🔙", callback_data="JC_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# писек
def jc_pi_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pi_dk0")
    kb.button(text="На карте 🗺", callback_data="pi_dk1")
    kb.button(text="📞 Телефон", callback_data="pi_dk2")
    kb.button(text="Как работает?", callback_data="pi_dk3")

    kb.button(text="🔙", callback_data="JC_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Йиндрихув Градец
def jc_jg_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="jg_dk0")
    kb.button(text="На карте 🗺", callback_data="jg_dk1")
    kb.button(text="📞 Телефон", callback_data="jg_dk2")

    kb.button(text="🔙", callback_data="JC_exit_call")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


# Карловарский край
def ka_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="ka_dk0")
    kb.button(text="На карте 🗺", callback_data="ka_dk1")
    kb.button(text="📞 Телефон", callback_data="ka_dk2")
    kb.button(text="Как работает?", callback_data="ka_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# краловоградетский край
def hk_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="hk_dk0")
    kb.button(text="На карте 🗺", callback_data="hk_dk1")
    kb.button(text="📞 Телефон", callback_data="hk_dk2")
    kb.button(text="Как работает?", callback_data="hk_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# либерец
def lb_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="lb_dk0")
    kb.button(text="На карте 🗺", callback_data="lb_dk1")
    kb.button(text="📞 Телефон", callback_data="lb_dk2")
    kb.button(text="Как работает?", callback_data="lb_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Моравскосилезский
def ms_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Острава", callback_data="ms_sity_k0")
    kb.button(text="Фридек-Мистек", callback_data="ms_sity_k1")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# острава
def ms_o_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="o_dk0")
    kb.button(text="На карте 🗺", callback_data="o_dk1")
    kb.button(text="📞 Телефон", callback_data="o_dk2")
    kb.button(text="Как работает?", callback_data="o_dk3")

    kb.button(text="🔙", callback_data="ms_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Фридек-Мистек
def ms_fm_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="fm_dk0")
    kb.button(text="На карте 🗺", callback_data="fm_dk1")
    kb.button(text="📞 Телефон", callback_data="fm_dk2")
    kb.button(text="Как работает?", callback_data="fm_dk3")

    kb.button(text="🔙", callback_data="ms_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Оломоуцкий
def ol_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="ol_dk0")
    kb.button(text="На карте 🗺", callback_data="ol_dk1")
    kb.button(text="📞 Телефон", callback_data="ol_dk2")
    kb.button(text="Как работает?", callback_data="ol_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Пардубицкий
def par_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="par_dk0")
    kb.button(text="На карте 🗺", callback_data="par_dk1")
    kb.button(text="📞 Телефон", callback_data="par_dk2")
    kb.button(text="Как работает?", callback_data="par_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Пльзенский
def pl_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pl_dk0")
    kb.button(text="На карте 🗺", callback_data="pl_dk1")
    kb.button(text="📞 Телефон", callback_data="pl_dk2")
    kb.button(text="Как работает?", callback_data="pl_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# прага
# mvcr
def prag_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Прага I", callback_data="Pr_sity_k0")
    kb.button(text="Прага II", callback_data="Pr_sity_k1")
    kb.button(text="Прага III", callback_data="Pr_sity_k2")
    kb.button(text="Прага-Летна", callback_data="Pr_sity_k3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# прага I
def pr1_cb_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pr1_dk0")
    kb.button(text="На карте 🗺", callback_data="pr1_dk1")
    kb.button(text="📞 Телефон", callback_data="pr1_dk2")
    kb.button(text="Как работает?", callback_data="pr1_dk3")

    kb.button(text="🔙", callback_data="prag_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# прага II
def pr2_cb_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pr2_dk0")
    kb.button(text="На карте 🗺", callback_data="pr2_dk1")
    kb.button(text="📞 Телефон", callback_data="pr2_dk2")
    kb.button(text="Как работает?", callback_data="pr2_dk3")

    kb.button(text="🔙", callback_data="prag_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# прага III
def pr3_cb_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pr3_dk0")
    kb.button(text="На карте 🗺", callback_data="pr3_dk1")
    kb.button(text="📞 Телефон", callback_data="pr3_dk2")
    kb.button(text="Как работает?", callback_data="pr3_dk3")

    kb.button(text="🔙", callback_data="prag_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# прага letna
def pr4_cb_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pr4_dk0")
    kb.button(text="На карте 🗺", callback_data="pr4_dk1")
    kb.button(text="Как работает?", callback_data="pr4_dk2")

    kb.button(text="🔙", callback_data="prag_exit_call")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)


# среднечешский
def sk_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Бенешов", callback_data="sk_sity_k0")
    kb.button(text="Кладно", callback_data="sk_sity_k1")
    kb.button(text="Кутна Гора", callback_data="sk_sity_k2")
    kb.button(text="Млада Болеслав", callback_data="sk_sity_k3")
    kb.button(text="Пршибрам", callback_data="sk_sity_k4")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Бенешов
def sk_be_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="be_dk0")
    kb.button(text="На карте 🗺", callback_data="be_dk1")
    kb.button(text="📞 Телефон", callback_data="be_dk2")
    kb.button(text="Как работает?", callback_data="be_dk3")

    kb.button(text="🔙", callback_data="sk_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# кладно
def sk_kl_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="kl_dk0")
    kb.button(text="На карте 🗺", callback_data="kl_dk1")
    kb.button(text="📞 Телефон", callback_data="kl_dk2")
    kb.button(text="Как работает?", callback_data="kl_dk3")

    kb.button(text="🔙", callback_data="sk_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# кутна гора
def sk_kg_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="kg_dk0")
    kb.button(text="На карте 🗺", callback_data="kg_dk1")
    kb.button(text="📞 Телефон", callback_data="kg_dk2")
    kb.button(text="Как работает?", callback_data="kg_dk3")

    kb.button(text="🔙", callback_data="sk_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Млада болеслав
def sk_m_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="m_dk0")
    kb.button(text="На карте 🗺", callback_data="m_dk1")
    kb.button(text="📞 Телефон", callback_data="m_dk2")
    kb.button(text="Как работает?", callback_data="m_dk3")

    kb.button(text="🔙", callback_data="sk_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# пришбрам
def sk_pr_details_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="pr_dk0")
    kb.button(text="На карте 🗺", callback_data="pr_dk1")
    kb.button(text="📞 Телефон", callback_data="pr_dk2")
    kb.button(text="Как работает?", callback_data="pr_dk3")

    kb.button(text="🔙", callback_data="sk_exit_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Устецкий
# усти над лабем
def ust_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="unl_dk0")
    kb.button(text="На карте 🗺", callback_data="unl_dk1")
    kb.button(text="📞 Телефон", callback_data="unl_dk2")
    kb.button(text="Как работает?", callback_data="unl_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# Высочина
def vys_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="vys_dk0")
    kb.button(text="На карте 🗺", callback_data="vys_dk1")
    kb.button(text="📞 Телефон", callback_data="vys_dk2")
    kb.button(text="Как работает?", callback_data="vys_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# злин
def zlin_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="zl_dk0")
    kb.button(text="На карте 🗺", callback_data="zl_dk1")
    kb.button(text="📞 Телефон", callback_data="zl_dk2")
    kb.button(text="Как работает?", callback_data="zl_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


# brno
def brno_keyboard_mvcr() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Адрес", callback_data="br_dk0")
    kb.button(text="На карте 🗺", callback_data="br_dk1")
    kb.button(text="📞 Телефон", callback_data="br_dk2")
    kb.button(text="Как работает?", callback_data="br_dk3")

    kb.button(text="🔙", callback_data="MVCR_start_call")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
