# **Social Media Feed Backend**  

## **📌 Overview**  
This project involves building a scalable backend for a social media feed using **Django, PostgreSQL, and GraphQL (Graphene)**. The system handles **post management, user interactions (likes, comments, shares), and flexible querying** to support high-traffic applications.  

### **🔹 Key Takeaways**  
✔ **GraphQL for flexible data fetching** – Efficiently query only the needed data.  
✔ **Scalable schema design** – Optimized for high-volume interactions.  
✔ **Real-time interaction management** – Track likes, comments, and shares.  
✔ **API testing with GraphQL Playground** – Easy debugging and exploration.  

---

## **🎯 Project Goals**  
1. **Post Management** – CRUD operations for posts.  
2. **Flexible Querying** – GraphQL API for fetching nested data.  
3. **Interaction System** – Like, comment, and share functionality.  
4. **Performance Optimization** – Efficient database queries for scalability.  

---

## **🛠 Technologies Used**  
| **Tech** | **Purpose** |  
|----------|------------|  
| **Django** | Backend framework |  
| **PostgreSQL** | Relational database |  
| **GraphQL (Graphene)** | Flexible API queries |  
| **GraphQL Playground** | API testing & documentation |  

---

## **✨ Key Features**  
### **1. GraphQL API Endpoints**  
- Fetch posts, comments, and interactions in a single query.  
- Mutations for creating, updating, and deleting posts.  

### **2. Interaction Management**  
- Like, comment, and share functionality.  
- Analytics on user engagement.  

### **3. API Testing & Documentation**  
- Hosted **GraphQL Playground** for easy testing.  
- Well-documented schema for frontend developers.  

---

## **🚀 Implementation Process**  
### **Git Commit Workflow**  
1. `feat: set up Django project with PostgreSQL`  
2. `feat: create models for posts, comments, and interactions`  
3. `feat: implement GraphQL API for querying posts`  
4. `feat: add like/comment/share mutations`  
5. `perf: optimize database queries for interactions`  
6. `docs: update README with API usage`  

---

## **📤 Submission Details**  
- **Hosted API**: Deploy on **Render, Heroku, or AWS**.  
- **GraphQL Playground**: Accessible for testing.  

---

## **📝 Evaluation Criteria**  
✅ **Functionality** – Fully working GraphQL API.  
✅ **Code Quality** – Clean, modular, and well-structured.  
✅ **Performance** – Optimized database queries.  
✅ **User Experience** – Intuitive GraphQL Playground.  
✅ **Version Control** – Clear and frequent commits.  

---

## **💡 Suggested Next Project**  
### **🔹 Real-Time Notification System**  
**Why?**  
- Extends the social media backend by adding **real-time notifications** (WebSockets).  
- Users get instant alerts for likes, comments, and shares.  

**Tech Stack:**  
- **Django Channels** (WebSockets)  
- **Redis** (Pub/Sub for real-time updates)  
- **GraphQL Subscriptions** (Push notifications)  

**Features:**  
✔ Real-time notifications via WebSockets.  
✔ User preference settings (email/push/in-app alerts).  
✔ Scalable with Redis for pub/sub messaging.  
