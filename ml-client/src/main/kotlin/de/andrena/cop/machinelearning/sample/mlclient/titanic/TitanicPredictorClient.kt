package de.andrena.cop.machinelearning.sample.mlclient.titanic

import de.andrena.cop.machinelearning.sample.mlclient.MediaTypes
import de.andrena.cop.machinelearning.sample.mlclient.PredictionResponse
import feign.Headers
import feign.RequestLine

object TitanicConstants {
    const val PREDICT_TITANIC = "/api/titanic/latest"
}

interface TitanicPredictorClient {
    @RequestLine("POST " + TitanicConstants.PREDICT_TITANIC)
    @Headers("Content-Type: ${MediaTypes.JSON}")
    fun predict(passenger: Passenger): PredictionResponse
}