package de.andrena.cop.machinelearning.sample

import de.andrena.cop.machinelearning.sample.mlclient.houses.House
import de.andrena.cop.machinelearning.sample.mlclient.titanic.Passenger
import org.amshove.kluent.shouldBeEqualTo
import org.junit.jupiter.api.Test

private const val ZIPCODE_NY = "10021"
private const val ZIPCODE_DETROIT = "48212"

internal class PredictorIntegrationTest {
    @Test
    internal fun titanic_Predict_ChildSurvives() {
        val childSurvived = Predictor().predictTitanicSurvived(Passenger(age = 1.0))
        childSurvived.prediction shouldBeEqualTo "1"
    }

    @Test
    internal fun titanic_Predict_AdultDoesNotSurviveSurvives() {
        val adultSurvived = Predictor().predictTitanicSurvived(Passenger(age = 99.0))
        adultSurvived.prediction shouldBeEqualTo "0"
    }

    @Test
    internal fun houses_Predict_CheapHouse() {
        val cheapHouse = Predictor().predictHousePrice(House(lotSizeInSf = 1000, livingAreaInSF = 300, zipcode = ZIPCODE_DETROIT))
        cheapHouse.prediction shouldBeEqualTo "63629.255"
    }

    @Test
    internal fun houses_Predict_ExpensiveHouse() {
        val expensiveHouse = Predictor().predictHousePrice(House(lotSizeInSf = 1000000, livingAreaInSF = 3000, zipcode = ZIPCODE_NY))
        expensiveHouse.prediction shouldBeEqualTo "1101732.04"
    }
}