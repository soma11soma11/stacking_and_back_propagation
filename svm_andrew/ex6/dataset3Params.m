function [C, sigma] = dataset3Params(X, y, Xval, yval)
%DATASET3PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = DATASET3PARAMS(X, y, Xval, yval) returns your choice of C 

%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 10;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

%M1=3; %Our two multiplying factors
%M2=10; 
%ep=0.0001;%  Our seeding parameters
%E=2;    %Number of different values
%G=zeros(E,E); %Our vector of different 
%for n=1:E  
 % for m=1:E 
  %G(n,m)=ep*(M1^(m+3))*(M2^(n+2));
%end;
%end;
Gobby=[0.01,0.03,0.1,0.3,1,3,10,30];
E=length(Gobby);
G=Gobby;
MinC=G(1);
Minsigma=G(1);
model=svmTrain(X,y,MinC,@(x1, x2) gaussianKernel(x1, x2, Minsigma));
predictions = svmPredict(model, Xval);
Minerror=mean(double(predictions ~= yval));
     
for n=1:E 
 for m=1:E 
     model=svmTrain(X,y,G(m),@(x1, x2) gaussianKernel(x1, x2, G(n)));
     predictions = svmPredict(model, Xval);
     error=mean(double(predictions ~= yval));
     
     if Minerror > error;
       Minerror=error;
     MinC= G(m);
      Minsigma= G(n);
     end;
     
end;
end;


C=MinC;
sigma=Minsigma;









% =========================================================================

end
