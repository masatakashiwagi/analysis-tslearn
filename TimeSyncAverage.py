# -*- coding: utf-8 -*-

import glob
import numpy as np
import matplotlib.pyplot as plt
from tslearn.clustering import KShape, TimeSeriesKMeans


def calculate_TSA(df, column, rpm, sampling_rate, start, num_avg=10):
	dataset = list()
	step = int(sampling_rate * (60 / rpm))
	end = start + step * num_avg

	x = np.array(df[column])

	for i in range(start, end, step):
		channel = x[i: i + step]
		dataset.append(channel)

	# calculate TSA
	# TSA = Time Synchronous Averaging
	# the denoise method for Waveform
	average_in = dataset[0]
	for i in dataset[1:]:
		average_in += i
	average_in /= len(dataset)

	return average_in


def load_dataset(path):
	# load a model data
	filenames = sorted(glob.glob(path + '/*.npy'))
	dataset = list()
	for filename in filenames:
		print(filename)
		dataset.append(np.load(filename))
	return dataset


def transform_dataset(dataset):
	tsdata = list()
	for i, data in enumerate(dataset):
		tsdata.append(data.tolist()[:])
		# Check the maximum length of each time series data
		len_max = 0
		for ts in tsdata:
			if len(ts) > len_max:
				len_max = len(ts)
		# Add the last data to make the time series data have the same length
		for j, ts in enumerate(tsdata):
			len_add = len_max - len(ts)
			tsdata[j] = ts + [ts[-1]] * len_add

	tsdata = np.array(tsdata)
	return tsdata


def transform_vector(time_series_array):
	# transform a vector
	stack_list = list()
	for j in range(len(time_series_array)):
		data = np.array(time_series_array[j])
		data = data.reshape((1, len(data))).T
		stack_list.append(data)
	# One-dimensional array
	stack_data = np.stack(stack_list, axis=0)
	return stack_data


def clustering_Kshape(tsdata, n_clusters, random_state, n_init, max_iter=100):
	np.random.seed(random_state)
	# Need to be normalized to calculate cross correlation
	# stack_data = TimeSeriesScalerMeanVariance(mu=0.0, std=1.0).fit_transform(stack_data)

	# Instantiate of KShape Class
	ks = KShape(n_clusters=n_clusters, n_init=n_init, verbose=True, random_state=random_state, max_iter=max_iter)
	y_pred = ks.fit_predict(tsdata)

	return y_pred


def clustering_TimeSeriesKMeans(tsdata, n_clusters, random_state, n_init, metric="softdtw", metric_params={"gamma_sdtw": 0.01}):
	np.random.seed(random_state)
	# Instantiate of TimeSeriesKMeans Class
	dtw_km = TimeSeriesKMeans(n_clusters=n_clusters, n_init=n_init, metric=metric, metric_params=metric_params, verbose=True, random_state=random_state)
	y_pred = dtw_km.fit_predict(tsdata)

	return y_pred
