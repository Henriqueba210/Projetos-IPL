# Build the application using Gradle
FROM gradle:jdk17 as builder
WORKDIR /app
COPY . .
RUN ./gradlew build

# Use OpenJDK 11 JRE slim as the base image
FROM eclipse-temurin:17-jre-focal

# Copy the built JAR file to the container
COPY --from=builder /app/build/libs/DataMS-0.0.1.jar /app/DataMS-0.0.1.jar

# Set the entrypoint to run the application
ENTRYPOINT ["java", "-jar", "/app/DataMS-0.0.1.jar"]