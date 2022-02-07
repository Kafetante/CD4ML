package de.andrena.cop.machinelearning.sample

import com.fasterxml.jackson.module.kotlin.jacksonObjectMapper
import feign.Feign
import feign.Logger
import feign.jackson.JacksonDecoder
import feign.jackson.JacksonEncoder
import feign.slf4j.Slf4jLogger

class ClientFactory(private val port: Int = 11000) {
    fun <T> create(clazz: Class<T>): T {
        return Feign.builder()
            .encoder(JacksonEncoder(jacksonObjectMapper()))
            .decoder(JacksonDecoder(jacksonObjectMapper()))
            .logger(Slf4jLogger())
            .logLevel(Logger.Level.FULL)
            .target(clazz, "http://localhost:$port")
    }
}