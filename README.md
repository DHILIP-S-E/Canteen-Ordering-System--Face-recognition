# Canteen Ordering System with Face Recognition 🍽️

A smart canteen management system that uses face recognition for authentication and provides an efficient ordering platform for students, staff, and administrators.

## Features 🌟

- **Face Recognition Authentication**
  - Secure login using facial biometrics
  - Traditional password login as fallback
  - Face registration for new users

- **Multi-Role System**
  - Student: Order food, track orders, view history
  - Staff: Manage orders, update order status
  - Admin: User management, menu management, analytics

- **Menu Management**
  - Dynamic menu items with categories
  - Stock management
  - Support for daily and regular items
  - Image support for food items

- **Order Processing**
  - Real-time order tracking
  - Multiple payment methods (Cash on Delivery, Razorpay)
  - Automatic stock updates
  - Order notifications

- **Analytics & Reporting**
  - Sales analytics
  - Payment method statistics
  - Most sold items tracking
  - Order history export

## Tech Stack 💻

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** SQLite
- **Face Recognition:** dlib, face_recognition
- **Payment Integration:** Razorpay

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Canteen-Ordering-System--Face-recognition.git
cd Canteen-Ordering-System--Face-recognition
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python app.py
```

## Project Structure 📁

```
├── app.py              # Main application file
├── auth.py            # Authentication handling
├── db_utils.py        # Database utilities
├── payment.py         # Payment processing
├── utils.py           # Utility functions
├── components/        # UI components
│   └── ui.py         # UI utility functions
├── database/         # Database files
│   └── canteen.db    # SQLite database
├── faces/            # Stored face images
└── data/             # Face encodings
```

## Usage 🔧

1. Start the application:
```bash
streamlit run app.py
```

2. Default admin credentials:
   - Username: admin
   - Password: admin123

3. Register new users through the admin panel:
   - Create user account
   - Register face for authentication

## Features by Role 👥

### Student
- Face/Password login
- Browse menu items
- Add items to cart
- Place orders
- Track order status
- View order history
- Receive notifications

### Staff
- Manage incoming orders
- Update order status
- View completed orders
- Real-time updates

### Admin
- User management
- Face registration
- Menu management
- Stock control
- View analytics
- Export reports

## Security 🔒

- Face recognition for secure authentication
- Password hashing for traditional login
- Role-based access control
- Secure payment processing

## Contributing 🤝

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Face recognition implementation using dlib
- Streamlit for the interactive web interface
- SQLite for lightweight database management
- Razorpay for payment processing