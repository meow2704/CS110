#omyaasree balaji
#cs 110
#in class :Introduction to Classes & Objects
from movie import Movie

M1 = Movie('Shin-chan', '2017-04-15', '99%', 'Akira Takumi')
M2 = Movie('Naruto OG', '2014-12-06', '93%', 'Kishimoto')
M3 = Movie('Your Name', '1995-07-15', '77%', 'Mokoto Shinkai')

M1.set_director('Usui')
print(M1.get_director())

print(M1)

M2.set_releasedate('2023-08-03')
print(M2.get_releasedate())

print(M2)

M3.set_rating('89%')
print(M2.get_rating())

M3.set_title('crayon shin chan')
print(M2.get_title())

print(M3)

