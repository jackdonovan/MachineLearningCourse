
Chapter 10 Exercises 2-8

2. Why is it generally preferable to use a Logistic Regression classifier rather than a Perception? How can you tweak a Perception to make it equvalent to a Logistic Regression clasifier?

    -Answer: In preceptron, you will not be able to calculate the probababilities for the classes effectively. A perceptron will only converge if the dataset is linearly seperable. Instead, a logistic regression classifier will converge even if the dataset is not linealy seperable. It will also output the classprobabilities unlike a perceptron. If you were to change the perceptrons acivation function to the logistic activation or trian it with a gradient descent function, it would make it equivalent to a logistic regression classifier.
    
3. Why was the logistic activation function a key ingredient in training the first MLPs?

    -Answer: when the function used for activation is a step function, the gradient descent cannot really run, and always requires a function with a derivative of nonzero.
    
4. Name three popular activition functions. Can you draw them?

    -Answer: 
    
    Sigmoid
    ![sigmoid.png](attachment:sigmoid.png)
    
    Tanh
    ![tanh.png](attachment:tanh.png)
    
    Relu
    ![relu.png](attachment:relu.png)
    
5. Suppose you have an MLP composed of one input layer with 10 passthrough neurons, followed by one hidden layer with 50 artifical neurons, and finally one output layer with 3 artificial neurons. All artificial neurons use the ReLU activation functions.

    -What is the shape of input matrix X?
    
        -Answer: Inpute size * 10
        
    -What about the shape of hidden layer's weight vector Wh, and the shape of its bias vector bh?
    
        -Answer: 10 pass neurons * 50 art neurons == 10x50
        -Answer: bias vector = 1x50
    
    -What is the shape of the network's output matrix y?
    
        -Answer: matrix height x 3
        
    -Write the equation that computes the network's output matrix Y as a function of X, Wh, bh, Wa and b0.
    
        -Answer: Relu( Relu( X * Wh + bh ) * Wa + bo)
        
6. How many neurons do you need in the output layer if you want to classify email into spam or ham? What activation function should you use in the output layer? If instead you want to tackle the MNIST, how many neurons do you need int the output layer, using what activation function? Answer the same questions for getting your network to predict housing prices as in Chapter 2?

    -Using the logistic function, you would only need one neuron.
    -Using the softmax function, you would 10 neurons or more

7. What is backpropagation and how does it work? What is the difference between backpropagation and reverse-mode autodiff?

    -Answer: Backpropagation is where you perform many gradient descent functions which then are used to train a neural net. Reverse mode autodiff is the process used for solving and computing gradient descent functions which in turn are used by backpropagation.
    
8. Can you list all the hyperparameters you can tweak in an MLP? If the MLP overfits the training data, how could you tweak thest hyperparameters to try to solve the problem?

    -Answer: You can change the number of hidden layers and the number of neuronns per layer. If it overfits the training data you could tweak the activation function.
    


```python

```
