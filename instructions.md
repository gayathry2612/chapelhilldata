# Pull from Docker hub
` $docker run gayathry2612/hello`
> It is uploading ....check the remote repo on docker hub(3PM EET)![alt text](/img/docker_status_14:40PM.png)

# Build from Source
1. Clone the current repository. cd to it
2. Initiate docker on your local / cloud machine
3. Build an image from Dockerfile (notice the fullstop):  
` $docker image build -t hello .`
4. Build a container : 
` $docker-compose build hello`
5. Start the container : 
` $docker-compose up hello`

You will see a jupyter notebook terminal. Make sure you have port : 8888 free
Please click on that and navigate to /notebooks/Notebook.ipynb
