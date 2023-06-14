from aiogram import Router, types
# парсинг
from bs4 import BeautifulSoup

# для работы с геолокацией
from geopy.geocoders import Nominatim

from keyboards.integration_keyboard import *
from url.url_integration import *
from keyboards.mvcr_keyboard import start_keyboard
# фото
from photo import photo as ph
# from photo import photo_test as ph

router = Router()  # [2]


# start / exit keyboard integ
@router.callback_query(text="INTEG_start_call")
async def integration_sity_start(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    await callback.message.answer("Вот центры интеграции о которых мне известно:",
                                  reply_markup=integration_keyboard())
    await callback.message.delete()


# exit mvcr region hendler
@router.callback_query(text="integration_exit_call")
async def integration_sisy_exit(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    start_message0 = "Привет👋 \nЯ <b>информационный</b> бот." \
                     "\n    <i>Используй клавиатуру для навигации по меню</i>"
    await callback.message.answer(start_message0,
                                  reply_markup=start_keyboard())
    await callback.message.delete()


# брно
@router.callback_query(text="IC_K0")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Брно (Brno)"
    await callback.message.answer_photo(ph.ICBrno_jpg, text,
                                        reply_markup=brno_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="brno_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(brno_integ_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="brno_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(brno_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="brno_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(brno_integ_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="brno_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(brno_integ_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# злин
@router.callback_query(text="IC_K1")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Злин (Zlin)"
    await callback.message.answer_photo(ph.ICZlin_jpg, text,
                                        reply_markup=zlin_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="zlin_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(zlin_integ_url.text, "html.parser")
    bs = (location.select_one(".elementor-text-editor p"))
    find = bs.text[:15] + ", " + bs.text[15:]
    await callback.message.answer(find)


@router.callback_query(text="zlin_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(zlin_integ_url.text, "html.parser")
    bs = (location_gps.select_one(".elementor-text-editor p"))
    find = bs.text[:15] + ", " + bs.text[15:]
    geolocator = Nominatim(user_agent="info_Czesh_bot")
    location = geolocator.geocode(find)
    send_lat = location.latitude
    send_long = location.longitude
    await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="zlin_dk2")
async def phone_cd(callback: types.CallbackQuery):
    contacts = BeautifulSoup(zlin_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-461ad213 elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = (text.getText("\n").strip())
    await callback.message.answer(contacts)


@router.callback_query(text="zlin_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(zlin_ru_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-902a8e5 elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = (text.getText("\n").strip())
    await callback.message.answer(working_time)


# прага
@router.callback_query(text="IC_K2")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Прага (Praha)"
    await callback.message.answer_photo(ph.ICPrague1_jpg, text,
                                        reply_markup=praha_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="praha_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(praha_integ_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="praha_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(praha_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="praha_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(praha_integ_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="praha_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(praha_integ_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# кадае
@router.callback_query(text="IC_K3")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Кадан (Kadaň)"
    await callback.message.answer_photo(ph.ICUstiNadLabem_jpg, text,
                                        reply_markup=kadan_details_keyboard_integration())
    await callback.message.delete()


location_cadan = "Mírové nám. 85, 431 01 Kadaň"


@router.callback_query(text="kadan_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    await callback.message.answer(location_cadan)


@router.callback_query(text="kadan_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    geolocator = Nominatim(user_agent="info_Czesh_bot")
    location = geolocator.geocode(location_cadan)
    send_lat = location.latitude
    send_long = location.longitude
    await callback.message.answer_location(send_lat, send_long)


# плзень
@router.callback_query(text="IC_K4")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Плзень (Plzen)"
    await callback.message.answer_photo(ph.ICPlzen_jpg, text,
                                        reply_markup=plzen_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="plzen_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(plzen_integ_url.text, "html.parser")
    bs = (location.select_one(".elementor-text-editor p"))
    find = bs.text[:11] + ", " + bs.text[11:]
    await callback.message.answer(find)


@router.callback_query(text="plzen_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(plzen_integ_url.text, "html.parser")
    bs = (location_gps.select_one(".elementor-text-editor p"))
    find = bs.text[:11] + ", " + bs.text[11:]
    geolocator = Nominatim(user_agent="info_Czesh_bot")
    location = geolocator.geocode(find)
    send_lat = location.latitude
    send_long = location.longitude
    await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="plzen_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(plzen_ru_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-1553f47 elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = (text.getText("\n").strip())
    await callback.message.answer(contacts)


@router.callback_query(text="plzen_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(plzen_ru_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-afb3bf9 elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = (text.getText("\n").strip())
    await callback.message.answer(working_time)


# кладно
@router.callback_query(text="IC_K5")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Кладно (Kladno)"
    await callback.message.answer_photo(ph.ICKladno_jpg, text,
                                        reply_markup=kladno_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="kladno_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(kladno_integ_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="kladno_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(kladno_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="kladno_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(kladno_integ_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="kladno_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(kladno_integ_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# теплице
@router.callback_query(text="IC_K6")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Теплице (Teplice)"
    await callback.message.answer_photo(ph.ICTeplice_jpg, text,
                                        reply_markup=teplice_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="teplice_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(teplice_integ_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="teplice_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(teplice_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="teplice_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(teplice_integ_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="teplice_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(teplice_integ_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# бенешов
@router.callback_query(text="IC_K7")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Бенешов (Benešov)"
    await callback.message.answer_photo(ph.ICBenesov_jpg, text,
                                        reply_markup=benesov_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="benesov_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(benesov_integ_url.text, "html.parser")
    find = location.find_all(class_="elementor-element elementor-element-e2030c5 elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText().strip()
        await callback.message.answer(location)


@router.callback_query(text="benesov_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(benesov_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="elementor-element elementor-element-e2030c5 elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText().strip()
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="benesov_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(benesov_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-a9f655d elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="benesov_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(benesov_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-8c6d02f elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = (text.getText("\n").strip())
    await callback.message.answer(working_time)


# оломоуц
@router.callback_query(text="IC_K8")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Оломоуц (Olomouc)"
    await callback.message.answer_photo(ph.ICOlomoc_jpg, text,
                                        reply_markup=olomouc_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="olomouc_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(olomouc_integ_url.text, "html.parser")
    find = location.find_all(
        class_="elementor-element elementor-element-70f7668 elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText(" \n").strip()
        await callback.message.answer(location)


@router.callback_query(text="olomouc_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(olomouc_integ_url.text, "html.parser")
    find = location_gps.find_all(
        class_="elementor-element elementor-element-70f7668 elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText(" \n").strip()
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="olomouc_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(olomouc_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-93c7cf9 elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="olomouc_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(olomouc_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-2470f90 elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = (text.getText("\n").strip())
    await callback.message.answer(working_time)


# Йиглава
@router.callback_query(text="IC_K9")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Йиглава (Jihlava)"
    await callback.message.answer_photo(ph.ICJihlavaFake_jpg, text,
                                        reply_markup=jihlava_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="jihlava_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(jihlava_integ_url.text, "html.parser")
    find = location.find_all(
        class_="elementor-element elementor-element-22064b7 elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText(" \n").strip()
        await callback.message.answer(location)


@router.callback_query(text="jihlava_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(jihlava_integ_url.text, "html.parser")
    find = location_gps.find_all(
        class_="elementor-element elementor-element-22064b7 elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText(" \n").strip()
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="jihlava_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(jihlava_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-91db60a elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="jihlava_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(jihlava_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-77c99e8 elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = (text.getText("\n").strip())
    await callback.message.answer(working_time)


# Либерец
@router.callback_query(text="IC_K10")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г.Либерец(Liberec)"
    await callback.message.answer_photo(ph.ICLiberec_jpg, text,
                                        reply_markup=liberec_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="liberec_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(liberec_integ_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="liberec_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(liberec_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())[:32]
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="liberec_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(liberec_integ_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="liberec_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(liberec_integ_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Острава
@router.callback_query(text="IC_K11")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Острава (Ostrava)"
    await callback.message.answer_photo(ph.ICOstrava_jpg, text,
                                        reply_markup=ostrava_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="ostrava_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(ostrava_integ_url.text, "html.parser")
    find = location.find_all(
        class_="elementor-element elementor-element-384a301 elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText(" \n").strip()
        await callback.message.answer(location)


@router.callback_query(text="ostrava_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(ostrava_integ_url.text, "html.parser")
    find = location_gps.find_all(
        class_="elementor-element elementor-element-384a301 elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText(" \n").strip()
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="ostrava_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(ostrava_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-18488c7 elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="ostrava_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(ostrava_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-4d8017d elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = text.getText("\n").strip()
    await callback.message.answer(working_time)


# Пршибрам
@router.callback_query(text="IC_K12")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Пршибрам (Příbram)"
    await callback.message.answer_photo(ph.ICPribram_jpg, text,
                                        reply_markup=pribram_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="pribram_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(pribram_integ_url.text, "html.parser")
    find = location.find_all(
        class_="elementor-element elementor-element-c7c4d53 elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText(" \n").strip()
        await callback.message.answer(location)


@router.callback_query(text="pribram_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(pribram_integ_url.text, "html.parser")
    find = location_gps.find_all(
        class_="elementor-element elementor-element-c7c4d53 elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText(" \n").strip()
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pribram_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(pribram_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-f14502c elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="pribram_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(pribram_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-4ecb41d elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = text.getText("\n").strip()
    await callback.message.answer(working_time)


# Пардубице
@router.callback_query(text="IC_K13")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г.Пардубице(Pardubice)"
    await callback.message.answer_photo(ph.ICPardubice_jpg, text,
                                        reply_markup=pardubice_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="pardubice_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(pardubice_integ_url.text, "html.parser")
    find = location.find_all(
        class_="elementor-element elementor-element-2d7a3e3 elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText(" \n").strip()
        await callback.message.answer(location)


@router.callback_query(text="pardubice_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(pardubice_integ_url.text, "html.parser")
    find = location_gps.find_all(
        class_="elementor-element elementor-element-2d7a3e3 elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText(" \n").strip()
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="pardubice_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(pardubice_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-eddab3c elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="pardubice_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(pardubice_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-bef71c7 elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = text.getText("\n").strip()
    await callback.message.answer(working_time)


# Кутна Гора
@router.callback_query(text="IC_K14")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Кутна Гора (Kutná Hora)"
    await callback.message.answer_photo(ph.ICKutnaHora_jpg, text,
                                        reply_markup=kutnah_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="kutnah_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(kutnah_integ_url.text, "html.parser")
    find = location.find_all(
        class_="elementor-element elementor-element-649d8ae elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText(" \n").strip()
        await callback.message.answer(location)


@router.callback_query(text="kutnah_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(kutnah_integ_url.text, "html.parser")
    find = location_gps.find_all(
        class_="elementor-element elementor-element-649d8ae elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText(" \n").strip()
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="kutnah_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(kutnah_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-30f0fff elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="kutnah_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(kutnah_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-85fdadc elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = text.getText("\n").strip()
    await callback.message.answer(working_time)


# карловы вары
@router.callback_query(text="IC_K15")
async def mvd_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г.Карловы Вары (Karlovy Vary)"
    await callback.message.answer_photo(ph.ICKarVar_jpg, text,
                                        reply_markup=karlovyv_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="karlovyv_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(karlovyv_integ_url.text, "html.parser")
    find = location.find_all(
        class_="elementor-element elementor-element-d337ed4 elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText(" \n").strip()
        await callback.message.answer(location)


@router.callback_query(text="karlovyv_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(karlovyv_integ_url.text, "html.parser")
    find = location_gps.find_all(
        class_="elementor-element elementor-element-d337ed4 elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText(" \n").strip()[:39]
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="karlovyv_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(karlovyv_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-668f6a0 elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="karlovyv_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(karlovyv_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-3c8d79d elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = text.getText("\n").strip()
    await callback.message.answer(working_time)


# Млада болеслав
@router.callback_query(text="IC_K16")
async def integration_mladab(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Млада Болеслав (Mladá Boleslav)"
    await callback.message.answer_photo(ph.ICMladaBoleslav_jpg, text,
                                        reply_markup=mladab_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="mladab_dk0")
async def location_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(mladab_integ_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="mladab_dk1")
async def location_gps_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(mladab_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="mladab_dk2")
async def phone_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(mladab_integ_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="mladab_dk3")
async def working_time_cd(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(mladab_integ_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Усти над Лабем
@router.callback_query(text="IC_K17")
async def integration_ustinl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Усти над лабем (Ústí nad Labem)"
    await callback.message.answer_photo(ph.ICUstiNadLabem_jpg, text,
                                        reply_markup=ustinl_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="ustinl_dk0")
async def location_ustinl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(ustinl_integ_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="ustinl_dk1")
async def location_gps_ustinl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(ustinl_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="ustinl_dk2")
async def phone_ustinl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(ustinl_integ_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="ustinl_dk3")
async def working_time_ustinl(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(ustinl_integ_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Градец Кралове
@router.callback_query(text="IC_K18")
async def integration_hradeck(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г. Градец Кралове (Hradec Králové)"
    await callback.message.answer_photo(ph.ICHradecKralove_jpg, text,
                                        reply_markup=hradeck_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="hradeck_dk0")
async def location_hradeck(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(hradeck_integ_url.text, "html.parser")
    find = location.find_all(class_="detailAddress")
    for text in find:
        location = (text.getText().strip())
        await callback.message.answer(location)


@router.callback_query(text="hradeck_dk1")
async def location_gps_hradeck(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(hradeck_integ_url.text, "html.parser")
    find = location_gps.find_all(class_="detailAddress")
    for text in find:
        location_gps = (text.getText().strip())
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="hradeck_dk2")
async def phone_hradeck(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    phone_number = BeautifulSoup(hradeck_integ_url.text, "html.parser")
    find = phone_number.find(class_="value detailPhone detailPhonePrimary")
    for text in find:
        phone_number = (text.getText().strip())
    await callback.message.answer(phone_number)


@router.callback_query(text="hradeck_dk3")
async def working_time_hradeck(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(hradeck_integ_url.text, "html.parser")
    find = working_time.find(class_="today")
    for text in find:
        working_time = (text.getText().strip())
    text_today = f"Cегодня:" \
                 f"\n        <b>{working_time}</b>"
    await callback.message.answer(text_today)


# Ческе Будеёвице
@router.callback_query(text="IC_K19")
async def integration_ceskeb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    text = "<b>Интеграционный центр:</b>\n      г.Ческе-Будеевице (České Budějovice)"
    await callback.message.answer_photo(ph.ICCzeshBudev_jpg, text,
                                        reply_markup=ceskeb_details_keyboard_integration())
    await callback.message.delete()


@router.callback_query(text="ceskeb_dk0")
async def location_ceskeb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location = BeautifulSoup(ceskeb_integ_url.text, "html.parser")
    find = location.find_all(
        class_="elementor-element elementor-element-d92634f elementor-widget elementor-widget-text-editor")
    for text in find:
        location = text.getText(" \n").strip()
        await callback.message.answer(location)


@router.callback_query(text="ceskeb_dk1")
async def location_gps_ceskeb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    location_gps = BeautifulSoup(ceskeb_integ_url.text, "html.parser")
    find = location_gps.find_all(
        class_="elementor-element elementor-element-d92634f elementor-widget elementor-widget-text-editor")
    for text in find:
        location_gps = text.getText(" \n").strip()
        geolocator = Nominatim(user_agent="info_Czesh_bot")
        location = geolocator.geocode(location_gps)
        send_lat = location.latitude
        send_long = location.longitude
        await callback.message.answer_location(send_lat, send_long)


@router.callback_query(text="ceskeb_dk2")
async def phone_ceskeb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    contacts = BeautifulSoup(ceskeb_integ_url.text, "html.parser")
    find = contacts.find_all(
        class_="elementor-element elementor-element-fe54f2d elementor-widget elementor-widget-text-editor")
    for text in find:
        contacts = text.getText("\n").strip()
    await callback.message.answer(contacts)


@router.callback_query(text="ceskeb_dk3")
async def working_time_ceskeb(callback: types.CallbackQuery):
    await callback.answer(cache_time=1)
    working_time = BeautifulSoup(ceskeb_integ_url.text, "html.parser")
    find = working_time.find_all(
        class_="elementor-element elementor-element-39b300a elementor-widget elementor-widget-text-editor")
    for text in find:
        working_time = text.getText("\n").strip()
    await callback.message.answer(working_time)

