# Ticketing Module for Odoo - Event Management System

This repository contains the custom **Ticketing module** for **Odoo**, developed as part of the M10_RE_02 challenge. The module is designed to help an event management company register and handle customer tickets such as claims, inquiries, and suggestions, all linked to reservations of cultural events.

## 📌 Project Context

A company that manages events needed a solution to efficiently track and respond to service-related issues. This module allows employees to manage client data, event bookings, and tickets through an intuitive interface integrated into Odoo.

## 🛠️ Functional Scope

The module provides complete support for the following:

- **Events**: Manage code, description, date, time, location, and price.
- **Clients**: Manage client data such as code, name, surname, phone, address, and email.
- **Reservations**:
  - Each client can make multiple reservations.
  - Each reservation links one client to one event.
- **Tickets**:
  - Linked to a specific reservation.
  - Types: Complaint, Inquiry, or Suggestion.
  - Status: Created, Pending Confirmation, Denied, Successfully Processed.
  - Created by an employee (linked to `hr.employee`).

## 🧩 Module Components

- **Python Models**: Define data structure and relations.
- **XML Views**:
  - List and form views for all entities.
  - Form view of the client includes related reservations and tickets.
- **Menus**: Easy navigation to Clients, Events, Reservations, and Tickets.

## 🧪 Database Access

SQL queries allow access to all data stored by the module. These include joins between clients, reservations, events, and tickets to extract meaningful information.

## 📝 Delivery Content

- ✅ Class Diagram (Draw\.io or compatible)
- ✅ Fully working Odoo module (models + views)
- ✅ SQL queries to retrieve module data
- 🧪 Must be tested and validated by the instructor

## 🤝 Contributing

We welcome contributions! Feel free to fork the repository, submit issues, or create pull requests to improve the application.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

If you have any questions or suggestions, feel free to contact us at 148581386+rwxce@users.noreply.github.com.