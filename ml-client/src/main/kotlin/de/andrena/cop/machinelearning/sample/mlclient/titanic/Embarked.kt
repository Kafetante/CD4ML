package de.andrena.cop.machinelearning.sample.mlclient.titanic

@Suppress("unused")
enum class Embarked {
    CHERBOURG, QUEENSTOWN, SOUTHAMPTON;

    override fun toString(): String {
        return super.toString().first().toString()
    }}