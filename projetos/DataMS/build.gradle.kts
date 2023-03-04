plugins {
	java
	id("org.springframework.boot") version "3.0.2"
	id("io.spring.dependency-management") version "1.1.0"
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
	implementation("org.projectlombok:lombok")
	annotationProcessor("org.mapstruct:mapstruct-processor:1.5.3.Final")
	implementation("org.flywaydb:flyway-core")
	implementation("org.postgresql:postgresql")
	implementation("org.springframework.amqp:spring-rabbit")
	implementation("io.springfox:springfox-swagger2:2.10.5")
	implementation("io.springfox:springfox-swagger-ui:2.10.5")
	implementation("org.mapstruct:mapstruct:1.5.3.Final")
	testImplementation("org.springframework.boot:spring-boot-starter-test")
}

tasks.withType<Test> {
	useJUnitPlatform()
}

java {
	modularity.inferModulePath.set(true)
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
