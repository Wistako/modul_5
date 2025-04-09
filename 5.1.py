from faker import Faker

fake = Faker('es_ES')

class BaseCard:
   def __init__(self, first_name, last_name, position, email):
      self.first_name = first_name
      self.last_name = last_name
      self.position = position
      self.email = email
      
      self._str_length = 0

   @property
   def str_length(self):
      first_length = len(self.first_name)
      last_length = len(self.last_name)
      return f'{first_length} {last_length}'

   def __repr__(self):
      return f"{self.first_name} {self.last_name} {self.email}"

   def contact(self):
      print(f'Kontaktuje się z {self.first_name} {self.last_name} {self.position} {self.email}')

peoples = []
def create_fake_people():      
   for i in range(5):
      p = fake.name()
      p = p.split(' ')

      peoples.append(VisitCard(p[0], p[1], 'Pracownik', fake.email() ))


create_fake_people()

for people in peoples:
   print(people)
   print(people.str_length)


by_name = sorted(peoples, key=lambda p: p.first_name)
by_last_name = sorted(peoples, key=lambda p: p.last_name)
by_email = sorted(peoples, key=lambda p: p.email)