import random
import bisect

def generate_random_list(n: int):
	#generate list of 2n unique positive intergers
	list_n = []
	list_orginal = []
	while len(list_n) < 2*n:	#2n element
		random_number = random.randint(1, 2**n -1)	#maximum n bits
	#generate random number k
		if random_number not in list_n:
			list_orginal.append(random_number)
			bisect.insort(list_n, random_number)
	k = random.randint(1, 2**n -1)
	return k, list_n, list_orginal

def binary_search(k: int, n: int, list_n: list[int]):
	low = 0
	high = n -1
	while low <= high:
		mid = (low+high) // 2
		# if the middle element is k,return its position. 
		if list_n[mid] == k:
			return mid
		elif list_n[mid] < k:
			low = mid + 1
		else:
			high = mid - 1
	return -1
def search_k(k: int, n: int, list_n: list[int]):
	result = binary_search(k, n, list_n)
	if result != -1:
		print("true " + str(result + 1))
	else:
		print("false")
	return result
def less_than_k(k: int, position: int, list_n: list[int]):
	list_less_than = []
	position -= 1
	if position >= 0:
		while(position >= 0):
			list_less_than.append(list_n[position])
			position -= 1
		print(list_less_than, k)
	else:
		print("nothing")

def main():
	n = abs(int(input("Enter the number of bits (n must be a positive value): ")))
	k, list_n, list_orginal = generate_random_list(n)
	print(str(k)+",", list_n)
	position = search_k(k, 2*n, list_n)
	less_than_k(k, position, list_n)

if __name__ == "__main__":
	main()
