# bode-diagram
A utility to plot Bode diagrams of LTI systems (both TC and TD)

## How to run
Create a virtual environment in the cloned repository directory:  
`python3 -m venv venv`  
Activate the virtual environment:  
`source venv/bin/activate`  
Install requirements:  
`pip3 install -r requirements.txt`  
Run:  
`python3 bode_diagrams.py`  
Edit the values of `nmt`, `det`, `k` and `sample_time` accordingly to the the transfer function you're trying to plot.  
Choose (comment/uncomment) if you want to plot a time continuous function, or a time discrete function.  
When finished, exit the virtual environment:  
`deactivate`  

Enjoy the beauty of Bode diagrams!
![alt text](https://imgur.com/t8IlXQl.png)
