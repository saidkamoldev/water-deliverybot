from aiogram.dispatcher.filters.state import State, StatesGroup

class Feedback(StatesGroup):
    Commentary = State()


class Purchace(StatesGroup):
    commentary = State()
    name = State()
    need_partner_sex = State()

class NewItem(StatesGroup):
    Category = State()
    Name = State()
    Description = State()
    DescriptionUz = State()
    Photo = State()
    Price = State()
    Confirm = State()

class Mailing(StatesGroup):
    Text = State()
    Language = State()

class Order(StatesGroup):
    CategoryChoice = State()
    OfferChoise = State()
    ChoiseQuality = State()
    ChoisePayments = State()
    LocationChoise = State()
    Invoise = State()
    Successful = State()
    Commentary = State()

class Admin(StatesGroup):
    Photo = State()
    Price = State()

class Kuller(StatesGroup):
    ChoseKuller = State()
    ChosePompa = State()


