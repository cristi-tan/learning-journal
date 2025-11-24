Exercise 1 — Positive test case Write a test case for: login with valid credentials (like example above). Try to include: ID, Title, Preconditions, Steps, Expected result.

Test Case: Login With Valid Credentials

Test Case ID: TC_LOGIN_001
Title: Login with valid username and password
Preconditions:

User account exists in the system

User has a valid username and password

Browser is open and application URL is accessible

Test Steps:

Navigate to the Login page

Enter a valid username in the “Username” field

Enter a valid password in the “Password” field

Click the Login button

Test Data:

Username: valid_user

Password: valid_password123

Expected Result:

User is successfully authenticated

User is redirected to the Dashboard page

=========================================

Exercise 2 — Negative test case (invalid password) Scenario: valid username, wrong password. Expected error: "Invalid username or password" message.

Exercise 2 — Negative Test Case (Invalid Password)

Test Case ID: TC_LOGIN_002
Title: Login with valid username and invalid password
Preconditions:

User account exists

Browser is open on Login page

Test Steps:

Enter a valid username

Enter an invalid password

Click Login

Test Data:

Username: valid_user

Password: wrongPassword!

Expected Result:

Login fails

Error message displayed: "Invalid username or password"

User remains on Login page

=========================================

Exercise 3 — Empty fields Scenario: click “Login” with both fields empty. Expected: validation message (e.g. “Username is required”).

Exercise 3 — Empty Fields

Test Case ID: TC_LOGIN_003
Title: Attempt login with empty username and password
Preconditions:

Login page is loaded

Test Steps:

Leave Username field empty

Leave Password field empty

Click Login

Test Data:

Username: ""

Password: ""

Expected Result:

Validation error displayed, e.g.: "Username is required"

Optional second message: "Password is required"

User stays on Login page

=========================================

Exercise 4 — Boundary test (password length) Assume password must be minimum 8 characters. Create a test case for a 7-character password → expect error.

Exercise 4 — Boundary Test (Password Length = 7)

Assumption: Password must be at least 8 characters.

Test Case ID: TC_LOGIN_004
Title: Login attempt with password shorter than minimum (7 chars)
Preconditions:

Login page is open

Test Steps:

Enter a valid username

Enter a 7-character password

Click Login

Test Data:

Username: valid_user

Password: abcdefg (7 chars)

Expected Result:

Validation error shown: "Password must be at least 8 characters long"

Login is not attempted

=========================================

Exercise 5 — “Forgot password” link Test that clicking “Forgot password”: opens reset password page or sends reset email (depending on flow you imagine)

Exercise 5 — Forgot Password Link

Test Case ID: TC_LOGIN_005
Title: Verify functionality of “Forgot Password” link
Preconditions:

Login page is open

Test Steps:

Click the Forgot Password link

Expected Result (choose depending on system):

Option A – Reset Page Flow

User is redirected to Password Reset page

Reset form is displayed (email field + submit button)

Option B – Email Flow

A message appears: “Password reset link sent to your email”

=========================================

Defects / Bug Reports In real QA jobs, you’ll also log defects when test cases fail. Basic bug report structure: Bug ID Title / Summary Environment (Test / Prod / Browser / OS) Steps to Reproduce Expected Result Actual Result Severity (how bad) Priority (how fast it must be fixed) Attachments (screenshots, logs) Example: ID: BUG_LOGIN_001 Title: Login allows empty password Steps: Open login page Fill in username Leave password empty Click Login Expected: Error message “Password is required” Actual: User is logged in Severity: Critical Priority: High 🧪 Exercise: Write 1 bug report based on one of your negative test cases (for example, if the app did something wrong).

Bug Report

Bug ID: BUG_LOGIN_002
Title: System logs in user even when an invalid password is entered

Environment:

Environment: Test

Browser: Chrome 119

OS: Windows 11

App Version: v1.0.3

Steps to Reproduce:

Navigate to the Login page

Enter a valid username (e.g., valid_user)

Enter an invalid password (e.g., wrongPassword!)

Click the Login button

Expected Result:

User should NOT be authenticated

Error message displayed: "Invalid username or password"

User remains on the Login page

Actual Result:

User is successfully logged in

Dashboard page is displayed

No error message shown

Severity: High (Authentication bypass → security risk)
Priority: Critical (Must be fixed immediately)
Attachments:

Screenshot: login_invalid_password_allows_access.png

Logcat / console logs (if available)