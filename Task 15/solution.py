# from astropy.stats import sigma_clipped_stats
# from astropy.nddata import Cutout2D
# from photutils import DAOStarFinder
import numpy as np
import matplotlib.pyplot as plt 
from astropy.io import fits


def gaussian_2d(yy, xx, y0, x0, width, peak):
	x = (xx - x0) ** 2 / 2 / width / width
	y = (yy - y0) ** 2 / 2 / width / width
	return np.exp(-x - y) * peak


def estimate_psf(image, nstars=10, size=20):
	'''
	Estimate an empirical psf from the image

	image: 2D array, image with some stars
	nstars: int, number of brightest stars to stack
	size: int, size of the resulting PSF image (square stamp)

	returns a 2D array with the PSF image
	'''
	# do stuff here

	hdul = fits.open(image)
	data = hdul[0].data

	# print data.shape

	count = 0

	x_pos = []
	y_pos = []
	vals = []

	for i in range(1, data.shape[0]-1):
		for j in range(1, data.shape[1]-1):
			# if data[i,j] + data[i+1,j] + data[i-1,j] + data[i,j+1] + data[i,j-1] > 66000:
			if data[i,j] > 1500:
				# print data[i,j]
				count += 1
				x_pos.append(j)
				y_pos.append(i)
				vals.append(data[i,j])
	print count

	plt.figure()
	plt.imshow(data)
	plt.plot(x_pos, y_pos, 'x')

	plt.figure()
	plt.hist(vals, 100)
	plt.show()

	# return psf


estimate_psf(image='M34_Clear_60s_B2_T5_27886.fit', nstars=10, size=20)