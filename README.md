# CHES Data 2019
Chapel hill data analysis with Dimensionality reduction

● Justify your methodological choices in each step (1–4). What other choices could you
have made? What would have been their pros and cons?

## Step 1: The loading and cleaning of data. 

I have considered numerical columns for analysis and discarded expert demographics data. 
For missing values in numerical data, I chose mean imputation, so that it doesn't disturb the overall distribution of the data. 
For cases where mean imputation was not possible, None object was chosen, as it will not affect the downstream analysis and it will be reported as absence. 

There is a slight difference between stata file and csv. The don't know option appears as ".d" in csv, whereas in stata file it is a NaN. 
Standard scaler was chosen as it is a recommended technique to have unit variance for dimensionality reduction in non-linear optimisations like t-SNE and UMAP. 

## Step 2: Dimensionality reduction 
I used both t-SNE and UMAP to plot a 2D distribution during exploration. In the final version, I used UMAP. 
The reason for that is the perplexity parameter, time taken to run t-SNE, my lack of expertise in running an inverse transform on t-SNE without a PCA. 
UMAP provides an API with inverse transforms and it is considered an improvement over t-SNE.
The 52 dimension numerical matrix was downsized to 2D and plots were generated. (Refer : Notebook.ipynb for sequence)
The distribution of the parties was not a clustered one. Its all over the place. 
The aggregated distributions of the average dataset I observed during EDA, provided much spaced out and neat resolutions. I have not used the average data set as I suspected it might not have been scaled as per my requirement. 

![alt text](/img/newplot.png)

## Step 3 : Sampling 10 random points within the distribution
I used the extreme limits of the distribution observed on the graph to obtain the range for a reasonable random number data point
> Range (x,y) : [2,11],[2,8]


## Step 4 : Map it back to higher dimensions
Used random generated points to estimate the higher dimensions. Used inverse transform and standard scaler object to re-create the higher dimensions. 

## Step 5 : Brownie question
Observing the ranges of x and y and comparing them with the original questionnaire in the code book, reasonable ranges (R1) were estimated. However, to avoid the hassle of painting individual cells, made a heat map, which will highlight the cells of higher frequency. Added an additional histogram on the left to help in the analysis 

![alt text](/img/heatmap.png)


● Explain in a non-technical way what the low-dimensional representation of the data
means (your visualization in the step 2). What could you teach a politician about the European party distribution based on the dimensionality reduction and/or possible
additional analyses you may produce?





● How would you deploy the model to a cloud environment so that it would be able to
withstand 1 million users per hour? You can for example include a sketch of a cloud
architecture.
