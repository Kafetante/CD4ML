package de.andrena.cop.machinelearning.sample.mlclient.houses

import de.andrena.cop.machinelearning.sample.mlclient.MediaTypes
import de.andrena.cop.machinelearning.sample.mlclient.PredictionResponse
import feign.Headers
import feign.RequestLine

object HousesConstants {
    const val PREDICT_HOUSES = "/api/houses/latest"
}

interface HousesPredictorClient {
    @RequestLine("POST " + HousesConstants.PREDICT_HOUSES)
    @Headers("Content-Type: ${MediaTypes.JSON}")
    fun predict(house: House): PredictionResponse
}