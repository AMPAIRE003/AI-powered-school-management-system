# School Management System - Frontend

React web application for the AI-powered School Management System.

## 🚀 Setup

### Prerequisites
- Node.js 18+
- npm or yarn

### Installation

1. **Navigate to frontend directory**
```bash
cd frontend
```

2. **Install dependencies**
```bash
npm install
```

3. **Create environment file**
```bash
cp .env.example .env.local
# Edit .env.local with your configuration
```

4. **Start development server**
```bash
npm start
```

The application will open at `http://localhost:3000`

## 📁 Project Structure

```
frontend/
├── public/                    # Static files
├── src/
│   ├── components/           # Reusable components
│   │   ├── Layout/
│   │   ├── Dashboard/
│   │   ├── Forms/
│   │   └── Common/
│   ├── pages/                # Page components
│   │   ├── Login/
│   │   ├── Dashboard/
│   │   ├── Students/
│   │   ├── Teachers/
│   │   ├── Exams/
│   │   ├── Reports/
│   │   ├── Fees/
│   │   └── Notifications/
│   ├── services/             # API services
│   │   ├── api.ts
│   │   ├── auth.ts
│   │   ├── students.ts
│   │   ├── exams.ts
│   │   ├── reports.ts
│   │   └── fees.ts
│   ├── stores/               # State management (Zustand)
│   │   ├── authStore.ts
│   │   ├── userStore.ts
│   │   └── notificationStore.ts
│   ├── styles/               # Global styles
│   ├── types/                # TypeScript types
│   ├── utils/                # Utility functions
│   ├── App.tsx               # Main app component
│   └── index.tsx             # Entry point
├── package.json
├── tsconfig.json
├── tailwind.config.js
└── Dockerfile
```

## 🎨 Available Scripts

### Development
```bash
npm start          # Start development server
npm run lint       # Run ESLint
npm run type-check # Check TypeScript types
```

### Production
```bash
npm run build      # Build for production
npm test           # Run tests
```

## 🔐 Authentication

The frontend uses JWT tokens for authentication stored in localStorage.

### Login Flow
1. User submits credentials
2. Backend returns JWT token
3. Token is stored in localStorage
4. Token is included in all subsequent API requests

## 📚 Key Features

### Dashboard
- Overview of key metrics
- Recent notifications
- Quick actions

### Student Management
- View all students
- Add/edit student information
- Track academic progress

### Exam Management
- Create and schedule exams
- View exam results
- Generate AI exam questions

### Report Generation
- Generate comprehensive reports
- View historical reports
- Download reports as PDF

### Fee Management
- View fee structures
- Track payments
- Send payment reminders

### Notifications
- View all notifications
- Mark notifications as read
- Set notification preferences

## 🎯 Components

### Layout Components
- `Sidebar` - Navigation sidebar
- `Header` - Top header with user info
- `Footer` - Footer component

### Form Components
- `StudentForm` - Add/edit student
- `ExamForm` - Create exam
- `FeeForm` - Configure fees

### Dashboard Components
- `MetricsCard` - Display metrics
- `Chart` - Recharts integration
- `RecentNotifications` - Latest notifications

## 🧪 Testing

Run tests with:
```bash
npm test
```

## 🐳 Docker

Build and run with Docker:
```bash
docker build -t school-management-frontend .
docker run -p 3000:3000 school-management-frontend
```

## 📝 Contributing

1. Create a feature branch
2. Follow React best practices
3. Write TypeScript
4. Submit a pull request

## 📞 Support

For issues and questions, please open an issue on GitHub.
