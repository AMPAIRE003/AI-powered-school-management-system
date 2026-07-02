# School Management System - Mobile

Flutter mobile application for the AI-powered School Management System.

Supports iOS and Android platforms.

## 🚀 Setup

### Prerequisites
- Flutter SDK (latest stable)
- Xcode (for iOS) or Android Studio (for Android)
- Cocoapods (for iOS)

### Installation

1. **Navigate to mobile directory**
```bash
cd mobile
```

2. **Get dependencies**
```bash
flutter pub get
```

3. **Create environment file**
```bash
cp .env.example .env
```

4. **Run the app**
```bash
# For Android
flutter run -d android

# For iOS
flutter run -d ios

# For web (development)
flutter run -d web
```

## 📁 Project Structure

```
mobile/
├── lib/
│   ├── main.dart                 # Entry point
│   ├── models/                   # Data models
│   │   ├── user.dart
│   │   ├── student.dart
│   │   ├── exam.dart
│   │   ├── report.dart
│   │   └── fee.dart
│   ├── screens/                  # App screens
│   │   ├── auth/
│   │   │   ├── login_screen.dart
│   │   │   └── register_screen.dart
│   │   ├── dashboard/
│   │   │   └── dashboard_screen.dart
│   │   ├── students/
│   │   ├── exams/
│   │   ├── reports/
│   │   ├── fees/
│   │   └── notifications/
│   ├── widgets/                  # Reusable widgets
│   │   ├── custom_app_bar.dart
│   │   ├── bottom_nav_bar.dart
│   │   ├── metric_card.dart
│   │   └── loading_widget.dart
│   ├── services/                 # API and services
│   │   ├── api_service.dart
│   │   ├── auth_service.dart
│   │   ├── storage_service.dart
│   │   └── notification_service.dart
│   ├── providers/                # State management (Riverpod)
│   │   ├── auth_provider.dart
│   │   ├── user_provider.dart
│   │   ├── students_provider.dart
│   │   └── notifications_provider.dart
│   ├── utils/                    # Utility functions
│   │   ├── constants.dart
│   │   ├── app_colors.dart
│   │   └── validators.dart
│   └── theme/                    # App theme
│       └── app_theme.dart
├── assets/                       # Images, icons, animations
│   ├── images/
│   ├── icons/
│   └── animations/
├── pubspec.yaml
└── Dockerfile
```

## 🎨 Supported Features

### Authentication
- Login with credentials
- Secure token storage
- Auto-login on app restart
- Logout

### Dashboard
- Key metrics overview
- Recent notifications
- Quick access buttons

### Student Management
- View student list
- Student details
- Academic history
- Performance charts

### Exams
- View scheduled exams
- Submit exam answers
- View results
- AI-generated questions

### Reports
- View report list
- Report details
- Download reports as PDF
- Share reports

### Fees
- View fee structure
- Payment history
- Make payments
- Reminders

### Notifications
- Real-time notifications
- Notification history
- Mark as read
- Delete notifications

## 🔐 Security

- JWT token-based authentication
- Secure token storage using flutter_secure_storage
- HTTPS for all API calls
- Certificate pinning (recommended)

## 📱 Platform-Specific Setup

### Android
- Minimum SDK: 21
- Target SDK: 34
- Configure signing key for release

### iOS
- Minimum iOS: 11.0
- Configure code signing
- Update Info.plist for permissions

## 🧪 Testing

Run tests:
```bash
flutter test
```

## 🚀 Building for Release

### Android
```bash
flutter build apk --release
# or for App Bundle
flutter build appbundle --release
```

### iOS
```bash
flutter build ios --release
```

## 📦 Dependencies Management

Update dependencies:
```bash
flutter pub upgrade
```

Get specific version:
```bash
flutter pub get
```

## 📝 Contributing

1. Follow Flutter best practices
2. Use null safety throughout
3. Write meaningful tests
4. Submit a pull request

## 📞 Support

For issues and questions, please open an issue on GitHub.
