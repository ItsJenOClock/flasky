from app import create_app, db
from app.models.cat import Cat

my_app = create_app()
with my_app.app_context():
    db.session.add(Cat(name="Luna", color="ash", personality="Tomato Queen")),
    db.session.add(Cat(name="Simon", color="black", personality="might be a human stuck in a cats body")),
    db.session.add(Cat(name="Midnight", color="black", personality="skittish")),
    db.session.add(Cat(name="Leo", color="gray tabby", personality="friendly")),
    db.session.add(Cat(name="Ash", color="gray", personality="cranky")),
    db.session.add(Cat(name="Alder", color="auburn", personality="bouncy, trouncy, flouncy, pouncy, fun, fun, fun, fun, fun")),
    db.session.add(Cat(name="Morty", color="orange", personality="orange")),
    db.session.add(Cat(name="fluffy", color="white", personality="evil with a hint of benevolent")),
    db.session.add(Cat(name="Reginold", color="orange", personality="only has one brain cell, but is descendent of Reginold the Great Tabby")),
    db.session.add(Cat(name="Katosa", color="gray tabby", personality="Crazy Hunter")),
    db.session.add(Cat(name="Milly", color="Tortoiseshell", personality="Loves you a lot but will probably sneeze all over you")),
    db.session.add(Cat(name="Meryl", color="Tortoiseshell", personality="Bossy but tries to pass as the sweet one")),
    db.session.add(Cat(name="Zelda", color="white, gray", personality="a mystery")),
    db.session.add(Cat(name="Jupiter", color="orange", personality="socially selective")),
    db.session.add(Cat(name="Neo", color="black", personality="stoic")),
    db.session.add(Cat(name="Gato", color="grey", personality="fun")),
    db.session.add(Cat(name="Red XIII", color="red", personality="serious")),
    db.session.add(Cat(name="Gizzy", color="white", personality="unbothered")),
    db.session.commit()

# cats = [
#     Cat(1, "Luna", "black/white", "lazy"),
#     Cat(2, "Simon", "black", "might be a human stuck in a cat's body"),
#     Cat(3, "Midnight", "black", "skittish"),
#     Cat(4, "Leo", "gray tabby", "friendly"),
#     Cat(5, "Ash", "gray", "cranky"),
#     Cat(6, "Alder", "auburn", "bouncy, trouncy, flouncy, pouncy, fun, fun, fun, fun, fun"),
#     Cat(7, "Morty", "orange", "orange"),
#     Cat(8, "fluffy", "white", "evil with a hint of benevolent"),
#     Cat(9, "Reginold", "orange", "only has one brain cell, but is descendent of Reginold the Great Tabby"),
#     Cat(10, "Katosa", "gray tabby", "Crazy Hunter"),
#     Cat(11, "Milly", "Tortoiseshell", "Loves you a lot but will probably sneeze all over you"),
#     Cat(12, "Meryl", "Tortoiseshell", "Bossy but tries to pass as the sweet one"),
#     Cat(13, "Zelda", "white, gray", "a mystery"),
#     Cat(14, "Jupiter", "orange", "socially selective"),
# ]