from faker import Faker
from datetime import datetime

def fun_timer(func):
   def wrapper(*args, **kwargs):
      start = datetime.now()
      result = func(*args, **kwargs)
      end = datetime.now()
      print(end - start)
      return result
   return wrapper



fake = Faker('es_ES')

class BaseContact:
   def __init__(self, first_name, last_name, email, tel_private):
      self.first_name = first_name
      self.last_name = last_name
      self.tel_private = tel_private
      self.email = email
      

   @property
   def label_length(self):
      first_length = len(self.first_name)
      last_length = len(self.last_name)
      return f'{first_length} {last_length}'

   def __repr__(self):
      return f"{self.first_name} {self.last_name} {self.email}"

   def contact(self):
      print(f'Wybieram numer {self.tel_private} i dzwonię do {self.first_name} {self.last_name}')

class BusinessContact(BaseContact):
   def __init__(self, position, company_name, tel_business, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.position = position
      self.company_name = company_name
      self.tel_business = tel_business

   def contact(self):
      print(f'Wybieram numer {self.tel_business} i dzwonię do {self.first_name} {self.last_name}')

@fun_timer
def create_contacts(typ, count): 
   if typ not in ['B','P' ]:
      print('Nieobsługiwany typ wizytówki')
      return     
   peoples = []
   for i in range(count):
      p = fake.name()
      p = p.split(' ')
      if typ == 'B':
         peoples.append(BaseContact(first_name=p[0], last_name=p[1], email=fake.email(), tel_private=fake.phone_number() ))
      elif typ == 'P':
         peoples.append(BusinessContact(
            first_name=p[0],
            last_name=p[1],  
            tel_private=fake.phone_number(), 
            email=fake.email(), 
            tel_business=fake.phone_number(), 
            company_name=fake.company(),
            position='Manager'
            ))
   return peoples



error = create_contacts('', 2)
bussines_cards = create_contacts('B', 5)
base_cards = create_contacts('P', 4)

for people in bussines_cards:
   print(people)
   print(people.label_length)
   people.contact()
for people in base_cards:
   print(people)
   print(people.label_length)
   people.contact()


create_contacts('P', 1000) 


# by_name = sorted(peoples, key=lambda p: p.first_name)
# by_last_name = sorted(peoples, key=lambda p: p.last_name)
# by_email = sorted(peoples, key=lambda p: p.email)

