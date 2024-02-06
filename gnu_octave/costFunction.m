function J=costFunction(X,Y,teta)

m=size(X,1);
guess=X*teta;
squareMistake=(guess-Y).^2;

J=1/(2*m)*sum(squareMistake);
