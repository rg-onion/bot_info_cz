from aiogram import Router, types
# парсинг
from bs4 import BeautifulSoup

# для работы с геолокацией
from geopy.geocoders import Nominatim

from keyboards.mvcr_keyboard import *
from url.url_mvcr import *

# фото
from photo import photo as ph
# from photo import photo_test as ph

router = Router()  # [1]

start_message0 = "Я <b>информационный</b> бот." \
                 "\n\nВот карта отделений mvcr и интеграционных центров Чехии." \
                 "\n    <i>Используй клавиатуру для навигации по меню</i>"


@router.message(commands=['start'])
async def start(message: types.Message):
    # if not db.subscriber_exists(message.from_user.id):
    #     # если юзера нет,добавляем
    #     db.add_subscriber(message.from_user.id)
    # else:
    #     # если он есть, то обновляем статус подписки
    #     db.update_subscription(message.from_user.id, True)
    markup = types.ReplyKeyboardRemove()
    user = message.from_user.first_name
    await message.answer(text=f"Привет, <b>{user}</b>👋", reply_markup=markup)
    await message.answer(start_message0,
                         reply_markup=start_keyboard())


@router.message(commands=['help'])
async def help_set(message: types.Message):
    text_help = "Пользуясь кнопками клавиатуры ты можешь ознакомиться с информацией " \
                "о <b>местоположении</b> и <b>графике работы</b> департаментов проживания иностранцев <b>(mvcr)</b>, " \
                "а так же <b>центров интеграции</b> на территории Чешской Республики🇨🇿"
    await message.answer(text_help)


