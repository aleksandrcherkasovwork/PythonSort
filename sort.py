from datetime import datetime
import time
import random
def bubbleSort(array):
	print("Исходный список:",array)
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
	print("Конечный список:",array)
def insertSort(array):
	start_time = datetime.now()
	print("Исходный список:",array)
	for i in range(1,len(array)):
		currentValue = array[i]
		currentPosition = i
		while currentPosition > 0 and array[currentPosition - 1] < currentValue:
			array[currentPosition] = array[currentPosition - 1]
			currentPosition = currentPosition - 1
		array[currentPosition] = currentValue
	print("Конечный список:",array)
def sortTest(array,n):
	print("Сортировка пузырьком")
	start_time = datetime.now()
	for _ in range(n):
		test_array = array.copy()
		bubbleSort(test_array)
	bubbleSortTime = datetime.now() - start_time 
	print("Сортировка вставкой")
	start_time = datetime.now()
	for _ in range(n):
		test_array = array.copy()
		insertSort(test_array)
	insertSortTime = datetime.now() - start_time
	print("Время работы bubbleSort: ",bubbleSortTime,"Для",n,"Итерраций")
	print("Время работы insertSort: ",insertSortTime," Для", n,"Итерраций")


temp_array = list(range(0,50,2))
random.shuffle(temp_array)
print(temp_array)
sortTest(temp_array,50)