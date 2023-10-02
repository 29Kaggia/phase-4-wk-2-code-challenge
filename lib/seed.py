# seed.py

from app import db, Hero, Power

def seed_data():
    # Create some Hero and Power records
    hero1 = Hero()
    hero2 = Hero()
    power1 = Power(description="Super Strength")
    power2 = Power(description="Flight")
    power3 = Power(description="Telekinesis")

    # Add powers to heroes
    hero1.hero_powers.append(power1)
    hero1.hero_powers.append(power2)
    hero2.hero_powers.append(power3)

    # Add records to the session and commit
    db.session.add(hero1)
    db.session.add(hero2)
    db.session.add(power1)
    db.session.add(power2)
    db.session.add(power3)
    db.session.commit()

if __name__ == '__main__':
    # Initialize the app and database
    from app import app
    with app.app_context():
        db.create_all()
        seed_data()
