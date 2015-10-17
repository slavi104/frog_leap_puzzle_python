from hw1 import *
# test next_step function
if next_step([-1, -1, -1, 0, 1, 1, 1]) == [-1, 0, -1, -1, 1, 1, 1]:
	print('OK')
else:
	print(next_step([-1, -1, -1, 0, 1, 1, 1]))

# 
if next_step(generate_start_step(3)) == [-1, 0, -1, -1, 1, 1, 1]:
	print('OK')
else:
	print(next_step(generate_start_step(3)))

# 
if next_step([1, 1, 1, 0, -1, -1, -1]):
	print('OK')
else:
	print(next_step([1, 1, 1, 0, -1, -1, -1]))

# 
if next_step(generate_final_step(21)):
	print('OK')
else:
	print(next_step(generate_final_step(21)))

# 
if next_step(generate_start_step(3), [[-1, 0, -1, -1, 1, 1, 1]]) == [-1, -1, 0, -1, 1, 1, 1]:
	print('OK')
else:
	print(next_step(generate_start_step(3)))

# 
if next_step(generate_start_step(3), [[-1, 0, -1, -1, 1, 1, 1], [-1, -1, 0, -1, 1, 1, 1]]) == [-1, -1, -1, 1, 0, 1, 1]:
	print('OK')
else:
	print(next_step(generate_start_step(3)))

# 
if next_step(generate_start_step(3), [[-1, 0, -1, -1, 1, 1, 1], [-1, -1, 0, -1, 1, 1, 1], [-1, -1, -1, 1, 0, 1, 1]]) == [-1, -1, -1, 1, 1, 0, 1]:
	print('OK')
else:
	print(next_step(generate_start_step(3)))

# 
if next_step(generate_start_step(3), [[-1, 0, -1, -1, 1, 1, 1], [-1, -1, 0, -1, 1, 1, 1], [-1, -1, -1, 1, 0, 1, 1], [-1, -1, -1, 1, 1, 0, 1]]):
	print(next_step(generate_start_step(3)))
else:
	print('OK')

# 
if next_step([-1, 1, -1, 0, 1, -1, 1]) == [-1, 1, 0, -1 , 1, -1, 1]:
	print('OK')
else:
	print(next_step([-1, 1, -1, 0 , 1, -1, 1]))

# 
if next_step([-1, 1, 1, 0, -1, 1, -1]) == [-1, 1, 1, 1, -1, 0, -1]:
	print('OK')
else:
	print(next_step([-1, 1, -1, 0 , 1, -1, 1]))

# 
if next_step([-1, 1, -1, -1, 1, 1, 0]):
	print(next_step([-1, 1, -1, -1, 1, 1, 0]))
else:
	print('OK')

# 
if next_step([0, -1, -1, -1, 1, 1, 1]):
	print(next_step([0, -1, -1, -1, 1, 1, 1]))
else:
	print('OK')

# 
if next_step([-1, 1, -1, 1, -1, 1, 0]) == [-1, 1, -1, 1, 0, 1, -1]:
	print('OK')
else:
	print(next_step([-1, 1, -1, 1, -1, 1, 0]))

# 
if next_step([0, -1, 1, -1, -1, 1, 1]) == [1, -1, 0, -1, -1, 1, 1]:
	print('OK')
else:
	print(next_step([0, -1, 1, -1, -1, 1, 1]))

