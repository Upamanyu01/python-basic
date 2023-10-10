class Car:
	speed = 0
	started=False
	def start(self):
		self.started=True
		print("car started,let's ride!")
	def increse_speed(self,delta):
		if self.started:
			self.speed=self.speed+delta
			print('Vroom!')
		else:
			print("You need to start the car first")
	def stop(self):
		self.speed=0
		print('Halting')
car = Car()
car.increse_speed(10)
car.start()
car.increse_speed(10)
car.stop()