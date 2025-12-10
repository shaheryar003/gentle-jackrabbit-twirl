# Backend Development Plan: Museum Thematic Tour App

## 1️⃣ Executive Summary
This project builds the backend for the **Museum Thematic Tour App**, creating a RESTful API to replace the current static frontend data. The system uses **FastAPI (Python 3.13)** and **MongoDB Atlas** to serve curated themes, objects, and tour itineraries.

**Constraints & Architecture:**
- **Framework:** FastAPI (Async, Python 3.13).
- **Database:** MongoDB Atlas (Motor driver, Pydantic v2).
- **Infrastructure:** No Docker, local Python environment.
- **Workflow:** Single branch (`main`), manual testing per task.
- **Scope:** Public access to museum data + Mandatory Basic Auth (S1).
- **Sprints:** 3 Sprints (S0-S2) to cover Setup, Auth, and Core Data Features.

---

## 2️⃣ In-Scope & Success Criteria

### In-Scope Features
- **Themes:** List and detail views of curated themes.
- **Objects:** Detailed profiles with images and context.
- **Tours:** Logic to retrieve specific object sequences based on Theme + Size.
- **Authentication:** Signup, Login, Logout (JWT).
- **Search/Filter:** Basic retrieval by ID and parameters.

### Success Criteria
- **Frontend Connectivity:** App functions identically to the dummy-data version but consumes live JSON.
- **Auth Compliance:** Users can sign up, log in, and access a protected route.
- **Data Integrity:** Tours correctly filter objects by theme and size.
- **Deployment:** Code pushed to `main` passes all manual checks.

---

## 3️⃣ API Design

**Base Path:** `/api/v1`

### Authentication
- `POST /auth/signup`
  - **Purpose:** Register new user.
  - **Body:** `{ "email": "...", "password": "..." }`
- `POST /auth/login`
  - **Purpose:** Authenticate and receive HttpOnly cookie (or token).
  - **Body:** `{ "email": "...", "password": "..." }`
- `POST /auth/logout`
  - **Purpose:** Clear auth cookie.
- `GET /auth/me`
  - **Purpose:** Verify token and get current user details (Protected).

### Themes
- `GET /themes`
  - **Purpose:** List all available themes.
  - **Response:** `[ { "id": "...", "name": "...", "image": "..." }, ... ]`
- `GET /themes/{id}`
  - **Purpose:** Get single theme details.

### Tours & Objects
- `GET /tours/{theme_id}/{size}`
  - **Purpose:** Get the ordered list of objects for a specific tour configuration.
  - **Response:** `[ { "id": "...", "title": "...", "galleryLocation": "...", ... }, ... ]`
  - **Note:** Returns full object details to prevent N+1 frontend fetches.
- `GET /objects/{id}`
  - **Purpose:** Get detailed object profile.

---

## 4️⃣ Data Model (MongoDB Atlas)

### `users`
- `email` (string, required, unique)
- `password_hash` (string, required)
- `created_at` (datetime)

### `themes`
- `_id` (string, maps to `id` in JSON, e.g., "roman-empire")
- `name` (string)
- `description` (string)
- `image` (string)

### `objects`
- `_id` (string, maps to `id`, e.g., "obj-01")
- `title` (string)
- `shortDescription` (string)
- `contextualBackground` (string)
- `galleryLocation` (string)
- `image` (string)
- `themeIds` (array of strings)
- `mapPosition` (object: `{ "top": "...", "left": "..." }`)

### `tours`
- `themeId` (string)
- `size` (string: "Small", "Medium", "Large")
- `objectIds` (array of strings, ordered)

---

## 5️⃣ Frontend Audit & Feature Map

| Component / Page | Route | Data Needed | Backend Endpoint |
| :--- | :--- | :--- | :--- |
| **Index.tsx** | `/` | List of Themes | `GET /themes` |
| **ThemeDetail.tsx** | `/theme/:id` | Single Theme info | `GET /themes/{id}` |
| **Tour.tsx** | `/tour/:themeId/:size` | Theme info + List of Objects | `GET /tours/{themeId}/{size}` |
| **ObjectDetail.tsx** | `/object/:id` | Single Object details | `GET /objects/{id}` |
| **Layout/Nav** | (Global) | User Auth Status | `GET /auth/me` |

---

