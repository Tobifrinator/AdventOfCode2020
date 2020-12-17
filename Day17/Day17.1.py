import numpy as np

#counts the active ('#') neighbors
def active_neighbors(cube_array, cubex, cubey, cubez):
	active=0
	for x in [-1,0,1]:
		for y in [-1,0,1]:
			for z in [-1,0,1]:
				if(x==0 and y==0 and z==0):
					continue
				if(cube_array[z+cubez][y+cubey][x+cubex]=='#'):
					active=active+1
	return active

#prints an 3d array in a nice way
def show_3darray(array):
	for z in range(len(array)):
		print("\nz =",z-(len(array)//2))
		for y in range(len(array[0])):
			print(array[z][y])

#computes a single round
def round_change(cube_array):
	needs_change=np.zeros_like(cube_array,int)
	#process where changes are necessary
	for z in range(len(cube_array)):
		for y in range(len(cube_array[z])):
			for x in range(len(cube_array[z][y])):
				#if cube is active and not exactly 2 or 3 cubes are active around it, the cube becomes inactive
				if cube_array[z][y][x]=='#':
					if(active_neighbors(cube_array,x, y, z) not in [2,3]):
						needs_change[z][y][x]=1
				#if cube is inactive and exactly 3 cubes are active around it, the cube becomes active
				if cube_array[z][y][x]=='.':
					if(active_neighbors(cube_array,x, y, z)==3):
						needs_change[z][y][x]=1

	#make changes
	for z in range(len(cube_array)):
		for y in range(len(cube_array[z])):
			for x in range(len(cube_array[z][y])):
				if needs_change[z][y][x]==1:
					if cube_array[z][y][x]=='#':
						cube_array[z,y,x]='.'
					else:
						cube_array[z,y,x]='#'


#in every round the active cubes can take one step away from the middle -> for 6 rounds we need 6 padding outside of the start_array + a border so that we can simplify active_neighbors
def create_necessary_array(start_array):
	rounds=6
	array=np.full((rounds*2+1,len(start_array)+rounds*2,len(start_array)+rounds*2),'.')
	for y in range(len(start_array)):
		for x in range(len(start_array)):
			array[0+rounds][y+rounds][rounds+x]=start_array[y][x]
	array=np.pad(array,1,'constant', constant_values='0')
	return array


def main():
	data=open('data.txt','r')
	start_array=data.read().split()
	cube_array=create_necessary_array(start_array)

	for _ in range(6):
		round_change(cube_array)

	#count the active cubes
	unique,counts=np.unique(cube_array, return_counts=True)
	occurences=dict(zip(unique,counts))
	print(occurences['#'],' cubes are active')

if __name__ == "__main__":
	main()