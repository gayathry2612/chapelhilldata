# Notes 

A meta file to create a docker config 

ETL module to do Extract, Transform and Loading
     Write some tests to ensure the following
     1. Extraction 
      * Is URL valid, check if the host is active
      * Is Data as per the standard reported - lossy / lossless. 
        > Number of lines in average_data = 277
        > Number of lines in expert_data = 3823
      * Load the clean data as a serialised file / at a cloud location.
       > Choose a format that holds the clean data and takes less space 
       > Store the file at a publicly accessible location. Verify it. 

Hierarchy 
1. Extract  (Extract)
2. Clean the data, apply transformations (Transform)
3. Load : Store the data locally (Load)


make the conda environment from requirements.txt

run the setup file if needed