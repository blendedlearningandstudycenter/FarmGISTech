"""
Backend Models Documentation for CV Building System

This module defines the database models for a CV-building system using SQLAlchemy ORM.
It allows users to create multiple profiles, each with different job applications, 
and stores job posting information associated with those profiles.

The following models are defined:

1. User:
   - Represents the user who uses the system.
   - Each user can have multiple profiles.
   - Columns:
     - id: Primary key.
     - name: User's name.
     - email: User's email address.
     - password: User's hashed password.
   - Relationships:
     - profiles: One-to-many relationship with the Profile model (i.e., one user can have many profiles).

2. Profile:
   - Represents a CV profile created by a user.
   - A user can create multiple profiles, each containing different information (like education, experience).
   - Columns:
     - id: Primary key.
     - title: The title of the profile (e.g., "Software Engineer Profile").
     - profile_data: Text field to store the content of the profile (e.g., education, work experience).
     - created_at: The date and time the profile was created.
     - user_id: Foreign key linking this profile to the corresponding user.
   - Relationships:
     - user: Many-to-one relationship with the User model (i.e., multiple profiles belong to one user).
     - job_postings: One-to-many relationship with the JobPosting model (i.e., one profile can have many job applications).

3. JobPosting:
   - Represents a job application linked to a specific profile.
   - Contains details about the job posting (e.g., job title, company, job description).
   - Columns:
     - id: Primary key.
     - job_title: Title of the job being applied for (e.g., "Data Scientist").
     - company_name: The name of the company offering the job.
     - job_description: Description of the job role.
     - profile_id: Foreign key linking this job posting to the associated profile.
   - Relationships:
     - profile: Many-to-one relationship with the Profile model (i.e., multiple job postings belong to one profile).

Usage Notes:
-------------
- Each user can create multiple profiles, and for each profile, they can apply to multiple jobs.
- To start using this system, you need to first create a user, then create profiles for that user,
  and finally add job postings for each profile.
- The datetime field `created_at` in the Profile model automatically captures the creation time using `datetime.utcnow()`.

How to use:
------------
1. Define a `User`.
2. Create one or more `Profile` entries for the user.
3. For each profile, add `JobPosting` entries to track job applications.

Relationships:
---------------
- **User - Profile**: One-to-many (A user can have multiple profiles).
- **Profile - JobPosting**: One-to-many (A profile can have multiple job postings).

This model setup supports the functionality of a CV-building app where users can manage different profiles and job applications.

"""
from database import Base
from sqlalchemy import Column, String
import uuid

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

