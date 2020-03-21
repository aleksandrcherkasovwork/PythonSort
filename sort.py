#! /usr/bin/env python
# -*- coding: utf-8 -*-
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


def shellSort(array):
	subListCount = len(array)//2
	while subListCount > 0:
		for startPosition in range(subListCount):
			for i in range(startPosition + subListCount,len(array),subListCount):
				currentValue = array[i]
				position = i
				while position >= subListCount and array[position - subListCount] > currentValue:
					array[position] = array[position - subListCount]
					position = position - subListCount
				array[position] = currentValue
		subListCount = subListCount // 2
def selectionSort(array):
	for fillSlot in range(len(array) - 1,0,-1):
		positionMax = 0
		for currentPosition in range(1,fillSlot+1):
			if array[currentPosition] > array[positionMax]:
				positionMax = currentPosition
			temp = array[fillSlot]
			array[fillSlot] = array[positionMax]
			array[positionMax] = temp


def sortTest(array,n):
	print("Сортировка пузырьком")
	start_time = datetime.now()
	print("Typeof:",type(array))
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
	print("Сортировка выбором")
	start_time = datetime.now()
	for _ in range(n):
		test_array = array.copy()
		selectionSort(test_array)
	selectionSortTime = datetime.now() - start_time
	print("Сортировка Шелл")
	start_time = datetime.now()
	for _ in range(n):
		test_array = array.copy()
		shellSort(test_array)
	shellSortTime = datetime.now() - start_time
	print("Время работы bubbleSort: ",bubbleSortTime,"Для",n,"Итерраций")
	print("Время работы insertSort: ",insertSortTime," Для", n,"Итерраций")
	print("Время работы mergeSort: ",mergeSortTime," Для", n,"Итерраций")
	print("Время работы selectionSort: ",selectionSortTime," Для", n,"Итерраций")
	print("Время работы shellSort: ",shellSortTime," Для", n,"Итерраций")


temp_array = list(range(0,100))
random.shuffle(temp_array)
sortTest(temp_array,10000)
