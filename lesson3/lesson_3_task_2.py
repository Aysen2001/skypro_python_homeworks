from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Ipone", "15 Pro Max", "+79120000001")
phone2 = Smartphone("Google Pixel", "8 Pro", "+79120000002")
phone3 = Smartphone("Samsung", "Galaxy S24 Ultra", "+79120000003")
phone4 = Smartphone("Xiaomi", "14 Ultra", "+79120000004")
phone5 = Smartphone("Asus", "ROG Phone 8 Pro", "+79120000005")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.name} - {phone.model} . {phone.number}")
    