# sample codes using tslearn.
- Purpose: clustering for waveform data or time series data.<br>
- tslearn is one of the Machine Learning libraries based on python.<br>
- tslearn: https://github.com/rtavenar/tslearn

# description
- Waveform clustering is performed on the sample data using the KShape algorithm.
- The number of clusters must be given as an argument to the algorithm.
    - In this case, we set `n_clusters=2` since we know that there are two classes after checking the data in advance.
- There are several ways to check the number of clusters, but in this case the elbow method was used.
    - Other possible methods are
        - BIC・AIC
        - GAP method
        - Silhouette method
        - Elbow method

# directory
- `data/`: sample dataset for clustering waveform
- `notebook/`: jupyter notebook implementing tslearn sample code