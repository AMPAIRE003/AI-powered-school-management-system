FROM cirrusci/flutter:latest

WORKDIR /app

COPY pubspec.* ./

RUN flutter pub get

COPY . .

RUN flutter pub get

EXPOSE 5555

CMD ["flutter", "run", "-d", "web"]
