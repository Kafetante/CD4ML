package de.andrena.cop.machinelearning.sample.mlclient.titanic

@Suppress("unused")
enum class Sex {
    FEMALE, MALE;

    override fun toString(): String {
        return super.toString().lowercase()
    }}