# выход из меню
@router.callback_query(text="MVCR_exit_call")
async def mvcr_exit(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    await callback.message.answer(start_message0,
                                  reply_markup=start_keyboard())
    await callback.message.delete()


# start / exit mvcr region hendler
@router.callback_query(text="MVCR_start_call")
async def mvcr_region_exit(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    await callback.message.answer("Выбери свой <b>край</b> на клавиатуре внизу:",
                                  reply_markup=mvcr_keyboard())
    await callback.message.delete()


# регионы Чехии

# Южночешский край
@router.callback_query(text="JC_K0")
async def mvd_jk(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Южночешский край</b>, департаменты:"
    await callback.message.answer(text,
                                  reply_markup=jc_keyboard_mvcr())
    await callback.message.delete()


# exit JC hendler
@router.callback_query(text="JC_exit_call")
async def mvd_jk_exit(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Южночешский край</b>, департаменты:"
    await callback.message.answer(text,
                                  reply_markup=jc_keyboard_mvcr())
    await callback.message.delete()


# České Budějovice
@router.callback_query(text="JC_sity_k0")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>" \
           "\nг.Ческе Будейовице (České Budějovice) " \
           "\n\n<b>Cфера деятельности, районы:</b> " \
           "\nЧеске-Будейовице, Прахатице и Чески-Крумлов " \
           "\n(České Budějovice Prachatice a Český Krumlov)."
    await callback.message.answer_photo(ph.czBudevice_ph, text,
                                        reply_markup=jc_cb_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="cb_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(ceske_budejovice_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="cb_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(ceske_budejovice_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="cb_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(ceske_budejovice_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="cb_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(ceske_budejovice_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# писек
@router.callback_query(text="JC_sity_k1")
async def mvd_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>" \
           "\nг.Писек (Písek) \n\n<b>Cфера деятельности, районы:</b>" \
           "\nПисек и Страконице\n(Písek a Strakonice)."
    await callback.message.answer_photo(ph.pisek_ph, text,
                                        reply_markup=jc_pi_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="pi_dk0")
async def location_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(pisek_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="pi_dk1")
async def location_gps_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(pisek_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pi_dk2")
async def phone_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(pisek_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="pi_dk3")
async def working_time_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(pisek_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Йиндрихув Градец
@router.callback_query(text="JC_sity_k2")
async def mvd_jg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Йиндрихув Градец (Jindřichův Hradec)" \
           "\n\n<b>Cфера деятельности, район:</b> \nЙиндрихув Градец\n(Jindřichův Hradec)."
    await callback.message.answer_photo(ph.jindrichevHradec_ph, text,
                                        reply_markup=jc_jg_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="jg_dk0")
async def location_jg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(jindrichuv_hradec_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="jg_dk1")
async def location_gps_jg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(jindrichuv_hradec_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="jg_dk2")
async def phone_jg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(jindrichuv_hradec_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


# брно
@router.callback_query(text="JC_K1")
async def mvd_jg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Брно (Brno)" \
           "\n\n<b>Cфера деятельности, районы:</b> " \
           "\nБрно-город, Брно-Венков, Вышков, Бланско, Бржецлав, Зноймо и Годонин.\n(Brno-město, " \
           "Brno-venkov, Vyškov, Blansko, Břeclav, Znojmo a Hodonín)."
    await callback.message.answer_photo(ph.brno_ph, text,
                                        reply_markup=brno_keyboard_mvcr())
    await callback.message.delete()


brno_location = 'Cejl 62b, 602 00  Brno'


@router.callback_query(text="br_dk0")
async def location_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    await callback.message.answer(brno_location)


@router.callback_query(text="br_dk1")
async def location_gps_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    geolocator = Nominatim(user_agent="info_Czesh_bot")
    location = geolocator.geocode(brno_location)
    send_lat = location.latitude
    send_long = location.longitude
    await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="br_dk2")
async def phone_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(brno_url.text, "html.parser")
    find = phone_number.find(class_="c-block")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="br_dk3")
async def working_time_pi(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(brno_url.text, "html.parser")
    find = working_time.find_all(class_="c-block")
    for text in find:
        working_time = (text.getText().strip())
    await callback.message.answer(working_time)


# Карловарский
@router.callback_query(text="JC_K2")
async def mvd_ka(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Карловы Вары (Karlovy Vary) \n\n<b>Cфера " \
           "деятельности, районы:</b> \nХеб, Карловы Вары и Соколов\n(Cheb, Karlovy Vary a Sokolov)."
    await callback.message.answer_photo(ph.karloviVary_ph, text,
                                        reply_markup=ka_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="ka_dk0")
async def location_ka(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(karlovy_vary_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="ka_dk1")
async def location_gps_ka(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(karlovy_vary_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="ka_dk2")
async def phone_ka(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(karlovy_vary_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="ka_dk3")
async def working_time_ka(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(karlovy_vary_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Краловеградецкий
@router.callback_query(text="JC_K3")
async def mvd_hk(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Градец Кралове (Hradec Králové) " \
           "\n\n<b>Cфера деятельности, районы:</b> \nГрадец Кралове, Рихнов над Кнежной и Йичин" \
           "\n(Hradec Králové, Rychnov nad Kněžnou a Jičín)."
    await callback.message.answer_photo(ph.hradecKralove_ph, text,
                                        reply_markup=hk_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="hk_dk0")
async def location_hk(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(hradec_kralove_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="hk_dk1")
async def location_gps_hk(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(hradec_kralove_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="hk_dk2")
async def phone_hk(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(hradec_kralove_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="hk_dk3")
async def working_time_hk(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(hradec_kralove_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Либерецкий
@router.callback_query(text="JC_K04")
async def mvd_lb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Либерец (Liberec)"
    await callback.message.answer_photo(ph.liberec_ph, text,
                                        reply_markup=lb_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="lb_dk0")
async def location_lb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(liberec_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="lb_dk1")
async def location_gps_lb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(liberec_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())[:34]
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="lb_dk2")
async def phone_lb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(liberec_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="lb_dk3")
async def working_time_lb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(liberec_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Моравскосилезский
@router.callback_query(text="JC_K5")
async def mvd_ms(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Моравскосилезский край</b>, департаменты:"
    await callback.message.answer(text,
                                  reply_markup=ms_keyboard_mvcr())
    await callback.message.delete()


# exit ms hendler
@router.callback_query(text="ms_exit_call")
async def mvd_ms_exit(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Моравскосилезский край</b>, департаменты:"
    await callback.message.answer(text,
                                  reply_markup=ms_keyboard_mvcr())
    await callback.message.delete()


# острава
@router.callback_query(text="ms_sity_k0")
async def mvd_o(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Острава (Ostrava) \n\n<b>Cфера деятельности, " \
           "районы:</b> \nОстрава, Опава и Карвина\n(Ostrava, Opava a Karviná)."
    await callback.message.answer_photo(ph.ostrava_ph, text,
                                        reply_markup=ms_o_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="o_dk0")
async def location_o(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(ostrava_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="o_dk1")
async def location_gps_o(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(ostrava_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="o_dk2")
async def phone_o(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(ostrava_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="o_dk3")
async def working_time_o(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(ostrava_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Фридек-Мистек
@router.callback_query(text="ms_sity_k1")
async def mvd_fm(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Фридек-Мистек (Frýdek-Místek) \n\n<b>Cфера деятельности, " \
           "районы:</b> \nФридек-Мистек и Новый Йичин\n(Frýdek-Místek и Nový Jičín)."
    await callback.message.answer_photo(ph.frydekMistek_ph, text,
                                        reply_markup=ms_fm_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="fm_dk0")
async def location_fm(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(frydekMistek_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="fm_dk1")
async def location_gps_fm(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(frydekMistek_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="fm_dk2")
async def phone_fm(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(frydekMistek_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="fm_dk3")
async def working_time_fm(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(frydekMistek_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Оломоуцкий
@router.callback_query(text="JC_K6")
async def mvd_ol(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Пршеров (Přerov) \n\n<b>Cфера деятельности, " \
           "районы:</b> \nПршеров, Оломоуц, Простейов, Шумперк, Есеник и Брунтал\n( " \
           "Přerov, Olomouc, Prostějov, Šumperk, Jeseník a Bruntál)."
    await callback.message.answer_photo(ph.ICOlomoc_jpg, text,
                                        reply_markup=ol_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="ol_dk0")
async def location_ol(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(olomouc_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="ol_dk1")
async def location_gps_ol(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(olomouc_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())[:36]
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="ol_dk2")
async def phone_ol(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(olomouc_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="ol_dk3")
async def working_time_ol(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(olomouc_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Пардубицкий
@router.callback_query(text="JC_K7")
async def mvd_par(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Пардубице (Pardubice) \n\n<b>Cфера " \
           "деятельности, районы:</b> \nХрудим, Пардубице, Свитавы и Усти-над-Орлици\n(" \
           "Chrudim, Pardubice, Svitavy a Ústí nad Orlicí)."
    await callback.message.answer_photo(ph.pardubice_ph, text,
                                        reply_markup=par_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="par_dk0")
async def location_par(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(pardubice_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="par_dk1")
async def location_gps_par(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(pardubice_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="par_dk2")
async def phone_par(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(pardubice_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="par_dk3")
async def working_time_par(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(pardubice_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Пльзенский
@router.callback_query(text="JC_K8")
async def mvd_pl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Плзень (Plzeň) \n\n<b>Cфера деятельности, " \
           "районы:</b> \nПльзень-город, Пльзень-Юг, Пльзень-Север, Тахов, Рокицаны, Клатовы и Домажлице\n(" \
           "Plzeň-město, Plzeň-jih, Plzeň-sever, Tachov, Rokycany, Klatovy a Domažlice)."
    await callback.message.answer_photo(ph.plzen_ph, text,
                                        reply_markup=pl_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="pl_dk0")
async def location_pl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(plzen_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="pl_dk1")
async def location_gps_pl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(plzen_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pl_dk2")
async def phone_pl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(plzen_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="pl_dk3")
async def working_time_pl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(plzen_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Прага
@router.callback_query(text="JC_K9")
async def mvd_pr(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Прага</b>, департаменты:"
    await callback.message.answer(text,
                                  reply_markup=prag_keyboard_mvcr())
    await callback.message.delete()


# exit praga hendler
@router.callback_query(text="prag_exit_call")
async def mvd_pr_exit(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Прага</b>, департаменты:"
    await callback.message.answer(text,
                                  reply_markup=prag_keyboard_mvcr())
    await callback.message.delete()


# прага1
@router.callback_query(text="Pr_sity_k0")
async def mvd_pr1(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nПереходное, долгосрочное и постоянное пребывание\nотд. " \
           "Прага I (Praha I) \n\n<b>Cфера деятельности, районы:</b> \nПрага-Восток, Прага-Запад, " \
           "Прага 1, 2, 3, 6, 7 \nКлиенты без записи Прага 8 и 9" \
           "\n(Praha-Východ, Praha-Západ, Praha 1, 2, 3, 6, 7 \nneobjednaní klienti Praha 8 a 9)."
    await callback.message.answer_photo(ph.praha_ph, text,
                                        reply_markup=pr1_cb_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="pr1_dk0")
async def location_pr1(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(prague1_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="pr1_dk1")
async def location_gps_pr1(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(prague1_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pr1_dk2")
async def phone_pr1(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(prague1_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="pr1_dk3")
async def working_time_pr1(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(prague1_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# прага2
@router.callback_query(text="Pr_sity_k1")
async def mvd_pr2(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nотд. Прага II (" \
           "Praha II)\n\n<b>Cфера деятельности, районы:</b> \nПрага 4, 5 a 10\n(" \
           "Praha 4, 5 a 10)."
    await callback.message.answer_photo(ph.praha_ph, text,
                                        reply_markup=pr2_cb_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="pr2_dk0")
async def location_pr2(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(prague2_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="pr2_dk1")
async def location_gps_pr2(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(prague2_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pr2_dk2")
async def phone_pr2(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(prague2_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="pr2_dk3")
async def working_time_pr2(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(prague2_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# прага3
@router.callback_query(text="Pr_sity_k2")
async def mvd_pr3(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания для иностранных студентов:</b>\nотд. Прага III " \
           "\n\n<b>Cфера деятельности:</b>" \
           "\nИностранные студенты университетов проживающие в Праге, районы:\n" \
           "Прага-Восток и Прага-Запад\n(Prahy-Východ, Prahy-Západ)"
    await callback.message.answer_photo(ph.praha_ph, text,
                                        reply_markup=pr3_cb_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="pr3_dk0")
async def location_pr3(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(prague3_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="pr3_dk1")
async def location_gps_pr3(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(prague3_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pr3_dk2")
async def phone_pr3(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(prague3_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="pr3_dk3")
async def working_time_pr3(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(prague3_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# прага_letna
@router.callback_query(text="Pr_sity_k3")
async def mvd_pr4(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>" \
           "\n<i>СПЕЦИАЛИЗИРОВАННОЕ РАБОЧЕЕ МЕСТО - по запросу административного органа</i>" \
           "\n<b>Cфера деятельности:</b> \n<i>Специализированная</i>"
    await callback.message.answer_photo(ph.praha_ph, text,
                                        reply_markup=pr4_cb_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="pr4_dk0")
async def location_pr4(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(prague_letna_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="pr4_dk1")
async def location_gps_pr4(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(prague_letna_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pr4_dk2")
async def working_time_pr4(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(prague_letna_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# среднечешский
@router.callback_query(text="JC_K10")
async def mvd_sr(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Среднечешский край</b>, департаменты:"
    await callback.message.answer(text,
                                  reply_markup=sk_keyboard_mvcr())
    await callback.message.delete()


# exit среднечешский hendler
@router.callback_query(text="sk_exit_call")
async def mvd_sr_exit(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Среднечешский край</b>, департаменты:"
    await callback.message.answer(text,
                                  reply_markup=sk_keyboard_mvcr())
    await callback.message.delete()


# Бенешов
@router.callback_query(text="sk_sity_k0")
async def mvd_be(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Бенешов (Benešov) \n\n<b>Cфера деятельности, " \
           "районы:</b> \nБенешов и Табор\n(Benešov a Tábor)."
    await callback.message.answer_photo(ph.benesov_ph, text,
                                        reply_markup=sk_be_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="be_dk0")
async def location_be(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(benesov_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="be_dk1")
async def location_gps_be(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(benesov_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="be_dk2")
async def phone_be(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(benesov_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="be_dk3")
async def working_time_be(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(benesov_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Кладно
@router.callback_query(text="sk_sity_k1")
async def mvd_kl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Кладно (Kladno) \n\n<b>Cфера деятельности, " \
           "районы:</b> \nКладно и Раковник\n(" \
           "Kladno, Rakovník)."
    await callback.message.answer_photo(ph.kladno_ph, text,
                                        reply_markup=sk_kl_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="kl_dk0")
async def location_kl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(kladno_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="kl_dk1")
async def location_gps_kl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(kladno_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="kl_dk2")
async def phone_kl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(kladno_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="kl_dk3")
async def working_time_kl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(kladno_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Кутна гора
@router.callback_query(text="sk_sity_k2")
async def mvd_kg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Кутна Гора (Kutná Hora) \n\n<b>Cфера деятельности, " \
           "районы:</b> \nКутна Гора, Нимбурк и Колин\n(" \
           "Kutná Hora, Nymburk, Kolín)."
    await callback.message.answer_photo(ph.kutnaHora_ph, text,
                                        reply_markup=sk_kg_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="kg_dk0")
async def location_kg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(kutna_hora_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="kg_dk1")
async def location_gps_kg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(kutna_hora_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="kg_dk2")
async def phone_kg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(kutna_hora_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="kg_dk3")
async def working_time_kg(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(kutna_hora_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# млада болеслав
@router.callback_query(text="sk_sity_k3")
async def mvd_m(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Млада-Болеслав (Mladá Boleslav) \n\n<b>Cфера деятельности, " \
           "районы: </b>\nМлада-Болеслав и Мельник\n(" \
           "Mladá Boleslav, Mělník)."
    await callback.message.answer_photo(ph.mladaBoleslav_ph, text,
                                        reply_markup=sk_m_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="m_dk0")
async def location_m(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(mlada_boleslav_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="m_dk1")
async def location_gps_m(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(mlada_boleslav_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="m_dk2")
async def phone_m(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(mlada_boleslav_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="m_dk3")
async def working_time_m(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(mlada_boleslav_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# пршибрам
@router.callback_query(text="sk_sity_k4")
async def mvd_pr(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Пршибрам (Příbram) \n\n<b>Cфера деятельности, " \
           "районы:</b>\nБероун и Пршибрам\n(" \
           "Beroun, Příbram)."
    await callback.message.answer_photo(ph.pribram_ph, text,
                                        reply_markup=sk_pr_details_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="pr_dk0")
async def location_pr(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(pribram_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="pr_dk1")
async def location_gps_pr(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(pribram_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pr_dk2")
async def phone_pr(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(pribram_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="pr_dk3")
async def working_time_pr(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(pribram_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Устецкий
# усти над лабем
@router.callback_query(text="JC_K11")
async def mvd_unl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент проживания иностранцев:</b>\nг.Усти-над-Лабем (Ústí nad Labem) \n\n<b>Cфера деятельности, " \
           "районы:</b>\nУсти-над-Лабем, Теплице, Литомержице и Дечин\n(" \
           "Ústí nad Labem, Teplice, Litoměřice, Děčín)."
    await callback.message.answer_photo(ph.ustiNadLabem_ph, text,
                                        reply_markup=ust_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="unl_dk0")
async def location_unl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(usti_nad_labem_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="unl_dk1")
async def location_gps_unl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(usti_nad_labem_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="unl_dk2")
async def phone_unl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(usti_nad_labem_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="unl_dk3")
async def working_time_unl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(usti_nad_labem_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# богемия
# Йиглава
@router.callback_query(text="JC_K12")
async def mvd_vys(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Департамент по делам иностранцев Высочинского района:</b>" \
           "\nг.Йиглава(Jihlava)" \
           "\n\n<b>Cфера деятельности, районы:</b> \nГавличкув Брод, Йиглава, Тршебич," \
           "Пельгржимов и Жарар-над-Сазавой\n(Havlíčkův Brod, Jihlava, Třebíč, Pelhřimov a Žďár nad " \
           "Sázavou)."
    await callback.message.answer_photo(ph.jihlava_ph, text,
                                        reply_markup=vys_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="vys_dk0")
async def location_vys(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(jihlava_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="vys_dk1")
async def location_gps_vys(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(jihlava_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="vys_dk2")
async def phone_vys(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(jihlava_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="vys_dk3")
async def working_time_vys(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(jihlava_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# злинский
# злин
@router.callback_query(text="JC_K13")
async def mvd_zl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Региональный отдел по месту жительства иностранцев:</b>" \
           "\nг.Злин(Zlin)\n\n<b>Cфера деятельности:</b> \nвесь регион."
    await callback.message.answer_photo(ph.zlin_ph, text,
                                        reply_markup=zlin_keyboard_mvcr())
    await callback.message.delete()


@router.callback_query(text="zl_dk0")
async def location_zl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(zlin_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="zl_dk1")
async def location_gps_zl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(zlin_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="zl_dk2")
async def phone_zl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(zlin_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="zl_dk3")
async def working_time_zl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(zlin_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)

