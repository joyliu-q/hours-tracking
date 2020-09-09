CREATE TABLE IF NOT EXISTS main.members (
   first_name text,
   last_name text,
   class int, 
   email text,
   paid_dues text,
   auth_admin text
);
CREATE TABLE IF NOT EXISTS main.projects (
   name_of_project text,
   date DATE,
   number_of_members int, 
   hours_per_member int,
   total_hours int,
   led_by text
);
CREATE TABLE IF NOT EXISTS main.hours (
   first_name text,
   last_name text,
   member_total_projects int, 
   member_total_hours int
);