## 6️⃣ Configuration & ENV Vars
- `APP_ENV`: `development`
- `PORT`: `8000`
- `MONGODB_URI`: Connection string for Atlas
- `JWT_SECRET`: Secret key for signing tokens
- `JWT_EXPIRES_IN`: `86400` (24 hours)
- `CORS_ORIGINS`: `http://localhost:5173` (Vite default)

---

## 7️⃣ Testing Strategy
- **Scope:** Manual verification via Frontend UI.
- **Process:**
  1.  Implement Backend Task.
  2.  Update Frontend `src/lib/museum-data.ts` (or similar adapter) to fetch from API.
  3.  Execute **Manual Test Step**.
  4.  If pass → Commit.

---

## 🔟 Dynamic Sprint Plan & Backlog

### 🧱 S0 – Environment Setup & Frontend Connection

**Objectives:**
- Initialize FastAPI project.
- Connect to MongoDB Atlas.
- Configure CORS.
- Push to GitHub.

**Tasks:**
- **Task 0.1: Project Skeleton & DB Connection**
  - Create `main.py` with `FastAPI`.
  - Add `Motor` client.
  - Create `/healthz` endpoint checking DB ping.
  - **Manual Test Step:** Run `uvicorn main:app`, open browser to `http://localhost:5173`. Check Network tab for `http://localhost:8000/healthz` (after pointing frontend there or using curl).
  - **User Test Prompt:** "Start the backend and verify that accessing `/healthz` returns a 200 OK with DB status 'connected'."

- **Task 0.2: Git Init**
  - Initialize git, add `.gitignore`, push to `main`.
  - **Manual Test Step:** Check GitHub repo.
  - **User Test Prompt:** "Confirm the repository is live on GitHub with the initial skeleton."

---

### 🧩 S1 – Basic Auth (Signup / Login / Logout)

**Objectives:**
- Secure the app infrastructure (User management).
- Add "Profile" button to Layout to demonstrate protected route.

**Tasks:**
- **Task 1.1: User Model & Signup**
  - Create `User` model.
  - Implement `POST /api/v1/auth/signup`.
  - **Manual Test Step:** Use Postman/Curl to create a user, check MongoDB Atlas collection.
  - **User Test Prompt:** "Send a POST request to signup and confirm the document exists in Atlas."

- **Task 1.2: Login & JWT Issue**
  - Implement `POST /api/v1/auth/login`.
  - Return HTTP-only cookie or Token.
  - **Manual Test Step:** Login via API client, receive token.
  - **User Test Prompt:** "Perform login and verify a valid JWT is returned."

- **Task 1.3: Protect Route & Frontend Integration**
  - Implement `GET /api/v1/auth/me` (Protected).
  - Create simple "Login" page and "Profile" state in Frontend (or just a simple "Auth Check" component for testing).
  - **Manual Test Step:** Login on UI, see "Logged in as [email]".
  - **User Test Prompt:** "Log in via the frontend and confirm the session is active."

---

### 🏛️ S2 – Core Museum Data (Themes, Objects, Tours)

**Objectives:**
- Migrate static data to MongoDB.
- Serve dynamic content to all app pages.

**Tasks:**
- **Task 2.1: Database Seeding**
  - Write a script to insert the static data from `museum-data.ts` into MongoDB (`themes`, `objects`, `tours` collections).
  - **Manual Test Step:** Check Atlas to see 3 collections populated.
  - **User Test Prompt:** "Run the seed script and confirm data in MongoDB Atlas."

- **Task 2.2: Themes API**
  - Implement `GET /themes` and `GET /themes/{id}`.
  - Update Frontend `Index.tsx` and `ThemeDetail.tsx` to fetch from API.
  - **Manual Test Step:** Refresh Home page, see Themes loaded from DB.
  - **User Test Prompt:** "Open the Home page and verify themes are displayed. Click one to see details."

- **Task 2.3: Objects & Tours API**
  - Implement `GET /tours/{theme_id}/{size}` (aggregating object data) and `GET /objects/{id}`.
  - Update Frontend `Tour.tsx` and `ObjectDetail.tsx` to fetch from API.
  - **Manual Test Step:** Go through a full "Small Roman Empire" tour. Verify list and map work. Click object for details.
  - **User Test Prompt:** "Complete a 'Small' tour flow: Select Theme -> Select Size -> View Itinerary -> View Object Details."