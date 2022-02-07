import org.jetbrains.kotlin.gradle.tasks.KotlinCompile

plugins {
    kotlin("jvm") version "1.6.10"
}

repositories {
    mavenCentral()
    maven {
        url = uri("https://mvnrepository.com/artifact/io.github.openfeign/feign-core")
    }
}

dependencies {
    implementation(kotlin("stdlib"))
    implementation("io.github.openfeign:feign-core:11.8")
    implementation("com.netflix.feign:feign-slf4j:8.18.0")
    implementation("com.netflix.feign:feign-jackson:8.18.0")

    implementation("com.fasterxml.jackson.core:jackson-core:2.13.1")
    implementation("com.fasterxml.jackson.module:jackson-module-kotlin:2.13.1")

    implementation("ch.qos.logback:logback-classic:1.2.10")

    testImplementation("org.amshove.kluent:kluent:1.68")
    testImplementation("org.junit.jupiter:junit-jupiter-api:5.8.2")
    testImplementation("com.github.tomakehurst:wiremock-jre8:2.32.0")
    testRuntimeOnly("org.junit.jupiter:junit-jupiter-engine:5.8.2")
}

tasks.test {
    useJUnitPlatform()
}

tasks.withType<KotlinCompile> {
    kotlinOptions {
        jvmTarget = "11"
        freeCompilerArgs = listOf("-Xjsr305=strict")
    }
}
