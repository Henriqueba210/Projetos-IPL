plugins {
    java
    id("org.springframework.boot") version "3.0.2"
    id("io.spring.dependency-management") version "1.1.0"
    id("org.openapi.generator") version "6.4.0"
}

group = "com.tonnie.microsservices"
version = "0.0.1"
java.sourceCompatibility = JavaVersion.VERSION_17

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.springframework.boot:spring-boot-starter-data-jpa")
    implementation("org.springframework.boot:spring-boot-starter-validation")
    compileOnly("org.projectlombok:lombok")
    annotationProcessor("org.projectlombok:lombok")
    annotationProcessor("org.mapstruct:mapstruct-processor:1.5.3.Final")
    implementation("org.flywaydb:flyway-core")
    implementation("org.postgresql:postgresql")
    implementation("org.springframework.amqp:spring-rabbit")
    implementation("org.springdoc:springdoc-openapi-starter-webmvc-ui:2.0.2")
    implementation("org.mapstruct:mapstruct:1.5.3.Final")
    implementation("com.google.code.gson:gson:2.8.9")
    implementation("com.squareup.okhttp3:logging-interceptor:4.9.3")
    implementation("com.squareup.okhttp3:okhttp:4.9.3")
    implementation("com.squareup.okio:okio:2.8.0")
    implementation("io.gsonfire:gson-fire:1.8.5")
    implementation("io.swagger:swagger-core:1.6.9")
    implementation("javax.annotation:javax.annotation-api:1.3.2")
    implementation("javax.ws.rs:javax.ws.rs-api:2.1.1")
    implementation("org.openapitools:jackson-databind-nullable:0.2.2")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
}

tasks.withType<Test> {
    useJUnitPlatform()
}

java {
    modularity.inferModulePath.set(true)
}

val generateVehicleClient by tasks.registering(org.openapitools.generator.gradle.plugin.tasks.GenerateTask::class) {
    generatorName.set("java")
    inputSpec.set("$rootDir/src/main/resources/clients/vehicle.yml")
    outputDir.set("$buildDir/generated-sources")
    apiPackage.set("com.tonnie.microsservices.api")
    invokerPackage.set("com.tonnie.microsservices.invoker")
    modelPackage.set("com.tonnie.microsservices.model")
    invokerPackage.set("com.tonnie.microsservices")
    configOptions.set(
        mapOf(
            "dateLibrary" to "java8",
            "java8" to "true",
            "useBeanValidation" to "true",
            "interfaceOnly" to "true",
            "serializableModel" to "true"
        )
    )
}

val generateTelemetryProfileClient by tasks.registering(org.openapitools.generator.gradle.plugin.tasks.GenerateTask::class) {
    generatorName.set("java")
    inputSpec.set("$rootDir/src/main/resources/clients/telemetry.yml")
    outputDir.set("$buildDir/generated-sources")
    apiPackage.set("com.tonnie.microsservices.api")
    invokerPackage.set("com.tonnie.microsservices.invoker")
    modelPackage.set("com.tonnie.microsservices.model")
    invokerPackage.set("com.tonnie.microsservices")
    configOptions.set(
        mapOf(
            "dateLibrary" to "java8",
            "java8" to "true",
            "useBeanValidation" to "true",
            "interfaceOnly" to "true",
            "serializableModel" to "true"
        )
    )
}

tasks.compileJava() {
    dependsOn(arrayOf(generateVehicleClient, generateTelemetryProfileClient))
}


configure<SourceSetContainer> {
    named("main") {
        java.srcDir("$buildDir/generated-sources/src/main/java")
    }
}

val sonarqube by tasks.registering {
    dependsOn(tasks.named("test"))
    group = "Code Quality"
    description = "Runs Sonarqube analysis"
    doLast {
        exec {
            commandLine = listOf(
                "sonar-scanner",
                "-Dsonar.projectKey=com.example.api",
                "-Dsonar.sources=src/main",
                "-Dsonar.host.url=http://localhost:9000"
            )
        }
    }
}

tasks.named<org.springframework.boot.gradle.tasks.bundling.BootJar>("bootJar") {
    launchScript()
}
