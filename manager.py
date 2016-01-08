#!flask/bin/python
from faker import Factory

from flask.ext.script import Manager

from app import create_app

app = create_app()
manager = Manager(app)

@manager.command
def forged():
    from app.core.models import db, User, Category, Post, Tag
    from random import choice, sample, randint

    db.drop_all()
    db.create_all()

    faker = Factory.create()

    def generate_post(func_user, func_categorys, func_tags):
        return Post(title=faker.sentence(),
                    body=faker.paragraph(),
                    user=func_user(),
                    category=func_categorys(),
                    tags=func_tags())

    def generate_user():
        return User(email=faker.email(),
                    username=faker.word(),
                    nickname=faker.name(),
                    password='buyaoyongroot')

    def generate_category():
        return Category(name=faker.last_name(),
                        description=faker.sentence())

    def generate_tag():
        return Tag(name=faker.first_name())

    users = [generate_user() for i in xrange(10)]
    db.session.add_all(users)

    categorys = [generate_category() for i in xrange(5)]
    db.session.add_all(categorys)

    tags = [generate_tag() for i in xrange(30)]
    db.session.add_all(tags)

    random_user = lambda: choice(users)
    random_category = lambda: choice(categorys)
    random_tags = lambda: sample(tags, randint(1, 5))

    posts = [generate_post(random_user,
                           random_category, random_tags) for i in xrange(15)]
    db.session.add_all(posts)

    db.session.commit()

if __name__ == '__main__':
    manager.run()
