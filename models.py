from BookStoreManager import db,admin
from sqlalchemy import Column, Integer,Boolean, String ,Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from flask_admin.contrib.sqla import ModelView
from  flask_login import UserMixin, current_user,logout_user
from  flask_admin import  BaseView, expose
from flask import  redirect
# class usertype(db.Model):
#     __tablename__ = 'category'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    birthday = Column(Date)
    address = Column(String(100))
    phone = Column(Integer)
    Position = Column(String(50))
    loginname = Column(String(50))
    password = Column(String(50), default= False)
    start_word_date = Column(Date)
    salary = Column(Float)


    def __str__ (self):
        return self.name
    # userType = Column(Integer, ForeignKey(usertype.id), nullable=False)
    #
    # def __str__(self):
    #     return self.hoten

# db.create_all()







class Customers(db.Model):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable= False)
    birthday = Column(Date)
    address = Column(String(100))
    phone = Column(Integer)
    owe = Column(Float)

    def __str__ (self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product',backref='category', lazy=True)

    def __str__ (self):
        return self.name


class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    publisher = Column(String(100), nullable=True)
    publishing_year =Column(Integer)
    description = Column(String(500))
    amount = Column(Integer)

    def __str__ (self):
        return self.name


class LougoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        return  redirect("/admin")

    def is_accessible(self):
        return current_user.is_authenticated
# class order(db.model):
#     __tablename__ = 'order'
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     Column(Integer, ForeignKey(usertype.id), nullable=False)
#     date = Column(Date)
    # totalMoney = Colum

# admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
admin.add_view(LougoutView(name ="Log Out"))
admin.add_view(ModelView(User, db.session))


db.create_all()