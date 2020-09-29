import sqlite3
class Dbms(object):
              def __init__(self,name,address,city,qualification,gender):
                  self.name=name
                  self.address=address
                  self.city=city
                  self.qualification=qualification
                  self.gender=gender
              
              @classmethod    
              def querry(self,name,address,city,qualification,gender):
                  
                  connectObj= sqlite3.connect('Form.db')
                  cursorObj=connectObj.cursor()
                  cursorObj.execute('''Insert into Enteries(Name,Address,City,Qualification,Gender) values(?,?,?,?,?);''',(name,address,city,qualification,gender))
                  connectObj.commit()
