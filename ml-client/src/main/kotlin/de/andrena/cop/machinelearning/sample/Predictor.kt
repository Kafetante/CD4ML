package de.andrena.cop.machinelearning.sample

import de.andrena.cop.machinelearning.sample.mlclient.PredictionResponse
import de.andrena.cop.machinelearning.sample.mlclient.houses.House
import de.andrena.cop.machinelearning.sample.mlclient.houses.HousesPredictorClient
import de.andrena.cop.machinelearning.sample.mlclient.titanic.Passenger
import de.andrena.cop.machinelearning.sample.mlclient.titanic.TitanicPredictorClient

class Predictor(port: Int = 11000) {

    private val titanicClient = ClientFactory(port).create(TitanicPredictorClient::class.java)
    private val housesClient = ClientFactory(port).create(HousesPredictorClient::class.java)

    fun predictTitanicSurvived(passenger: Passenger): PredictionResponse {
        return (titanicClient.predict(passenger)).also {
            println("$passenger -> $it")
        }
    }

    fun predictHousePrice(house: House): PredictionResponse {
        return (housesClient.predict(house)).also {
            println("$house -> $it")
        }
    }
}