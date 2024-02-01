from heapq import heappush, heappop
stóg = []
dane = [1,50, 30, 1.5, 7, 9, 2,-4.55, 4, 6, 8, 0]
for element in dane:
     heappush(stóg, element)

posortowana = []
while stóg:
     posortowana.append(heappop(stóg))

print (posortowana)
dane.sort()
print (dane == posortowana)
print ('Jakie mamy maximum i minimum')


def find_min_max(array: list) -> (int, int):
     min = array[0]
     max = array[0]

     for i in range (1, len (array)):
          if array[i] < min:
               min = array[i]
          elif array[i] > max:
               max = array[i]

     return min, max


array = [dane]

min, max = find_min_max (dane)

print (f'Minimum: {min}, Maximum: {max}')

