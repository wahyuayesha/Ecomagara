from datetime import date
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# USER  
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    username = db.Column(db.String(255), nullable=True)
    profilePicture = db.Column(db.String(100), nullable=True)
    joinDate = db.Column(db.DateTime, nullable=False)  
    points = db.Column(db.Integer, nullable=False, default=0)
    currentIslandTheme = db.Column(db.Integer, nullable=False, default=0)
    firebase_uid = db.Column(db.String(255), nullable=True, unique=True)


class DailyCarbonLog(db.Model):
    __tablename__ = 'dailycarbonlogs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usersId = db.Column(db.Integer, db.ForeignKey('users.id'))
    totalCarbon = db.Column(db.Float)
    carbonLevel = db.Column(db.Integer)
    IslandPath = db.Column(db.Integer)
    carbonSaved = db.Column(db.Integer)
    carTravelKm = db.Column(db.Float)
    packagedFood = db.Column(db.Boolean)
    showerTimeMinutes = db.Column(db.Integer)
    electronicTimeHours = db.Column(db.Integer)
    onlineShopping = db.Column(db.Boolean)
    wasteFood = db.Column(db.Boolean)
    airConditioningHeating = db.Column(db.Boolean)
    noDriving = db.Column(db.Boolean)
    plantMealThanMeat = db.Column(db.Boolean)
    useTumbler = db.Column(db.Boolean)
    saveEnergy = db.Column(db.Boolean)
    separateRecycleWaste = db.Column(db.Boolean)
    logDate = db.Column(db.Date, nullable=False, default=date.today) 

    def to_dict(self):
        return {
            "id": self.id,
            "usersId": self.usersId,
            "totalCarbon": self.totalCarbon,
            "carbonLevel": self.carbonLevel,
            "IslandPath": self.IslandPath,
            "carbonSaved": self.carbonSaved,
            "carTravelKm": self.carTravelKm,
            "packagedFood": self.packagedFood,
            "showerTimeMinutes": self.showerTimeMinutes,
            "electronicTimeHours": self.electronicTimeHours,
            "onlineShopping": self.onlineShopping,
            "wasteFood": self.wasteFood,
            "airConditioningHeating": self.airConditioningHeating,
            "noDriving": self.noDriving,
            "plantMealThanMeat": self.plantMealThanMeat,
            "useTumbler": self.useTumbler,
            "saveEnergy": self.saveEnergy,
            "separateRecycleWaste": self.separateRecycleWaste,
            "logDate": self.logDate.isoformat() if self.logDate else None
        }
