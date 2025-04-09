from faker import Faker

fake = Faker('es_ES')

class BaseContact:
   def __init__(self, first_name, last_name, email, tel_private):
      self.first_name = first_name
      self.last_name = last_name
      self.tel_private = tel_private
      self.email = email
      
      self._str_length = 0

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
      self.position = position
      self.company_name = company_name
      self.tel_business = tel_business
      super().__init__(*args, **kwargs)

   def contact(self):
      print(f'Wybieram numer {self.tel_business} i dzwonię do {self.first_name} {self.last_name}')


peoples = []
def create_fake_people():      
   for i in range(5):
      p = fake.name()
      p = p.split(' ')

      peoples.append(BaseContact(p[0], p[1], 'Pracownik', fake.email() ))


create_fake_people()

for people in peoples:
   print(people)
   print(people.str_length)


by_name = sorted(peoples, key=lambda p: p.first_name)
by_last_name = sorted(peoples, key=lambda p: p.last_name)
by_email = sorted(peoples, key=lambda p: p.email)