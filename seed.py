from app import app, db
from models import Hero, Power, HeroPower

with app.app_context():
    db.create_all()

    hero1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
    hero2 = Hero(name="Misita Khan", super_name=" mas   mas mas mas mas mas")
    hero3 = Hero(name="Ashley Johnson", super_name="Ashley")
    hero4 = Hero(name="Aleks Aliday", super_name="  Aleks")

    power1 = Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed")
    power2 = Power(name="teleportation", description="gives the wielder the ability to move instantaneously through space and time")
    power3 = Power(name="superhuman strength", description="gives the wielder an unparalleled physical strength")
    power4 = Power(name="superhuman agility", description="gives the wielder an unparalleled agility")

    db.session.add(hero1)
    db.session.add(power1)
    db.session.commit()

    hero_power = HeroPower(strength="Strong", hero_id=hero1.id, power_id=power1.id)
    db.session.add(hero_power)
    db.session.commit()

    print("Database seeded!")
