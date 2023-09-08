from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class GI(db.Model):
    # class for generated images information 
    # contains the information regarding : 
    #   - which gan was used 
    #   - which plant class
    #   - what sub class ie which disease or healthy
    #   - image data in the form of array before conversion 
    id = db.Column(db.Integer, primary_key=True) 
    GanName = db.Column(db.String(128))
    PlantClass = db.Column(db.String(128))
    SubClass = db.Column(db.String(128))
    # can contain the image array 
    ImageData = db.Column(db.LargeBinary)

    # def set_image_data(self, image_data):
    #     # Serialize the 3D NumPy array and store it as binary data
    #     self.ImageData = np.array(image_data).tobytes()

    # def get_image_data(self):
    #     # Deserialize the binary data back into a 3D NumPy array
    #     return np.frombuffer(self.ImageData, dtype=np.uint8).reshape((self.width, self.height, self.channels))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    email = db.Column(db.String(10000), unique=True)
    password = db.Column(db.String(128))
    FirstName = db.Column(db.String(128))
    # GeneratedImg = db.relationship('GI',  primaryjoin="User.id == GI.id")