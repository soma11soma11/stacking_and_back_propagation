//Neural Net

#include <vector>
#include <iostream>
#include <cstdlib>
#include <cassert>
#include <cmath>

using namespace std;

struct Connection{
  double weight;
  double deltaWeight;
}

class Neuron;

typedef vector<Neuron> Layer;

// *****class Neuron

class Neuron{
public:
  Neuron(unsigned numOutputs, unsigned myIndex);
  void setOutputVal(double val) {m_outputVal = val;}
  double getOutputVal(void) const {return m_outputVal;}
  void feedForward(const Layer &prevLayer);

private:
  static double transferFunction(double x);
  static double transferFunctionDerivative(double x);
  static double rendomWeight(void) {return rand() / double(RAND_MAX); }
  //By using static, the value is preserved even after the function
  //so by calling it again you can use the preserved value
  //But you cant access from outside
  double m_outputVal;
  vector<Connection> m_outputWeights;
  unsigned m_myindex;
};

double Neuron::transferFunction(double x)
{
  // tanh -output range[-1..1]
  return tanh(x)
}

double Neuron::transferFunctionDerivative(double x)
{
  // tanh derivative
  return 1.0 - x*x;
}

void Neuron::feedForward(const Layer &prevLayer)
{
  double sum = 0.0;
  //Sum the previous layer's outputs
  //include the previous Layer

  for (unsigned n = 0; n < prevLayer.size(); ++n){
    sum += prevLayer[n].getOutputVal() *
            prevLayer[n].m_outputWeights[m_myIndex].weight;
  }
  m_outputVal = Neuron::transferFunction(sum);
}


Neuron::Neuron(unsigned numOutputs, unsigned myIndex){
  for (unsigned c = 0; c < numOutputs; c++){
    m_outputWeights.push_back(Connection());
    m_outputWeights.back().weight = randomWeight();
  }
  m_myIndex = myIndex;
}



// *****class Net

class Net{
public:
  Net (const vector<unsigned> &topology);
  void feedForward(const vector<double> &inputVals);
  void backProp(const vector<double> &targetVals) {};
  void getResults(vector<double> &resultVals) const {};

private:
  vector<Layer> m_layers; // m_layers[layerNum][neuronNum]
  double m_error;
  double m_recentAverageError;
  double m_recentAverageSmoothingFactor;
};

void Net::backProp(const vector<double> &targetVals)
{
  // Caluculate overall net error (RMS of output neuron errors)
  Layer &outputLayer = m_layers.back();
  m_error = 0.0;
  for (unsigned n=0; n < outputLayer.size() - 1; ++n){
    double delta = targetVals[n] - outputLayer[n].getOutputVal();
    m_error += delta * delta;
  }
  m_error /= outputLayer.size() - 1;
  m_error += sqrt(m_error); //RMS

 //Implemnt a recent average measurement

 m_recentAverageError =
  (m_recentAverageError * m_recentAverageSmoothingFactor + m_error)
  / (m_recentAverageSmoothingFactor + 1.0);

  // Calculate output layer gradients

  for (unsigned n = 0; n < outputLayer.size() - 1; ++n) {
    outputLayer[n].calcOutputGradients(targetVals[n]);
  }

  // Calculate gradients on hidden layers

  for (unsigned layerNum = m_layers.size() - 2; layerNum > 0; --layerNum){
    Layer &hiddenLayer = m_layers[layerNum];
    Layer &nextLayer = m_layers[LayerNum + 1];

    for (unsigned n = 0; n < hiddenLayer.size(); ++n){
      hiddenLayer[n].calcHiddenGradients(nextLayer);
    }
  }


  //For all layers from outputs to first hidden layer,
  // Update connection weights

  for (unsigned layerNum = m_layers.size() - 1; ++n){
    Layer &layer = m_layers[layerNum];
    Layer &prevLayer = m_layers[layerNum - 1];

    for (unsigned n = 0; n <layer.size() - 1; ++n){
      layer[n].updateInputWeights(prevLayer);
      
    }
  }

}

void Net::feedForward(const vector<double> &inputVals){
  assert(inputVals.size() == m_layers[0].size() - 1)
  //Assign the input values into the input neurons.
  for (unsigned i = 0; i < inputVals.size(); ++i){
    m_layers[0][i].setOutputVal(inputVals[i]);
  }

  //forward propagate
  for (unsigned layerNum = 1; layerNum < m_layers.size(); ++layerNum){
    Layer &prevLayer = m_layers[layerNum - 1];
    for(unsigned n = 0; n < m_layers[layerNum].size() - 1; ++n){
      m_layers[layerNum][n].feedForward(prevLayer);
    }
  }
}



Net::Net(const vector<unsigned> &topology){
  unsigned numLayers = topology.size();
  for (unsigned layerNum  = 0; layerNum < numLayers; ++layerNum){
    m_layers.push_back(Layer());
    unsigned numOutputs =  layerNum == topology.size() - 1 ? 0 : topology [layerNum+1];
    // we have made a new Layer, now fill it with neurons
    // and a bias neuron to the layerNum
    for (unsigned neuronNum = 0; neuronNum <= topology[layerNum]; ++neuronNum)
    // <= because of bias{
      m_layers.back().push_back(Neuron(numOutputs, neuronNum));
      cout << "Made a Neuron!" << endl;
    }
  }
}

int main(){
  vector<unsigned> topology;
  topology.push_back(3);
  topology.push_back(2);
  topology.push_back(1);

  Net myNet(topology);

  vector<double> inputVals;
  myNet.feedForward(inputVals);

  vector<double> targetVals;
  myNet.backProp(targetVals);

  vector<double> resultVals;
  myNet.getResults(resultVals);
}
