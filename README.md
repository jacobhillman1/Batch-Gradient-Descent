# Batch Gradient Descent for Single Variable Linear Regression
This is an implementation of gradient descent used to minimize the cost
function (in this case, squared difference) for a single variable linear
hypothesis.

The program currently supports data input via .xls files, and the example I used
for training is included in the src file.

## Example Output
I provided the algorithm with a small data set of cricket chirps v. temperature.
After **25 iterations**, the algorithm produced parameters **theta0 = 0.292315839612**
and **theta1 = 4.80156273351**. The resulting linear function, the orange line, is seen in [this graph](https://github.com/jacobhillman1/Batch-Gradient-Descent/blob/master/Figure_1.png). The blue dots represent the original data.
