package de.andrena.cop.machinelearning.sample.mlclient

class PredictionResponse(val prediction: String, val probabilities: Map<String, Double>?) {
    override fun toString(): String {
        return "predicted class: $prediction with probability " +
                "${probabilities?.getOrDefault(prediction, -1.0) ?: "n/a"}"
    }
}