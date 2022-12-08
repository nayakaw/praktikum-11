class Student:
	'A student class'
	stuCount = 0

	def __init__(self):
         self.name = input('Masukkan Nama: ')
         self.nim = input('Masukkan Nim: ')
         self.angkatan = input('Masukkan Angkatan: ')
         Student.stuCount += 1

	def displayStudent(self):
		print("\nNama: ", self.name, "\nNIM: ", self.nim, "\nAngkatan: ", self.angkatan)


stu1 = Student()
stu1.displayStudent()

print('Jumlah Mahasiswa:', Student.stuCount)