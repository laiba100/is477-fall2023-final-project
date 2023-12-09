# is477-fall2023-final-project
Workflow 
[Workflow graph.png and graph.svg](https://edotor.net/?engine=dot?engine=dot#digraph%20snakemake_dag%20%7B%0A%20%20%20%20graph%5Bbgcolor%3Dwhite%2C%20margin%3D0%5D%3B%0A%20%20%20%20node%5Bshape%3Dbox%2C%20style%3Drounded%2C%20fontname%3Dsans%2C%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20fontsize%3D10%2C%20penwidth%3D2%5D%3B%0A%20%20%20%20edge%5Bpenwidth%3D2%2C%20color%3Dgrey%5D%3B%0A%20%20%20%20%20%20%20%200%5Blabel%20%3D%20%22prepare%22%2C%20color%20%3D%20%220.00%200.6%200.85%22%2C%20style%3D%22rounded%22%5D%3B%0A%20%20%20%20%20%20%20%201%5Blabel%20%3D%20%22reproduce%22%2C%20color%20%3D%20%220.17%200.6%200.85%22%2C%20style%3D%22rounded%22%5D%3B%0A%20%20%20%20%20%20%20%202%5Blabel%20%3D%20%22profile%22%2C%20color%20%3D%20%220.33%200.6%200.85%22%2C%20style%3D%22rounded%22%5D%3B%0A%20%20%20%20%20%20%20%203%5Blabel%20%3D%20%22analyze%22%2C%20color%20%3D%20%220.50%200.6%200.85%22%2C%20style%3D%22rounded%22%5D%3B%0A%20%20%20%20%20%20%20%202%20-%3E%201%0A%20%20%20%20%20%20%20%203%20-%3E%201%0A%20%20%20%20%20%20%20%200%20-%3E%202%0A%20%20%20%20%20%20%20%200%20-%3E%203%0A%7D%20%20%20%20%20%20%20%20%20%20%0A)


## Reproducing:
1. The first step in reproducing these results is to create a GitHub Account. Navigate to https://github.com/signup and sign up for an account. After you have signed up for an account, create a new public repository, making sure to add in a README file as well as a .gitignore.
2. The compiler I used was VSCode. In order to use it, please downlaod the VSCode application from https://code.visualstudio.com/download. 
3. Please ensure that you have at least Python 3.0 running for your envioronment. Please install Python from https://www.python.org/downloads/ and use your command line to ensure that the version you have is admissible. 
4. Install Python in VScode by navigating to the Extensions tab in VSCode and downloading the Python extension. 
5. Navigate to the requirements.txt page. These are all of the packages needed to run this program. In order to dowload these packages, open up the terminal and run the "pip install" command followed by the name of each of the packages. 
6. Navigate to the Scripts folder and run prepare_data.py. This will load in the data set and prepare it for analysis.
7. In order to create the profile for the wine dataset, please run the profile.py under the scripts section. This might take a minute or two to load.
8. In order to analyze the data, please run analysis.py under the scripts section. This will output the summary statistics for the dataset as well as a histogram and model accuracy for the dataset. These will all be stores in their own respective files under the results folder.
