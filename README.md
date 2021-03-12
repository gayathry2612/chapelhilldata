# CHES Data 2019
Chapel hill data analysis with Dimensionality reduction. 

The analysis is presented here in the form of a notebook to show my thought process and intentions. I spent some time analysing the dataset, code book and questionnaire. 
> Google sheet  :  
![Full details of the columns](https://docs.google.com/spreadsheets/d/e/2PACX-1vRMNnnvLPRFYRiw5GduBKtIaw6c9u9vMioiK6ss6GW7TpvXSeHHmsaz0DHbRnzgus-Y6bYTibzx1yGK/pubhtml?gid=1230933217&single=true)

## Question 1 
● Justify your methodological choices in each step (1–4). What other choices could you
have made? What would have been their pros and cons?

> Step 1: The loading and cleaning of data. 

I have considered numerical columns for analysis and discarded expert demographics data. 
For missing values in numerical data, I chose mean imputation, so that it doesn't disturb the overall distribution of the data. 
For cases where mean imputation was not possible, None object was chosen, as it will not affect the downstream analysis and it will be reported as absence. The other choice was to impute zero or eliminate a column. I chose not to do that as 0 would disrupt the scales on one side - it is a key label to estimate party leanings. 



There is a slight difference between stata file and csv. The don't know option appears as ".d" in csv, whereas in stata file it is a NaN. Standard scaler was chosen as it is a recommended technique to have unit variance for dimensionality reduction in non-linear optimisations like t-SNE and UMAP. 

> Step 2: Dimensionality reduction 

I used both t-SNE and UMAP to plot a 2D distribution during exploration. In the final version, I used UMAP. 
The reason for that is the perplexity parameter, time taken to run t-SNE, my lack of expertise in running an inverse transform on t-SNE without a PCA. UMAP provides an API with inverse transforms and it is considered an improvement over t-SNE.
The 52 dimension numerical matrix was downsized to 2D and plots were generated. (Refer : Notebook.ipynb for sequence)
The distribution of the parties was not a clustered one. Its all over the place. 
The aggregated distributions of the average dataset I observed during EDA, provided much spaced out and neater resolutions. I have not used the average data set as I suspected it might not have been standardised as per my requirement. 

![alt text](/img/newplot.png)


Step 3 : Sampling 10 random points within the distribution

I used the extreme limits of the distribution observed on the graph to obtain the range for a reasonable random number data point
> Range (x,y) : [2,11],[2,8]


> Step 4 : Mapping it back to higher dimensions

Used random generated points to estimate the higher dimensions. Used inverse transform and standard scaler object to re-create the higher dimensions. 

I could have been more creative at Step 3, and estimated points based on density. It would need some research on my part, hence saved it for later. 

> Step 5 : Brownie question

Observing the ranges of x and y and comparing them with the original questionnaire in the code book, reasonable ranges (R1) were estimated. However, to avoid the hassle of painting individual cells, made a heat map, which will highlight the cells of higher frequency. Added an additional histogram on the left to help in the analysis . I'm not sure if I did what you asked me here. 

![alt text](/img/heatmap.png)

# Question 2:
● Explain in a non-technical way what the low-dimensional representation of the data means (your visualization in the step 2). What could you teach a politician about the European party distribution based on the dimensionality reduction and/or possible
additional analyses you may produce?

> Analogy : Birds of same feather, flock together

A politician can understand which parties think alike on a highlevel. If they want to brainstorm on common issues, who should they approach, who will align and who will be radically different from them. This analysis on a high level can help in understanding politics scene in EU. For example, the plot below has a functionality to select data as per country.As the politician hovers over points, they will understand the party leanings. There are more analyses that can be done - for example through topics. 

> A vs B : Analysis reduced by topics
* General topics
* EU_Integration
* Specific_EU_Policy
* Ideology
* Policy dimensions
* party_characteristics
* Turkey related
* Vignettes
* Expert Demographics 

For example, an aggregated opinion of experts can map all parties in a space. Neighbouring parties can have something similar in the way they are perceived by the experts. 

![alt text](/img/aggregated_umap.png)


The data fields on excel sheet where 1vs1 analysis can be done :

![Full details of the columns](https://docs.google.com/spreadsheets/d/e/2PACX-1vRMNnnvLPRFYRiw5GduBKtIaw6c9u9vMioiK6ss6GW7TpvXSeHHmsaz0DHbRnzgus-Y6bYTibzx1yGK/pubhtml?gid=1230933217&single=true)


● How would you deploy the model to a cloud environment so that it would be able to withstand 1 million users per hour? You can for example include a sketch of a cloud
architecture.

> Reference Architecture 

For Azure, the reference architecture published at MSFT website, is a good starting point. It covers the general theme of how to design a high throughput low latency system.  

The general theme is to interface a webapp with Kubernetes service that manages the containers. It can happen in sequence of actions : 

* The ML Engineering team pushes the latest updates to the container registry
* The Containers are hosted on a kubernetes cluster. The master node, manages which pods to launch and which one to kill, with an autoscale feature. 
* To handle the million requests, the front end also will be actively hosted on a container framework to handle the throughput
* The webapps run inference with the help of serverless functions to optimise the costs.
* Note : There is no online training happening in this case. All training is done in batch mode.    

![alt text](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/media/ai-at-the-edge.svg)

Thank you for giving me this opportunity to attempt this problem.
