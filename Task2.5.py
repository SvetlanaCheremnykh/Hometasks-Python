#Реализуйте алгоритм перемешивания списка.
import random
test_list = [1, 4, 5, 6, 3]
print ("Последовательность чисел: " + str(test_list))
random.shuffle(test_list)
print ("Перемешанная последовательность: " +  str(test_list))
