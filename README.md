# OLA (https://yjw.info)
Following OLA (online learning algorithms) implementations.
- REG = regression learning.
- PAL = passive-aggressive learning.
- PWEA = prediction with expert advice.
- CILM = conformal intervals learning machine.

## REG

To run the code:
- download `onlinereg`
- execution example `python coirr.py`

Changing following few lines will allow the user to have any data, but please make sure the format is the same.


      array = np.loadtxt(args.data_file, delimiter=' ')
      n = len(array[0][:-1])
      model = COIRR(args.tuning_parameter, n)
      for i, a in enumerate(array):
        x, y = a[:-1], a[-1]
        new_y = model.predict(x)


### Description  

Online regression - not much worse than the true forecaster in the hindsight.
  
### Dependencies

The implementation require `python` along with `argparse` and `numpy`.  
 

To get a feel for the tool user will also require: 

`matplotlib.pyplot` and `sklearn.metrics` 

### Inputs

- The original datasets as an array with size N x D, where ‘D’ represents the number of dimensions in the original space and ‘N’ is the number of observations.   
- Hyperparameters (optional) initialisation by the use.  
 
 
### Outputs    

- Predicted label 

  
## PAL

To run the code:
- download `pal` 
- execute `python paexp.py`
- record `python paexp.py --record 1`

Changing following few lines will allow the user to have any data, but please make sure the format is the same.

    parser.add_argument("--data-file", default='data/gas.txt', type=str, help="path of the data file")

    for i in range(len(train_dataset.y)):

        fig_left.scatter(x=train_dataset.dataset.x1[i], y=train_dataset.dataset.x2[i], color=cm.cool(train_dataset.dataset.label[i]), alpha=0.5)

        model_PA.fit(train_dataset.feature_vec[i], train_dataset.y[i])
        model_PA_one.fit(train_dataset.feature_vec[i], train_dataset.y[i])

        accuracies_PA.append(test_dataset.valid_training_result(model_PA))
        accuracies_PA_one.append(test_dataset.valid_training_result(model_PA_one))


### Description  

The adaptation to large data and real-time learning is a crucial challenge in supervised learning, aiming to reliably reveal the underlying data structure by constraining the surrogate loss function through slack variable. Moving average passive aggressive learning solves classification problem. This learning technique has several benefits, to name a few; ability to handle large datasets, real-time learning, minimal memory usage and resistance to overfitting.  


### Dependencies
 
The implementation requires `python` along with `numpy`, `argparse`, `pandas`.  

To get a feel for the tool user will also require: 
 
`Matplotlib.pyplot`, `matplotlib.cm`, `matplotlib.animation` and `matplotlib.gridspec` 

### Inputs    

- The original datasets as an array with size N x D, where ‘D’ represents the number of dimensions in the original space and ‘N’ is the number of observations.     
- Hyperparameter (optional) initialisation by the user, default is 0.1.  

### Outputs    

- Predicted class 

    
## PWEA

To run the code:
- download `pwea`
- execution example `seaa.py`

Changing following few lines will allow the user to have any data, but please make sure the format is the same.

    parser.add_argument("--data-file", default='data/gas.txt', type=str, help="path of the data file")

    array = np.loadtxt(args.data_file, delimiter=' ')
    n = len(array[0][:-1])
    model = SEAA(args.min_val,args.max_val,args.tuning_parameter,args.switch_rate, n,args.a_a)
    for i, a in enumerate(array):
        x, y = a[:-1], a[-1]
        new_y = model.predict(x)

### Description  

Super expert aggregation-algorithm is an algorithm that can perform classification. Moreover, the input of the problem at hand may continuously evolve, that is, the underlying distribution of the input changes over time leading to what is known as concept drift. The constraint to adhere to concept drift is imposed through discrete time irreducible Markov chain. 

  
### Dependencies

The implementation require `python` along with `argparse` and `numpy`.  
 

To get a feel for the tool user will also require: 

`matplotlib.pyplot` and `sklearn.metrics` 

### Inputs

- The original datasets as an array with size N x D, where ‘D’ represents the number of dimensions in the original space and ‘N’ is the number of observations.   
- Hyperparametera (optional) initialisation by the use.
  
### Outputs    

- Predicted label 

## CILM

To run the code:
- download `cilm`
- exection example `python devon_rainfall.py`

Changing following lines will allow the user to have any data, but please make sure the format is the same.

    pd.read_csv("devon_rainfall.csv")

### Description  

Prediction precision is an important part of uncertainty modelling, which the conformal intervals learning machines addresses. The objective is to have a routine to continuously obtain predictions by imposing exchangeability constraint.  

 ### Dependencies

The implementation require `python` along with `pandas` and `scipy.stats`.   

To get a feel for the tool user will also require: 

`matplotlib.pyplot`, `seaborn` and `numpy`  

### Inputs

- The original datasets as an array with size 1 x n, where ‘n’ represents the length of the dataset.
- Most recent available label.  


### Outputs    

- Neyman’s Prediction Intervals 
- Conformal Prediction Intervals 
