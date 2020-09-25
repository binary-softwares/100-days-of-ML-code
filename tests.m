data = load('dataset.txt')
x = data(:, 1)
y = data(:, 2)
m = length(y)
alpha = 0.01
num_of_iterations = 1000
theta =zeros(2,1)
x=[ones(m,1), data(:,1)]
h_of_x = theta'*x

for i = 1:num_of_iterations
  
  theta1 = theta1-(alpha/m) * sum((h_of_x'-y)*x)
  theta2 = theta2-(alpha/m) * sum((h_of_x'-y)*x)
endfor
disp(theta1)