from mysql import connector

class BloodDonorManager:
    def __init__(self):
        self.connection=connector.connect(
            host="localhost",
            user="root",
            password="Ardhra@17",
            database="blood_db"
        )
        print("connected successfully..!")


    def get_object(self, id=None):
      try:
        self.cursor = self.connection.cursor()
        query = "select * from donor where id=%s"
        values = (id,)
        self.cursor.execute(query, values)
        record = self.cursor.fetchone()
        return record
      except Exception as e:
        return None
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """INSERT INTO donor
                        (name, blood_group, phone, city, last_donate)
                        VALUES (%s, %s, %s, %s, %s)"""

            values =[v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("donor added successfully")

        except Exception as e:
            print("Error:", e)
    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from donor"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            # print(records)
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
           record=self.get_object(id=id)
           if record==None:
               print("record not found...!")
           else:
               print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
       try:
          record=self.get_object(id=id)
          values=(id,)
          if record!=None:
            query="delete from donor where id=%s"
            self.cursor.execute(query,values)
            self.connection.commit()
            print("donor deleted successfully....!")
          else:
            print("donor not found")
       except Exception as e:
          print(e)
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)  # to find the donor with given id
            if record!=None:  #if a record is found then record will not be none so the update operation continue
               self.cursor= self.connection.cursor()
               placeholder=""   # creates an empty string . this variable will be used to construct the set  part of sql query.
               for k in kwargs.keys():
                   placeholder +=k + "=%s, "
                   placeholder=placeholder.rstrip(", ") # this is necessary because we don't want a comma immediatly before WHERE clause
                   query=f"update donor SET {placeholder} where id=%s"
                   values=[v for v in kwargs.values()]
                   values.append(id)
                   self.cursor.execute(query, values)
                   self.connection.commit()
               print("donor details updated successfully")
            else:   # if no record is found
                print("donor not found")
        except Exception as e:
            print(e)

# donor_instance=BloodDonorManager()  #create object
# # donor_instance.post(
# #     name="Ardhra",
# #     blood_group="O+",
# #     phone="9876543210",
# #     city="Kochi",
# #     last_donation="2026-08-20"
# # )
# # donor_instance.post(
# #     name="dhivya",
# #     blood_group="B+",
# #     phone="58220366475",
# #     city="kakanad",
# #     last_donation="2022-01-18"
# # )
# # donor_instance.post(
# #     name="kira",
# #     blood_group="A+",
# #     phone="58996472310",
# #     city="aluva",
# #     last_donation="2014-06-26"
# # )
# donor_instance.get()
# print("__________________details of one donor__________________")
# donor_instance.retrieve(id=1)
# print("________________delete one data________________")
# donor_instance.delete(id=2)
# donor_instance.get()
# print("-----------------after updation----------------")
# donor_instance.put(id=1, city="calicut")
# donor_instance.get()