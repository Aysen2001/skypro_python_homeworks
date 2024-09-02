from address import Address
from mailing import Mailing

to_address = Address("123132", "Moscow", "Tverskaya", "20", "11")
from_adress = Address("999888", "Kazan", "Tukaya", "18", "25")

mailing = Mailing(to_address, from_adress, 500, "track123")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)