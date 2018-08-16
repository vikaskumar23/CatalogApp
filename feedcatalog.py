# -*- coding: utf-8 -*-
from flask import url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from database_setup import Base, User, Category, Item

engine = create_engine('postgresql://catalog:password@localhost/catalog')
Base.metadata.bind = engine
session = scoped_session(sessionmaker(bind=engine))

# Create dummy user
user1 = User(
    name="Vartika Pahuja",
    email="vartikapahuja19@gmail.com",
    picture="/static/icon.png")
session.add(user1)
session.commit()

# Create category #1 and add items to the category
category1 = Category(name="Fiction", user_id=1)
session.add(category1)
session.commit()

item1 = Item(
    user_id=1,
    name="Pride and Prejudice",
    description='''Pride and Prejudice is a romantic novel
                    by Jane Austen, first published in. The
                    story charts the emotional development of
                    the protagonist, Elizabeth Bennet, who
                    learns the error of making hasty judgments
                    and comes to appreciate the difference between
                    the superficial and the essential.''',
    image="/static/pride1.jpg",
    category=category1)
session.add(item1)
session.commit()

# Create category #2 and add items to the category
category2 = Category(name="Romance", user_id=1)
session.add(category2)
session.commit()

item2 = Item(
    user_id=1,
    name="A walk to remember",
    description='''A Walk to Remember is a novel
                    by American writer Nicholas Sparks''',
    image="/static/walk.jpg",
    category=category2)
session.add(item2)
session.commit()

item3 = Item(
    user_id=1,
    name="I too had a love story",
    description='''I Too Had a Love Story is an English
                    autobiographical novel written by Ravinder
                    Singh. This was the debut novel of the author.''',
    image="/static/lovestory.jpg",
    category=category2)
session.add(item3)
session.commit()

# Create category #3 and add items to the category
category3 = Category(name="Mystery", user_id=1)
session.add(category3)
session.commit()

item4 = Item(
    user_id=1,
    name="Gone Girl",
    description='''Gone Girl is a thriller novel by the
                    writer Gillian Flynn. It was published
                    by Crown Publishing Group. The novel soon
                    made the New York Times Best Seller list. The
                    novel's suspense comes from the main character,
                    Nick Dunne, and whether he is involved in the
                    disappearance of his wife.''',
    image="/static/gone_girl.jpg",
    category=category3)
session.add(item4)
session.commit()

# Create category #4 and add items to the category
category4 = Category(name="Horror", user_id=1)
session.add(category4)
session.commit()

item5 = Item(
    user_id=1,
    name="The Haunting Hill House",
    description=''' A horror novel by Shirley Jackson and
                    it also deals with complex relationships
                    between the mysterious events.''',
    image="/static/hill_house.jpg",
    category=category4)
session.add(item5)
session.commit()

item6 = Item(
    user_id=1,
    name="The Girl Next Door",
    description=''' A crime novel written by Jack Ketchum.
                    It is about two teen girls who are left
                    in the care of their aunt, and the systematic
                    and escalating abuse both of them and one sister
                    in particular suffer at the hands of their aunt
                    and her children.''',
    image="/static/girl.jpg",
    category=category4)
session.add(item6)
session.commit()
