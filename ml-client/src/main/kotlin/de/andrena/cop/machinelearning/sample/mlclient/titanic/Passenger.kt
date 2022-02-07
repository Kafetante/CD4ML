package de.andrena.cop.machinelearning.sample.mlclient.titanic

import com.fasterxml.jackson.annotation.JsonProperty

@Suppress("unused")
data class Passenger(
    val age: Double = 10.0,
    @JsonProperty("sibsp") val siblingsOrSpouse: Int = 0,
    @JsonProperty("parch") val parentsOrChildren: Int = 0,
    val fare: Double = 100.0,
    @JsonProperty("pclass") val passengerClass: Int = 2,
    val sex: Sex = Sex.FEMALE,
    val embarked: Embarked = Embarked.CHERBOURG,
    val cabin: String = "?"
)
