package de.andrena.cop.machinelearning.sample.mlclient.houses

import com.fasterxml.jackson.annotation.JsonProperty

@Suppress("unused")
data class House(
    @JsonProperty("lot_size_sf") val lotSizeInSf: Int = 5000,
    val beds: Int = 2,
    val baths: Int = 1,
    @JsonProperty("year_built") val yearBuilt: Int = 1950,
    @JsonProperty("kitchen_refurbished") val kitchenRefurbished: Int = 0,
    @JsonProperty("square_feet") val livingAreaInSF: Int = 1000,
    val pool: Int = 0,
    val parking: Int = 1,
    @JsonProperty("multi_family") val multiFamily: Int = 0,
    val zipcode: String = "12345",
    val style: Style = Style.COTTAGE
)