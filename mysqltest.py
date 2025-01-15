import streamlit as st

# Set page title and layout
st.set_page_config(page_title="MySQL Notes", layout="wide")

# Page header
st.title("MySQL Notes")
#st.subheader("revision  ")

# Sidebar with radio buttons for selecting course level
course_level = st.sidebar.radio("Select Course Level:", ["Beginner", "Intermediate", "Advanced"])

# Function to display code and notes based on the selected course level
def display_code_for_course(level):
    if level == "Beginner":
        # Section 1: MySQL Beginner Course
        st.markdown("### 1. CREATE TABLE")
        st.code("""
CREATE TABLE Students (
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    Age INT
);
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use proper data types to optimize storage.")
        st.markdown("- Specify constraints like `NOT NULL`, `UNIQUE`, or `DEFAULT` as needed.")

        st.markdown("### 2. INSERT VALUES")
        st.code("""
INSERT INTO Students (ID, Name, Age) 
VALUES (1, 'John Doe', 20);
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Always check for duplicate entries if primary keys are involved.")
        st.markdown("- Use transactions for bulk inserts to ensure atomicity.")

        st.markdown("### 3. SELECT COMMAND")
        st.code("""
SELECT Name, Age FROM Students;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use `*` to select all columns, but explicitly specify columns for better performance.")
        st.markdown("- Combine with `WHERE` for filtering data.")

        st.markdown("### 4. DISTINCT COMMAND")
        st.code("""
SELECT DISTINCT Age FROM Students;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Avoid using `DISTINCT` with all columns unless necessary, as it may impact performance.")

        st.markdown("### 5. WHERE CONDITION")
        st.code("""
SELECT * FROM Students WHERE Age > 18;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use logical operators (`AND`, `OR`) for complex conditions.")
        st.markdown("- Consider indexing columns used in `WHERE` clauses for faster searches.")

        st.markdown("### 6. AND, OR, NOT COMMANDS")
        st.code("""
SELECT * FROM Students WHERE Age > 18 AND Name LIKE 'J%';
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Parentheses can be used to group conditions for clarity.")

        st.markdown("### 7. BETWEEN AND NOT BETWEEN COMMAND")
        st.code("""
SELECT * FROM Students WHERE Age BETWEEN 18 AND 25;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- `BETWEEN` is inclusive of boundary values.")

        st.markdown("### 8. IN AND NOT IN COMMAND")
        st.code("""
SELECT * FROM Students WHERE Age IN (18, 20, 22);
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use `NOT IN` for excluding specific values.")

        st.markdown("### 9. AS COMMAND")
        st.code("""
SELECT Name AS StudentName FROM Students;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Aliases are temporary and only exist during the query.")

        st.markdown("### 10. LIMIT COMMAND")
        st.code("""
SELECT * FROM Students LIMIT 5;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Combine `LIMIT` with `ORDER BY` for deterministic results.")

    elif level == "Intermediate":
        # Section 2: MySQL Intermediate Course
        st.markdown("### 11. MIN AND MAX COMMAND")
        st.code("""
SELECT MIN(Age), MAX(Age) FROM Students;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Can be combined with `GROUP BY` for grouped results.")

        st.markdown("### 12. COUNT, AVG, SUM COMMANDS")
        st.code("""
SELECT COUNT(*), AVG(Age), SUM(Age) FROM Students;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use specific columns with `COUNT` for non-null counts.")

        st.markdown("### 13. LIKE COMMAND")
        st.code("""
SELECT * FROM Students WHERE Name LIKE 'A%';
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use `_` for single-character wildcards and `%` for multiple-character wildcards.")

        st.markdown("### 14. NOT LIKE COMMAND")
        st.code("""
SELECT * FROM Students WHERE Name NOT LIKE 'A%';
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Works similarly to `LIKE` but excludes matching rows.")

        st.markdown("### 15. UNION COMMAND")
        st.code("""
SELECT column1 FROM table1
UNION
SELECT column1 FROM table2;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use `UNION ALL` to include duplicate rows.")

    elif level == "Advanced":
        # Section 3: MySQL Advanced Course
        st.markdown("### 16. ORDER BY COMMAND")
        st.code("""
SELECT column1 FROM table_name ORDER BY column1 ASC|DESC;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Default sorting order is ascending (`ASC`).")
        st.markdown("- Combine with `LIMIT` for top-N queries.")

        st.markdown("### 17. GROUP BY COMMAND")
        st.code("""
SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use `HAVING` for filtering grouped results.")

        st.markdown("### 18. UPDATE COMMAND")
        st.code("""
UPDATE table_name SET column1 = value1 WHERE condition;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Always use `WHERE` to avoid updating all rows.")

        st.markdown("### 19. ALTER COMMAND")
        st.code("""
ALTER TABLE table_name ADD column_name datatype;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use carefully as changes might be irreversible.")

        st.markdown("### 20. CHANGE TABLE AND COLUMN NAME")
        st.code("""
ALTER TABLE old_table_name RENAME TO new_table_name;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Ensure proper backup before renaming critical tables.")

        st.markdown("### 21. SAVEPOINT COMMAND")
        st.code("""
SAVEPOINT savepoint_name;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Useful for partial rollbacks within a transaction.")

        st.markdown("### 22. ROLLBACK COMMAND")
        st.code("""
ROLLBACK TO SAVEPOINT savepoint_name;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Transactions must be initiated before using `ROLLBACK`.")

        st.markdown("### 23. COMMIT COMMAND")
        st.code("""
COMMIT;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use `COMMIT` only after verifying the transaction.")

        st.markdown("### 24. INNER JOIN COMMAND")
        st.code("""
SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Avoid joining large tables without appropriate indexes.")

        st.markdown("### 25. LEFT AND RIGHT JOIN COMMAND")
        st.code("""
SELECT * FROM table1 LEFT JOIN table2 ON table1.column = table2.column;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- `LEFT JOIN` includes unmatched rows from the left table.")
        st.markdown("- `RIGHT JOIN` includes unmatched rows from the right table.")

        st.markdown("### 26. FULL JOIN AND CROSS JOIN COMMAND")
        st.code("""
SELECT * FROM table1 FULL JOIN table2 ON table1.column = table2.column;
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- Use `FULL JOIN` carefully as it might result in a large result set.")

        st.markdown("### 27. PRIMARY KEY, FOREIGN KEY, NOT NULL, CHECK CONSTRAINTS")
        st.code("""
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    Amount DECIMAL(10, 2) CHECK (Amount > 0)
);
        """, language="sql")
        st.markdown("**Notes:**")
        st.markdown("- **Primary Key**: Ensures uniqueness.")
        st.markdown("- **Foreign Key**: Establishes a relationship between tables.")
        st.markdown("- **NOT NULL**: Prevents null values.")
        st.markdown("- **CHECK**: Validates data based on a condition.")

# Display the code and notes for the selected course level
display_code_for_course(course_level)
