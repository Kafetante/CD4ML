package de.andrena.cop.machinelearning.sample

import com.github.tomakehurst.wiremock.client.WireMock.*
import com.github.tomakehurst.wiremock.junit5.WireMockTest
import de.andrena.cop.machinelearning.sample.mlclient.MediaTypes
import de.andrena.cop.machinelearning.sample.mlclient.houses.House
import de.andrena.cop.machinelearning.sample.mlclient.houses.HousesConstants
import de.andrena.cop.machinelearning.sample.mlclient.houses.Style
import de.andrena.cop.machinelearning.sample.mlclient.titanic.Embarked
import de.andrena.cop.machinelearning.sample.mlclient.titanic.Sex
import de.andrena.cop.machinelearning.sample.mlclient.titanic.Passenger
import de.andrena.cop.machinelearning.sample.mlclient.titanic.TitanicConstants
import org.amshove.kluent.shouldBeEqualTo
import org.junit.jupiter.api.Test

object TestConstants {
    const val port = 8092
}

private const val OK_RESPONSE = "{\"prediction\":\"0\",\"probabilities\":{\"0\":0.6,\"1\":0.4}}"

@WireMockTest(httpPort = TestConstants.port)
class PredictorRestTest {

    @Test
    fun titanicPredictorIsCalledWithCorrectJson_AndResponseIsReturned() {
        stubFor(post(TitanicConstants.PREDICT_TITANIC)
            .willReturn(ok(OK_RESPONSE)))

        val response = Predictor(TestConstants.port).predictTitanicSurvived(
            Passenger(
                age = 11.2,
                siblingsOrSpouse = 2,
                parentsOrChildren = 3,
                fare = 123.45,
                passengerClass = 1,
                sex = Sex.FEMALE,
                embarked = Embarked.QUEENSTOWN,
                cabin = "EF 34"
            )
        )

        verify(
            postRequestedFor(urlPathEqualTo(TitanicConstants.PREDICT_TITANIC))
                .withRequestBody(equalTo("{\"age\":11.2,\"sibsp\":2,\"parch\":3,\"fare\":123.45,\"pclass\":1,\"sex\":\"FEMALE\",\"embarked\":\"QUEENSTOWN\"," +
                        "\"cabin\":\"EF 34\"}"))
                .withHeader("Content-Type", equalTo(MediaTypes.JSON))
        )

        response.prediction shouldBeEqualTo "0"
        response.probabilities shouldBeEqualTo mapOf("0" to 0.6, "1" to 0.4)
    }
    @Test
    fun housePredictorIsCalledWithCorrectJson_AndResponseIsReturned() {
        stubFor(post(HousesConstants.PREDICT_HOUSES)
            .willReturn(ok(OK_RESPONSE)))

        val response = Predictor(TestConstants.port).predictHousePrice(
            House(
                lotSizeInSf = 4000,
                beds = 4,
                baths = 5,
                yearBuilt = 1990,
                kitchenRefurbished = 1,
                livingAreaInSF = 1000,
                pool = 2,
                parking = 3,
                multiFamily = 1,
                zipcode = "12345",
                style = Style.COTTAGE
            )
        )

        verify(
            postRequestedFor(urlPathEqualTo(HousesConstants.PREDICT_HOUSES))
                .withRequestBody(equalTo("{\"lot_size_sf\":4000,\"beds\":4,\"baths\":5,\"year_built\":1990,\"kitchen_refurbished\":1," +
                        "\"square_feet\":1000,\"pool\":2,\"parking\":3,\"multi_family\":1,\"zipcode\":\"12345\",\"style\":\"COTTAGE\"}"))
                .withHeader("Content-Type", equalTo(MediaTypes.JSON))
        )

        response.prediction shouldBeEqualTo "0"
        response.probabilities shouldBeEqualTo mapOf("0" to 0.6, "1" to 0.4)
    }
}