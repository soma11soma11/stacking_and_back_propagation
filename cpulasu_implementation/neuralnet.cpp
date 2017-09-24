//Neural Net

#include <vector>
#include <iostream>
#include <cstdlib>

using namespace std;

struct Connection
{
  double weight;
  double deltaWeight;
}

class Neuron;

typedef vector<Neuron> Layer;

// *****class Neuron

class Neuron
{
public:
  Neuron(unsigned numOutputs);

private:
  static double rendomWeight(void) {return rand() / double(RAND_MAX); }
  //By using static, the value is preserved even after the function
  //so by calling it again you can use the preserved value
  //But you cant access from outside
  double m_outputVal;
  vector<Connection> m_outputWeights;

};

Neuron::Neuron(unsigned numOutputs)
{
  for (unsigned c = 0; c < numOutputs; c++)
  {
    m_outputWeights.push_back(Connection());
    m_outputWeights.back().weight = randomWeight();
  }
}



// *****class Net

class Net
{
public:
  Net (const vector<unsigned> &topology);
  void feedForward(const vector<double> &inputVals) {};
  void backProp(const vector<double> &targetVals) {};
  void getResults(vector<double> &resultVals) const {};

private:
  vector<Layer> m_layers; // m_layers[layerNum][neuronNum]
};


Net::Net(const vector<unsigned> &topology)
{
  unsigned numLayers = topology.size();
  for (unsigned layerNum  = 0; layerNum < numLayers; ++layerNum)
  {
    m_layers.push_back(Layer());
    unsigned numOutputs =  layerNum == topology.size() - 1 ? 0 : topology [layerNum+1];
    // we have made a new Layer, now fill it with neurons
    // and a bias neuron to the layerNum
    for (unsigned neuronNum = 0; neuronNum <= topology[layerNum]; ++neuronNum)
    // <= because of bias
    {
      m_layers.back().push_back(Neuron(numOutputs));
      cout << "Made a Neuron!" << endl;

    }


  }
}

int main()
{
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
