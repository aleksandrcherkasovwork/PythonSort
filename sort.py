from datetime import datetime
import time
import random
def bubbleSort(array):
	for i in range(len(array)):
		for j in range(len(array)-i-1):
			if array[j] > array[j+1]:
				array[j],array[j+1] = array[j+1],array[j]
def insertSort(array):
	for i in range(1,len(array)):
		currentValue = array[i]
		currentPosition = i
		while currentPosition > 0 and array[currentPosition - 1] < currentValue:
			array[currentPosition] = array[currentPosition - 1]
			currentPosition = currentPosition - 1
		array[currentPosition] = currentValue
def mergeSort(array):
	if len(array)>1:
		mid = int(len(array)/2)
		lefthalf = array[:mid]
		righthalf = array[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = 0
		j = 0
		k = 0
		while i<len(lefthalf) and j<len(righthalf):
			if lefthalf[i]<righthalf[j]:
				array[k] = lefthalf[i]
				i += 1
			else:
				array[k] = righthalf[j]
				j += 1
			k += 1
		while i<len(lefthalf):
			array[k] = lefthalf[i]
			i += 1
			k += 1
		while j<len(righthalf):
			array[k] = righthalf[j]
			j += 1
			k +=1
def fastSort(array):
	pass
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
	print("Сортировка слиянием")
	start_time = datetime.now()
	for _ in range(n):
		test_array = array.copy()
		mergeSort(test_array)
	mergeSortTime = datetime.now() - start_time
	print("Время работы bubbleSort: ",bubbleSortTime,"Для",n,"Итерраций")
	print("Время работы insertSort: ",insertSortTime," Для", n,"Итерраций")
	print("Время работы mergeSort: ",mergeSortTime," Для", n,"Итерраций")


temp_array = list(range(0,50,2))
random.shuffle(temp_array)
sortTest(temp_array,10000)